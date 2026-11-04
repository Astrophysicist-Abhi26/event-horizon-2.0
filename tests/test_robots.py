"""Sites' robots.txt rules are honoured, and the run reports what it skipped."""
import pytest
import requests

import common


class _R:
    def __init__(self, text, status=200, ctype="text/plain"):
        self.text, self.status_code, self.headers = text, status, {"content-type": ctype}
        self.apparent_encoding, self.encoding = "utf-8", None

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.HTTPError(f"{self.status_code}")


@pytest.fixture
def site(monkeypatch):
    common.reset_robots()
    common.reset_dead_hosts()
    monkeypatch.setenv("EH_ROBOTS", "enforce")
    pages = {}
    calls = []

    def fake(url, **kw):
        calls.append(url)
        return pages.get(url, _R("<html>page</html>", 200, "text/html"))
    monkeypatch.setattr(common.HTTP, "get", fake)
    return pages, calls


def test_disallowed_page_is_not_fetched(site):
    pages, calls = site
    pages["https://a.example/robots.txt"] = _R("User-agent: *\nDisallow: /private/\n")
    with pytest.raises(common.RobotsDisallowed):
        common.get("https://a.example/private/events.html")
    assert "https://a.example/private/events.html" not in calls
    assert common.get("https://a.example/events.html").status_code == 200
    assert calls.count("https://a.example/robots.txt") == 1          # read once per host


def test_rules_naming_us_apply(site):
    pages, _ = site
    pages["https://b.example/robots.txt"] = _R("User-agent: EventHorizon2\nDisallow: /\n\nUser-agent: *\nAllow: /\n")
    with pytest.raises(common.RobotsDisallowed):
        common.get("https://b.example/seminars")


def test_missing_or_html_robots_means_no_rules(site):
    pages, _ = site
    pages["https://c.example/robots.txt"] = _R("not found", 404)
    pages["https://d.example/robots.txt"] = _R("<html>Disallow: /</html>", 200, "text/html")
    assert common.get("https://c.example/x").status_code == 200
    assert common.get("https://d.example/x").status_code == 200


def test_report_mode_fetches_but_lists(site, monkeypatch):
    pages, calls = site
    monkeypatch.setenv("EH_ROBOTS", "report")
    pages["https://e.example/robots.txt"] = _R("User-agent: *\nDisallow: /\n")
    common.get("https://e.example/talks")
    assert "https://e.example/talks" in calls
    assert common.ROBOTS_BLOCKED == ["https://e.example/talks"]


def test_browser_agent_fallback_is_recorded(site):
    pages, _ = site
    seq = iter([_R("forbidden", 403), _R("<html>ok</html>", 200, "text/html")])
    pages["https://f.example/robots.txt"] = _R("")

    def fake(url, **kw):
        return pages[url] if url.endswith("robots.txt") else next(seq)
    import pytest as _p
    mp = _p.MonkeyPatch()
    mp.setattr(common.HTTP, "get", fake)
    try:
        assert common.get("https://f.example/news").status_code == 200
    finally:
        mp.undo()
    assert "f.example" in common.BROWSER_UA_HOSTS


def test_published_feeds_are_subscriptions_not_crawling(site):
    """Google Calendar's robots.txt disallows /calendar/, but a public iCal address is
    published by the calendar's owner for calendar apps to subscribe to."""
    pages, calls = site
    pages["https://calendar.google.com/robots.txt"] = _R("User-agent: *\nDisallow: /calendar/\n")
    url = "https://calendar.google.com/calendar/ical/x%40group.calendar.google.com/public/basic.ics"
    assert common.get(url, feed=True).status_code == 200
    with pytest.raises(common.RobotsDisallowed):
        common.get("https://calendar.google.com/calendar/embed?src=x")


def test_every_calendar_feed_is_fetched_as_a_feed():
    """A Google Calendar or .ics fetch without feed=True would be skipped by robots.txt
    (calendar.google.com disallows /calendar/): DESC was, on 2026-11-04."""
    import os, re
    here = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "scraper")
    for name in ("sources.py", "sources_india.py"):
        for line in open(os.path.join(here, name)):
            if re.search(r"\bget\((DESC_ICS|_gcal_url|f\"\{base\}/category/\{cat\}/events\.ics)", line):
                assert "feed=True" in line, (name, line)
