"""
French keywords for mathematics (PR M2, 2026-11-10).

The French maths Indico (indico.math.cnrs.fr) is the largest mathematics source, and most of
its seminar series and many talks are in French. These patterns map French terms to the same
branches and topics as the English ones in taxonomy.py and taxonomy_math.py.

Written from the "dev" half of the live French events (and the list of seminar series); the
other half was kept back to measure the result (PROJECT_LOG.md).

Rules of thumb:
* Write French as it is spelled, with accents. `fold()` makes every accented letter also match
  its plain form (and the plain form its accented ones), so "Equations aux derivees" matches.
* Only French words or French phrases: a bare word that is also English ("inference",
  "optimisation", "analyse") would tag English events. "groupe de travail" is a working group,
  not group theory, so bare "groupes" is not a keyword.
* A few French physics and AI terms are here too, so that a French physics seminar on a maths
  server is not filed under General mathematics.
"""

_FOLD = {
    "é": "[éèêëe]", "è": "[éèêëe]", "ê": "[éèêëe]", "ë": "[éèêëe]",
    "à": "[àâäa]", "â": "[àâäa]", "ä": "[àâäa]",
    "î": "[îïi]", "ï": "[îïi]", "ô": "[ôöo]", "ö": "[ôöo]",
    "û": "[ûùüu]", "ù": "[ûùüu]", "ü": "[ûùüu]", "ç": "[çc]",
    "œ": "(?:œ|oe)", "'": "['’]",
}


def fold(pattern):
    """Accent-tolerant version of a French pattern (no accents occur in regex syntax here)."""
    return "".join(_FOLD.get(ch, ch) for ch in pattern)


FRENCH = {
    # -- general --------------------------------------------------------------------------
    "math.other": [r"mathématiques?", r"mathématicien\w*"],
    # -- logic, combinatorics --------------------------------------------------------------
    "math.logic": [r"logique(?: mathématique)?", r"fondements des mathématiques", r"preuves? formelles?",
                   r"assistants? de preuve", r"théorie de la démonstration", r"calculabilité"],
    "math.logic.logic": [r"théorie des modèles", r"théorie des ensembles"],
    "math.logic.category": [r"théorie des catégories", r"catégories (?:supérieures|dérivées|monoïdales|triangulées)",
                            r"structures supérieures", r"higher structures"],
    "math.comb": [r"combinatoire", r"mathématiques discrètes"],
    "math.comb.graph": [r"théorie des graphes", r"graphes"],
    "math.comb.algebraic": [r"combinatoire algébrique"],
    "math.comb.enumerative": [r"combinatoire (?:énumérative|analytique)"],
    # -- number theory, algebra ------------------------------------------------------------
    "math.nt": [r"théorie des nombres", r"arithmétiques?"],
    "math.nt.analytic": [r"théorie analytique des nombres"],
    "math.nt.algebraic": [r"théorie algébrique des nombres", r"corps de nombres"],
    "math.nt.arithmetic": [r"géométrie arithmétique", r"courbes elliptiques", r"variétés abéliennes"],
    "math.nt.modular": [r"formes (?:modulaires|automorphes)", r"programme de Langlands"],
    "math.nt.coding": [r"codes correcteurs", r"théorie de l'information"],
    "math.algebra": [r"algèbres?"],
    "math.algebra.group": [r"théorie des groupes", r"actions de groupes",
                           r"groupes (?:finis|d'Artin|de Coxeter|de tresses|libres|hyperboliques|de surfaces?|discrets|profinis|algébriques)"],
    "math.algebra.lie": [r"théorie des représentations", r"représentations des groupes", r"algèbres de Lie"],
    "math.algebra.comm": [r"algèbre commutative", r"anneaux commutatifs"],
    "math.algebra.rings": [r"anneaux", r"algèbre non commutative"],
    "math.algebra.hopf": [r"algèbres de Hopf", r"groupes quantiques", r"catégories tensorielles"],
    "math.algebra.field": [r"théorie de Galois", r"corps finis", r"extensions de corps"],
    "math.algebra.linear": [r"algèbre (?:multi)?linéaire"],
    "math.algebra.homological": [r"algèbre homologique", r"K-théorie"],
    # -- geometry, topology -----------------------------------------------------------------
    "math.geometry": [r"géométries?", r"variétés"],
    "math.geometry.algebraic": [r"géométrie algébrique", r"espaces de modules", r"champs algébriques",
                                r"géométrie dérivée", r"derived seminar"],
    "math.geometry.complex": [r"géométrie complexe", r"géométrie (?:kählérienne|de Kähler)", r"variétés complexes",
                              r"surfaces de Riemann"],
    "math.geometry.diff": [r"géométrie (?:différentielle|riemannienne|conforme|sous-riemannienne)", r"courbure",
                           r"flot de Ricci"],
    "math.geometry.symplectic": [r"géométrie (?:symplectique|de contact)", r"topologie symplectique"],
    "math.geometry.discrete": [r"géométrie (?:convexe|discrète)", r"convexité", r"corps convexes"],
    "math.geometry.tropical": [r"géométrie (?:tropicale|torique)"],
    "math.geometry.lie": [r"groupes de Lie", r"espaces homogènes"],
    "math.topology.algebraic": [r"topologie algébrique", r"homotopie", r"théorie de l'homotopie"],
    "math.topology.low": [r"théorie des n(?:œ|oe)uds", r"n(?:œ|oe)uds", r"basse dimension",
                          r"variétés de dimension (?:3|4|trois|quatre)"],
    "math.topology.diff": [r"topologie (?:différentielle|géométrique)"],
    # -- analysis ---------------------------------------------------------------------------
    "math.analysis": [r"(?:séminaire|groupe de travail) d'analyse", r"séminaire analyse", r"équations différentielles",
                      r"analyse (?:mathématique|réelle|non linéaire|et (?:probabilités|géométrie|dynamique|modélisation|EDP|applications))"],
    "math.analysis.pde": [r"équations? aux dérivées partielles", r"EDP\w*", r"AnEDP", r"lois de conservation",
                          r"équations? (?:cinétiques?|de transport|elliptiques?|paraboliques?|hyperboliques?|des ondes|de la chaleur|de Schrödinger|d'Euler|de Navier-Stokes|de Boltzmann)",
                          r"problèmes elliptiques", r"théorie cinétique"],
    "math.analysis.ode": [r"équations différentielles ordinaires"],
    "math.analysis.calculus": [r"calcul des variations", r"transport optimal"],
    "math.analysis.harmonic": [r"analyse harmonique", r"analyse de Fourier"],
    "math.analysis.functional": [r"analyse fonctionnelle", r"théorie des opérateurs", r"espaces de Banach"],
    "math.analysis.opalg": [r"algèbres d'opérateurs", r"géométrie non commutative"],
    "math.analysis.complex": [r"analyse complexe", r"fonctions holomorphes"],
    "math.analysis.potential": [r"théorie du potentiel"],
    "math.analysis.inverse": [r"problèmes inverses"],
    "math.analysis.approx": [r"théorie de l'approximation", r"fonctions spéciales", r"polynômes orthogonaux"],
    "math.analysis.real": [r"théorie de la mesure", r"analyse réelle", r"fractales"],
    # -- probability and statistics ---------------------------------------------------------
    "math.probability": [r"probabilistes?", r"aléatoires?"],
    "math.stat": [r"statistiques?"],
    "math.probability.theory": [r"processus (?:stochastiques?|aléatoires|de branchement|ponctuels?|de Lévy)",
                                r"mouvement brownien", r"grandes déviations", r"graphes aléatoires", r"particules en interaction"],
    "math.probability.stochastic": [r"calcul stochastique", r"équations? (?:aux dérivées partielles |différentielles )?stochastiques"],
    "math.probability.walks": [r"marches? aléatoires?", r"markovien\w*", r"chaînes de Markov", r"processus de Markov"],
    "math.probability.geometry": [r"géométrie aléatoire", r"arbres aléatoires", r"cartes aléatoires"],
    "math.probability.rmt": [r"matrices aléatoires", r"probabilités libres"],
    "math.stat.mathstat": [r"statistique (?:mathématique|des processus)", r"apprentissage statistique", r"analyse (?:de|des) données",
                           r"tests? statistiques?", r"inférence statistique", r"MAD-Stat"],
    "math.stat.bayes": [r"statistique bayésienne", r"inférence bayésienne"],
    "math.stat.highdim": [r"statistique (?:non paramétrique|en grande dimension)", r"estimation non paramétrique"],
    "math.stat.timeseries": [r"séries temporelles", r"statistique spatiale", r"géostatistique"],
    "math.stat.causal": [r"inférence causale", r"plans d'expériences"],
    "math.stat.bio": [r"biostatistiques?", r"essais cliniques", r"épidémiologie statistique"],
    # -- mathematical physics, dynamics -----------------------------------------------------
    "math.mathphys": [r"physique mathématique", r"mathématiques?[- ]physique", r"maths?[- ]physique"],
    "math.mathphys.integrable": [r"systèmes intégrables", r"probabilités intégrables"],
    "math.mathphys.qft": [r"théorie (?:quantique )?des champs"],
    "math.mathphys.statmech": [r"mécanique statistique"],
    "math.mathphys.relativity": [r"relativité générale"],
    "math.dyn": [r"systèmes dynamiques", r"billards?",
                 r"dynamique(?! (?:des fluides|moléculaire|des populations|cellulaire|collective|des gaz|quantique))"],
    "math.dyn.ergodic": [r"théorie ergodique", r"dynamique topologique"],
    "math.dyn.complex": [r"dynamique (?:holomorphe|complexe)"],
    "math.dyn.hyperbolic": [r"dynamique hyperbolique", r"systèmes hamiltoniens"],
    # -- numerical, optimisation, applied ---------------------------------------------------
    "math.numeric.analysis": [r"analyse numérique", r"calcul scientifique", r"méthodes? numériques?",
                              r"simulations? numériques?", r"éléments finis", r"volumes finis", r"schémas numériques",
                              r"mécanique des fluides numérique"],
    "math.numeric.symbolic": [r"calcul formel", r"Macaulay2"],
    "math.optim": [r"optimisation (?:et|convexe|combinatoire|stochastique|continue|numérique|non lisse|de forme)",
                   r"(?:statistique|recherche opérationnelle) et optimisation", r"recherche opérationnelle"],
    "math.optim.control": [r"théorie du contrôle", r"contrôle optimal", r"contrôlabilité", r"optimisation et contrôle"],
    "math.optim.game": [r"théorie des jeux", r"jeux à champ moyen", r"mathématiques financières", r"finance mathématique",
                        r"CS:FiME"],
    "math.applied.biology": [r"biologie mathématique", r"CS:Maths? Bio", r"mathématiques (?:pour|de) la biologie",
                             r"épidémiologie", r"dynamique des populations", r"biomathématiques?"],
    "math.applied.mechanics": [r"mécanique des (?:fluides|solides|milieux continus)", r"méca(?:nique)? flu\w*"],
    "math.applied.modelling": [r"modélisation(?: mathématique)?", r"modèles mathématiques", r"mathématiques appliquées",
                               r"traitement (?:du signal|d'images?)", r"imagerie"],
    "math.edu.education": [r"didactique(?: des mathématiques)?", r"enseignement des mathématiques",
                           r"histoire des mathématiques", r"vulgarisation", r"Mathematic Park"],
    # -- a little French physics and AI -----------------------------------------------------
    "phys.general": [r"physique(?! mathématique) ||| mathématiques?[- ]physique|maths?[- ]physique", r"physiciens?"],
    "phys.condmat": [r"matière condensée"],
    "ai.general": [r"intelligence artificielle", r"apprentissage (?:automatique|profond)"],
    "ai.theory": [r"fondements mathématiques de l'IA", r"théorie de l'apprentissage"],
}
