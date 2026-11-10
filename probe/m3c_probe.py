"""Temporary (removed before merge): before/after for PR M3c on the live site's events (run 2)."""
import collections, json, os, re, subprocess, sys, urllib.request
ROOT = os.getcwd()
OLD = os.path.join(ROOT, "_old_scraper"); os.makedirs(OLD, exist_ok=True)
for f in subprocess.run(["git", "ls-tree", "--name-only", "origin/main", "scraper/"], capture_output=True, text=True).stdout.split():
    if f.endswith((".py", ".yaml")):
        open(os.path.join(OLD, os.path.basename(f)), "w").write(subprocess.run(["git", "show", f"origin/main:{f}"], capture_output=True, text=True).stdout)
d = json.load(urllib.request.urlopen("https://astrophysicist-abhi26.github.io/event-horizon-2.0/events.json", timeout=60))
ev = d["events"]
print("live data generated", d.get("generated"), "events", len(ev))
for e in ev:
    e.pop("declared", None)
json.dump(ev, open("_events.json", "w"))
sys.path.insert(0, os.path.join(ROOT, "scraper"))
from embed import EmbeddingClassifier          # noqa: E402
json.dump(EmbeddingClassifier().classify_many(ev), open("_emb.json", "w"))
open("_dump.py", "w").write(r'''
import json, sys
sys.path.insert(0, sys.argv[1])
import scrape as S, profiles as P
ev = json.load(open("_events.json")); emb = json.load(open("_emb.json"))
defaults = S.default_fields()
profs = P.load()
out = []
for e, m in zip(ev, emb):
    subs, fields, basis = S.classify_event(e, tuple(m) if m else None, None, defaults)
    info = not S.names_only(e["title"]) and len(e["title"].split()) >= 4
    out.append({"junk": bool(S.JUNK_TITLE.search(e["title"])), "subs": subs, "basis": basis, "info": info,
                "score": {p.id: p.score(subs, basis=basis) for p in profs}})
json.dump(out, open(sys.argv[2], "w"))
''')
for name, path in (("old", OLD), ("new", os.path.join(ROOT, "scraper"))):
    r = subprocess.run([sys.executable, "_dump.py", path, f"_{name}.json"], capture_output=True, text=True)
    print(name, "dump:", r.returncode, r.stderr[-600:])
old, new = json.load(open("_old.json")), json.load(open("_new.json"))
import taxonomy as T                           # noqa: E402
fam = lambda t: T.ancestors(t)[-1] if t in T.SUBFIELDS else t.split(".")[0]
for label, res in (("old", old), ("new", new)):
    rows = [(e, r) for e, r in zip(ev, res) if not r["junk"]]
    m = [x for x in rows if any(fam(t) == "math" for t in x[1]["subs"])]
    mi = [x for x in m if x[1]["info"]]
    mt = [x for x in mi if any(fam(t) == "math" and (t in T.PARENT_SF or t.count(".") >= 2) for t in x[1]["subs"])]
    print(f"  {label}: recognised as maths {len(m)} | informative titles {len(mi)}, with a topic {len(mt)} ({100*len(mt)//max(1,len(mi))}%)")

r = subprocess.run([sys.executable, "-c", "import sys, json; sys.path.insert(0, sys.argv[1]); import taxonomy as T; print(json.dumps(sorted(T.SUBFIELDS)))", OLD],
                   capture_output=True, text=True)
old_ids = set(json.loads(r.stdout))
new_ids = sorted(t for t in T.SUBFIELDS if t not in old_ids)
print(f"\n## events per new topic ({len(new_ids)} new ids)")
c = collections.Counter(t for r in new for t in r["subs"] if t in new_ids)
for k in new_ids:
    print(f"   {c.get(k, 0):3d} {k}")

print("\n## (general) topics that gave way to a narrower one")
for g in T.NARROWER:
    gone = sum(1 for o, n in zip(old, new) if g in o["subs"] and g not in n["subs"])
    print(f"   {g}: was on {sum(g in o['subs'] for o in old)}, now on {sum(g in n['subs'] for n in new)} (dropped from {gone})")

print("\n## profile scores that changed (old tags+old weights vs new tags+new weights)")
for pid in new[0]["score"]:
    ch = [(e["title"][:70], o["score"][pid], n["score"][pid]) for e, o, n in zip(ev, old, new)
          if abs(o["score"][pid] - n["score"][pid]) > 1e-9]
    print(f"   {pid}: {len(ch)} events")
    for t, a, b in sorted(ch, key=lambda x: -abs(x[2] - x[1]))[:8]:
        print(f"        {a:6.1f} -> {b:6.1f}  {t}")

print("\n## tag changes outside mathematics")
for e, o, n in zip(ev, old, new):
    a = {t for t in o["subs"] if fam(t) != "math"}; b = {t for t in n["subs"] if fam(t) != "math"}
    if a != b:
        print(f"    {e['title'][:80]:80} | -{','.join(sorted(a - b))} +{','.join(sorted(b - a))}")

print("\n## maths recognition changes (an event gained or lost every maths tag)")
for e, o, n in zip(ev, old, new):
    a = any(fam(t) == "math" for t in o["subs"]); b = any(fam(t) == "math" for t in n["subs"])
    if a != b:
        print(f"    {'+' if b else '-'} {e['title'][:90]} | {n['subs']}")

dash = re.compile(r"\b[A-Z][a-zà-ÿ]+[–‐‑—][A-Z][a-zà-ÿ]+")
dd = [e["title"] for e, r in zip(ev, new) if dash.search(e["title"]) and any(fam(t) == "math" for t in r["subs"])]
print(f"\n## maths titles with an en-dash name (Navier–Stokes style): {len(dd)}")
for t in dd[:15]:
    print("    ", t[:100])

print("\n## every maths tag change")
rows = []
for e, o, n in zip(ev, old, new):
    a, b = set(o["subs"]), set(n["subs"])
    if a != b:
        rows.append(f"    {e['title'][:80]:80} | -{','.join(sorted(a - b))} +{','.join(sorted(b - a))}")
print(f"   {len(rows)} events changed")
for r in rows[:400]:
    print(r)

import classify as CL                          # noqa: E402
def mhits(e):
    out = {}
    for part in ("title", "series", "description"):
        for sf, hs in CL.keyword_hits(e.get(part) or "").items():
            if fam(sf) == "math":
                out.setdefault(sf, set()).update(h.lower() for h in hs)
    return {k: sorted(v)[:4] for k, v in out.items()}

print("\n## which words put an event in a new topic (one line per event)")
seen = set()
for e, o, n in zip(ev, old, new):
    add = [t for t in n["subs"] if t in new_ids and t not in o["subs"]]
    if add and e["title"] not in seen:
        seen.add(e["title"])
        h = mhits(e)
        print(f"    {e['title'][:70]:70} | " + "; ".join(f"{t}: {h.get(t, '(none)')}" for t in add))

print("\n## informative maths titles with no topic (new code)")
k = 0
for e, r in zip(ev, new):
    if r["junk"] or not r["info"]:
        continue
    if any(fam(t) == "math" for t in r["subs"]) and not any(fam(t) == "math" and t in T.PARENT_SF for t in r["subs"]):
        k += 1
        print(f"    {e['title'][:95]:95} | {','.join(r['subs'])} | {e.get('source','')[:25]}")
print("   total", k)
