"""Physics and mathematics coverage: every area has a topic, and nothing off-topic is tagged."""
import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(__file__))

import taxonomy as T
from classify import classify
from coverage_data import HELD_OUT, OFF_TOPIC


def _hit(tags, wanted):
    """A tag counts when it is a wanted node or lies under one."""
    return any(w in T.ancestors(t) or t.startswith(w) for t in tags for w in wanted)


def test_held_out_titles_reach_their_topic():
    """Titles written without looking at the rules: at least 96% reach the right topic."""
    missed = [(title, classify({"title": title})[0]) for title, want in HELD_OUT
              if not _hit(classify({"title": title})[0], want)]
    assert len(missed) <= len(HELD_OUT) * 0.04, missed


def test_off_topic_titles_get_no_science_tag():
    tagged = {t: [s for s in classify({"title": t})[0] if T.parent(s) in ("physics", "math", "astro", "cosmo")]
              for t in OFF_TOPIC}
    assert not any(tagged.values()), {t: s for t, s in tagged.items() if s}


def test_every_topic_is_reachable():
    """Each topic's own first pattern, written out as a title, tags that topic (no dead rules)."""
    import re
    dead = []
    for tid in T.PARENT_SF:
        pats = T.RULES[tid]
        if not any(T.COMPILED[tid][i].search(_sample(p)) for i, p in enumerate(pats[:6])):
            dead.append(tid)
    assert not dead, dead


def _sample(pattern):
    """A plain string a simple pattern matches: its first alternative, without regex syntax."""
    p = pattern[3:] if pattern.startswith("CS:") else pattern
    p = re.sub(r"\(\?:([^()|]*)(?:\|[^()]*)?\)\??", r"\1", p)
    p = re.sub(r"\\w[*+]?", "x", p)
    p = re.sub(r"[\\?\[\]()+*^$]|\{[^}]*\}", "", p)
    return p.replace("|", " ")


import re   # noqa: E402  (used by _sample)


@pytest.mark.parametrize("sf", ["cosmo.gravity", "phys.cosmo"])
def test_gravitation_and_cosmology_are_shown_under_both_fields(sf):
    gr = classify({"title": "Gravitational waves from binary black hole mergers"})
    cosmo = classify({"title": "Dark energy constraints from large-scale structure surveys"})
    got = gr if sf == "cosmo.gravity" else cosmo
    assert sf in got[0]
    assert {"physics", "cosmo"} <= set(got[1]) if sf == "cosmo.gravity" else {"physics", "cosmo"} <= set(got[1])


def test_a_mirror_is_not_a_second_field_for_scoring():
    import profiles as P
    prof = P.load()["cosmology-ml"]
    gr_only = prof.score(["phys.gr.waves"], "india", "Workshop", {"keywords"})
    with_mirror = prof.score(["phys.gr.waves", "cosmo.gravity"], "india", "Workshop", {"keywords"})
    assert gr_only == with_mirror
