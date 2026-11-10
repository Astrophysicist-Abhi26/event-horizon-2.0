"""PR M3c (2026-11-10): 24 more maths topics, "(general)" topics that give way, saved selections."""
import classify as C
import taxonomy as T


def tags(title, series=None):
    return C.classify({"title": title, "series": series, "description": series or ""})[0]


# one or two titles for every new topic (written as they appear on seminar and conference lists)
SAMPLES = [
    ("Model theory of valued fields and o-minimality", "math.logic.model"),
    ("Neostability and NIP theories", "math.logic.model"),
    ("Set theory and large cardinals", "math.logic.sets"),
    ("Forcing axioms and the continuum hypothesis", "math.logic.sets"),
    ("Proof theory and reverse mathematics", "math.logic.computability"),
    ("Computable structure theory and Turing degrees", "math.logic.computability"),
    ("Lean Together: formalising mathematics with mathlib", "math.logic.formal"),
    ("Homotopy type theory and univalent foundations", "math.logic.formal"),
    ("Geometric group theory and hyperbolic groups", "math.algebra.ggt"),
    ("Quasi-isometric rigidity of right-angled Artin groups", "math.algebra.ggt"),
    ("Tau-tilting theory and silting objects", "math.algebra.quivers"),
    ("Cluster algebras and quiver representations", "math.algebra.quivers"),
    ("Moduli spaces of Higgs bundles", "math.geometry.moduli"),
    ("Teichmüller theory and hyperbolic surfaces", "math.geometry.moduli"),
    ("Gromov-Witten invariants and mirror symmetry", "math.geometry.enumerative"),
    ("Hurwitz numbers and topological recursion", "math.geometry.enumerative"),
    ("Ricci flow and geometric analysis", "math.geometry.analysis"),
    ("Min-max theory for minimal surfaces", "math.geometry.analysis"),
    ("Topological data analysis and persistent homology", "math.topology.applied"),
    ("Persistence modules and zigzag persistence", "math.topology.applied"),
    ("Regularity for elliptic and parabolic equations", "math.analysis.elliptic"),
    ("Free boundary problems and the obstacle problem", "math.analysis.elliptic"),
    ("Nonlinear dispersive equations and wave maps", "math.analysis.waves"),
    ("Hyperbolic conservation laws and shock waves", "math.analysis.waves"),
    ("Navier-Stokes and Euler equations", "math.analysis.fluids"),
    ("Kinetic equations: Boltzmann and Vlasov", "math.analysis.fluids"),
    ("Optimal transport and Wasserstein distances", "math.analysis.ot"),
    ("Sinkhorn algorithm and entropic optimal transport", "math.analysis.ot"),
    ("Homogeneous dynamics and unipotent flows", "math.dyn.homogeneous"),
    ("Arithmetic dynamics and canonical heights", "math.dyn.homogeneous"),
    ("Discontinuous Galerkin methods for conservation laws", "math.numeric.pde"),
    ("Finite element exterior calculus", "math.numeric.pde"),
    ("Krylov subspace methods and preconditioners", "math.numeric.linalg"),
    ("Mixed-precision algorithms for numerical linear algebra", "math.numeric.linalg"),
    ("Uncertainty quantification with polynomial chaos", "math.numeric.uq"),
    ("Ensemble Kalman methods for data assimilation", "math.numeric.uq"),
    ("Semidefinite programming and interior-point methods", "math.optim.convex"),
    ("Proximal methods for nonsmooth optimisation", "math.optim.convex"),
    ("Mixed-integer programming and branch-and-cut", "math.optim.discrete"),
    ("Vehicle routing and operational research", "math.optim.discrete"),
    ("Option pricing and rough volatility", "math.optim.finance"),
    ("Bachelier Finance Society World Congress", "math.optim.finance"),
    ("Variational methods in image processing", "math.applied.imaging"),
    ("Compressed sensing and phase retrieval", "math.applied.imaging"),
    ("Information theory and rate-distortion", "math.applied.info"),
    ("IEEE International Symposium on Information Theory (ISIT)", "math.applied.info"),
    ("History and philosophy of mathematics", "math.edu.history"),
    ("Kerala school and medieval mathematics", "math.edu.history"),
]


def test_every_new_topic_has_titles_that_reach_it():
    for title, sf in SAMPLES:
        assert sf in tags(title), (title, tags(title))
    new = {sf for _, sf in SAMPLES}
    assert len(new) == 24 and new <= set(T.PARENT_SF)


def test_a_general_topic_gives_way_to_a_narrower_one():
    assert tags("Elliptic PDE seminar") == ["math.analysis.elliptic"]
    assert "math.probability.theory" not in tags("Stochastic processes and SPDEs")
    assert "math.optim.optimisation" not in tags("Convex optimisation methods")
    assert "math.logic.logic" not in tags("Mathematical logic: set theory and forcing")
    # without a narrower topic the general one stays
    assert "math.analysis.pde" in tags("Partial differential equations seminar")
    assert "math.dyn.general" in tags("Dynamical systems seminar")
    # only within its own area: a PDE talk can still be both PDE and numerical PDE
    both = tags("Finite element methods for PDEs")
    assert "math.numeric.pde" in both and "math.analysis.pde" in both


def test_every_general_topic_says_so_in_its_label():
    for g, narrower in T.NARROWER.items():
        assert "(general)" in T.SUBFIELDS[g][1], g
        assert all(T.PARENT_SF[n] == T.PARENT_SF[g] for n in narrower), g


def test_precision_fixes_made_while_moving():
    assert not any(t.startswith("math.") for t in tags("Hartree-Fock methods for nuclei"))
    # a speaker called Zakharov is not the Zakharov system (seen on the live site)
    assert not any(t.startswith("math.") for t in tags("GIT and quantization of Chern-Simons — Alexander Zakharov"))
    assert "math.analysis.waves" in tags("The Zakharov system")
    assert "math.algebra.ggt" not in tags("Kazhdan-Lusztig polynomials")
    assert "math.algebra.ggt" not in tags("Cubical type theory")
    assert "math.logic.formal" in tags("Cubical type theory")
    assert "math.algebra.group" not in tags("Geometric group theory")
    assert "math.algebra.group" in tags("Finite group theory")
    # mean curvature is geometric analysis, not also the general curvature word
    assert "math.geometry.diff" not in tags("Mean curvature flow")
    assert "math.geometry.diff" in tags("Curvature and holonomy")
    # hyperbolic groups are group theory, not moduli of hyperbolic surfaces
    assert "math.geometry.moduli" not in tags("Geometric group theory and hyperbolic groups")
    # univalent functions (complex analysis) are not univalent foundations
    assert tags("Univalent functions and the Bieberbach conjecture") == ["math.analysis.complex"]
    # heat flow in a material is physics; the heat equation is a PDE
    assert not any(t.startswith("math.") for t in tags("Heat flow in nanostructures"))
    assert "math.analysis.elliptic" in tags("The heat equation on manifolds")


def test_maths_flows_and_polynomial_chaos_are_not_physics():
    for t in ["Ricci flow and geometric analysis", "Homogeneous dynamics and unipotent flows",
              "Hamiltonian flows and symplectic geometry", "Mean curvature flow",
              "Wasserstein gradient flows"]:
        assert "phys.fluids" not in tags(t), (t, tags(t))
    for t in ["Uncertainty quantification with polynomial chaos", "Propagation of chaos for mean-field particle systems"]:
        assert not any(s.startswith(("math.dyn", "phys.complex")) for s in tags(t)), (t, tags(t))
    # real fluid flows and chaos keep their tags
    assert "phys.fluids.turbulence" in tags("Turbulent flows in pipes")
    assert "phys.complex.nonlinear" in tags("Chaos in the double pendulum")


def test_keywords_moved_to_another_branch_keep_their_old_tag_too():
    # profiles weight branches, so a keyword shared with another branch stays there (no ranking moves)
    assert {"math.topology.applied", "math.applied.modelling"} <= set(tags("Topological data analysis"))
    assert {"math.numeric.uq", "math.applied.modelling"} <= set(tags("Uncertainty quantification"))
    assert {"math.numeric.uq", "math.analysis.inverse"} <= set(tags("Data assimilation"))


def test_information_theory_is_applied_mathematics_now():
    # decision D-3: information theory leaves Number theory; coding theory stays
    assert tags("Information theory") == ["math.applied.info"]
    assert "math.nt.coding" in tags("Coding theory and error-correcting codes")
    assert T.declared_codes("math.IT")[0][0] == "math.applied.info"
    assert T.declared_codes("cs.IT")[0][0] == "math.applied.info"


FRENCH = [
    ("Séminaire de théorie des modèles", "math.logic.model"),
    ("Groupe de travail transport optimal", "math.analysis.ot"),
    ("Équations elliptiques et paraboliques", "math.analysis.elliptic"),
    ("Équations dispersives et lois de conservation", "math.analysis.waves"),
    ("Théorie cinétique et équations de Boltzmann", "math.analysis.fluids"),
    ("Théorie géométrique des groupes", "math.algebra.ggt"),
    ("Représentations des carquois", "math.algebra.quivers"),
    ("Espaces de modules et fibrés de Higgs", "math.geometry.moduli"),
    ("Homologie persistante", "math.topology.applied"),
    ("Méthodes de Galerkin discontinues", "math.numeric.pde"),
    ("Quantification d'incertitudes", "math.numeric.uq"),
    ("Recherche opérationnelle", "math.optim.discrete"),
    ("Mathématiques financières", "math.optim.finance"),
    ("Traitement d'images", "math.applied.imaging"),
    ("Théorie de l'information", "math.applied.info"),
    ("Histoire des mathématiques", "math.edu.history"),
]


def test_french_terms_reach_the_new_topics():
    for title, sf in FRENCH:
        assert sf in tags(title), (title, tags(title))


def test_migration_versions_increase_so_each_applies_once():
    versions = [m["version"] for m in T.MIGRATIONS]
    assert versions == sorted(versions) and len(set(versions)) == len(versions)
    # an old topic always keeps itself, so nobody loses what they had picked
    for m in T.MIGRATIONS[1:]:
        for old, new in m["map"].items():
            assert old in new, old


def test_no_pattern_has_a_doubled_backslash():
    # r"\\w" in a raw string is a literal backslash: "probability inequalities" never matched (M3b, fixed here)
    bad = [(sf, p) for sf, pats in T.RULES.items() for p in pats if "\\\\" in p]
    assert not bad, bad
    assert "math.probability.theory" in tags("Probability inequalities")
    assert "math.stat.highdim" in tags("Empirical processes and VC classes")


def test_maths_titles_that_had_no_topic():
    # Q-6 / Q-16 in PROJECT_LOG.md
    assert "math.probability.theory" in tags("Sharp Survival Estimates for Jump Processes")
    assert "math.probability.walks" in tags("Intersection local times of random walks")
    assert "math.probability.geometry" in tags("Limits of uniform spanning trees")
    assert "math.geometry.discrete" in tags("The Santaló inequality and its functional forms")
    assert "math.dyn.ergodic" in tags("Surjonctivité des sous-décalages")
