"""Temporary (removed before merge): checks for PR M1 against the live site's events."""
import collections, json, random, re, sys, urllib.request
sys.path.insert(0, "scraper")
import classify as CL, scrape as S, taxonomy as T
from common import get
random.seed(3)
d = json.load(urllib.request.urlopen("https://astrophysicist-abhi26.github.io/event-horizon-2.0/events.json", timeout=60))
ev = d["events"]
fam = lambda t: T.ancestors(t)[-1]
print("events", len(ev))

print("\n## 1. titles the new placeholder rule drops")
for e in ev:
    if S.JUNK_TITLE.search(e["title"]):
        print("   DROP", e.get("source", "")[:22].ljust(22), e["title"][:100])
print("\n   short '<series>: X' titles that stay (check for missed placeholders):")
for e in ev:
    m = re.match(r"^(.{3,80}):\s*(.{0,25})$", e["title"])
    if m and not S.JUNK_TITLE.search(e["title"]) and len(m.group(2).split()) <= 2:
        print("   keep", e["title"][:100])

print("\n## 2. French maths Indico categories (live export)")
try:
    import datetime as dt
    t0 = dt.date.today().isoformat(); t1 = (dt.date.today() + dt.timedelta(days=540)).isoformat()
    data = get("https://indico.math.cnrs.fr/export/categ/0.json", params={"from": t0, "to": t1, "limit": 500}, feed=True).json()
    cats = collections.Counter(); sample = {}
    for r in data["results"]:
        c = r.get("category"); c = c.get("title") if isinstance(c, dict) else c
        cats[c] += 1; sample.setdefault(c, r.get("title"))
    for c, n in cats.most_common():
        print(f"   {n:3d}  {str(c)[:60]:60}  e.g. {str(sample[c])[:60]}")
except Exception as exc:
    print("   export failed:", exc)

print("\n## 3. embedding guard")
blocked = [e for e in ev if S.no_embedding_guess(e)]
print("   events the guard blocks:", len(blocked))
hit = [e for e in blocked if "embedding" in (e.get("basis") or [])]
print("   ...of which the embedding contributed to the current tags:", len(hit))
for e in hit[:70]:
    why = "foreign" if S.foreign_title(e["title"]) else "names" if S.names_only(e["title"]) else "little"
    print(f"   {why:7} {e['title'][:70]:70} -> {','.join(e['subfields'][:3])} {e.get('basis')} |{len(e.get('description') or '')}")
only = [e for e in ev if e.get("basis") == ["embedding"] and not S.no_embedding_guess(e)]
print(f"\n   embedding-only events the guard still allows: {len(only)} (sample 40)")
for e in random.sample(only, min(40, len(only))):
    print(f"   {e['title'][:80]:80} -> {','.join(e['subfields'][:3])}")

print("\n## 4. maths keyword matches on events that also carry other fields")
agg = collections.Counter()
rows = []
for e in ev:
    tags = e.get("subfields") or []
    m = [t for t in tags if fam(t) == "math"]
    o = [t for t in tags if fam(t) != "math"]
    if not m or not o:
        continue
    ht = CL.keyword_hits(e["title"])
    hd = CL.keyword_hits((e.get("description") or "")[:3000])
    det = []
    for t in m:
        for sf in [t] + list(T.ancestors(t)[1:]):
            if sf in ht:
                det += [f"{sf}:T:{h}" for h in ht[sf]]
                agg.update((sf, h.lower(), "T") for h in ht[sf])
            elif sf in hd:
                det += [f"{sf}:D:{h}" for h in hd[sf][:3]]
                agg.update((sf, h.lower(), "D") for h in hd[sf][:3])
    rows.append((e, m, o, det))
print("   events:", len(rows))
for (sf, h, w), n in agg.most_common(90):
    print(f"   {n:3d} {w} {sf:28} {h}")
print("\n   sample of 60 such events")
for e, m, o, det in random.sample(rows, min(60, len(rows))):
    print(f"   {e['title'][:80]:80} | other={','.join(o[:2])} | {'; '.join(det)[:150]}")
