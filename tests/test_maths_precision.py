"""PR M1 (2026-11-10): maths precision. Every case below was seen on the live site."""
import classify as C
import scrape as S
import sources_india as SI
import taxonomy as T


def _maths(title):
    return sorted(k for k in C.keyword_hits(title) if T.ancestors(k)[-1] == "math")


# ---------------------------------------------------------------------------
# placeholder slots
# ---------------------------------------------------------------------------
def test_placeholder_slots_are_dropped_even_after_a_series_prefix():
    junk = ["Titre à venir", "TBA ENS", "(Thibault) TBA - ICJ", "Séminaire des Doctorants et Doctorantes: TBA - ICJ",
            "Séminaire des Doctorants et Doctorantes: (Thibault) TBA - ICJ", "Séminaire des Doctorants et Doctorantes: - ICJ",
            "Séminaire de Probabilités: Vacances", "Séminaire de Géométrie Complexe: -", "Séminaire de Géométrie Complexe: -Férié",
            "Séminaire de Géométrie Complexe: Férié", "-", "—", "Vacances de Noël", "Séminaire: titre à préciser", "TBA IMJ-PRG"]
    keep = ["Introduction to the TBA equations of integrable models", "TBA equations and Y-systems", "Seminar on TBA-free methods",
            "Thermodynamic Bethe Ansatz (TBA) and ODE/IM", "Les défis à venir en géométrie", "Séminaire des Doctorants et Doctorantes: ICJ",
            "Session régionale du séminaire des doctorant·e·s", "Journée de rentrée du 11 Janvier", "Séance de novembre",
            "Derived Seminar", "Hadrien Notarantonio", "Vacancies in graphene", "Holiday lectures on black holes",
            "Formation of galaxies", "Pre- and post-processing", "A-B workshop"]
    for t in junk:
        assert S.JUNK_TITLE.search(t), t
    for t in keep:
        assert not S.JUNK_TITLE.search(t), t


def test_a_placeholder_is_not_taken_for_a_speakers_name():
    # the root cause: "Férié" looked like a name, so the series was prefixed and the filter missed it
    for t in ["Férié", "-Férié", "TBA ENS", "-", "(Thibault) TBA - ICJ", "Vacances"]:
        assert not SI.speaker_only(t), t
    assert SI.speaker_only("Paolo Bellingeri") and SI.speaker_only("Hadrien Notarantonio")


def _indico_results(*rows):
    when = {"date": "2099-01-05", "time": "10:00:00"}
    return {"results": [{"title": t, "category": c, "url": f"https://x/e/{i}", "startDate": when, "endDate": when}
                        for i, (t, c) in enumerate(rows)]}


def test_indico_holiday_slot_keeps_its_own_title_and_is_dropped(monkeypatch):
    data = _indico_results(("Férié", "Séminaire de Géométrie Complexe"), ("TBA ENS", "Séminaire des Doctorants et Doctorantes"))
    monkeypatch.setattr(SI, "get", lambda url, **kw: type("R", (), {"json": lambda self: data, "text": ""})())
    out = SI._indico({"name": "x", "base": "https://x", "category": 0})
    assert [e["title"] for e in out] == ["Férié", "TBA ENS"]
    assert all(S.JUNK_TITLE.search(e["title"]) for e in out)


def test_indico_skip_categories(monkeypatch):
    data = _indico_results(("Formation GIT collaboratif", "Formations"), ("Page de recensement", "RT Mathrice"),
                           ("Immersion double licence math info", "Activités tournées vers les lycées"),
                           ("Journées Arithmétiques 2027", "Colloques"))
    monkeypatch.setattr(SI, "get", lambda url, **kw: type("R", (), {"json": lambda self: data, "text": ""})())
    cfg = {"name": "x", "base": "https://x", "category": 0, "skip_categories": ["^Formations$", "^RT Mathrice$", "lycées"]}
    assert [e["title"] for e in SI._indico(cfg)] == ["Journées Arithmétiques 2027"]


def test_french_maths_indico_skips_its_non_research_categories():
    cfg = next(c for c in SI._registry() if c["name"] == "French maths Indico")
    assert "^Formations$" in cfg["skip_categories"]


# ---------------------------------------------------------------------------
# no embedding guess on French or name-only titles
# ---------------------------------------------------------------------------
def test_no_embedding_guess_for_french_names_and_placeholders():
    blocked = [("Titre à venir", "Séminaire de Probabilités · résumé à venir"), ("Marie Doumic (INRIA Paris)", "Maths Bio"),
               ("Colloquium: Bertrand Maury (Univ. Paris-Saclay)", "Colloquium"),
               ("Séminaire 08/01/2027 - Mathurin Massias and Claire Boyer", "Séminaire Parisien"),
               ("Session régionale du séminaire des doctorant·e·s", "Séminaire des doctorants · Lyon"),
               ("Un cadre général pour l'analyse numérique des inéquations variationnelles", ""),
               ("Ruth Baker (Oxford University)", "Maths Bio"), ("Louis de Broglie", "Colloquium"),
               ("Квантовая гравитация и космология", ""), ("Introduction à l'analyse harmonique", ""), ("Hadrien Notarantonio", "Géométrie, Algèbre, Dynamique et Topologie")]
    allowed = [("Joe Formaggio (MIT)", "Neutrino mass measurement with Project 8 and KATRIN at MIT, and what comes next"),
               ("Sharp Survival Estimates for Jump Processes — Jing Wang", ""),
               ("Self-dual theories, celestial algebras and Moyal deformations — Ricardo Monteiro", ""),
               ("Au+Au collisions at RHIC and the QGP", ""), ("Dark Energy Survey Collaboration Meeting", ""),
               ("Introduction to the TBA equations of integrable models", ""), ("De Sitter space and la Jolla workshop", ""),
               ("Software Provenance with Snakemake", ""), ("International Space Radio Interferometry Conference", ""),
               ("Forming Stars in Cardiff", ""), ("The d'Alembert operator on curved backgrounds", ""), ("Journées Arithmétiques 2027", "The Journées Arithmétiques is a major conference in number theory")]
    for t, d in blocked:
        assert S.no_embedding_guess({"title": t, "description": d}), t
    for t, d in allowed:
        assert not S.no_embedding_guess({"title": t, "description": d}), t


# ---------------------------------------------------------------------------
# maths keywords on physics, CS and AI events (pitfall P-1)
# ---------------------------------------------------------------------------
NOT_MATHS = [
    "Worldsheet String Theory and String Field Theory", "The 44th International Symposium on Lattice Field Theory",
    "Modern Applications of Field Theory", "FC 2027 — Financial Cryptography and Data Security",
    "Advances in Quantum Cryptography, Paris", "EUROCRYPT 2027 — European Cryptology Conference",
    "AI for Scientific Discovery Colloquia Series - Generative AI and Diffusion Models",
    "WE-Heraeus-Summer School Exact Methods: from Lattice Models to String Theory",
    "CAV 2027 — International Conference on Computer-Aided Verification",
    "ICALP 2027 — EATCS International Colloquium on Automata, Languages, and Programming",
    "Multiresolution Modelling of Intracellular Processes", "Joint Storage Optimization and Scaling ML meeting",
    "The Quantum Monte Carlo Sign Problem: Structure, Complexity, and New Directions",
    "Stochastic gravitational wave background from inflation", "Bose-Einstein statistics of photons",
    "Workshop on Geometric Phase, Berry Curvature and Topological Phenomena",
    "Probing Quantum Matter: From Topology to Emerging devices", "Topological insulators and superconductors",
    "Curvature perturbations during inflation", "Magnetic monopoles in spin ice", "Moduli stabilisation in string cosmology",
    "Spinor-helicity formalism for amplitudes", "Tensor modes and the tensor-to-scalar ratio",
    "Statistical Physics of Long-Range Interacting Systems",
]
STILL_MATHS = [
    ("Field extensions and Galois groups", "math.algebra.field"), ("Isogeny-based cryptography", "math.nt.crypto"),
    ("Diffusions on manifolds", "math.probability.stochastic"), ("Perfect matchings in hypergraphs", "math.comb.graph"),
    ("Markov chain Monte Carlo methods", "math.probability"), ("Stochastic processes and SPDEs", "math.probability.stochastic"),
    ("Statistics for high-energy physics", "math.stat"), ("Low-dimensional topology and knot theory", "math.topology.low"),
    ("Topological data analysis", "math.topology"), ("Ricci curvature and optimal transport", "math.geometry.analysis"),
    ("Mean curvature flow", "math.geometry.analysis"), ("Moduli spaces of curves", "math.geometry.moduli"),   # M3c topics
    ("Tensors and tensor rank", "math.algebra.linear"), ("Riemannian geometry", "math.geometry"),
    ("Multiresolution analysis and wavelets", "math.analysis.harmonic"),
]


def test_physics_cs_and_ai_titles_get_no_maths_keywords():
    for t in NOT_MATHS:
        assert _maths(t) == [], (t, _maths(t))


def test_maths_titles_keep_their_maths_keywords():
    for t, sf in STILL_MATHS:
        assert sf in _maths(t), (t, _maths(t))


def test_a_pattern_can_name_a_context_that_cancels_it():
    p = T._compile("topolog\\w* ||| insulators?")
    assert p.search("Topology of manifolds")
    assert p.search("Topological insulators and topology") is None


# ---------------------------------------------------------------------------
# INSPIRE's "Math and Math Physics" box on broad meetings
# ---------------------------------------------------------------------------
def _tags(title, declared=()):
    return C.classify({"title": title, "description": "", "declared": list(declared)})[0]


def test_inspire_math_box_counts_only_on_focused_meetings():
    eps = ["Accelerators", "Astrophysics", "Computing", "Experiment-HEP", "Gravitation and Cosmology", "Instrumentation",
           "Lattice", "Phenomenology-HEP", "Theory-HEP", "Math and Math Physics", "Data Analysis and Statistics"]
    assert "math.mathphys" not in _tags("2027 European Physical Society Conference on High Energy Physics", eps)
    loop = ["Gravitation and Cosmology", "Theory-HEP", "Theory-Nucl", "Phenomenology-HEP", "Astrophysics", "Math and Math Physics"]
    assert "math.mathphys" not in _tags("Loop-the-Loop 2026", loop)
    assert "math.mathphys" in _tags('MITP Topical Workshop: "Strings, Symmetries, and Singularities"', ["Theory-HEP", "Math and Math Physics"])
    assert "math.mathphys" in _tags("Tunneling in QFT: XXVIII", ["Theory-HEP", "Quantum Physics", "Math and Math Physics"])
    # a broad meeting about mathematical physics still gets it from its own words
    assert "math.mathphys" in _tags("Mathematical physics days", eps)


def test_optimisation_in_a_list_title_still_counts():
    assert "math.optim.optimisation" in _tags("Calculus of Variations, Optimization and Image Processing")
