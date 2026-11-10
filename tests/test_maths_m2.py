"""PR M2 (2026-11-10): French keywords, series names, maths-only source fallback."""
import classify as C
import scrape as S
import sources_india as SI
import taxonomy as T
from taxonomy_math_fr import FRENCH, fold


def under(sf, subs):
    """sf itself, or a topic below it (a topic replaces its branch in the tags)."""
    return any(sf == t or sf in T.ancestors(t) for t in subs)


def tags(title, series=None, description=None):
    return C.classify({"title": title, "series": series,
                       "description": series if description is None else description})[0]


# ---------------------------------------------------------------------------
# series names
# ---------------------------------------------------------------------------
def test_series_counts_like_a_title():
    assert "math.probability" in tags("Irene Marcovici (Université de Rouen)", "Statistique - Probabilités - Optimisation et Contrôle")
    assert tags("Claire Barbier (UniCA)", "Maths Bio") == ["math.applied.biology"]
    assert "math.probability.stat" in tags("Moritz Madern from University of Vienna", "Séminaire de Biostatistique")


def test_a_series_naming_more_than_three_branches_says_only_mathematics():
    assert tags("Hadrien Notarantonio", "Géométrie, Algèbre, Dynamique et Topologie") == ["math.other"]
    three = set(tags("Some speaker", "Algèbre, géométrie, topologie"))
    assert {"math.algebra", "math.geometry", "math.topology"} <= three
    # a talk title still adds its own topic
    assert "math.numeric.symbolic" in tags("Macaulay2 Workshop", "Algèbre, géométrie, topologie")


def test_series_already_in_the_title_and_in_the_description_counts_once():
    ev = {"title": "Séminaire de Probabilités: Paolo Bellingeri", "series": "Séminaire de Probabilités",
          "description": "Séminaire de Probabilités · Algèbre et géométrie"}
    score, _ = C.gather_evidence(ev)
    assert score["math.probability"] == 1.0
    # the description's own words still count, at half weight
    assert score["math.algebra"] == 0.5


def test_indico_keeps_the_series_and_normalise_passes_it_on(monkeypatch):
    import datetime as dt
    from common import today
    when = {"date": (today() + dt.timedelta(days=10)).isoformat(), "time": "10:00:00"}
    data = {"results": [{"title": "Claire Barbier (UniCA)", "category": "Maths Bio", "url": "https://x/e/1",
                         "startDate": when, "endDate": when}]}
    monkeypatch.setattr(SI, "get", lambda url, **kw: type("R", (), {"json": lambda self: data, "text": ""})())
    raw = SI._indico({"name": "French maths Indico", "base": "https://x", "category": 0})
    assert raw[0]["series"] == "Maths Bio"
    assert S.normalise(raw)[0]["series"] == "Maths Bio"


# ---------------------------------------------------------------------------
# French keywords
# ---------------------------------------------------------------------------
FRENCH_CASES = [
    ("Mejdi Azaiez (INP Bordeaux)", "AnEDP et Méca Flu", "math.analysis.pde"),
    ("Mejdi Azaiez (INP Bordeaux)", "AnEDP et Méca Flu", "math.applied.mechanics"),
    ("Séance de décembre", "CTOP (Convexité, Transport Optimal et Probabilités)", "math.analysis.calculus"),
    ("Journées des Jeunes EDPistes en France 2026-2027", "Colloques", "math.analysis.pde"),
    ("Colloque tournant 2027 du RT algèbre", "Conférences", "math.algebra"),
    ("Derived Seminar", "Derived Seminar", "math.geometry.algebraic"),
    ("Adrien Abgrall : \"Plongements entre groupes d’Artin à angles droits sans carrés\"", "GdT Actions !", "math.algebra.group"),
    ("Grigalius Taujanskas", "Mathématique-Physique", "math.mathphys"),
    ("14e séminaire ITZYKSON - Dualité markovienne : méthodes algébriques et applications", "Physique", "math.probability.theory"),
    ("Séminaire des jeunes EDPistes (1)", "Séminaire MACS (Modélisation, Analyse et Calcul Scientifique)", "math.numeric.analysis"),
    ("Séminaire FDD - FiME - MIRTE", "Séminaire commun Chaire FDD - Laboratoire FiME", "math.optim.game"),
    ("Séminaire des doctorant·es SO", "Séminaire de Statistique et Optimisation", "math.optim"),
    ("Dynamique du billard dans un prisme", "", "math.dyn"),
    ("Modèles mathématiques pour la dynamique collective cellulaire", "", "math.applied.modelling"),
    ("Un cadre général pour l'analyse numérique des inéquations variationnelles", "", "math.numeric.analysis"),
    ("Journées Arithmétiques 2027", "Colloques", "math.nt"),
    ("Séminaire Equations aux dérivées partielles", "", "math.analysis.pde"),
    ("Groupe de travail parisien de calcul des variations", "", "math.analysis.calculus"),
    ("Séminaire de Géométrie Complexe", "", "math.geometry.complex"),
    ("Rencontres de théorie analytique des nombres", "", "math.nt.analytic"),
    ("Séminaire Calcul stochastique", "", "math.probability.theory"),
]


def test_french_seminars_and_talks_get_their_branch():
    for title, series, sf in FRENCH_CASES:
        assert sf in tags(title, series or None), (title, series, tags(title, series or None))


def test_french_physics_and_maths_physics_are_told_apart():
    assert tags("Grigalius Taujanskas", "Mathématique-Physique") == ["math.mathphys"]
    assert "phys.general" in tags("Bernard Dupont", "Séminaire de Physique Théorique")
    # a group-theory talk needs the word for groups; a working group ("groupe de travail") is not one
    assert "math.algebra.group" not in tags("Groupe de travail parisien de calcul des variations")


ENGLISH = ["LLM inference serving at scale", "We analyse the data from LIGO", "Detector optimisation for the LHC",
           "Graph neural networks for particle physics", "Statistical physics of disordered systems",
           "Modelling the early universe", "Physics colloquium", "Algebraic geometry seminar",
           "Stochastic processes in finance", "Optimisation of storage systems", "Analysis of variance",
           "Bayesian inference with Bilby", "Variational inference", "Data analysis school"]


def test_french_patterns_do_not_fire_on_english_text():
    french = [(sf, T._compile(fold(p))) for sf, pats in FRENCH.items() for p in pats]
    for t in ENGLISH:
        hits = [sf for sf, p in french if p.search(t)]
        assert hits == [], (t, hits)


# ---------------------------------------------------------------------------
# maths-only sources fall back to General mathematics
# ---------------------------------------------------------------------------
def test_maths_only_sources_fall_back_to_general_mathematics():
    defaults = SI.default_fields()
    assert defaults["French maths Indico"] == "math.other"
    assert defaults["Vakil algebraic geometry"] == "math.other"     # it also lists neighbouring fields
    e = {"title": "Bertrand Remy", "series": "Théminaire", "description": "Théminaire", "source": "French maths Indico"}
    assert S.classify_event(e, None, None, defaults) == (["math.other"], ["math"], ["source"])
    # only when nothing else tags it
    p = {"title": "Bernard Dupont", "series": "Séminaire de Physique Théorique", "description": "", "source": "French maths Indico"}
    assert S.classify_event(p, None, None, defaults)[0] == ["phys.general"]
    # a source that is not maths-only leaves an untagged event untagged
    o = {"title": "Bertrand Remy", "description": "", "source": "CMI seminars"}
    assert S.classify_event(o, None, None, defaults)[0] == []


# ---------------------------------------------------------------------------
# words moved out of General mathematics (X-6)
# ---------------------------------------------------------------------------
def test_words_for_areas_with_their_own_branch_leave_general_mathematics():
    assert under("math.comb", tags("Combinatorics seminar"))
    assert under("math.logic", tags("Set theory and forcing"))
    assert under("math.dyn", tags("Chaos in low-dimensional maps"))
    assert under("math.optim", tags("Optimal control of PDEs"))
    assert "math.other" not in tags("Combinatorics seminar")
    assert "math.nt.coding" not in tags("Quantum information theory and entanglement")
    assert not under("math.dyn", tags("Quantum chaos and black holes"))


# ---------------------------------------------------------------------------
# found on the held-out half (2026-11-10), fixed after it was scored
# ---------------------------------------------------------------------------
def test_held_out_findings():
    # a placeholder with the speaker in brackets
    for t in ["TBA (Hu Yining)", "Séminaire Combinatoire et Théorie des Nombres ICJ: TBA (Hu Yining)", "TBA (Anthony Masson) - ICJ"]:
        assert S.JUNK_TITLE.search(t), t
    for t in ["Thermodynamic Bethe Ansatz (TBA) and ODE/IM", "Introduction to the TBA equations of integrable models"]:
        assert not S.JUNK_TITLE.search(t), t
    # a navigation link is not an event
    assert S.NOT_EVENTS.match("Return to my homepage")
    # one French word plus an accented lowercase word is French; capitalised names with accents are not
    assert S.foreign_title("Analyse spectrale semiclassique des opérateurs de Bloch-Torrey")
    for t in ["Poincaré duality and Kähler manifolds", "Schrödinger operators with Erdős–Rényi potentials",
              "Hénon maps and the Lorenz attractor", "The strong coupling regime of QCD"]:
        assert not S.foreign_title(t), t
