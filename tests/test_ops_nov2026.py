"""Fixes after the November 2026 audit: see RUNBOOK.md for each incident."""
import datetime as dt
import json

import pytest
import requests

import common
import notify
import scrape as S
import sources_india as SI


# --- 1. a dead host is skipped for the rest of the run ---------------------------------
def test_dead_host_is_not_retried_in_the_same_run(monkeypatch):
    common.reset_dead_hosts()
    calls = []

    def boom(url, **kw):
        calls.append(url)
        raise requests.exceptions.ConnectTimeout("no route")
    monkeypatch.setattr(common.HTTP, "get", boom)
    with pytest.raises(requests.exceptions.ConnectTimeout):
        common.get("https://dead.example.org/a")
    with pytest.raises(requests.exceptions.ConnectTimeout):
        common.get("https://dead.example.org/b")           # second source on the same host
    assert calls == ["https://dead.example.org/a"]
    common.reset_dead_hosts()


def test_a_slow_answer_does_not_mark_the_host_dead(monkeypatch):
    common.reset_dead_hosts()
    monkeypatch.setattr(common.HTTP, "get",
                        lambda url, **kw: (_ for _ in ()).throw(requests.exceptions.ReadTimeout("slow")))
    with pytest.raises(requests.exceptions.ReadTimeout):
        common.get("https://slow.example.org/")
    assert "slow.example.org" not in common._DEAD_HOSTS


# --- 2. next year's page may not exist yet (IISc Mathematics, 404 in November) ----------
def test_missing_lookahead_page_is_ignored(monkeypatch):
    monkeypatch.setattr(SI, "today", lambda: dt.date(2026, 11, 4))
    cfg = {"name": "IISc Maths", "url": "https://x.ac.in/Seminars{year}.html"}
    seen = []

    def one(url):
        seen.append(url)
        if "2027" in url:
            raise requests.HTTPError("404 Client Error")
        return [{"title": "a seminar"}]
    assert SI._collect(cfg, one) == [{"title": "a seminar"}]
    assert seen == ["https://x.ac.in/Seminars2026.html", "https://x.ac.in/Seminars2027.html"]


def test_missing_current_page_is_still_an_error(monkeypatch):
    monkeypatch.setattr(SI, "today", lambda: dt.date(2026, 11, 4))
    cfg = {"name": "IISc Maths", "url": "https://x.ac.in/Seminars{year}.html"}

    def one(url):
        if "2026" in url:
            raise requests.HTTPError("404 Client Error")
        return [{"title": "next year"}]
    with pytest.raises(requests.HTTPError):
        SI._collect(cfg, one)


# --- 3. only the repository's people can put events on the site ------------------------
def test_intake_ignores_strangers_unless_verified():
    mine = {"author_association": "OWNER", "labels": []}
    outsider = {"author_association": "NONE", "labels": [{"name": "add-event"}]}
    approved = {"author_association": "NONE", "labels": [{"name": "add-event"}, {"name": "verified"}]}
    pr = {"author_association": "OWNER", "pull_request": {}, "labels": []}
    assert SI._trusted_issue(mine) and SI._trusted_issue(approved)
    assert not SI._trusted_issue(outsider) and not SI._trusted_issue(pr)


def test_intake_end_to_end_drops_the_stranger(monkeypatch):
    form = "### Event name\n\nGood Meeting\n\n### Link\n\nhttps://good.example.org\n\n### Start date\n\n2099-01-02"
    issues = [dict(number=1, title="[Event] Good", body=form, author_association="OWNER", labels=[]),
              dict(number=2, title="[Event] Spam", body=form.replace("Good", "Spam"),
                   author_association="NONE", labels=[{"name": "add-event"}])]
    monkeypatch.setenv("GITHUB_REPOSITORY", "o/r")
    monkeypatch.setattr(SI, "get", lambda *a, **kw: type("R", (), {"json": lambda self: issues})())
    assert [e["title"] for e in SI.scrape_issue_intake()] == ["Good Meeting"]


# --- 4. health bookkeeping and alerts --------------------------------------------------
def _run(prev_health, fn, today="2026-11-04", monkeypatch=None):
    class D(dt.date):
        @classmethod
        def today(cls):
            return dt.date.fromisoformat(today)
    monkeypatch.setattr(S.dt, "date", D)
    monkeypatch.setattr(S, "GLOBAL_SOURCES", [("Flaky", fn, 0)])
    monkeypatch.setattr(S, "india_sources", lambda: [])
    monkeypatch.setattr(S, "scrape_watchlist", lambda: [])
    monkeypatch.setattr(S, "scrape_issue_intake", lambda: [])
    return S.run_sources(prev_health, [])[1][0]


def _boom():
    raise RuntimeError("down")


def test_bad_since_is_kept_and_a_week_of_failure_alerts_once(monkeypatch):
    h = _run([], _boom, "2026-11-04", monkeypatch)
    assert (h["status"], h["bad_since"], h["long_due"]) == ("error", "2026-11-04", False)
    h = _run([h], _boom, "2026-11-10", monkeypatch)
    assert (h["bad_since"], h["long_due"]) == ("2026-11-04", False)       # 6 days
    h = _run([h], _boom, "2026-11-11", monkeypatch)
    assert (h["bad_since"], h["long_due"], h["long_alerted"]) == ("2026-11-04", True, True)
    h = _run([h], _boom, "2026-11-12", monkeypatch)
    assert h["long_due"] is False and h["long_alerted"] is True            # once, not daily
    h = _run([h], lambda: [{"title": "x"}], "2026-11-13", monkeypatch)
    assert (h["status"], h["bad_since"], h["long_alerted"]) == ("ok", None, False)


def test_chronic_failure_alert_lists_every_broken_source(tmp_path, monkeypatch):
    monkeypatch.setattr(S, "NOTIFY_DIR", str(tmp_path))
    S.notifications([
        {"name": "Old", "status": "error", "previous": "error", "message": "timeout",
         "bad_since": "2026-10-25", "long_due": True},
        {"name": "Fresh", "status": "stale", "previous": "ok", "message": "502", "bad_since": "2026-11-04"}])
    body = (tmp_path / "health.md").read_text()
    assert "- **Fresh** — stale 502" in body and "- **Old** — error since 2026-10-25" in body
    assert "enabled: false" in body
    assert json.loads((tmp_path / "bad.json").read_text()) == ["Old", "Fresh"]


# --- 5. notify.py: closes recovered alerts, survives API errors -----------------------
def test_alert_resolution_by_named_sources():
    body = "These sources stopped returning events:\n\n- **IISc (institute events)** — stale x\n- **B** — error y"
    assert notify.listed_sources(body) == ["IISc (institute events)", "B"]
    assert not notify.resolved(body, {"B"})
    assert notify.resolved(body, {"Some other chronic source"})        # unrelated failures do not hold it open
    assert notify.resolved("old format, no names", set()) and not notify.resolved("old format", {"A"})


def _notify_env(tmp_path, monkeypatch, bad, health_md=None, issues=()):
    monkeypatch.setattr(notify, "NOTIFY_DIR", str(tmp_path))
    (tmp_path / "bad.json").write_text(json.dumps(bad))
    if health_md:
        (tmp_path / "health.md").write_text(health_md)
    log = []

    def fake_gh(*args, **kw):
        log.append(args)
        if args[:2] == ("issue", "list"):
            return json.dumps(list(issues))
        return "ok"
    monkeypatch.setattr(notify, "gh", fake_gh)
    return log


def test_notify_closes_only_recovered_alerts(tmp_path, monkeypatch):
    issues = [{"number": 29, "body": "- **IISc (institute events)** — stale"},
              {"number": 22, "body": "- **IIT Bombay Mathematics seminars** — error"}]
    log = _notify_env(tmp_path, monkeypatch, ["IIT Bombay Mathematics seminars"], issues=issues)
    notify.main()
    closed = [a[2] for a in log if a[:2] == ("issue", "close")]
    assert closed == ["29"]


def test_notify_posts_new_alert_before_closing_old_ones(tmp_path, monkeypatch):
    log = _notify_env(tmp_path, monkeypatch, ["A"], health_md="- **A** — error",
                      issues=[{"number": 5, "body": "- **Z** — stale"}])
    notify.main()
    verbs = [a[:2] for a in log if a[0] == "issue"]
    assert verbs.index(("issue", "create")) < verbs.index(("issue", "close"))


def test_notify_keeps_old_alerts_when_the_new_one_cannot_be_posted(tmp_path, monkeypatch):
    log = _notify_env(tmp_path, monkeypatch, ["A"], health_md="- **A** — error",
                      issues=[{"number": 5, "body": "- **Z** — stale"}])
    monkeypatch.setattr(notify, "gh", lambda *a, **kw: json.dumps([{"number": 5, "body": ""}])
                        if a[:2] == ("issue", "list") else (None if a[:2] == ("issue", "create") else "ok"))
    notify.main()                                  # must not raise
    assert not any(a[:2] == ("issue", "close") for a in log)


def test_unreliable_sources_never_raise_alerts(tmp_path, monkeypatch):
    """researchseminars.org does not answer GitHub's runners: shown in health, never alerted."""
    import json, os
    import scrape as S
    monkeypatch.setattr(S, "NOTIFY_DIR", str(tmp_path))
    health = [dict(name="researchseminars.org talks", status="stale", message="ConnectTimeout", previous="ok", long_due=True),
              dict(name="Some institute", status="error", message="HTTP 500", previous="ok", long_due=False)]
    S.notifications(health)
    assert json.load(open(tmp_path / "bad.json")) == ["Some institute"]
    assert "researchseminars" not in open(tmp_path / "health.md").read()


def test_empty_ok_marks_a_listing_as_allowed_to_be_empty():
    import sources_india as SI
    assert "ARIES seminars" in SI.empty_ok_names()


def test_placeholders_holidays_exams_and_cancelled_events_are_dropped():
    import scrape as S
    junk = ["TBA", "TBD", "vacant", "Seminar", "-Férié", "Pause pédagogique", 'Laurent Bourgeois: "TBA"',
            "Adrien Abgrall, \"TBA\"", "HE215 final exam (Chep office)", "*** CANCELLED *** 1st Joint Kuwait University-ICTP Science Symposium",
            "Workshop postponed", "exam for Math Methods"]
    keep = ["Workshop on Black Holes", "Examining dark matter with lensing", "Seminar on TBA-free methods",
            "Introduction to the TBA equations of integrable models", "Exact WKB and Seminars in Algebra"]
    for t in junk:
        assert S.JUNK_TITLE.search(t), t
    for t in keep:
        assert not S.JUNK_TITLE.search(t), t


def test_too_little_text_blocks_language_model_guesses():
    import scrape as S
    assert S.too_little_text({"title": "Massyle Dendene", "description": ""})
    assert S.too_little_text({"title": "-Férié", "description": ""})
    assert not S.too_little_text({"title": "Workshop on gravitational wave astronomy", "description": ""})
    assert not S.too_little_text({"title": "Joe Formaggio (MIT)", "description": "Neutrino mass measurement with Project 8 and KATRIN at MIT"})


def test_indico_seminar_slot_titled_with_a_name_gets_its_series(monkeypatch):
    import sources_india as SI
    data = {"results": [
        {"title": "Paolo Bellingeri", "category": "Séminaire de Probabilités", "url": "https://x/e/1", "startDate": {"date": "2099-01-05", "time": "10:00:00"}, "endDate": {"date": "2099-01-05", "time": "11:00:00"}},
        {"title": "Algebra Down Under", "category": "Conferences", "url": "https://x/e/2", "startDate": {"date": "2099-01-06", "time": "10:00:00"}, "endDate": {"date": "2099-01-06", "time": "11:00:00"}}]}
    monkeypatch.setattr(SI, "get", lambda url, **kw: type("R", (), {"json": lambda self: data, "text": ""})())
    out = SI._indico({"name": "x", "base": "https://x", "category": 0})
    assert out[0]["title"] == "Séminaire de Probabilités: Paolo Bellingeri" and out[0]["speaker"] == "Paolo Bellingeri"
    assert out[1]["title"] == "Algebra Down Under"
    assert "Séminaire de Probabilités" in out[0]["description"]
