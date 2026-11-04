import os, yaml
import profiles as P
import taxonomy as T
from classify import classify, keyword_hits

PROFILE = P.load()["cosmology-ml"]     # Event Horizon's original ranking


def score(ev):
    subs, _, basis = classify(ev)
    return PROFILE.score(subs, ev.get("region"), ev.get("type"), basis)

LABELS = yaml.safe_load(open(os.path.join(os.path.dirname(T.__file__), "labels.yaml")))

def test_taxonomy_consistent():
    original = {s for s in T.SUBFIELDS if s not in T.PARENT_SF and s not in T.INHERITS and s not in T.MIRRORS}
    assert original == set(T.PROTOTYPES)           # the embedding classifier knows only these
    assert set(T.RULES) == original | set(T.PARENT_SF)
    assert all(T.SUBFIELDS[s][0] in T.FIELDS for s in T.SUBFIELDS)
    # a topic sits in the same field as its sub-field, and every sub-field resolves to its field
    for t, up in T.PARENT_SF.items():
        assert up in T.SUBFIELDS and T.parent(t) == T.parent(up), t
    for s in T.SUBFIELDS:
        assert T.ancestors(s)[-1] == T.parent(s)

def test_labelled_set_field_accuracy():
    ok = 0
    for title, lab in LABELS:
        subs, fields, _ = classify({"title": title})
        ok += (not subs) if lab.startswith("neg") else (T.parent(lab) in fields)
    assert ok / len(LABELS) >= 0.95, f"field accuracy {ok}/{len(LABELS)}"

def test_word_boundaries():
    # v1-v4: "bao" matched a speaker called Bao, "desi" matched "design"
    assert "cosmo.lss" not in keyword_hits("Metric State Estimation for Robots — Bao Nguyen")
    assert "cosmo.lss" not in keyword_hits("Design principles for interfaces")
    assert "cosmo.lss" in keyword_hits("New BAO constraints from DESI")
    assert "phys.general" not in keyword_hits("Astrophysics of compact objects")  # 'physics' inside 'astrophysics'

def test_no_blanket_tags():
    # v1-v4: every ICTS event got astro+physics+math regardless of topic
    subs, fields, _ = classify({"title": "Winter School on Biological Physics"})
    assert "astro" not in fields and "cosmo" not in fields

def test_declared_codes_win():
    ev = {"title": "Modularity in genus 2", "declared": ["math_NT"]}
    tags = classify(ev)[0]
    assert len(tags) == 1 and "math.nt" in T.ancestors(tags[0])      # a number-theory topic
    assert score(ev) >= 20                     # visible at the default threshold

def test_cosmology_profile_ranks_cosmology_highest():
    s_cosmo = score({"title": "Dark energy and the Hubble tension"})
    s_nt = score({"title": "Modular forms and L-functions"})
    s_cm = score({"title": "Superconductivity in twisted bilayers"})
    assert s_cosmo > s_nt > s_cm

def test_cosmo_ml_intersection_bonus():
    s = score({"title": "Simulation-based inference for DESI dark energy constraints"})
    assert s >= 90

def test_local_bonus():
    base = {"title": "Recent advances in low-dimensional topology"}
    far = score({**base, "region": "abroad"})
    near = score({**base, "region": "bengaluru"})
    assert near == far + PROFILE.places["bengaluru"]

def test_watchlist_fields():
    subs, _, _ = classify({"title": "Some meeting", "declared": ["field:cosmo.de", "field:ai.science"]})
    assert set(subs) == {"cosmo.de", "ai.science", "phys.cosmo"}     # cosmology is also shown under Physics
    # a bare 'math' topic from a source stays WEAK and does not tag on its own
    assert classify({"title": "x", "declared": ["math"]})[0] == []


def test_display_tree_covers_every_tag_and_shares_branches():
    """The site's five disciplines show every tag somewhere, and a shared branch is
    the same branch (same id, topics and members) wherever it appears."""
    tree = T.display_tree()
    assert [d["id"] for d in tree] == ["physics", "astro", "math", "cs", "ai"]
    members = {m for d in tree for b in d["branches"] for m in b["members"]}
    assert set(T.SUBFIELDS) <= members
    seen = {}
    for d in tree:
        for b in d["branches"]:
            if b["id"] in seen:
                assert b == seen[b["id"]]
            seen[b["id"]] = b
    where = {k: [d["id"] for d in tree if any(b["id"] == k for b in d["branches"])]
             for k in T.SHARED}
    assert where == {"@gr": ["physics", "astro"], "@cosmology": ["physics", "astro"],
                     "@mathphys": ["physics", "math"]}
    # the catch-all of each discipline comes last
    for d in tree:
        assert "general" in d["branches"][-1]["id"] or d["branches"][-1]["id"] == "math.other"
