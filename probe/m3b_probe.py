"""Temporary (removed before merge): before/after for PR M3b on the live site's events."""
import collections, json, os, subprocess, sys, urllib.request
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
import scrape as S
ev = json.load(open("_events.json")); emb = json.load(open("_emb.json"))
defaults = S.default_fields()
out = []
for e, m in zip(ev, emb):
    subs, fields, basis = S.classify_event(e, tuple(m) if m else None, None, defaults)
    info = not S.names_only(e["title"]) and len(e["title"].split()) >= 4
    out.append({"junk": bool(S.JUNK_TITLE.search(e["title"])), "subs": subs, "basis": basis, "info": info})
json.dump(out, open(sys.argv[2], "w"))
''')
for name, path in (("old", OLD), ("new", os.path.join(ROOT, "scraper"))):
    r = subprocess.run([sys.executable, "_dump.py", path, f"_{name}.json"], capture_output=True, text=True)
    print(name, "dump:", r.returncode, r.stderr[-600:])
old, new = json.load(open("_old.json")), json.load(open("_new.json"))
import taxonomy as T                           # noqa: E402
fam = lambda t: T.ancestors(t)[-1]
for label, res in (("old", old), ("new", new)):
    rows = [(e, r) for e, r in zip(ev, res) if not r["junk"]]
    m = [x for x in rows if any(fam(t) == "math" for t in x[1]["subs"])]
    mi = [x for x in m if x[1]["info"]]
    mt = [x for x in mi if any(fam(t) == "math" and t in T.PARENT_SF for t in x[1]["subs"])]
    print(f"  {label}: recognised as maths {len(m)} | informative titles {len(mi)}, with a topic {len(mt)} ({100*len(mt)//max(1,len(mi))}%)")
print("\n## events under Probability / Statistics (new)")
c = collections.Counter(t for e, r in zip(ev, new) for t in r["subs"] if t.startswith(("math.probability", "math.stat")))
for k, v in sorted(c.items()):
    print(f"   {v:3d} {k}")
print("\n## every tag change")
rows = []
for e, o, n in zip(ev, old, new):
    a, b = set(o["subs"]), set(n["subs"])
    if a != b:
        rows.append(f"    {e['title'][:80]:80} | -{','.join(sorted(a - b))} +{','.join(sorted(b - a))}")
print(f"   {len(rows)} events changed")
for r in rows[:220]:
    print(r)
