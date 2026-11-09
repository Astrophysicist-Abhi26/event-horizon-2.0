"""Temporary (removed before merge): how are maths (and CS/AI) events tagged on the live site?"""
import collections, json, random, re, urllib.request, sys
sys.path.insert(0, "scraper")
import taxonomy as T
d = json.load(urllib.request.urlopen("https://astrophysicist-abhi26.github.io/event-horizon-2.0/events.json", timeout=60))
ev = d["events"]; random.seed(7)
fam = lambda t: T.ancestors(t)[-1]
def disc(e): return {fam(t) for t in e.get("subfields", [])}
print("events", len(ev))
for f in ["math", "cs", "ai"]:
    es = [e for e in ev if f in disc(e)]
    topic = [e for e in es if any(fam(t) == f and t in T.PARENT_SF for t in e["subfields"])]
    print(f"\n#### {f}: {len(es)} events, {len(topic)} with a topic ({100*len(topic)//max(1,len(es))}%)")
    c = collections.Counter(t for e in es for t in e["subfields"] if fam(t) == f)
    print("  tag counts:", ", ".join(f"{k}:{v}" for k, v in c.most_common(40)))
    if f == "math":
        nb = [e for e in es if not any(fam(t) == "math" and t in T.PARENT_SF for t in e["subfields"])]
        print(f"\n  -- {len(nb)} maths events with a branch but no topic (sample 45) --")
        for e in random.sample(nb, min(45, len(nb))):
            print("   ", e["title"][:95], "->", ",".join(e["subfields"][:3]))
        sus = [e for e in es if e.get("basis") == ["embedding"]]
        print(f"\n  -- {len(sus)} maths events tagged by the language model only (sample 20) --")
        for e in random.sample(sus, min(20, len(sus))):
            print("   ", e["title"][:95], "->", ",".join(e["subfields"][:3]))
src_math = {"French maths Indico", "Math institutes events", "IISc Mathematics seminars", "CMI seminars", "Vakil algebraic geometry",
            "IIT Jodhpur Mathematics seminars", "IIT (BHU) Mathematical Sciences events"}
un = [e for e in ev if not e.get("subfields") and set(e.get("sources") or [e.get("source")]) & src_math]
print(f"\n#### {len(un)} UNCLASSIFIED events from maths sources (sample 60)")
for e in random.sample(un, min(60, len(un))):
    print("   ", (e.get("source") or "")[:14].ljust(14), e["title"][:90], "|", (e.get("description") or "")[:60].replace("\n", " "))
fr = [e for e in ev if (e.get("source") == "French maths Indico")]
print(f"\nFrench maths Indico: {len(fr)} events, {sum(1 for e in fr if e.get('subfields'))} classified")
