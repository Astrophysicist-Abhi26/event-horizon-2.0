"""
Event Horizon 2.0 — daily pipeline.

  sources -> health check -> normalise -> drop past/undated -> de-duplicate
  -> classify (declared codes + keywords + embeddings [+ Claude])
  -> score once per research profile (profiles.yaml)
  -> docs/events.json  (+ a health-alert file for the GitHub Action)

Run locally:  python scraper/scrape.py
Options (env): ANTHROPIC_API_KEY enables Option C; EH_NO_EMBED=1 skips
Option B (faster local runs).
"""

import datetime as dt
import hashlib
import json
import os
import re
import sys
import time
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import profiles as P                                      # noqa: E402
import taxonomy as T                                      # noqa: E402
from classify import classify                             # noqa: E402
from classify import keyword_hits as classify_keyword_hits  # noqa: E402
import common as C                                        # noqa: E402
from common import clean, norm_title, today               # noqa: E402
from geo import locate                                     # noqa: E402
import sources as G                                        # noqa: E402
from sources_india import (default_fields, empty_ok_names, india_sources, scrape_issue_intake,  # noqa: E402
                           scrape_watchlist)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EVENTS = os.path.join(ROOT, "docs", "events.json")
NOTIFY_DIR = os.path.join(ROOT, "notify")
HORIZON_DAYS = 730

GLOBAL_SOURCES = [
    # (name, function, minimum events expected when healthy)
    ("DESC Cosmology Meetings", G.scrape_desc_cosmology, 5),
    ("CADC Astronomy Meetings", G.scrape_cadc, 30),
    ("INSPIRE conferences", G.scrape_inspire_conferences, 50),
    ("INSPIRE seminars", G.scrape_inspire_seminars, 10),
    ("researchseminars.org talks", G.scrape_researchseminars, 30),
    ("researchseminars.org conferences", G.scrape_researchseminars_conferences, 1),
    ("AI Deadlines", G.scrape_ai_deadlines, 10),
    ("CCF Deadlines", G.scrape_ccf_deadlines, 50),
    ("ML summer schools", G.scrape_ml_schools, 3),
]

# Earlier source = preferred copy when the same event appears twice
SOURCE_PRIORITY = ["Added by you", "Watchlist", "DESC Cosmology Meetings"]
MANUAL = {"Watchlist", "Added by you"}

TYPE_RULES = [
    (r"\bschools?\b", "School"), (r"summer course|winter course|refresher course", "School"),
    (r"lecture series|lectures\b|distinguished lecture|memorial lecture", "Lecture series"),
    (r"\bworkshops?\b|hackathon|discussion meeting|\bprogram(me)?\b|thinkshop|hands-on", "Workshop"),
    (r"conference|symposium|congress|meeting|\bforum\b|\bdays\b|summit|\bfest\b", "Conference"),
    (r"colloqui|seminar|\btalks?\b|webinar|journal club|lecture\b", "Talk / Seminar"),
]
JUNK_TITLE = C.JUNK_TITLE      # placeholders, holidays, exams, cancellations (see common.py)
NOT_EVENTS = re.compile(
    r"^(programs?|past programs?|program committee|lectures?|events?|current (&|and) upcoming|"
    r"special (events|lectures)|summer courses?|archives?|home|news|load more)$", re.I)


def classify_type(title, raw_type, source):
    text = f"{raw_type or ''} {title or ''}".lower()
    for pat, label in TYPE_RULES:
        if re.search(pat, text):
            return label
    if raw_type and "seminar" in raw_type.lower():
        return "Talk / Seminar"
    return "Talk / Seminar" if "seminar" in (source or "").lower() else "Conference"


def event_id(title, start):
    return hashlib.sha1(f"{norm_title(title)}|{start or ''}".encode()).hexdigest()[:12]


def load_previous():
    try:
        with open(EVENTS) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


# ---------------------------------------------------------------------------
CARRY_MAX_DAYS = 14   # how long a broken source may keep showing its last good events


def carry_forward(name, prev_events, last_ok):
    """A source that fails today (server down, 502s, page suddenly unreadable)
    keeps its still-upcoming events from the last deployed events.json, for at
    most CARRY_MAX_DAYS after its last successful run. Returned in raw form so
    they go through normalise / dedupe / classify like fresh events."""
    if not last_ok:
        return []
    try:
        age = dt.datetime.now(dt.timezone.utc) - dt.datetime.fromisoformat(last_ok)
    except (TypeError, ValueError):
        return []
    if age > dt.timedelta(days=CARRY_MAX_DAYS):
        return []
    t = today().isoformat()
    out = []
    for e in prev_events or []:
        if name not in (e.get("sources") or [e.get("source")]):
            continue
        if (e.get("end_date") or e.get("start_date") or "") < t or not e.get("url"):
            continue
        out.append(dict(title=e.get("title"), url=e["url"], start_date=e.get("start_date"),
                        end_date=e.get("end_date"), deadline=e.get("deadline"),
                        location=e.get("location"), country=e.get("country"),
                        online=bool(e.get("online")), tz=None,
                        description=e.get("description") or "", speaker=e.get("speaker"),
                        source=name, raw_type=e.get("type"), declared=[],
                        priority=bool(e.get("priority"))))
    return out


def run_sources(prev_health, prev_events=None):
    registry = GLOBAL_SOURCES + india_sources() + [("Watchlist", scrape_watchlist, 0),
                                                  ("Added by you", scrape_issue_intake, 0)]
    raw, health = [], []
    prev = {h["name"]: h for h in prev_health or []}
    quiet_ok = MANUAL | empty_ok_names()
    today_iso = dt.date.today().isoformat()
    for name, fn, min_exp in registry:
        t0 = time.time()
        p = prev.get(name, {})
        ua0 = set(C.BROWSER_UA_HOSTS)
        try:
            batch = fn() or []
            status = "ok" if len(batch) >= max(1, min_exp) else ("low" if batch else "empty")
            if name in quiet_ok and not batch:
                status = "ok"
            msg = ""
        except Exception as exc:
            batch, status, msg = [], "error", f"{exc.__class__.__name__}: {exc}"[:300]
        secs = round(time.time() - t0, 1)
        last_ok = dt.datetime.now(dt.timezone.utc).isoformat() if status == "ok" \
            else p.get("last_ok")
        # A page that answered with items last time and suddenly yields none is
        # as broken as one that errors: keep yesterday's events rather than lose them.
        if status == "error" or (status == "empty" and (p.get("raw") or 0) > 0):
            kept = carry_forward(name, prev_events, last_ok)
            if kept:
                why = msg or "page returned no recognisable events"
                status, batch = "stale", kept
                msg = (f"{why[:200]} — showing {len(kept)} upcoming event(s) from the last "
                       f"good run ({(last_ok or '')[:10]})")
        # How long has this source been broken? Chronic failures are alerted once,
        # after LONG_FAILURE_DAYS, so a source that stays broken is never forgotten.
        bad = status in BAD
        since = ((p.get("bad_since") if p.get("status") in BAD else None) or today_iso) if bad else None
        due = bad and not p.get("long_alerted") \
            and (dt.date.fromisoformat(today_iso) - dt.date.fromisoformat(since)).days >= LONG_FAILURE_DAYS
        health.append(dict(name=name, status=status, raw=len(batch), kept=0,
                           message=msg, seconds=secs, last_ok=last_ok,
                           previous=p.get("status"), bad_since=since,
                           long_alerted=bool(bad and (p.get("long_alerted") or due)),
                           long_due=bool(due),
                           # the site turned away our named agent and answered as for a browser
                           browser_ua=sorted(set(C.BROWSER_UA_HOSTS) - ua0)))
        print(f"[{status:5s}] {name}: {len(batch)} raw ({secs}s) {msg}")
        for e in batch:
            e["source"] = name
        raw.extend(batch)
    if C.ROBOTS_BLOCKED:
        print(f"robots.txt: {len(C.ROBOTS_BLOCKED)} page(s) skipped or flagged: " + ", ".join(C.ROBOTS_BLOCKED[:20]))
    if C.BROWSER_UA_HOSTS:
        print("Answered only a browser user agent: " + ", ".join(sorted(C.BROWSER_UA_HOSTS)))
    return raw, health


def normalise(raw):
    t = today().isoformat()
    horizon = (today() + dt.timedelta(days=HORIZON_DAYS)).isoformat()
    out = []
    for e in raw:
        title = clean(e.get("title"))
        if not title or not e.get("url") or NOT_EVENTS.match(title) or JUNK_TITLE.search(title):
            continue
        start = e.get("start_date")
        end = e.get("end_date") or start
        if start and end and end < start:
            end = start
        if not start and not e.get("priority"):
            continue                       # undated: cannot be placed in time
        if (end or start or t) < t:
            continue                       # already over
        if start and start > horizon:
            continue
        country, region, online = locate(e.get("location"), e.get("country"),
                                         e.get("online"), e.get("tz"))
        out.append(dict(
            id=event_id(title, start), title=title, url=e["url"], start_date=start,
            end_date=end, deadline=e.get("deadline"), location=clean(e.get("location")) or None,
            country=country, region=region, online=online,
            type=classify_type(title, e.get("raw_type"), e.get("source")),
            source=e.get("source"), sources=[e.get("source")],
            speaker=e.get("speaker"), series=clean(e.get("series")) or None,
            description=clean(e.get("description")),
            declared=[d for d in (e.get("declared") or []) if d],
            priority=bool(e.get("priority"))))
    return out


def _rank(e):
    s = e["source"]
    return (SOURCE_PRIORITY.index(s) if s in SOURCE_PRIORITY else len(SOURCE_PRIORITY),
            -len(e["description"] or ""), -len(e["declared"]))


_SERIES = re.compile(r"^\s*(?:(?:IEEE|ACM|IEEE/ACM|USENIX)\s+)?((?=(?:[^A-Z]*[A-Z]){2})[A-Za-z][A-Za-z0-9&+/\-]{1,15})\s+(20\d\d)\b")


def series_key(title):
    """'CVPR 2027 — IEEE/CVF ...' -> 'cvpr 2027': a conference series and its year."""
    m = _SERIES.match(title or "")
    return f"{m.group(1).lower()} {m.group(2)}" if m else None


def _merge(twin, e):
    for s in e["sources"]:
        if s not in twin["sources"]:
            twin["sources"].append(s)
    twin["declared"] = sorted(set(twin["declared"]) | set(e["declared"]))
    twin["priority"] = twin["priority"] or e["priority"]
    for f in ("deadline", "location", "speaker", "end_date", "series"):
        twin[f] = twin.get(f) or e.get(f)
    if len(e["description"] or "") > len(twin["description"] or ""):
        twin["description"] = e["description"]
    if twin["region"] == "unknown" and e["region"] != "unknown":
        twin.update(country=e["country"], region=e["region"])


def _days_apart(a, b):
    try:
        return abs((dt.date.fromisoformat(a) - dt.date.fromisoformat(b)).days)
    except (TypeError, ValueError):
        return 99


def dedupe(events):
    """Same normalised title + same start date = same event. Also merges when
    one normalised title contains the other on the same start date, and the same
    'ACRONYM YEAR' conference ('CVPR 2027') listed by two databases with start
    dates up to 3 days apart."""
    by_date = {}
    for e in events:
        by_date.setdefault(e["start_date"], []).append(e)
    out = []
    for date, group in by_date.items():
        group.sort(key=_rank)
        kept = []
        for e in group:
            nt = norm_title(e["title"])
            ns = set(nt.split())
            twin = None
            for k in kept:
                kt = norm_title(k["title"])
                ks = set(kt.split())
                jac = len(ns & ks) / max(1, len(ns | ks))
                if nt == kt or (min(len(nt), len(kt)) >= 14 and (nt in kt or kt in nt)) \
                        or (min(len(ns), len(ks)) >= 3 and jac >= 0.8):
                    twin = k
                    break
            if twin is None:
                kept.append(e)
            else:
                _merge(twin, e)
        out.extend(kept)
    by_series, final = {}, []
    for e in sorted(out, key=_rank):
        key = series_key(e["title"])
        twin = next((k for k in by_series.get(key, [])
                     if _days_apart(k["start_date"], e["start_date"]) <= 3), None) if key else None
        if twin is None:
            final.append(e)
            if key:
                by_series.setdefault(key, []).append(e)
        else:
            _merge(twin, e)
    return final


def too_little_text(e):
    """True for a title of three words or fewer with next to no description: typically a
    speaker's name ("Massyle Dendene") or a holiday. Keywords may still tag it."""
    return len(clean(e.get("title")).split()) <= 3 and len(clean(e.get("description"))) < 40


# Words that mark a French title. Two different ones are needed, so a name ("Au", "Du"),
# "et al." or "Paris" alone does not count.
_FRENCH = re.compile(
    r"(?<!\w)(?:les|des|du|aux|au|une|pour|sur|dans|avec|entre|et|sont|par|à|titre|venir|"
    r"s[ée]minaires?|journ[ée]es?|colloques?|expos[ée]s?|soutenance|th[èe]se|rentr[ée]e|s[ée]ance|"
    r"th[ée]orie|[ée]quations?|g[ée]om[ée]trie|alg[èe]bre|probabilit[ée]s|math[ée]matiques?|physique|"
    r"mod[èe]les?|m[ée]thodes?|probl[èe]mes?|num[ée]rique|d[ée]riv[ée]es|partielles|calcul|groupe|travail|"
    r"doctorant\S*)(?!\w)|(?<!\w)[ld]['’](?=\w)", re.I)          # l'analyse, d'Alembert
# a talk slot titled by its speakers: "Marie Doumic (INRIA Paris)", "Colloquium: Bertrand Maury",
# "Séminaire 08/01/2027 - Mathurin Massias and Claire Boyer"
_SLOT = re.compile(r"seminar|s[ée]minaire|colloqu|lecture|talk|expos[ée]|webinar|journal club|"
                   r"working group|groupe de travail|series", re.I)
# words that name an event, not a person: "International Space Radio Interferometry Conference"
_NOT_A_NAME = re.compile(r"\b(?:conference|congress|workshop|school|symposium|meeting|summit|forum|days|week|"
                         r"program(?:me)?|course|festival|award|prize|lab|group|institute|centre|center|university|"
                         r"software|data|science|physics|mathematics|computing|systems?|theory|methods?)\b", re.I)
_NAME_GLUE = {"and", "et", "&", "und", "de", "van", "der", "von", "da", "di", "du", "le",
              "la", "del", "dos", "das", "ter", "ten", "bin", "al", "y", "e"}


def foreign_title(title):
    """French (two French marker words), or mostly in a non-Latin script."""
    t = clean(title)
    if len({m.group(0).lower() for m in _FRENCH.finditer(t)}) >= 2:
        return True
    letters = [ch for ch in t if ch.isalpha()]
    latin = sum(1 for ch in letters if "LATIN" in unicodedata.name(ch, ""))
    return bool(letters) and latin < len(letters) / 2


def names_only(title):
    """The title only names people (speakers), apart from a series or date prefix."""
    raw = clean(title)
    t = re.sub(r"\([^()]*\)|\[[^\[\]]*\]", " ", raw)     # affiliations, "[DPS Seminar]"
    segs = [x.strip(" ,.") for x in re.split(r"\s*[:|–—]\s*|\s+-+\s+", t) if x.strip(" ,.")]
    names, prefix, glue, longest = 0, False, False, 0
    for seg in segs:
        if _SLOT.search(seg) and len(seg.split()) <= 6:
            prefix = True                          # "Colloquium", "Séminaire 08/01/2027"
            continue
        parts = [w for w in re.split(r"[\s,]+", seg) if w]
        words = [w for w in parts if w.lower() not in _NAME_GLUE]
        glue = glue or len(words) < len(parts)
        if not 1 <= len(words) <= 8 or re.search(r"\d", seg) or _NOT_A_NAME.search(seg) \
                or classify_keyword_hits(seg) or not all(w[:1].isupper() for w in words if w[:1].isalpha()):
            return False
        names += 1
        longest = max(longest, len(words))
    # a person shows by an affiliation in brackets, a series prefix, "A and B", or a short name
    return names > 0 and (prefix or glue or t != raw or longest <= 3)


def no_embedding_guess(e):
    """When the English-only embedding model has nothing it can judge, it guesses (on 2026-11-09,
    11 of 14 maths events tagged by it alone were "Number theory": "Titre à venir", speakers'
    names). Keywords, declared codes and the series name still tag such events."""
    if too_little_text(e) or foreign_title(e.get("title")):
        return True
    return names_only(e.get("title")) and len(clean(e.get("description"))) < 60


def classify_event(e, emb=None, llm=None, defaults=None):
    """One event's (subfields, fields, basis), given the embedding and Claude results."""
    if emb and no_embedding_guess(e):
        emb = None             # a name, a placeholder or French: nothing the model can judge
    subs, fields, basis = classify(e, emb if emb and emb[0] != "neg" else None, llm)
    fallback = next((defaults[s] for s in e.get("sources") or [e.get("source")] if s in (defaults or {})), None)
    if not subs and fallback:
        # a source that lists one subject only: known to be mathematics, branch unknown (2026-11-10)
        subs, fields, basis = [fallback], [T.parent(fallback)], ["source"]
    return subs, fields, basis


def classify_all(events):
    status = {}
    embed_results = [None] * len(events)
    if os.environ.get("EH_NO_EMBED"):
        status["embedding"] = {"status": "off", "detail": "disabled by EH_NO_EMBED"}
    else:
        try:
            from embed import EmbeddingClassifier
            clf = EmbeddingClassifier()
            embed_results = clf.classify_many(events)
            status["embedding"] = {"status": clf.status, "detail": clf.detail}
        except Exception as exc:
            status["embedding"] = {"status": "off", "detail": f"{exc}"[:200]}
    try:
        from llm_classify import classify_all as llm_all
        llm_results, status["llm"] = llm_all(events)
    except Exception as exc:
        llm_results, status["llm"] = [None] * len(events), {"status": "off", "detail": f"{exc}"[:200]}
    defaults = default_fields()
    for e, emb, llm in zip(events, embed_results, llm_results):
        subs, fields, basis = classify_event(e, emb, llm, defaults)
        e.update(subfields=subs, fields=fields, basis=basis)
        if llm and llm.get("reason"):
            e["reason"] = llm["reason"]
    return status


def rank_all(events, profiles):
    """One relevance score per research profile; `score` is the default's."""
    for e in events:
        e["scores"] = {p.id: P.pinned_score(p.score(e["subfields"], e.get("region"),
                                                    e.get("type"), e["basis"]),
                                            e["priority"])
                       for p in profiles}
        e["score"] = e["scores"][profiles.default]


# ---------------------------------------------------------------------------
BAD = ("error", "empty", "stale")
LONG_FAILURE_DAYS = 7
# Extra sources whose server often does not answer GitHub's runners (researchseminars.org
# timed out on every try on 2026-11-05). They stay in the Source health panel, with the
# last good events kept, but never open or hold open a maintainer alert.
UNRELIABLE = {"researchseminars.org talks", "researchseminars.org conferences"}


def notifications(health):
    """Maintainer alert (GitHub issue -> e-mail). Written when a source newly stops
    returning events, or has been broken for LONG_FAILURE_DAYS. The alert lists every
    source that is broken now, so an alert that replaces an older one loses nothing.
    `bad.json` always lists the broken sources: scraper/notify.py closes an open alert
    once none of the sources it names is broken any more. (No personal "events you
    should see" notices: the site serves many profiles.)"""
    os.makedirs(NOTIFY_DIR, exist_ok=True)
    for f in os.listdir(NOTIFY_DIR):
        os.remove(os.path.join(NOTIFY_DIR, f))
    bad = [h for h in health if h["status"] in BAD and h["name"] not in UNRELIABLE]
    with open(os.path.join(NOTIFY_DIR, "bad.json"), "w") as f:
        json.dump([h["name"] for h in bad], f)
    new = [h for h in bad if h.get("previous") not in BAD]
    chronic = [h for h in bad if h.get("long_due")]
    if new or chronic:
        lines = []
        if new:
            lines += ["These sources stopped returning events:", ""]
            lines += [f"- **{h['name']}** — {h['status']} {h['message']}" for h in new]
        rest = [h for h in bad if h not in new]
        if rest:
            lines += ["", "Still broken" + (" (**%s** for %d days or more)" % (
                ", ".join(h["name"] for h in chronic), LONG_FAILURE_DAYS) if chronic else "") + ":", ""]
            lines += [f"- **{h['name']}** — {h['status']} since {h.get('bad_since') or '?'}: "
                      f"{(h['message'] or '')[:160]}" for h in rest]
        lines += ["", "Fix the source, or park it with `enabled: false` in "
                  "`scraper/institutes.yaml`; this alert closes itself once none of "
                  "the sources above is broken."]
        with open(os.path.join(NOTIFY_DIR, "health.md"), "w") as f:
            f.write("\n".join(lines))


def main():
    profiles = P.load()                    # a broken profiles.yaml stops the run early
    prev = load_previous()
    prev_events = {e["id"]: e for e in prev.get("events", []) if "id" in e}
    raw, health = run_sources(prev.get("health"), prev.get("events"))
    events = dedupe(normalise(raw))
    status = classify_all(events)
    rank_all(events, profiles)

    t = today().isoformat()
    for e in events:
        e["first_seen"] = prev_events.get(e["id"], {}).get("first_seen", t)
        e["description"] = (e["description"] or "")[:280]
        e.pop("declared", None)
    kept = {}
    for e in events:
        for s in e["sources"]:
            kept[s] = kept.get(s, 0) + 1
    for h in health:
        h["kept"] = kept.get(h["name"], 0)

    events.sort(key=lambda e: (not e["priority"], e["start_date"] or "9999", -e["score"]))
    os.makedirs(os.path.dirname(EVENTS), exist_ok=True)
    with open(EVENTS, "w") as f:
        json.dump({"version": 6,
                   "generated": dt.datetime.now(dt.timezone.utc).isoformat(),
                   "taxonomy": T.export_for_frontend(),
                   "profiles": P.export_for_frontend(profiles),
                   "health": health, "classifiers": status,
                   "events": events}, f, ensure_ascii=False, separators=(",", ":"))
    notifications(health)
    n_cls = sum(1 for e in events if e["fields"])
    print(f"\nWrote {len(events)} events ({n_cls} classified) -> docs/events.json")
    print("Classifiers:", json.dumps(status))


if __name__ == "__main__":
    main()
