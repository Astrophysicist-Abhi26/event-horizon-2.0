"""Temporary (removed before merge): before/after report for PR M1 on the live site's events.

Old code = origin/main, new code = this branch. Both classify the same events with the same
embedding results; declared subject codes are not in events.json, so both run without them."""
import collections, json, os, subprocess, sys, urllib.request

ROOT = os.getcwd()
OLD = os.path.join(ROOT, "_old_scraper")
os.makedirs(OLD, exist_ok=True)
for f in subprocess.run(["git", "ls-tree", "--name-only", "origin/main", "scraper/"], capture_output=True, text=True).stdout.split():
    if f.endswith((".py", ".yaml")):
        with open(os.path.join(OLD, os.path.basename(f)), "w") as out:
            out.write(subprocess.run(["git", "show", f"origin/main:{f}"], capture_output=True, text=True).stdout)

d = json.load(urllib.request.urlopen("https://astrophysicist-abhi26.github.io/event-horizon-2.0/events.json", timeout=60))
ev = d["events"]
for e in ev:
    e.pop("declared", None)
with open("_events.json", "w") as f:
    json.dump(ev, f)

# embedding results once, with the (unchanged) embedding classifier
sys.path.insert(0, os.path.join(ROOT, "scraper"))
from embed import EmbeddingClassifier          # noqa: E402
clf = EmbeddingClassifier()
print("embedding:", clf.status, clf.detail)
emb = clf.classify_many(ev)
with open("_emb.json", "w") as f:
    json.dump(emb, f)

DUMP = r'''
import json, sys
sys.path.insert(0, sys.argv[1])
import scrape as S, classify as C
ev = json.load(open("_events.json")); emb = json.load(open("_emb.json"))
guard = getattr(S, "no_embedding_guess", S.too_little_text)
out = []
for e, m in zip(ev, emb):
    m = tuple(m) if m else None
    if m and guard(e):
        m = None
    subs, fields, basis = C.classify(e, m if m and m[0] != "neg" else None, None)
    out.append({"junk": bool(S.JUNK_TITLE.search(e["title"])), "subs": subs, "basis": basis})
json.dump(out, open(sys.argv[2], "w"))
'''
with open("_dump.py", "w") as f:
    f.write(DUMP)
for name, path in (("old", OLD), ("new", os.path.join(ROOT, "scraper"))):
    r = subprocess.run([sys.executable, "_dump.py", path, f"_{name}.json"], capture_output=True, text=True)
    print(name, "dump:", r.returncode, r.stderr[-800:])
old, new = json.load(open("_old.json")), json.load(open("_new.json"))

import taxonomy as T                           # noqa: E402
fam = lambda t: T.ancestors(t)[-1]


def stats(res, label):
    keep = [(e, r) for e, r in zip(ev, res) if not r["junk"]]
    m = [(e, r) for e, r in keep if any(fam(t) == "math" for t in r["subs"])]
    mt = [x for x in m if any(fam(t) == "math" and t in T.PARENT_SF for t in x[1]["subs"])]
    fr = [(e, r) for e, r in keep if e.get("source") == "French maths Indico"]
    emb_only = [x for x in m if x[1]["basis"] == ["embedding"]]
    print(f"  {label}: kept {len(keep)} | maths {len(m)}, with a topic {len(mt)} ({100*len(mt)//max(1,len(m))}%) | "
          f"French maths Indico {len(fr)}, classified {sum(1 for e, r in fr if r['subs'])} | maths by embedding alone {len(emb_only)}")
    return emb_only


print("\n## 1. summary (no declared codes in either)")
stats(old, "old")
eo = stats(new, "new")
print("\n   maths events still tagged by the embedding alone (new):")
for e, r in eo:
    print("    ", e["title"][:80], "->", ",".join(r["subs"][:3]))

print("\n## 2. newly dropped titles")
for e, o, n in zip(ev, old, new):
    if n["junk"] and not o["junk"]:
        print("    DROP", e["title"][:100])

print("\n## 3. every tag change on kept events")
byfield = collections.Counter()
rows = []
for e, o, n in zip(ev, old, new):
    if n["junk"]:
        continue
    a, b = set(o["subs"]), set(n["subs"])
    if a != b:
        for t in a - b:
            byfield["-" + fam(t)] += 1
        for t in b - a:
            byfield["+" + fam(t)] += 1
        rows.append(f"    {e['title'][:78]:78} | -{','.join(sorted(a - b))} +{','.join(sorted(b - a))}")
print("   changes by field:", dict(byfield))
print(f"   {len(rows)} events changed")
for r in rows[:260]:
    print(r)

print("\n## 4. INSPIRE: how 'Math and Math Physics' is declared")
import sources as G                            # noqa: E402
for fn in (G.scrape_inspire_conferences, G.scrape_inspire_seminars):
    try:
        rows = fn()
    except Exception as exc:
        print("   ", fn.__name__, "failed:", exc)
        continue
    mp = [r for r in rows if any("math" in (c or "").lower() for c in r.get("declared") or [])]
    print(f"   {fn.__name__}: {len(rows)} events, {len(mp)} declare maths")
    dist = collections.Counter(len(r["declared"]) for r in mp)
    print("   number of categories on those:", dict(sorted(dist.items())))
    for r in mp[:45]:
        print(f"    [{len(r['declared'])}] {r['title'][:70]:70} {r['declared']}")
