# run 2: after the held-out fixes
"""Temporary (removed before merge): before/after and held-out report for PR M2.

Old code = origin/main, new code = this branch, same live events, same embedding results.
events.json has no `series` field yet: it is rebuilt from the description for French maths
Indico ("<series> · ...") and CMI (description = series). Held-out = events with an odd id."""
import collections, json, os, subprocess, sys, urllib.request

ROOT = os.getcwd()
OLD = os.path.join(ROOT, "_old_scraper")
os.makedirs(OLD, exist_ok=True)
for f in subprocess.run(["git", "ls-tree", "--name-only", "origin/main", "scraper/"], capture_output=True, text=True).stdout.split():
    if f.endswith((".py", ".yaml")):
        open(os.path.join(OLD, os.path.basename(f)), "w").write(
            subprocess.run(["git", "show", f"origin/main:{f}"], capture_output=True, text=True).stdout)
d = json.load(urllib.request.urlopen("https://astrophysicist-abhi26.github.io/event-horizon-2.0/events.json", timeout=60))
ev = d["events"]
print("live data generated", d.get("generated"), "events", len(ev))
for e in ev:
    e.pop("declared", None)
    if e.get("source") == "French maths Indico" and e.get("description"):
        e["series"] = e["description"].split(" · ")[0]
    elif e.get("source") == "CMI seminars":
        e["series"] = e.get("description") or None
json.dump(ev, open("_events.json", "w"))
sys.path.insert(0, os.path.join(ROOT, "scraper"))
from embed import EmbeddingClassifier          # noqa: E402
clf = EmbeddingClassifier()
print("embedding:", clf.status, clf.detail)
json.dump(clf.classify_many(ev), open("_emb.json", "w"))
open("_dump.py", "w").write(r'''
import json, sys
sys.path.insert(0, sys.argv[1])
import scrape as S, classify as C
ev = json.load(open("_events.json")); emb = json.load(open("_emb.json"))
new = hasattr(S, "classify_event")
defaults = S.default_fields() if new else {}
out = []
for e, m in zip(ev, emb):
    m = tuple(m) if m else None
    if new:
        subs, fields, basis = S.classify_event(e, m, None, defaults)
    else:
        if m and S.no_embedding_guess(e):
            m = None
        subs, fields, basis = C.classify(e, m if m and m[0] != "neg" else None, None)
    out.append({"junk": bool(S.JUNK_TITLE.search(e["title"])), "subs": subs, "basis": basis})
json.dump(out, open(sys.argv[2], "w"))
''')
for name, path in (("old", OLD), ("new", os.path.join(ROOT, "scraper"))):
    r = subprocess.run([sys.executable, "_dump.py", path, f"_{name}.json"], capture_output=True, text=True)
    print(name, "dump:", r.returncode, r.stderr[-600:])
old, new = json.load(open("_old.json")), json.load(open("_new.json"))
import taxonomy as T                           # noqa: E402
fam = lambda t: T.ancestors(t)[-1]
GEN = {"math.other"}


def kind(r):
    m = [t for t in r["subs"] if fam(t) == "math"]
    if not r["subs"]:
        return "unclassified"
    if r["basis"] == ["source"]:
        return "fallback"
    if not m:
        return "not maths"
    return "general maths" if set(m) <= GEN else "specific maths"


def report(label, res, sel):
    rows = [(e, r) for e, r in zip(ev, res) if sel(e) and not r["junk"]]
    c = collections.Counter(kind(r) for e, r in rows)
    mt = sum(1 for e, r in rows if any(fam(t) == "math" and t in T.PARENT_SF for t in r["subs"]))
    print(f"  {label}: {len(rows)} kept | " + ", ".join(f"{k} {v}" for k, v in sorted(c.items())) + f" | with a maths topic {mt}")
    return rows


print("\n## 1. French maths Indico")
for half, sel in (("all", lambda e: True), ("dev", lambda e: int(e["id"], 16) % 2 == 0),
                  ("HELD-OUT", lambda e: int(e["id"], 16) % 2 == 1)):
    print(f" {half}:")
    report("old", old, lambda e, s=sel: e.get("source") == "French maths Indico" and s(e))
    report("new", new, lambda e, s=sel: e.get("source") == "French maths Indico" and s(e))

print("\n## 2. all maths events")
for label, res in (("old", old), ("new", new)):
    rows = [(e, r) for e, r in zip(ev, res) if not r["junk"]]
    m = [x for x in rows if any(fam(t) == "math" for t in x[1]["subs"])]
    mt = [x for x in m if any(fam(t) == "math" and t in T.PARENT_SF for t in x[1]["subs"])]
    gen = sum(1 for x in m if {t for t in x[1]["subs"] if fam(t) == "math"} <= GEN)
    print(f"  {label}: kept {len(rows)} | maths {len(m)}, with a topic {len(mt)} ({100*len(mt)//max(1,len(m))}%) | "
          f"general maths only {gen} | unclassified overall {sum(1 for x in rows if not x[1]['subs'])}")

print("\n## 3. HELD-OUT French maths Indico events, new tags (judge precision here; no tuning after this)")
for e, r in report("new", new, lambda e: e.get("source") == "French maths Indico" and int(e["id"], 16) % 2 == 1):
    print(f"    {(e.get('series') or '')[:36]:36} | {e['title'][:70]:70} -> {','.join(r['subs'])} {r['basis']}")

print("\n## 4. tag changes outside French maths Indico")
byf = collections.Counter()
rows = []
for e, o, n in zip(ev, old, new):
    if n["junk"] or e.get("source") == "French maths Indico":
        continue
    a, b = set(o["subs"]), set(n["subs"])
    if a != b:
        for t in a - b:
            byf["-" + fam(t)] += 1
        for t in b - a:
            byf["+" + fam(t)] += 1
        rows.append(f"    {e['title'][:76]:76} | -{','.join(sorted(a - b))} +{','.join(sorted(b - a))}")
print("   by field:", dict(byf), "|", len(rows), "events")
for r in rows[:200]:
    print(r)
