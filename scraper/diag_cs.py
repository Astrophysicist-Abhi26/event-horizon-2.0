"""Temporary probe of CS sources from GitHub's network (not merged)."""
import re, sys, json, time
sys.path.insert(0, "scraper")
from common import get
from bs4 import BeautifulSoup

def probe(url, n=1500):
    t0 = time.time()
    try:
        r = get(url, insecure_ok=True, timeout=25)
    except Exception as e:
        print(f"\n### {url}\n  ERROR {type(e).__name__}: {str(e)[:200]}", flush=True); return None
    ct = r.headers.get("content-type", "")
    print(f"\n### {url}\n  {r.status_code} {r.url} {ct} {len(r.content)}B {time.time()-t0:.1f}s", flush=True)
    if "json" in ct:
        print("  JSON:", r.text[:n].replace("\n", " ")); return r
    soup = BeautifulSoup(r.text, "html.parser")
    print("  title:", (soup.title.string or "").strip()[:100] if soup.title else None)
    hits = set(re.findall(r"""(?:https?:)?//[^\s"'<>]*(?:calendar\.google|\.ics|ical|wp-json|tribe|feed|api)[^\s"'<>]*""", r.text))
    print("  feeds/apis:", sorted(hits)[:15])
    links = [(a.get_text(" ", strip=True)[:70], a["href"]) for a in soup.find_all("a", href=True)
             if re.search(r"event|seminar|talk|colloqui|lecture|calendar|news", a["href"] + a.get_text(), re.I)]
    print("  links:", links[:25])
    for s in soup(["script", "style", "nav", "footer"]): s.decompose()
    txt = re.sub(r"\s+", " ", soup.get_text(" "))
    dates = re.findall(r"\b\d{1,2}(?:st|nd|rd|th)? (?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* ?,? 20\d\d|\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{1,2},? 20\d\d|20\d\d-\d\d-\d\d", txt)
    print("  dates:", len(dates), dates[:12])
    i = max(0, txt.find(dates[0]) - 300) if dates else 0
    print("  text:", txt[i:i+n])
    return r

URLS = [
 "https://www.csa.iisc.ac.in/events/", "https://www.csa.iisc.ac.in/wp-json/",
 "https://www.csa.iisc.ac.in/seminars/", "https://www.csa.iisc.ac.in/feed/",
 "https://cni.iisc.ac.in/events/", "https://cni.iisc.ac.in/wp-json/tribe/events/v1/events?per_page=3",
 "https://kiac.iisc.ac.in/", "https://kiac.iisc.ac.in/events/",
 "https://eecs.iisc.ac.in/", "https://ece.iisc.ac.in/events/",
 "https://www.iiitb.ac.in/events", "https://www.iiitb.ac.in/news-and-events",
 "https://www.microsoft.com/en-us/research/lab/microsoft-research-india/events/",
 "https://www.microsoft.com/en-us/research/wp-json/wp/v2/types",
 "https://rbcdsai.iitm.ac.in/events/", "https://rbcdsai.iitm.ac.in/wp-json/tribe/events/v1/events?per_page=3",
 "https://www.cse.iitm.ac.in/seminars.php", "https://www.cse.iitb.ac.in/page134",
 "https://www.cmi.ac.in/activities/seminars.php", "https://india.acm.org/events",
 "https://artpark.in/events", "https://www.tcs.tifr.res.in/seminars",
 "https://www.isibang.ac.in/~statmath/", "https://cds.iisc.ac.in/wp-json/tribe/events/v1/events?per_page=3",
]
for u in URLS:
    probe(u)

print("\n\n===== global sources =====", flush=True)
import sources as G
for fn in (G.scrape_ai_deadlines, G.scrape_ccf_deadlines, G.scrape_ml_schools, G.scrape_researchseminars):
    t0 = time.time()
    try:
        b = fn()
        cs = [e for e in b if any(str(d).lower().startswith(("cs", "eess")) for d in e.get("declared") or [])]
        print(fn.__name__, len(b), f"{time.time()-t0:.1f}s", "cs-topic:", len(cs), [e["title"][:60] for e in (cs or b)[:8]], flush=True)
    except Exception as e:
        print(fn.__name__, "ERROR", e, flush=True)
