"""
Shared helpers for every Event Horizon 2.0 source.

One HTTP session with retries, one date parser that understands the date
formats academic sites actually use, and a tolerant iCal reader.
"""

import datetime as dt
import html as _html
import os
import re
import time
from urllib.parse import urlparse

import requests
from dateutil import parser as dateparser
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

REPO = os.environ.get("GITHUB_REPOSITORY", "Astrophysicist-Abhi26/event-horizon-2.0")
UA = f"EventHorizon2/1.0 (academic event aggregator; +https://github.com/{REPO})"
TIMEOUT = 30
CONNECT_TIMEOUT = 10     # a host that does not answer at all fails in seconds, not minutes


def session():
    s = requests.Session()
    retry = Retry(total=3, connect=1, backoff_factor=1.5,
                  status_forcelist=(429, 500, 502, 503, 504),
                  allowed_methods=("GET",), respect_retry_after_header=True)
    s.mount("https://", HTTPAdapter(max_retries=retry))
    s.mount("http://", HTTPAdapter(max_retries=retry))
    s.headers.update({"User-Agent": UA})
    return s


HTTP = session()


BROWSER_UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 14_5) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
_BROWSER_HEADERS = {"User-Agent": BROWSER_UA,
                    "Accept": "text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8",
                    "Accept-Language": "en-IN,en;q=0.9"}


# robots.txt: a site's own published rules for automated readers. We read it once per
# host per run and skip any page it asks tools like ours not to read (RFC 9309).
# EH_ROBOTS=enforce (default) | report (fetch anyway, list what would be skipped) | off.
ROBOTS_TOKEN = "EventHorizon2"
_ROBOTS = {}
ROBOTS_BLOCKED = []          # pages robots.txt asked us not to read, this run
BROWSER_UA_HOSTS = set()     # hosts that refused our named agent and answered a browser's


class RobotsDisallowed(requests.exceptions.RequestException):
    """The site's robots.txt asks automated tools not to read this page."""


def _robots_mode():
    return os.environ.get("EH_ROBOTS", "enforce").lower()


def robots_allowed(url):
    """True unless the host's robots.txt disallows `url` for us (or for every agent).
    No robots.txt (4xx) means no rules. When the file cannot be read at all (timeout,
    5xx) we read the page as before rather than lose the source: the page itself will
    usually fail the same way."""
    from urllib import robotparser
    p = urlparse(url)
    root = f"{p.scheme}://{p.netloc}"
    rp = _ROBOTS.get(root)
    if rp is None:
        rp = robotparser.RobotFileParser()
        try:
            r = HTTP.get(root + "/robots.txt", timeout=(CONNECT_TIMEOUT, 15))
            text = r.text if r.status_code < 400 else ""
            ctype = (getattr(r, "headers", None) or {}).get("content-type", "")
            if "html" in ctype.lower():      # a "page not found" page served as robots.txt
                text = ""
            rp.parse(text.splitlines())
        except requests.exceptions.ConnectTimeout:
            _DEAD_HOSTS.add(p.netloc.lower())
            rp.parse([])
        except Exception:
            rp.parse([])
        _ROBOTS[root] = rp
    return rp.can_fetch(ROBOTS_TOKEN, url)


def reset_robots():
    _ROBOTS.clear()
    ROBOTS_BLOCKED.clear()
    BROWSER_UA_HOSTS.clear()


# A host that did not even accept a connection is skipped for the rest of the run:
# without this, every source on it waits out its own timeouts (IIT Bombay Maths has
# two sources and cost ~100 s a run while its server was unreachable).
_DEAD_HOSTS = set()


def reset_dead_hosts():
    _DEAD_HOSTS.clear()


def get(url, insecure_ok=False, **kw):
    """GET with retries. Two fallbacks, both needed by Indian institute sites:
    * 403/406 with our honest bot UA -> retry once with a browser UA
      (several .res.in / .ac.in firewalls reject unknown agents outright);
    * TLS certificate-chain error -> retry without verification, but ONLY
      for sources marked `insecure_ok: true` in institutes.yaml (read-only
      public pages whose servers ship an incomplete certificate chain).
    """
    kw.setdefault("timeout", TIMEOUT)
    if isinstance(kw["timeout"], (int, float)):      # (connect, read)
        kw["timeout"] = (min(CONNECT_TIMEOUT, kw["timeout"]), kw["timeout"])
    headers = kw.pop("headers", None) or {}
    # A feed (iCal, RSS, Indico export, events API) is published by its owner for calendar
    # apps to subscribe to; robots.txt governs crawling web pages, so it is not consulted.
    feed = kw.pop("feed", False)
    verify = True
    host = urlparse(url).netloc.lower()
    if host in _DEAD_HOSTS:
        raise requests.exceptions.ConnectTimeout(f"{host} did not answer earlier in this run")
    if not feed:
        check_robots(url)
    try:
        r = HTTP.get(url, headers=headers, **kw)
    except requests.exceptions.ConnectTimeout:
        _DEAD_HOSTS.add(host)
        raise
    except requests.exceptions.SSLError:
        if not insecure_ok:
            raise
        import urllib3
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        verify = False
        r = HTTP.get(url, headers=headers, verify=False, **kw)
    if r.status_code in (403, 406):
        r = HTTP.get(url, headers={**headers, **_BROWSER_HEADERS}, verify=verify, **kw)
        if r.status_code < 400:
            BROWSER_UA_HOSTS.add(host)
    r.raise_for_status()
    # A server that names no charset gets ISO-8859-1 from requests, which turns
    # UTF-8 "It's" into "Itâs" (IIT Madras). Let the bytes decide instead.
    ctype = (getattr(r, "headers", None) or {}).get("content-type", "")
    if "charset" not in ctype.lower() and ("text" in ctype or "html" in ctype or "xml" in ctype):
        r.encoding = r.apparent_encoding or "utf-8"
    return r


def check_robots(url):
    """Raise RobotsDisallowed if the site's robots.txt asks us not to read `url`."""
    mode = _robots_mode()
    if mode == "off" or robots_allowed(url):
        return
    ROBOTS_BLOCKED.append(url)
    if mode == "enforce":
        raise RobotsDisallowed(f"the site's robots.txt asks automated tools not to read {url}")


def polite_sleep(seconds=0.4):
    time.sleep(seconds)


def today():
    return dt.date.today()


# ---------------------------------------------------------------------------
# Text
# ---------------------------------------------------------------------------
def clean(text):
    if text is None:
        return ""
    text = _html.unescape(str(text))
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def norm_title(title):
    """Canonical form used for cross-source de-duplication."""
    t = clean(title).lower()
    t = re.sub(r"\b(20\d\d)\b", r" \1 ", t)
    t = re.sub(r"[^a-z0-9 ]+", " ", t)
    t = re.sub(r"\b(the|a|an|on|of|and|in|for|at|workshop|conference|"
               r"international|meeting|school)\b", " ", t)
    return re.sub(r"\s+", " ", t).strip()


# Placeholders and housekeeping that calendar feeds carry (seen on 2026-11-05: "TBA", "vacant",
# "-Férié", "HE215 final exam", "*** CANCELLED *** ..."; on 2026-11-09: "Titre à venir",
# "TBA ENS", "(Thibault) TBA - ICJ", "Séminaire de Probabilités: Vacances", "Séminaire …: -").
# They are not events a visitor can attend.
_PLACEHOLDER = (r"tba|tbd|tbc|to be (?:announced|confirmed|determined)|(?:à|a) (?:confirmer|pr[ée]ciser)|"
                r"titre (?:et r[ée]sum[ée] )?(?:à|a) (?:venir|pr[ée]ciser|confirmer|d[ée]finir)|"
                r"(?:à|a) venir|f[ée]ri[ée]|jour f[ée]ri[ée]|vacances(?: \w+){0,2}|rel[âa]che")
_VENUE = r"(?:\s*[-–—]?\s*(?-i:[A-Z][A-Z-]{1,8}))?"      # "TBA ENS", "TBA - ICJ" (a capitalised venue code)
_Q = "[\"“”«»'‘’]?"
JUNK_TITLE = re.compile(
    r"^\W*$"                                                     # "-", "—": no words at all
    r"|^\W*(?:tba|tbd|tbc|vacant|none|n/?a|no (?:seminar|talk|session)s?|seminars?|talks?|colloquium|"
    r"meetings?|bi-?weekly meetings?|pause\b.*|f[ée]ri[ée]|jour f[ée]ri[ée].*|public holiday|holiday|closed)\W*$"
    rf"|(?:^|[:,\-–—]\s*)(?:\([^()]{{1,40}}\)\s*)?{_Q}\s*(?:{_PLACEHOLDER})\s*{_Q}(?:\s*\([^()]{{1,40}}\))?{_VENUE}\s*\.?\s*$"
    rf"|[:\-–—]\s*$|:\s*[-–—]+{_VENUE}\s*$"                         # "Séminaire …: -", "Séminaire …: - ICJ"
    r"|\bcancel+ed\b|\bannul[ée]e?\b|\bpostponed\b|\bexams?\b", re.I)


# ---------------------------------------------------------------------------
# Dates
# ---------------------------------------------------------------------------
MONTHS = ("jan|feb|mar|apr|may|jun|jul|aug|sep|sept|oct|nov|dec|january|"
          "february|march|april|june|july|august|september|october|"
          "november|december")
_M = rf"(?:{MONTHS})\.?"
_SEP = r"\s*(?:-|–|—|to|until|till)\s*"
_WD = r"(?:(?:mon|tue|wed|thu|fri|sat|sun)[a-z]*,?\s+)?"   # optional weekday

# Ordered from most to least specific. Each yields (start_text, end_text).
_RANGE_PATTERNS = [
    # 06 July 2026 to 10 July 2026 / 30 Nov 2026 - 4 Dec 2026
    re.compile(rf"(\d{{1,2}},?\s+{_M},?\s+\d{{4}}){_SEP}{_WD}(\d{{1,2}},?\s+{_M},?\s+\d{{4}})", re.I),
    # November 30, 2025 - December 7, 2025
    re.compile(rf"({_M}\s+\d{{1,2}},?\s+\d{{4}}){_SEP}({_M}\s+\d{{1,2}},?\s+\d{{4}})", re.I),
    # 30 Nov - 4 Dec 2026 / 30 Nov - 4 Dec, 2026
    re.compile(rf"(\d{{1,2}}\s+{_M}){_SEP}(\d{{1,2}}\s+{_M},?\s+(\d{{4}}))", re.I),
    # November 30 - December 7, 2025
    re.compile(rf"({_M}\s+\d{{1,2}}){_SEP}({_M}\s+\d{{1,2}},?\s+(\d{{4}}))", re.I),
    # 7-11 September 2026 / 7 – 11 Sep 2026 / 13 – 17 December, 2025
    re.compile(rf"(\d{{1,2}}){_SEP}(\d{{1,2}})\s+({_M}),?\s+(\d{{4}})", re.I),
    # September 7-11, 2026
    re.compile(rf"({_M})\s+(\d{{1,2}}){_SEP}(\d{{1,2}}),?\s+(\d{{4}})", re.I),
    # ISO range 2026-09-07 to 2026-09-11
    re.compile(rf"(\d{{4}}-\d{{2}}-\d{{2}}){_SEP}(\d{{4}}-\d{{2}}-\d{{2}})"),
    # Indian numeric, day first: 01/02/2027 - 05/02/2027 (also "01/02/2027 05/02/2027"
    # when a table puts start and end in adjacent cells)
    re.compile(r"\b(\d{1,2}[/.]\d{1,2}[/.]\d{4})(?:\s*(?:-|–|—|to|until|till)\s*|\s+)"
               r"(\d{1,2}[/.]\d{1,2}[/.]\d{4})\b"),
    # 12 Feb - Feb 16 2027 (IIT BHU: day-month, then month-day)
    re.compile(rf"(\d{{1,2}}\s+{_M}){_SEP}({_M}\s+\d{{1,2}},?\s+(\d{{4}}))", re.I),
]
_SINGLE_PATTERNS = [
    re.compile(r"(\d{4}-\d{2}-\d{2})"),
    re.compile(r"\b(\d{1,2}[/.]\d{1,2}[/.]\d{4})\b"),
    re.compile(rf"(\d{{1,2}}(?:st|nd|rd|th)?,?\s+{_M},?\s+\d{{4}})", re.I),
    re.compile(rf"({_M}\s+\d{{1,2}}(?:st|nd|rd|th)?,?\s+\d{{4}})", re.I),
]


def iso(value, dayfirst=True):
    """Best-effort 'YYYY-MM-DD' or None. Never invents a year."""
    if value is None or value == "":
        return None
    if isinstance(value, dt.datetime):
        return value.date().isoformat()
    if isinstance(value, dt.date):
        return value.isoformat()
    if isinstance(value, dict):  # Indico {"date": ..., "time": ...}
        value = value.get("date") or ""
    s = clean(value)
    m = re.match(r"^(\d{4})(\d{2})(\d{2})(?:T|$)", s)  # iCal 20261012 / 20261012T...
    if m:
        return f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
    if not re.search(r"\d{4}", s):
        return None
    m = re.match(r"^(\d{4})-(\d{2})-(\d{2})", s)            # ISO: never reinterpret
    if m:
        try:
            return dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3))).isoformat()
        except ValueError:
            return None
    s = re.sub(r"(\d)(st|nd|rd|th)\b", r"\1", s)
    # Parse twice with different defaults: if the results differ, the text was
    # missing a day or month and dateutil silently filled it in -> reject.
    try:
        a = dateparser.parse(s, fuzzy=True, dayfirst=dayfirst,
                             default=dt.datetime(2000, 1, 1))
        b = dateparser.parse(s, fuzzy=True, dayfirst=dayfirst,
                             default=dt.datetime(2001, 2, 2))
    except (ValueError, OverflowError, TypeError):
        return None
    if (a.month, a.day) != (b.month, b.day) or a.year != b.year:
        return None
    return a.date().isoformat()


def _dmy(s):
    """'01/02/2027' -> '2027-02-01' (Indian convention: day first). Rejects
    impossible dates instead of guessing."""
    m = re.fullmatch(r"(\d{1,2})[/.](\d{1,2})[/.](\d{4})", s.strip())
    if not m:
        return None
    try:
        return dt.date(int(m.group(3)), int(m.group(2)), int(m.group(1))).isoformat()
    except ValueError:
        return None


def parse_date_range(text):
    """Find the first date or date range in free text -> (start, end)."""
    if not text:
        return None, None
    t = clean(text).replace("\u2009", " ")
    # "8th - 10th December 2026" -> "8 - 10 December 2026", so day ranges written
    # with ordinals are read as ranges, not just their last day
    t = re.sub(r"\b(\d{1,2})(?:st|nd|rd|th)\b", r"\1", t)
    t = t.replace("|", " ")                     # "12 Feb - Feb 16 | 2027"
    for i, pat in enumerate(_RANGE_PATTERNS):
        m = pat.search(t)
        if not m:
            continue
        g = m.groups()
        if i in (0, 1, 6):
            a, b = iso(g[0]), iso(g[1])
        elif i == 7:
            a, b = _dmy(g[0]), _dmy(g[1])
        elif i in (2, 3, 8):
            a, b = iso(f"{g[0]} {g[2]}"), iso(g[1])
        elif i == 4:
            a, b = iso(f"{g[0]} {g[2]} {g[3]}"), iso(f"{g[1]} {g[2]} {g[3]}")
        else:
            a, b = iso(f"{g[1]} {g[0]} {g[3]}"), iso(f"{g[2]} {g[0]} {g[3]}")
        if a and b and b < a:  # "Dec 28 - Jan 3, 2027": start is previous year
            try:
                a = (dt.date.fromisoformat(a).replace(year=int(b[:4]) - 1)).isoformat()
            except ValueError:
                pass
        if a:
            return a, b or a
    for pat in _SINGLE_PATTERNS:
        m = pat.search(t)
        if m:
            d = _dmy(m.group(1)) if re.fullmatch(r"\d{1,2}[/.]\d{1,2}[/.]\d{4}", m.group(1)) \
                else iso(m.group(1))
            if d:
                return d, d
    return None, None


# ---------------------------------------------------------------------------
# iCal (RFC 5545) — small tolerant reader, enough for public calendars
# ---------------------------------------------------------------------------
def parse_ics(text):
    lines = []
    for raw in text.splitlines():
        if raw[:1] in (" ", "\t") and lines:
            lines[-1] += raw[1:]
        else:
            lines.append(raw.rstrip("\r"))
    events, ev = [], None
    for ln in lines:
        if ln == "BEGIN:VEVENT":
            ev = {}
        elif ln == "END:VEVENT" and ev is not None:
            events.append(ev)
            ev = None
        elif ev is not None and ":" in ln:
            key, val = ln.split(":", 1)
            key = key.split(";")[0].upper()
            val = (val.replace("\\,", ",").replace("\\;", ";")
                      .replace("\\n", "\n").replace("\\N", "\n").strip())
            ev[key] = val
    return events


def ics_end_date(start, dtend_raw, all_day):
    """iCal all-day DTEND is exclusive; convert to inclusive end."""
    end = iso(dtend_raw) if dtend_raw else None
    if end and all_day and start and end > start:
        end = (dt.date.fromisoformat(end) - dt.timedelta(days=1)).isoformat()
    return end or start


def first_url(text):
    m = re.search(r"https?://[^\s<>\"')]+", text or "")
    return m.group(0).rstrip(".,;") if m else None
