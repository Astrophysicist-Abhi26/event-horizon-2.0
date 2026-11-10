"""PR M3b (2026-11-10): Statistics as its own branch; Probability split into topics."""
import classify as C
import profiles as P
import taxonomy as T


def tags(title):
    return C.classify({"title": title, "description": ""})[0]


SAMPLES = [
    ("Bayesian hierarchical models and MCMC", "math.stat.bayes"),
    ("Approximate Bayesian computation for population genetics", "math.stat.bayes"),
    ("High-dimensional statistics and the lasso", "math.stat.highdim"),
    ("Nonparametric estimation of densities", "math.stat.highdim"),
    ("Time series analysis with state-space models", "math.stat.timeseries"),
    ("Geostatistics and kriging", "math.stat.timeseries"),
    ("Causal inference with instrumental variables", "math.stat.causal"),
    ("Design of experiments for industrial processes", "math.stat.causal"),
    ("Survival analysis and biostatistics", "math.stat.bio"),
    ("Statistical genetics and genome-wide association studies", "math.stat.bio"),
    ("Astrostatistics summer school", "math.stat.physical"),
    ("Joint PhyStat & Terascale School of Statistics 2027", "math.stat.physical"),
    ("Mathematical statistics seminar", "math.stat.mathstat"),
    ("Hypothesis testing and multiple testing", "math.stat.mathstat"),
    ("Rough paths and regularity structures", "math.probability.stochastic"),
    ("Stochastic differential equations with jumps", "math.probability.stochastic"),
    ("Mixing times of Markov chains", "math.probability.walks"),
    ("Random walks in random environment", "math.probability.walks"),
    ("Schramm-Loewner evolution and critical percolation", "math.probability.geometry"),
    ("Limits of uniform spanning trees and forests", "math.probability.geometry"),
    ("Large deviations and concentration of measure", "math.probability.theory"),
    ("Random matrices and free probability", "math.probability.rmt"),
]


def test_statistics_and_probability_topics():
    for title, sf in SAMPLES:
        assert sf in tags(title), (title, tags(title))


def test_statistics_is_a_branch_of_mathematics_after_probability():
    math = next(d for d in T.display_tree() if d["id"] == "math")
    ids = [b["id"] for b in math["branches"]]
    assert ids.index("math.stat") == ids.index("math.probability") + 1
    assert T.SUBFIELDS["math.probability"][1] == "Probability"
    assert T.SUBFIELDS["math.stat"][1] == "Statistics"


def test_statistics_keeps_the_weights_of_probability_in_every_profile():
    # decision D-9: nothing in anyone's ranking moves
    for prof in P.load():
        name = getattr(prof, 'id', prof)
        for topic in ("math.stat", "math.stat.bayes", "math.stat.physical"):
            assert prof.score([topic]) == prof.score(["math.probability"]), (name, topic)


def test_declared_statistics_codes_go_to_statistics():
    assert T.declared_codes("math.ST") and T.declared_codes("math.ST")[0][0] == "math.stat"
    assert T.declared_codes("stat.ME")[0][0] == "math.stat"


def test_saved_selections_are_widened_to_what_the_old_ids_covered():
    nodes = {"d:" + d["id"] for d in T.display_tree()}
    for d in T.display_tree():
        for b in d["branches"]:
            nodes.add("b:" + b["id"])
            nodes |= {"t:" + t["id"] for t in b["topics"]}
    for m in T.MIGRATIONS:
        for old, new in m["map"].items():
            assert new and all(n in nodes for n in new), (old, new)
    assert "t:math.probability.stat" not in nodes          # that topic is now the Statistics branch


def test_physics_statistics_words_stay_physics():
    for t in ["Bose-Einstein statistics of photons", "Statistical Physics of Long-Range Interacting Systems",
              "Clinical Trials Methodology Workshop"]:
        assert not any(s.startswith("math.stat") for s in tags(t)), (t, tags(t))
