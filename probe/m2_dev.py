"""Temporary (removed before merge): the DEV half of live maths-source events, for writing M2 patterns.
The other half (event id even/odd) is held out and only scored at the end."""
import collections, json, urllib.request
d = json.load(urllib.request.urlopen("https://astrophysicist-abhi26.github.io/event-horizon-2.0/events.json", timeout=60))
ev = d["events"]
dev = lambda e: int(e["id"], 16) % 2 == 0
MATHS = {"French maths Indico", "Math institutes events", "IISc Mathematics seminars", "IIT Jodhpur Mathematics seminars",
         "IIT (BHU) Mathematical Sciences events", "Vakil algebraic geometry", "CMI seminars"}
print("events", len(ev), "generated", d.get("generated"))
for src in sorted(MATHS):
    es = [e for e in ev if e.get("source") == src]
    dv = [e for e in es if dev(e)]
    print(f"\n## {src}: {len(es)} events, dev half {len(dv)}, classified {sum(1 for e in es if e.get('subfields'))}")
    rows = sorted(dv, key=lambda e: ((e.get("description") or "").split(" · ")[0], e["title"]))
    for e in rows:
        ser = (e.get("description") or "").split(" · ")[0][:48] if src == "French maths Indico" else ""
        print(f"   {ser:48} | {e['title'][:85]} -> {','.join(e.get('subfields') or [])[:60]}")
