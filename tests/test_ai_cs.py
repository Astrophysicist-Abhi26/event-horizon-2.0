"""AI / ML and computer science: finer topics, the CS conference databases, profiles."""
import datetime as dt
import io
import os
import zipfile

import yaml

import profiles as P
import scrape as S
import sources as G
import sources_india as SI
import taxonomy as T
from classify import classify

PROFILES = P.load()
SOON = (dt.date.today() + dt.timedelta(days=60)).isoformat()
LATER = (dt.date.today() + dt.timedelta(days=200)).isoformat()
PAST = (dt.date.today() - dt.timedelta(days=60)).isoformat()


def _tags(title, **kw):
    return classify({"title": title, **kw})[0]


# ---------------------------------------------------------------------------
# Topics
# ---------------------------------------------------------------------------
def test_finer_ai_topics():
    assert "ai.genai" in _tags("Workshop on large language models and in-context learning")
    assert "ai.vision" in _tags("Summer school on computer vision and multimodal learning")
    assert "ai.nlp" in _tags("Advances in machine translation for low-resource languages")
    assert "ai.rl" in _tags("Reinforcement learning and sequential decision making")
    assert "ai.trust" in _tags("Mechanistic interpretability and AI safety")
    assert "ai.theory" in _tags("Conference on Learning Theory")


def test_computer_science_topics():
    assert "cs.theory" in _tags("STOC 2027 — ACM Symposium on the Theory of Computing")
    assert "cs.security" in _tags("Post-quantum cryptography and zero-knowledge proofs")
    assert "cs.systems" in _tags("Workshop on distributed systems and cloud computing")
    assert "cs.pl" in _tags("Type systems and program verification")
    assert "cs.data" in _tags("Recommender systems and information retrieval")
    assert "cs.robotics" in _tags("Robot learning for legged locomotion")


def test_physics_words_do_not_leak_into_ai_or_cs():
    for title, bad in [
        ("Prompt emission of gamma-ray bursts", "ai.genai"),
        ("Spin alignment in galaxy clusters", "ai.trust"),
        ("Scaling laws in fully developed turbulence", "ai.theory"),
        ("Cell locomotion in active matter", "cs.robotics"),
        ("Fast algorithms for cosmological inference", "cs.theory"),
        ("Networking session for early-career astronomers", "cs.systems"),
        ("Robustness of the Hubble tension", "ai.trust"),
    ]:
        assert bad not in _tags(title), title


def test_ml_words_do_not_leak_into_physics():
    tags = _tags("Generative models", description="Diffusion and flow-based models; "
                 "flow matching for images")
    assert "phys.fluids" not in tags and "ai.genai" in tags


def test_ai_applied_to_physics_is_ml_for_science():
    assert "ai.science" in _tags("Transformers for gravitational-wave detection")
    assert "ai.science" not in _tags("Acoustics, speech and signal processing with deep learning")


def test_declared_codes():
    assert T.declared_codes("cs.CV") == [("ai.vision", T.STRONG)]
    assert T.declared_codes("cs_CR") == [("cs.security", T.STRONG)]
    assert T.declared_codes("eess.AS") == [("ai.nlp", T.STRONG)]
    assert T.declared_codes("cs.XY")[0][0] == "cs.general"
    assert T.declared_codes("ccf_ct") == [("cs.theory", T.STRONG)]
    assert T.declared_codes("mlss_rl") == [("ai.rl", T.STRONG)]
    assert T.declared_codes("computer-vision") == [("ai.vision", T.STRONG)]
    assert T.declared_codes("field:cs") == [("cs.general", T.STRONG)]


def test_declared_general_ml_venue_stays_general():
    tags = _tags("CVPR 2027 — Conference on Computer Vision", declared=["machine-learning"])
    assert set(tags) == {"ai.general", "ai.vision"}


def test_every_subfield_has_rules_and_a_prototype():
    for sf in T.SUBFIELDS:
        assert T.RULES.get(sf), sf
        assert T.PROTOTYPES.get(sf), sf


# ---------------------------------------------------------------------------
# Sources
# ---------------------------------------------------------------------------
class _Resp:
    def __init__(self, content):
        self.content = content
        self.text = content.decode("utf-8", "replace")


def _zip(files):
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as z:
        for name, data in files.items():
            z.writestr(name, yaml.safe_dump(data))
    return buf.getvalue()


def _date_text(a, b):
    a, b = dt.date.fromisoformat(a), dt.date.fromisoformat(b)
    return f"{a:%B} {a.day}-{b.day}, {a.year}" if a.month == b.month else \
        f"{a:%B} {a.day} - {b:%B} {b.day}, {a.year}"


def test_ai_deadlines_reads_every_venue_and_skips_past(monkeypatch):
    end = (dt.date.fromisoformat(SOON) + dt.timedelta(days=3)).isoformat()
    data = {
        "ai-deadlines-main/src/data/conferences/iros.yml": [
            {"title": "IROS", "year": 2027, "full_name": "Intelligent Robots and Systems",
             "link": "https://iros.org", "start": SOON, "end": end, "city": "Pune",
             "country": "India", "tags": ["robotics"],
             "deadlines": [{"type": "paper", "date": f"{LATER} 23:59:59"},
                           {"type": "paper", "date": f"{PAST} 23:59:59"}]}],
        "ai-deadlines-main/src/data/conferences/iclr.yml": [
            {"title": "ICLR", "year": 2027, "link": "https://iclr.cc", "start": SOON,
             "end": end, "tags": ["machine-learning", "computer-vision", "robotics"]},
            {"title": "ICLR", "year": 2020, "link": "https://iclr.cc", "start": PAST,
             "end": PAST, "tags": ["machine-learning"]}],
    }
    monkeypatch.setattr(G, "get", lambda url, **kw: _Resp(_zip(data)))
    evs = {e["title"]: e for e in G.scrape_ai_deadlines()}
    assert set(evs) == {"IROS 2027 — Intelligent Robots and Systems", "ICLR 2027"}
    assert evs["IROS 2027 — Intelligent Robots and Systems"]["deadline"] == LATER
    assert evs["ICLR 2027"]["declared"] == ["machine-learning"]      # broad venue = general ML


def test_ccf_deadlines_keeps_ranked_and_indian_venues(monkeypatch):
    end = (dt.date.fromisoformat(SOON) + dt.timedelta(days=3)).isoformat()
    when = _date_text(SOON, end)

    def conf(title, sub, ccf, core, place, date=when):
        return [{"title": title, "description": f"{title} long name", "sub": sub,
                 "rank": {"ccf": ccf, "core": core},
                 "confs": [{"year": 2027, "link": f"https://{title.lower()}.org", "date": date,
                            "place": place,
                            "timeline": [{"deadline": f"{LATER} 23:59:59",
                                          "abstract_deadline": f"{LATER} 12:00:00"}]}]}]
    data = {
        "ccf-deadlines-main/conference/CT/stoc.yml": conf("STOC", "CT", "A", "A*", "Atlanta, USA"),
        "ccf-deadlines-main/conference/SC/tiny.yml": conf("TINY", "SC", "C", "C", "Somewhere"),
        "ccf-deadlines-main/conference/SC/indo.yml": conf("INDOCRYPT", "SC", "N", "N",
                                                         "Bengaluru, India"),
        "ccf-deadlines-main/conference/AI/old.yml": conf("OLD", "AI", "A", "A*", "Paris",
                                                        date="June 1-3, 2020"),
    }
    monkeypatch.setattr(G, "get", lambda url, **kw: _Resp(_zip(data)))
    evs = {e["title"].split(" ")[0]: e for e in G.scrape_ccf_deadlines()}
    assert set(evs) == {"STOC", "INDOCRYPT"}
    assert evs["STOC"]["start_date"] == SOON and evs["STOC"]["declared"] == ["ccf_ct"]
    assert evs["STOC"]["title"] == "STOC 2027 — STOC long name"
    assert evs["STOC"]["deadline"] == LATER


def test_ml_schools(monkeypatch):
    data = [{"title": "Deep Learning Winter School", "link": "https://dl.school", "start": SOON,
             "end": SOON, "place": "Tromsø, Norway", "sub": ["ML", "CV"], "deadline": "TBA",
             "description": "Lectures on deep learning."},
            {"title": "Old school", "link": "https://old", "start": PAST, "end": PAST, "sub": ["ML"]}]
    monkeypatch.setattr(G, "get", lambda url, **kw: _Resp(yaml.safe_dump(data).encode()))
    evs = G.scrape_ml_schools()
    assert [e["title"] for e in evs] == ["Deep Learning Winter School"]
    assert evs[0]["declared"] == ["mlss_ml", "mlss_cv"] and evs[0]["raw_type"] == "school"
    assert evs[0]["deadline"] is None


def _raw(title, start, source, declared=()):
    return dict(title=title, url="https://x", start_date=start, end_date=start, deadline=None,
                location=None, country=None, online=False, tz=None, description="",
                speaker=None, source=source, raw_type="conference", declared=list(declared),
                priority=False)


def test_same_conference_from_two_databases_is_one_card():
    nxt = (dt.date.fromisoformat(SOON) + dt.timedelta(days=1)).isoformat()
    evs = S.dedupe(S.normalise([
        _raw("CVPR 2027 — IEEE/CVF Conference on Computer Vision", SOON, "AI Deadlines"),
        _raw("CVPR 2027 — Computer Vision and Pattern Recognition", nxt, "CCF Deadlines"),
        _raw("CVPR 2028 — IEEE/CVF Conference on Computer Vision", LATER, "AI Deadlines"),
    ]))
    assert len(evs) == 2
    assert sorted(evs[0]["sources"] + evs[1]["sources"]) == \
        ["AI Deadlines", "AI Deadlines", "CCF Deadlines"]


def test_series_key():
    assert S.series_key("CVPR 2027 — IEEE/CVF") == "cvpr 2027"
    assert S.series_key("IEEE VIS 2026 — Visualization") == "vis 2026"
    assert S.series_key("Dark energy 2026") is None
    assert S.series_key("The 2026 meeting") is None


def test_issue_form_ai_and_cs_fields():
    body = ("### Event name\n\nSchool on trustworthy ML\n\n### Start date\n\n2027-01-10\n\n"
            "### Research fields\n\n- [X] AI safety, fairness & interpretability\n"
            "- [X] Generative models & LLMs\n- [X] Algorithms & theory of computation\n"
            "- [X] Computer vision\n")
    it = SI.parse_issue_form("", body)
    assert it["fields"] == ["ai.trust", "ai.genai", "cs.theory", "ai.vision"]


def test_issue_form_options_all_map_to_a_topic():
    path = os.path.join(os.path.dirname(__file__), "..", ".github", "ISSUE_TEMPLATE",
                        "add-event.yml")
    with open(path) as f:
        form = yaml.safe_load(f)
    fields = next(b for b in form["body"] if b.get("id") == "fields")
    for opt in fields["attributes"]["options"]:
        body = f"### Research fields\n\n- [X] {opt['label']}\n"
        assert SI.parse_issue_form("x", body)["fields"], opt["label"]


# ---------------------------------------------------------------------------
# Profiles
# ---------------------------------------------------------------------------
def _score(pid, title, **kw):
    subs, _, basis = classify({"title": title, **kw})
    return PROFILES[pid].score(subs, kw.get("region"), kw.get("type"), basis)


def test_ai_and_cs_profiles_rank_their_fields_first():
    neurips = dict(title="NeurIPS 2026 — Neural Information Processing Systems",
                   declared=["machine-learning"])
    stoc = dict(title="STOC 2027 — Symposium on the Theory of Computing", declared=["ccf_ct"])
    colt = dict(title="COLT 2027 — Conference on Learning Theory", declared=["ccf_ai"])
    cosmo = dict(title="Dark energy and the Hubble tension")
    assert _score("machine-learning", **neurips) >= 90
    assert _score("machine-learning", **neurips) > _score("machine-learning", **cosmo)
    assert _score("computer-science", **stoc) >= 85
    assert _score("cosmology-ml", **stoc) == 0
    assert _score("ml-theory", **colt) == 100
    assert _score("ai-science", title="Simulation-based inference for cosmology") >= 100 - 1
    assert _score("explore", **stoc) == 50


def test_watchlist_event_without_a_page_links_to_its_entry():
    ev = SI._manual_event({"title": "Poster-only meeting", "start": SOON,
                           "notes": "Register through the poster."}, "Watchlist")
    assert ev["url"].endswith("/scraper/watchlist.yaml")      # the site shows the notes instead
    assert ev["description"] == "Register through the poster."


def test_ncm4_no_longer_points_at_a_homepage():
    ncm = next(e for e in SI.scrape_watchlist() if "Neighbourhood Cosmology" in e["title"])
    assert "christuniversity.in" not in ncm["url"]
    assert "poster" in ncm["description"]


def test_cmi_labelled_list():
    with open(os.path.join(os.path.dirname(__file__), "fixtures", "cmi_seminars.html")) as f:
        html = f.read()
    cfg = {"name": "CMI seminars", "location": "Chennai Mathematical Institute, Chennai, India",
           "type": "seminar"}
    evs = SI.labelled_list_from_html(cfg, html, "https://www.cmi.ac.in/activities/seminars.php")
    first = evs[0]
    assert first["title"] == "Quantum Battery: Science Fiction or Reality? — Sibasish Ghosh"
    assert first["start_date"] == "2026-10-12"
    assert first["speaker"] == "Sibasish Ghosh (Institute of Mathematical Sciences, Chennai)"
    assert first["location"] == "Lecture Hall 2, Chennai Mathematical Institute, Chennai, India"
    assert first["description"] == "Physics Seminar"
    no_year = next(e for e in evs if e["title"].startswith("Studying the redshift"))
    assert no_year["start_date"] == "2026-09-30"           # from the "30-09-26" line
    cs = evs[-1]
    assert cs["description"] == "Computer Science Seminar"
    assert {"ai.genai", "ai.trust"} <= set(_tags(cs["title"]))
    assert len(evs) >= 8


def test_cmi_registered():
    assert "CMI seminars" in [n for n, _, _ in SI.india_sources()]


def test_unreachable_hosts_fail_fast(monkeypatch):
    import common
    seen = {}

    class R:
        status_code = 200

        def raise_for_status(self):
            pass

    def fake(url, **kw):
        seen.update(kw)
        return R()
    monkeypatch.setattr(common.HTTP, "get", fake)
    common.get("https://example.org", timeout=90)
    assert seen["timeout"] == (common.CONNECT_TIMEOUT, 90)
    common.get("https://example.org")
    assert seen["timeout"] == (common.CONNECT_TIMEOUT, common.TIMEOUT)
