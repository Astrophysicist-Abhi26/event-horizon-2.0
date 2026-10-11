"""Temporary probe of CS sources from GitHub's network (not merged)."""
import re, sys, json
sys.path.insert(0, "scraper")
from common import get

def show(url, n=3000, around=None):
    try:
        r = get(url, insecure_ok=True, timeout=25)
    except Exception as e:
        print(f"\n### {url}\n  ERROR {e}"[:300], flush=True); return None
    t = r.text
    i = max(0, t.find(around) - 200) if around and around in t else 0
    print(f"\n### {url} {r.status_code} {len(t)}B\n{t[i:i+n]}", flush=True)
    return r

# CMI forthcoming seminars: raw HTML
show("https://www.cmi.ac.in/activities/seminars.php", 6000, "Forthcoming")
# CSA: how is the event list loaded?
r = show("https://www.csa.iisc.ac.in/events/", 0)
if r:
    print("SCRIPTS:", re.findall(r'<script[^>]+src="([^"]+)"', r.text))
    for m in re.finditer(r"(fetch\(|\$\.ajax|\$\.get|axios|XMLHttpRequest|admin-ajax|/api/|\.php\?)", r.text):
        print("JS@", r.text[max(0, m.start()-300):m.start()+300].replace("\n", " "))
    i = r.text.find("/event/251/")
    print("AROUND EVENT LINK:", r.text[max(0, i-1500):i+500])
show("https://www.csa.iisc.ac.in/event/251/electrical-flows-over-spanning-trees", 2500, "Electrical")
# MSR: event post types
r = get("https://www.microsoft.com/en-us/research/wp-json/wp/v2/types", timeout=25).json()
for k, v in r.items():
    if "event" in k or "event" in v.get("name", "").lower():
        print("MSR TYPE", k, v.get("rest_base"), v.get("taxonomies"))
show("https://www.microsoft.com/en-us/research/wp-json/wp/v2/msr-event?per_page=3", 3000)
show("https://www.microsoft.com/en-us/research/wp-json/wp/v2/msr-region?per_page=50&_fields=id,name,slug", 2500)
# KIAC posts
show("https://kiac.iisc.ac.in/wp-json/wp/v2/posts?per_page=6&_fields=date,link,title,categories", 2500)
show("https://kiac.iisc.ac.in/news-and-events/", 3000, "Latest")
