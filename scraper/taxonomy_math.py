"""
Mathematics topics: the third level of the taxonomy (field -> sub-field -> topic).
See taxonomy_physics.py for the format. The areas follow the top-level classes of
the Mathematics Subject Classification (MSC2020), grouped the way departments and
conferences group them.
"""

UMBRELLAS = {
    "math.logic":   ("math", "Logic, foundations & category theory", "math.other"),
    "math.comb":    ("math", "Combinatorics & discrete mathematics", "math.other"),
    "math.dyn":     ("math", "Dynamical systems & ergodic theory", "math.other"),
    "math.numeric": ("math", "Numerical analysis & scientific computing", "math.analysis"),
    "math.optim":   ("math", "Optimisation, control & games", "math.other"),
    "math.applied": ("math", "Applied & interdisciplinary mathematics", "math.other"),
    "math.edu":     ("math", "Mathematics education & history", "math.other"),
    # its own branch since 2026-11-10 (decision D-1); profiles weight it like Probability (D-9)
    "math.stat":    ("math", "Statistics", "math.probability"),
}

TOPICS = {
    # ── Number theory ──────────────────────────────────────────────────────────
    "math.nt.analytic": ("math.nt", "Analytic number theory", [
        r"analytic number theory", r"riemann (?:hypothesis|zeta)", r"zeta[- ]functions?", r"prime (?:numbers?|distribution|gaps|k-tuples|counting)", r"primes? (?:in|and) (?:arithmetic|progressions?|short intervals)",
        r"l-?functions?", r"sieve\w*", r"circle method", r"exponential sums?", r"multiplicative number theory", r"distribution of primes", r"goldbach", r"twin primes?", r"moments of (?:zeta|L-functions?)",
        r"character sums?", r"large sieve", r"subconvexity", r"trace formulas?", r"beyond endoscopy", r"random matrix (?:theory )?(?:and|in) (?:number theory|L-functions)", r"zero[- ]density", r"Dirichlet series"]),
    "math.nt.algebraic": ("math.nt", "Algebraic number theory", [
        r"algebraic number (?:theory|fields?)", r"class field theory", r"iwasawa", r"galois (?:representations?|cohomology|modules?)", r"selmer groups?", r"ideal class", r"local fields?", r"p-adic (?:hodge|methods|analysis|L-functions|numbers|groups?|geometry|representations?|fields?|cohomology|Langlands|integration|periods?|modular|Galois)",
        r"cyclotomic", r"ad(?:é|e)les?", r"rings? of integers", r"number fields?", r"reciprocity laws?", r"arakelov", r"units? (?:and|in) number fields?", r"class numbers?", r"étale cohomology", r"perfectoid\w*", r"prismatic", r"diophantine (?:and|&) algebraic number",
        r"(?:quadratic|cubic|abelian|galois) (?:fields?|extensions?|forms)", r"ramification", r"function fields?", r"cohomology of number fields"]),
    "math.nt.arithmetic": ("math.nt", "Elliptic curves & arithmetic geometry", [
        r"elliptic curves?", r"arithmetic geometry", r"rational points?", r"mordell", r"abelian varieties", r"faltings", r"modular curves?", r"shimura (?:varieties|curves)", r"birch and swinnerton-dyer",
        r"diophantine (?:equations?|geometry|problems?)", r"chabauty", r"hasse principle", r"brauer-manin", r"curves over (?:finite fields|number fields|Q)", r"motives?", r"arithmetic (?:dynamics|surfaces|statistics|of curves|of elliptic|intersection)",
        r"supersingular", r"isogenies?", r"complex multiplication", r"jacobians? of curves", r"torsion (?:points|subgroups?)", r"mordell-weil", r"integral points?", r"thue", r"diophantine", r"(?:arithmetic|algebraic) (?:cycles|curves|surfaces|threefolds)", r"K3 (?:surfaces|arithmetic)", r"rank of elliptic"]),
    "math.nt.modular": ("math.nt", "Modular & automorphic forms, Langlands", [
        r"modular forms?", r"automorphic (?:forms?|representations?|L-functions?|spectrum)", r"langlands", r"hecke", r"shimura", r"maass forms?", r"theta (?:functions?|series|correspondence|lifts?)", r"mock (?:theta|modular)", r"siegel (?:modular|forms?)",
        r"jacobi forms?", r"eichler", r"ramanujan", r"partitions? (?:and|&)? ?q-series", r"q-series", r"partition (?:function|identities|theory)", r"fourier coefficients?", r"half-integral weight", r"modularity", r"eisenstein", r"weil representation",
        r"harmonic maass", r"quantum modular", r"galois (?:and|&) automorphic", r"geometric langlands", r"local langlands", r"rankin-selberg", r"spectral (?:theory of )?automorphic", r"hilbert modular", r"vector-valued modular", r"supercuspidal", r"L-packets?"]),
    "math.nt.additive": ("math.nt", "Additive & Diophantine number theory", [
        r"additive (?:combinatorics|number theory|bases)", r"diophantine approximation", r"transcendental number\w*", r"transcendence", r"irrationality", r"continued fractions?", r"waring'?s? problem", r"sum[- ]product", r"szemer(?:é|e)di",
        r"arithmetic progressions?", r"freiman", r"uniform distribution", r"equidistribution", r"metric number theory", r"roth'?s? theorem", r"sumsets?", r"higher[- ]order fourier", r"green-tao", r"combinatorial number theory", r"linear forms in logarithms",
        r"baker'?s? method", r"lattice points", r"geometry of numbers", r"diophantine (?:inequalit\w+|exponents?)", r"badly approximable", r"littlewood conjecture", r"normal numbers?", r"Pisot", r"integer sequences?", r"Fraenkel'?s conjecture", r"Beatty sequences?"]),
    "math.nt.crypto": ("math.nt", "Cryptography (mathematical)", [
        r"mathematical (?:cryptography|cryptology|aspects of cryptography)", r"cryptography (?:and|&) (?:number theory|coding|arithmetic|algebraic geometry)", r"elliptic curve cryptography", r"post-?quantum (?:cryptography|crypto|security)", r"lattice[- ]based (?:cryptography|cryptosystems?|schemes?)", r"public[- ]key", r"pairing[- ]based", r"zero[- ]knowledge",
        r"homomorphic encryption", r"hash functions?", r"cryptanalysis", r"isogeny[- ]based", r"multivariate (?:cryptography|cryptosystems?)", r"coding (?:and|&) cryptography", r"secret sharing", r"digital signatures?", r"encryption", r"block ciphers?", r"stream ciphers?",
        r"number[- ]theoretic (?:cryptography|algorithms?)", r"discrete logarithms?", r"factori[sz]ation (?:algorithms?|of integers)", r"primality testing", r"cryptographic (?:protocols?|primitives?|hardness)", r"code[- ]based cryptography", r"quantum[- ]resistant", r"security (?:proofs?|reductions?)"]),
    "math.nt.coding": ("math.nt", "Coding theory", [
        r"coding theory", r"error[- ]correcting codes?", r"algebraic codes?", r"CS:LDPC", r"polar codes?",
        r"reed[- ]solomon", r"network coding", r"channel coding", r"rank[- ]metric",
        r"codes? over (?:rings|fields|finite)", r"sphere packings?", r"lattices? (?:and|&) codes", r"index coding",
        r"coded (?:computation|caching|storage|distributed)", r"locally recoverable", r"DNA storage",
        r"constrained coding", r"combinatorial designs? (?:and|&) codes", r"quantum (?:error[- ]correcting )?codes", r"linear codes?", r"evaluation codes?"]),

    # ── Algebra ────────────────────────────────────────────────────────────────
    "math.algebra.comm": ("math.algebra", "Commutative algebra", [
        r"commutative algebra", r"free resolutions?", r"local cohomology", r"gr(?:ö|o)bner bases?", r"cohen-macaulay", r"hilbert (?:functions?|series|polynomials?)", r"syzyg\w+", r"regular sequences?", r"monomial ideals?", r"rees algebras?", r"integral closure", r"tight closure",
        r"betti numbers?", r"determinantal", r"noetherian rings?", r"valuation (?:rings?|theory)", r"k(?:ä|a)hler differentials", r"ideals? (?:and|&) (?:modules?|rings?)", r"regularity (?:of|and) ideals", r"binomial ideals?", r"toric ideals?", r"Stanley-Reisner",
        r"graded (?:rings?|modules?)", r"local rings?", r"complete intersections?", r"Gorenstein", r"homological (?:methods|conjectures)", r"commutative (?:rings?|and noncommutative)", r"injective (?:hulls?|dimension)", r"matlis duality", r"rings? (?:and|&) (?:ideals|modules)"]),
    "math.algebra.rings": ("math.algebra", "Noncommutative rings & modules", [
        r"non-?commutative (?:ring|rings|algebra|algebras|geometry)", r"ring theory", r"module (?:theory|categories)",
        r"associative algebras?", r"azumaya", r"division (?:rings?|algebras?)", r"leavitt", r"hochschild",
        r"ore extensions?", r"goldie", r"skew polynomial", r"algebras? (?:and|&) modules", r"Frobenius algebras?",
        r"hereditary (?:rings?|algebras?)", r"semiprime", r"prime rings?", r"radicals? of rings?", r"group rings?",
        r"morita", r"non-?commutative (?:algebraic|projective)", r"Leavitt path",
        r"rings? and (?:algebras|modules)"]),
    "math.algebra.quivers": ("math.algebra", "Representations of algebras, quivers & cluster algebras", [
        r"artin algebras?", r"path algebras?", r"quiver\w*", r"representation type", r"auslander-reiten", r"tilting",
        r"almost split", r"finite[- ]dimensional algebras?", r"cluster[- ]tilted", r"selfinjective",
        r"cellular algebras?", r"Brauer (?:algebras?|trees?)", r"derived equivalences?", r"torsion pairs?",
        r"t-structures?", r"cluster algebras?", r"quiver representations?", r"τ-tilting", r"tau-tilting", r"silting",
        r"gentle algebras?", r"string algebras?", r"preprojective algebras?", r"Gabriel'?s theorem",
        r"representation theory of (?:finite-dimensional |artin |associative |quiver )?algebras",
        r"cluster categor\w+", r"(?:cluster|quiver) mutations?", r"(?:wild|tame) (?:algebras|representation type)"]),
    "math.algebra.group": ("math.algebra", "Group theory", [
        r"(?<!geometric )(?<!measured )group theory", r"finite (?:groups?|simple groups?)", r"coxeter groups?",
        r"solvable groups?", r"nilpotent groups?", r"permutation groups?", r"profinite", r"classification of finite",
        r"p-groups?", r"character theory", r"symmetric groups?",
        r"group (?:actions?|cohomology|extensions?|presentations?|algebras?|rings?)", r"sporadic (?:groups?|simple)",
        r"monstrous moonshine", r"moonshine", r"automorphism groups?", r"outer automorphism", r"cohomology of groups",
        r"groups? (?:and|&) representations", r"Burnside", r"arithmetic groups?",
        r"lattices in (?:Lie|semisimple|algebraic)", r"linear groups?", r"discrete groups?"]),
    "math.algebra.ggt": ("math.algebra", "Geometric group theory", [
        r"geometric group theory", r"cayley graphs?", r"hyperbolic groups?", r"free groups?", r"braid groups?",
        r"mapping class groups?", r"growth of groups", r"out\(F_?n\)", r"right-angled artin",
        r"kazhdan(?![- ]lusztig)", r"thompson'?s? groups?", r"amenable groups?", r"property \(?T\)?",
        r"just infinite", r"branch groups?", r"self-?similar groups?", r"limit groups?", r"relatively hyperbolic",
        r"cubical(?! (?:type theory|sets?|homotopy))", r"CAT\(0\)", r"Out\(F", r"quasi-?isometr\w+",
        r"Gromov[- ]hyperbolic", r"Bass-Serre", r"JSJ", r"small cancellation", r"cube complex\w*", r"Artin groups?",
        r"lamplighter", r"F(?:ø|o)lner", r"measured group theory",
        r"groups? acting on (?:trees|CAT|hyperbolic|cube|buildings)", r"boundar(?:y|ies) of (?:hyperbolic )?groups",
        r"asymptotic (?:cones?|dimension)", r"curve complex(?:es)?",
        r"groups? (?:and|&) (?:geometry|dynamics|topology)"]),
    "math.algebra.lie": ("math.algebra", "Lie algebras & representation theory", [
        r"lie (?:algebras?|superalgebras?|theory|groups? (?:and|&) lie algebras)", r"representation theory",
        r"representations? of (?:lie|p-adic|algebraic|finite|reductive|quantum|affine|symmetric|general linear|classical|Hecke|\w+ algebras?|\w+ groups?)",
        r"kac[- ]moody", r"vertex (?:operator )?algebras?", r"affine (?:lie|hecke|algebras?|grassmannian|weyl)",
        r"hecke algebras?", r"weyl groups?", r"highest weight", r"crystal bases?",
        r"springer (?:correspondence|fibres?|resolution)", r"geometric representation theory", r"D-modules?",
        r"category O", r"schur[- ]weyl", r"macdonald", r"kazhdan[- ]lusztig", r"W-algebras?", r"yangians?",
        r"super(?:groups?|algebras?)", r"virasoro algebras?", r"invariant theory", r"harish-chandra",
        r"character formulas?", r"BGG", r"verma modules?", r"khovanov-lauda", r"categorification",
        r"modular representation theory", r"(?:finite|reductive) groups? of lie type", r"lusztig", r"Deligne-Lusztig",
        r"root systems?", r"Lie (?:types?|ideals?)", r"representation (?:growth|varieties|stability)",
        r"nilpotent orbits?", r"coadjoint orbits?", r"orbit method",
        r"classical (?:and|&) quantum (?:groups?|algebras?)", r"universal enveloping"]),
    "math.algebra.hopf": ("math.algebra", "Hopf algebras, quantum groups & tensor categories", [
        r"hopf algebras?", r"quantum groups?", r"tensor categor\w+", r"fusion categor\w+", r"monoidal categor\w+", r"drinfeld", r"quantum (?:symmetric|enveloping|algebras?|affine|cluster|torus|Weyl|Grassmannians?)", r"Yang-Baxter (?:operators?|algebras?)",
        r"bialgebras?", r"quasi-?triangular", r"modular tensor", r"module categor\w+", r"Hopf (?:Galois|module|cyclic)", r"Nichols algebras?", r"pointed Hopf", r"Kac algebras?", r"locally compact quantum groups?", r"compact quantum groups?", r"Drinfeld (?:double|center|associators?)", r"R-matri(?:x|ces)",
        r"knot invariants? (?:and|from) quantum", r"ribbon categor\w+", r"Temperley-Lieb", r"skein (?:theory|modules?|algebras?)", r"Verlinde", r"fusion rules?"]),
    "math.algebra.field": ("math.algebra", "Field & Galois theory, polynomials", [
        r"field (?:extensions?|arithmetic)", r"galois (?:theory|extensions?|groups?)", r"inverse galois", r"polynomial (?:rings?|equations?|factori[sz]ation|identities|systems?|maps?|dynamics|optimi[sz]ation|invariants?)", r"finite fields?", r"real closed", r"valued fields?",
        r"differential (?:algebra|galois|fields?)", r"difference (?:algebra|galois|fields?)", r"model theory of fields", r"hilbert'?s tenth", r"brauer groups?", r"central simple algebras?", r"quadratic forms?", r"witt (?:rings?|groups?|vectors?)", r"algebraic (?:extensions?|closure|numbers?|equations?|structures?)",
        r"local[- ]global (?:principles?)?", r"hilbert irreducibility", r"galois (?:cohomology|descent|embedding|covers?)", r"function field", r"polynomial (?:and|&) (?:rational|exponential)", r"zeros of polynomials?", r"symmetric polynomials?", r"ordered (?:fields?|groups?)", r"algebraic (?:and|&) (?:combinatorial|geometric)",
        r"permutation polynomials?", r"Weil (?:conjectures|bounds?)", r"fields? of (?:definition|moduli)", r"Henselian", r"Skolem", r"descent theory"]),
    "math.algebra.linear": ("math.algebra", "Linear & multilinear algebra", [
        r"(?:linear|multilinear|matrix) algebra", r"matrix (?:analysis|theory|inequalit\w+|completion|equations?|factori[sz]ations?|decompositions?|computations?|functions?|means|groups?|pencils?|polynomials?|inversion)", r"eigenvalues?", r"tensors?(?! networks?| modes?| perturbations?| mesons?| fields?|[- ]to[- ]scalar| forces?) ||| energy[- ]momentum|stress[- ]energy|gravitational|cosmolog\w*|inflation\w*|mesons?|nuclear", r"positive (?:definite|semidefinite)(?: matrices)?",
        r"perron-frobenius", r"singular values?", r"canonical forms?", r"toeplitz", r"linear (?:operators?|preservers?|maps?|systems?|transformations?)", r"numerical range", r"spectral (?:inequalities|radius|theory of matrices)", r"nonnegative matrices", r"totally positive", r"Hadamard (?:matrices|product)",
        r"matrix (?:mechanics|algebras?|theory and)", r"inverse eigenvalue", r"Schur complements?", r"companion matrices", r"tensor (?:rank|decompositions?|eigenvalues?|analysis|products?|theory)", r"low[- ]rank", r"permanents?", r"determinants?", r"Gershgorin", r"Jordan (?:forms?|algebras?)", r"orthogonal matrices", r"unitary (?:matrices|groups?)"]),
    "math.algebra.homological": ("math.algebra", "Homological algebra & K-theory", [
        r"homological algebra", r"derived categor\w+", r"triangulated categor\w+", r"k-theory", r"algebraic k-theory", r"cyclic homology", r"hochschild (?:homology|cohomology)", r"motivic (?:cohomology|homotopy|integration|K-theory)", r"spectral sequences?", r"A-infinity", r"stable categor\w+",
        r"grothendieck groups?", r"koszul", r"dg[- ]?(?:categories|algebras|modules)", r"model categor\w+", r"derived (?:algebraic geometry|functors?|equivalences?|geometry|moduli|Morita|Picard)", r"cohomological (?:methods?|dimension|invariants?|operations?)", r"ext groups?", r"tate cohomology", r"Hodge (?:theory and )?K-theory",
        r"bott periodicity", r"Waldhausen", r"trace methods?", r"topological cyclic", r"negative cyclic", r"periodic cyclic", r"Weibel", r"Quillen", r"Milnor K-theory", r"Chow groups?", r"Bloch-Kato", r"higher (?:K-theory|Chow)", r"singularity categories"]),
    "math.algebra.universal": ("math.algebra", "Universal algebra, lattices & semigroups", [
        r"universal algebra", r"lattice theory", r"lattices? (?:and|&) (?:order|ordered)", r"ordered (?:sets|structures|groups|algebraic)", r"boolean algebras?", r"semigroups?", r"monoids?", r"semirings?", r"varieties of algebras", r"quasigroups?", r"loops?(?: (?:theory|and))", r"clones?",
        r"congruences?", r"partially ordered", r"posets?", r"general algebraic systems", r"tropical (?:algebra|semiring)", r"heyting", r"residuated", r"algebraic logic", r"abstract algebra", r"lattice[- ]ordered", r"Galois connections?", r"closure (?:operators?|systems?)", r"formal concept analysis", r"fuzzy (?:algebra|logic|sets?)", r"mal'?cev", r"term rewriting", r"free (?:algebras?|semigroups?|monoids?|lattices?|objects?)", r"inverse semigroups?", r"transformation semigroups?", r"syntactic (?:monoids?|semigroups?)", r"varieties and pseudovarieties", r"Green'?s relations"]),

    # ── Geometry ───────────────────────────────────────────────────────────────
    "math.geometry.algebraic": ("math.geometry", "Algebraic geometry", [
        r"algebraic geometry", r"birational (?:geometry|classification|automorphisms?|maps?)",
        r"minimal model (?:program|theory)", r"CS:MMP",
        r"hodge (?:theory|structures?|conjecture|numbers?|theoretic|modules?|classes)", r"calabi-yau",
        r"K3 surfaces?",
        r"algebraic (?:varieties|surfaces|curves|cycles|stacks|groups?|threefolds?|spaces?|surfaces|manifolds?|topology of varieties|singularities)",
        r"sheaves?", r"schemes?(?! (?:of work|for))", r"intersection theory", r"vector bundles?",
        r"chow (?:rings?|motives?)", r"hilbert schemes?", r"picard (?:groups?|schemes?|rank)", r"fano", r"kodaira",
        r"grassmannians?", r"brill-noether", r"linear systems?", r"singularity theory",
        r"resolution of singularities", r"arc spaces?", r"stability conditions", r"bridgeland", r"jacobians?",
        r"abelian varieties", r"complex (?:algebraic|projective) (?:geometry|varieties)",
        r"projective (?:varieties|geometry|spaces?|schemes?)", r"coherent sheaves?", r"quasi-?coherent",
        r"derived categories? of (?:coherent|varieties)", r"sheaf cohomology", r"Cremona",
        r"rational (?:varieties|surfaces|curves)", r"del Pezzo", r"weak Fano",
        r"cubic (?:threefolds?|fourfolds?|surfaces?)", r"quartic", r"enriques", r"ample", r"nef", r"GIT quotients?",
        r"geometric invariant theory", r"quotient (?:singularities|stacks?)",
        r"equivariant (?:geometry|cohomology|K-theory)", r"Schubert (?:varieties|calculus|cells)",
        r"flag (?:varieties|manifolds)", r"Hodge-Tate"]),
    "math.geometry.moduli": ("math.geometry", "Moduli spaces, Teichmüller theory & hyperbolic geometry", [
        r"moduli (?:spaces?|stacks?|of)", r"stacks?(?: (?:and|&) moduli)", r"torelli", r"teichm(?:ü|u)ller",
        r"hyperbolic (?:geometry|surfaces?|manifolds?|3-manifolds?|space|metrics?|orbifolds?)",
        r"moduli of curves", r"Kleinian groups?", r"Fuchsian", r"Bers", r"Higgs bundles?", r"Hitchin",
        r"higher teichm(?:ü|u)ller", r"character varieties", r"Weil-Petersson", r"quasi-?Fuchsian", r"Kleinian",
        r"tautological (?:rings?|classes|intersections?)", r"stable curves", r"non-?abelian Hodge",
        r"Deligne-Mumford", r"Hitchin (?:systems?|fibrations?|components?)"]),
    "math.geometry.enumerative": ("math.geometry", "Enumerative geometry & mirror symmetry", [
        r"mirror symmetry", r"gromov-witten", r"donaldson-thomas", r"enumerative geometry", r"cohomological DT",
        r"quantum cohomology", r"curve counting", r"wall[- ]crossing", r"Gopakumar-Vafa", r"Pandharipande-Thomas",
        r"PT invariants", r"DT invariants", r"Hurwitz (?:numbers?|theory|spaces?)", r"homological mirror symmetry",
        r"CS:SYZ", r"topological recursion", r"BPS invariants?", r"Vafa-Witten",
        r"counting (?:curves|sheaves|rational curves)", r"enumerative (?:invariants|problems|algebraic geometry)"]),
    "math.geometry.diff": ("math.geometry", "Differential & Riemannian geometry", [
        r"differential geometry", r"riemannian (?:geometry|manifolds?|metrics?|submersions?|foliations?)",
        r"einstein (?:manifolds?|metrics?)", r"geodesic (?:flows?|rays?|currents?)", r"spin geometry",
        r"dirac operators?", r"holonomy", r"special holonomy", r"CS:G2", r"connections? on", r"spectral geometry",
        r"laplacian (?:eigenvalues?|spectrum|eigenfunctions?)", r"comparison geometry", r"alexandrov",
        r"gromov-hausdorff", r"sub-?riemannian", r"finsler", r"lorentzian (?:geometry|manifolds?)",
        r"pseudo-?riemannian", r"submanifolds?", r"surfaces in",
        r"(?<!berry )(?<!spacetime )(?<!mean )(?<!scalar )(?<!ricci )curvature(?! perturbations?| radiation| of spacetime| flows?| bounds?| pinching| estimates?) ||| berry|inflation\w*|cosmolog\w*|black holes?",
        r"differential (?:forms|systems|equations on manifolds)", r"cartan (?:geometr\w+|connections?)",
        r"conformal geometry", r"CR geometry", r"projective differential", r"parabolic geometr\w+",
        r"affine differential", r"geometry of (?:curves|surfaces)", r"curves and surfaces",
        r"manifolds? with (?:boundary|corners|curvature)",
        r"almost (?:complex|Hermitian|contact) (?:structures?|manifolds?)", r"Weyl (?:geometry|tensor)", r"Sasakian",
        r"Kaluza-Klein", r"warped products?", r"geometric (?:structures?|quantization)", r"Ricci-flat",
        r"geometric (?:topology and geometry)", r"differentiable manifolds?",
        r"vector (?:fields|bundles) on manifolds", r"index theorems?", r"heat kernels? (?:on|and) manifolds?",
        r"Riemannian (?:and|&) (?:Lorentzian|Finsler)"]),
    "math.geometry.analysis": ("math.geometry", "Geometric analysis & geometric flows", [
        r"geometric (?:analysis|flows?|evolution equations?|measure theory)", r"ricci (?:flow|curvature|solitons?)",
        r"mean curvature flow", r"curvature (?:flow|bounds?|pinching|estimates?)",
        r"minimal (?:surfaces?|submanifolds?|hypersurfaces?)", r"harmonic maps?", r"yamabe",
        r"gauge theory (?:and|in) geometry", r"yang-mills (?:connections|equations|instantons?|theory in geometry)",
        r"isoperimetric", r"willmore", r"scalar curvature", r"Calabi (?:flow|conjecture)",
        r"geometric (?:PDEs?|inequalit\w+|variational)", r"min-max (?:theory|methods?)", r"Almgren-Pitts",
        r"free boundary minimal", r"constant mean curvature", r"CMC (?:surfaces|hypersurfaces)",
        r"harmonic map (?:heat )?flow", r"inverse mean curvature", r"Gauss curvature flow", r"Kähler-Ricci flow",
        r"Plateau'?s? problem", r"Lichnerowicz"]),
    "math.geometry.symplectic": ("math.geometry", "Symplectic & contact geometry", [
        r"symplectic (?:geometry|topology|manifolds?|reduction|structures?|capacities|embeddings?|groups?|field theory|cohomology)", r"contact (?:geometry|topology|structures?|manifolds?|homology|forms?|invariants?)", r"floer (?:theory|homology|cohomology)", r"hamiltonian (?:dynamics|geometry|floer|diffeomorphisms|actions?|group actions?|PDEs?)",
        r"lagrangian (?:submanifolds?|floer|fibrations?|intersections?|cobordisms?|torus|mean curvature)", r"fukaya", r"pseudo-?holomorphic", r"moment maps?", r"geometric quantization", r"poisson (?:geometry|manifolds?|structures?|brackets?|algebras?|cohomology)", r"toric symplectic", r"Weinstein", r"Reeb", r"Legendrian", r"Gromov width", r"Seidel", r"Kontsevich", r"deformation quantization", r"symplectic (?:and|&) (?:contact|Poisson|complex)", r"integrable (?:systems? and|Hamiltonian)", r"action[- ]angle", r"Hamiltonian (?:and|&) (?:Lagrangian|symplectic)", r"Maslov", r"Arnold conjecture", r"mirror symmetry (?:and|&) (?:Fukaya|symplectic)", r"holomorphic curves", r"Gromov"]),
    "math.geometry.complex": ("math.geometry", "Complex & Kähler geometry", [
        r"complex (?:geometry|manifolds?|surfaces?|structures?|analytic geometry|hyperbolic|projective|tori)",
        r"k(?:ä|a)hler (?:geometry|manifolds?|metrics?|-Einstein|Ricci|-Einstein metrics|classes|cone|identities|potential)",
        r"several complex variables", r"pluripotential",
        r"holomorphic (?:vector bundles?|foliations?|maps?|functions?|curves?|dynamics|sections?|symplectic|Poisson)",
        r"stein (?:manifolds?|spaces?)", r"hermitian (?:geometry|metrics?|manifolds?|Yang-Mills|vector)",
        r"riemann surfaces?", r"uniformi[sz]ation", r"quasi-?conformal", r"kobayashi",
        r"CR (?:manifolds?|geometry|structures?)", r"plurisubharmonic", r"bergman", r"monge-amp(?:è|e)re",
        r"kodaira dimension", r"complex (?:dynamics|Monge-Ampère|Hessians?)", r"hyperk(?:ä|a)hler", r"CS:SCV",
        r"Nevanlinna", r"Oka", r"hyperbolicity", r"Hodge (?:theory|metrics?)", r"harmonic (?:bundles?|metrics?)",
        r"stable (?:bundles?|sheaves?)", r"Donaldson-Uhlenbeck", r"Kobayashi-Hitchin",
        r"complex (?:Lie|Kleinian|hyperbolic)", r"geometric complex analysis",
        r"holomorphic (?:and|&) (?:meromorphic|analytic)"]),
    "math.geometry.discrete": ("math.geometry", "Convex & discrete geometry", [
        r"convex (?:geometry|bodies|sets?|polytopes?|analysis|hulls?|and discrete)", r"discrete (?:geometry|and computational geometry|differential geometry|and convex)", r"polytopes?", r"polyhedr\w+", r"lattice (?:packings?|points|geometry|polytopes?|tilings?|coverings?)", r"sphere (?:packings?|coverings?)", r"tilings?", r"tessellations?",
        r"combinatorial geometry", r"computational geometry", r"minkowski", r"helly", r"brunn-minkowski", r"Santal(?:ó|o)", r"zonotopes?", r"oriented matroids?", r"arrangements? of (?:hyperplanes|lines|curves|pseudolines)", r"hyperplane arrangements?", r"euclidean (?:geometry|distance|space|Ramsey)", r"packing (?:and|&) covering", r"origami", r"rigidity (?:theory|of frameworks|and flexibility)", r"voronoi", r"triangulations?",
        r"geometric (?:graph|combinatorics|probability|inequalit\w+)", r"erd(?:ő|o)s (?:distance|unit distance)", r"incidence (?:geometry|problems?|bounds?)", r"projective geometry", r"finite geometr\w+", r"steiner", r"convex (?:optimization and|and) geometry", r"isoperimetric (?:inequalit\w+|problems?)", r"mixed volumes?", r"Ehrhart", r"geometric tomography", r"Banach-Mazur",
        r"Reuleaux", r"kissing numbers?", r"stochastic geometry", r"integral geometry", r"valuations on convex"]),
    "math.geometry.lie": ("math.geometry", "Lie groups & homogeneous spaces", [
        r"lie groups?", r"homogeneous (?:spaces?|manifolds?|dynamics|varieties|geometr\w+)", r"symmetric spaces?",
        r"discrete subgroups?", r"arithmetic groups?", r"lattices? in (?:lie|semisimple|algebraic|higher rank)",
        r"locally symmetric", r"margulis", r"rigidity (?:theorems?|of lattices)", r"zariski dense", r"thin groups?",
        r"anosov (?:representations?|groups?)", r"representation varieties", r"buildings? (?:and|&) groups?",
        r"bruhat-tits", r"algebraic groups?", r"reductive groups?", r"semisimple (?:groups?|lie)",
        r"p-adic (?:groups?|lie)", r"orbit (?:method|closures?|equivalence)", r"unitary representations?",
        r"harish-chandra", r"spherical (?:functions?|varieties)", r"howe duality",
        r"Lie (?:group|algebra) (?:actions?|cohomology)", r"Ratner", r"higher rank", r"superrigidity",
        r"strong approximation", r"Kazhdan (?:property|groups)", r"geometry of (?:Lie|homogeneous|symmetric)",
        r"flag manifolds?", r"coset (?:spaces|geometry)", r"G-structures?", r"isometry groups?",
        r"transformation groups?", r"compact (?:Lie|group)", r"Peter-Weyl"]),
    "math.geometry.tropical": ("math.geometry", "Tropical & toric geometry", [
        r"tropical (?:geometry|curves?|varieties|mathematics|algebra|semiring|moduli|intersection|compactifications?|Hodge|linear)", r"toric (?:varieties|geometry|ideals?|degenerations?|surfaces?|actions?|topology|manifolds?|stacks?)", r"newton[- ]okounkov", r"berkovich", r"non-?archimedean (?:geometry|analytic|spaces?|dynamics|metrics?)", r"rigid analytic",
        r"gelfand-zetlin", r"cluster varieties", r"log(?:arithmic)? geometry", r"polyhedral (?:geometry|combinatorics|complexes|fans?)", r"matroids?", r"valuated matroids?", r"bergman fans?", r"Newton polytopes?", r"fans? and (?:polytopes|toric)", r"Okounkov bodies", r"Khovanskii", r"mixed volumes?", r"discriminants?(?: and|&)? resultants?", r"sparse (?:polynomial|systems?|resultants?)",
        r"amoebas?", r"Gelfand-Kapranov", r"hypergeometric (?:systems?|functions?|D-modules?)", r"A-hypergeometric", r"tropicali[sz]ation", r"degenerations? of", r"semialgebraic", r"real (?:algebraic|enumerative) geometry", r"positive (?:geometry|Grassmannian)"]),

    # ── Topology ───────────────────────────────────────────────────────────────
    "math.topology.algebraic": ("math.topology", "Algebraic topology & homotopy theory", [
        r"algebraic topology",
        r"homotopy (?:theory|groups?|type theory|equivalences?|colimits?|limits?|invariants?|coherent|categories|operads?|quotients?|fixed points?)",
        r"stable homotopy", r"spectra", r"cohomology (?:theories|operations|rings?|of spaces|and)",
        r"homology (?:theories|of|and)", r"cobordism", r"characteristic classes", r"fibrations?",
        r"fib(?:er|re) bundles?", r"classifying spaces?", r"obstruction theory",
        r"simplicial (?:sets?|methods|homotopy|complexes?|objects?)", r"CW complexes?", r"loop spaces?", r"steenrod",
        r"postnikov", r"whitehead", r"eilenberg-maclane", r"elliptic cohomology", r"chromatic homotopy",
        r"equivariant (?:homotopy|topology|cohomology|stable)", r"model structures?",
        r"topological (?:K-theory|Hochschild|cyclic homology|modular forms?)", r"operads?", r"manifold calculus",
        r"goodwillie", r"motivic homotopy", r"rational homotopy", r"homotopy groups of spheres",
        r"infinity[- ]categor\w+", r"higher (?:algebra|topos|categor\w+)", r"synthetic homotopy",
        r"configuration spaces?", r"mapping spaces?", r"free loop", r"string topology",
        r"Hopf (?:invariant|fibration)", r"Adams (?:spectral|operations)", r"complex cobordism", r"formal groups?",
        r"Morava", r"tmf", r"Lusternik-Schnirelmann", r"homotopy (?:and|&) (?:homology|cohomology)"]),
    "math.topology.low": ("math.topology", "Low-dimensional topology & knot theory", [
        r"low[- ]dimensional topology", r"knot (?:theory|invariants?|polynomials?|floer|concordance|homology|groups?|diagrams?|tables?|complements?)", r"knots?(?: (?:and|&) links?)", r"3-?manifolds?", r"4-?manifolds?", r"(?:three|four)[- ]manifolds?", r"braids?", r"mapping class groups?", r"heegaard", r"khovanov", r"jones polynomial", r"kauffman",
        r"virtual knots?", r"surface (?:bundles?|topology|homeomorphisms?|groups?)", r"dehn (?:surgery|twists?|fillings?)", r"thurston", r"geometri[sz]ation", r"hyperbolic (?:3-manifolds?|knots?)", r"contact 3-manifolds?", r"seifert", r"foliations? (?:and|of) 3-manifolds?", r"gauge theory (?:and|&) (?:3|4)-manifolds?", r"seiberg-witten", r"donaldson",
        r"exotic (?:smooth structures?|R\^?4|4-manifolds?)", r"trisections?", r"kirby calculus", r"link (?:homology|invariants?|concordance|diagrams?)", r"quantum topology", r"vassiliev", r"tangle", r"cobordism categories", r"surface (?:diagrams?|knots?)", r"floer (?:homology|theory) (?:and|for) (?:3|knots)", r"instanton (?:homology|Floer)", r"monopole", r"Casson", r"Alexander (?:polynomial|module)", r"Lens spaces?", r"Dehn", r"Teichm(?:ü|u)ller (?:space|theory) and mapping", r"skein (?:modules?|algebras?|theory|categor\w+|functors?)", r"handlebod(?:y|ies)"]),
    "math.topology.diff": ("math.topology", "Differential & geometric topology, manifolds", [
        r"differential topology", r"smooth manifolds?", r"manifolds?(?! (?:learning|regulari[sz]ation|optimi[sz]ation))", r"surgery theory", r"h-cobordism", r"foliations?", r"morse (?:theory|homology|functions?)", r"transversality", r"immersions?", r"embeddings?(?! (?:models?|vectors?|layers?|space))", r"index theory", r"atiyah-singer", r"diffeomorphism groups?",
        r"positive scalar curvature", r"geometric topology", r"PL topology", r"topological manifolds?", r"novikov conjecture", r"baum-connes", r"farrell-jones", r"assembly maps?", r"h-principle", r"exotic (?:spheres?|structures?)", r"dimension theory", r"Pontryagin", r"Euler characteristic", r"vector fields? on manifolds?", r"fixed point theory", r"Lefschetz", r"Poincar(?:é|e) conjecture", r"orbifolds?", r"stratified spaces?", r"Reidemeister", r"L-theory", r"geometric structures? on manifolds?", r"flat (?:manifolds?|connections?)", r"characteristic numbers?", r"cobordism (?:groups?|rings?|and)", r"Atiyah"]),
    "math.topology.general": ("math.topology", "General & set-theoretic topology", [
        r"general topology", r"set[- ]theoretic topology", r"point[- ]set topology", r"continuum theory", r"continua", r"topological (?:spaces?|groups?|dynamics|vector spaces?|algebra|games?|properties)", r"uniform spaces?", r"metric spaces?", r"compactifications?", r"(?:č|c)ech", r"hyperspaces?", r"selection theorems?", r"stone (?:duality|spaces?)", r"descriptive set theory",
        r"polish spaces?", r"ultrafilters?", r"cardinal (?:functions?|invariants?)", r"coarse (?:geometry|spaces?|structures?|topology)", r"metric geometry", r"Baire", r"locales?", r"pointless topology", r"frames? and locales", r"topological (?:semigroups?|rings?|fields?|lattices?)", r"non-?Hausdorff", r"Wallman", r"Stone-(?:Č|C)ech", r"hereditarily", r"dimension (?:theory|functions?)", r"compact (?:spaces?|Hausdorff)", r"Moore spaces?", r"function spaces?", r"Wijsman"]),
    "math.topology.applied": ("math.topology", "Applied & computational topology (TDA)", [
        r"persistent homology", r"CS:TDA", r"topological complexity", r"applied (?:algebraic )?topology",
        r"topological data analysis", r"computational topology",
        r"persistence (?:diagrams?|modules?|landscapes?|barcodes?|theory)", r"Mapper (?:algorithm|graphs?)",
        r"discrete Morse theory",
        r"topological (?:signal processing|deep learning|machine learning|methods (?:in|for) data)",
        r"applied sheaf theory", r"sheaves (?:in|for) (?:data|applications|networks)", r"zigzag persistence",
        r"Vietoris-Rips", r"magnitude homology", r"CS:AATRN", r"random (?:simplicial complexes|topology)",
        r"topology (?:of|for) data", r"computational (?:and|&) applied topology"]),

    # ── Analysis ───────────────────────────────────────────────────────────────
    "math.analysis.real": ("math.analysis", "Real analysis, measure theory & fractals", [
        r"real analysis", r"measure theory", r"geometric measure theory", r"hausdorff (?:dimension|measures?|spaces?)", r"fractals?", r"fractal (?:geometry|sets?|dimension|analysis|measures?)", r"lebesgue", r"differentiation (?:of integrals|theory)", r"rectifiab\w+", r"besicovitch", r"metric (?:measure )?spaces?", r"lipschitz", r"BV functions?",
        r"sets? of finite perimeter", r"varifolds?", r"radon (?:measures?|transforms?)", r"self-similar (?:sets?|measures?)", r"iterated function systems?", r"CS:IFS", r"dimension of (?:sets|measures)", r"absolutely continuous", r"maximal functions?", r"carleson", r"muckenhoupt", r"orlicz", r"lorentz spaces?", r"interpolation (?:of operators|spaces)", r"functions? of bounded variation", r"analysis on (?:metric|fractal)", r"dirichlet forms?", r"sobolev (?:spaces?|inequalit\w+|functions?|maps?)", r"singular (?:measures?|integrals?|functions?)", r"banach[- ]tarski", r"Fourier (?:dimension|decay) of measures", r"geometric (?:and|&) fractal", r"Assouad", r"packing dimension", r"Falconer", r"Cantor (?:sets?|functions?)", r"Hardy-Littlewood maximal", r"Denjoy", r"monotone functions?", r"Riemann integrals?", r"Henstock", r"gauge integrals?", r"Stieltjes", r"integration theory", r"integral inequalit\w+", r"Hardy inequalit\w+", r"Poincar(?:é|e) inequalit\w+", r"Sobolev embeddings?", r"capacity theory", r"quasi-?conformal analysis"]),
    "math.analysis.complex": ("math.analysis", "Complex analysis & function theory", [
        r"complex analysis", r"conformal (?:mapping|maps?|invariants?|welding|radius|metrics?)", r"entire functions?", r"meromorphic functions?", r"nevanlinna", r"value distribution", r"holomorphic functions?", r"univalent(?! foundations| type| mathematics)", r"bergman (?:spaces?|kernels?)", r"hardy spaces?", r"analytic functions?", r"complex (?:variables?|plane|polynomials?|function theory)",
        r"harmonic functions?", r"loewner", r"julia sets?", r"mandelbrot", r"rational maps?", r"quasi-?regular", r"function theory", r"geometric function theory", r"riemann mapping", r"zeros of (?:polynomials|analytic|entire|random)", r"riemann-hilbert", r"monodromy", r"riemann surfaces?", r"Blaschke", r"Fuchsian", r"automorphic functions?", r"Dirichlet series (?:and|&) complex",
        r"analytic (?:continuation|capacity|number theory and complex)", r"normal families", r"singularities of (?:analytic|holomorphic)", r"conformal (?:analysis|geometry and analysis)", r"Hele-Shaw", r"Bieberbach", r"coefficient problems?", r"Carath(?:é|e)odory", r"complex (?:differential|difference) equations?", r"Painlev(?:é|e) (?:equations?|transcendents?)", r"holomorphic approximation"]),
    "math.analysis.harmonic": ("math.analysis", "Harmonic analysis & Fourier analysis", [
        r"harmonic analysis", r"fourier (?:analysis|transforms?|series|restriction|multipliers?|integral operators?|uniqueness|coefficients?|decay|expansions?|extension|integrals?)", r"wavelets?", r"time[- ]frequency", r"gabor", r"singular integral operators?", r"calder(?:ó|o)n[- ]zygmund",
        r"oscillatory integrals?", r"kakeya", r"restriction (?:problem|conjecture|estimates?|theorems?)", r"decoupling", r"multilinear (?:analysis|estimates?|operators?|harmonic)", r"paraproducts?", r"pseudo-?differential", r"fourier integral operators?", r"microlocal", r"abstract harmonic analysis", r"harmonic analysis on (?:groups?|homogeneous|manifolds?)",
        r"plancherel", r"spherical harmonics", r"uncertainty principles?", r"sparse (?:representations?|recovery)", r"multiresolution analysis", r"shearlets?", r"curvelets?", r"CS:SampTA", r"Littlewood-Paley", r"Hardy-Littlewood", r"Fourier (?:and|&) (?:harmonic|wavelet)", r"Bochner", r"almost periodic", r"Wiener (?:algebras?|Tauberian)", r"Tauberian", r"dispersive estimates", r"Strichartz estimates", r"square functions?", r"Hilbert transforms?", r"Riesz (?:transforms?|potentials?)", r"Besov", r"Triebel-Lizorkin", r"function spaces? (?:and|&) harmonic", r"Fourier (?:ana|multiplier)", r"signal (?:and|&) harmonic", r"good[- ]lambda inequalit\w+"]),
    "math.analysis.functional": ("math.analysis", "Functional analysis & operator theory", [
        r"functional analysis", r"banach (?:spaces?|algebras?|lattices?|space theory|manifolds?)", r"hilbert (?:spaces?|space operators?|transforms?)", r"operator (?:theory|spaces?|semigroups?|inequalit\w+|means|monotone|ideals?|norms?|models?|pencils?)", r"spectral theory", r"spectral (?:theorem|analysis|problems?|gaps?|asymptotics?|measures?|synthesis|flow|triples?)",
        r"semigroups? of operators", r"nonlinear functional analysis", r"locally convex", r"topological vector spaces?", r"geometry of banach", r"asymptotic geometric analysis", r"isomorphic banach", r"ultraproducts?", r"nonlinear (?:analysis|operators?|semigroups?|spectral)", r"fixed[- ]point (?:theory|theorems?|methods?)", r"monotone operators?", r"variational inequalit\w+", r"convex analysis", r"schr(?:ö|o)dinger operators?", r"self-?adjoint", r"unbounded operators?", r"toeplitz operators?", r"hankel operators?", r"fredholm", r"compact operators?", r"invariant subspaces?", r"pseudo-?spectra", r"CS:IWOTA", r"normed (?:spaces?|linear)", r"bounded linear", r"Schauder (?:bases?|theorem)", r"weak topolog\w+", r"Grothendieck (?:inequality|theorem)", r"Banach[- ]Mazur", r"best approximation in", r"Hilbert-Schmidt", r"trace class", r"Sobolev spaces? and", r"operator (?:convex|valued|functions?)", r"multipliers? (?:on|and) function", r"composition operators?", r"weighted composition", r"functions? spaces? (?:and|&) operators"]),
    "math.analysis.opalg": ("math.analysis", "Operator algebras & noncommutative geometry", [
        r"operator algebras?", r"C\*-algebras?", r"CS:C\*", r"von neumann algebras?", r"free probability", r"subfactors?", r"non-?commutative (?:geometry|topology|analysis|probability|spaces?|dynamics|tori|harmonic analysis)", r"connes", r"K-theory of (?:operator algebras|C\*)", r"KK-theory", r"groupoids?", r"crossed products?", r"cuntz", r"UHF", r"classification of (?:C\*|nuclear|simple)", r"elliott",
        r"II_?1 factors?", r"jones (?:index|subfactor)", r"hilbert C\*-modules?", r"spectral triples?", r"roe algebras?", r"quantum (?:probability|metric spaces?|dynamical|information and operator)", r"AF[- ]algebras?", r"nuclear C\*", r"exact groups?", r"property \(?T\)? and operator", r"rigidity (?:of|in) (?:von Neumann|operator)", r"modular theory", r"Tomita-Takesaki", r"completely positive", r"operator systems?", r"quantum channels? (?:and|&) operator", r"matrix algebras?", r"free (?:groups? factors?|entropy|independence|convolution)", r"cyclic cohomology", r"Hopf-cyclic", r"noncommutative (?:Poisson|residues?|torus|sphere|differential)", r"Cuntz-Krieger"]),
    "math.analysis.ode": ("math.analysis", "Ordinary differential equations", [
        r"ordinary differential equations?", r"CS:ODEs?", r"CS:ODE", r"differential equations?(?! (?:and|&) (?:applications|numerical))", r"boundary value problems?", r"initial value problems?", r"sturm-liouville", r"stability (?:theory|of (?:solutions|equilibria|periodic))", r"oscillation theory", r"periodic solutions?", r"bifurcation (?:theory|analysis|of|problems?)", r"floquet",
        r"delay differential", r"functional differential", r"fractional (?:differential|calculus|derivatives?|order|integrals?)", r"painlev(?:é|e)", r"qualitative theory", r"center manifolds?", r"singular perturbation\w*", r"asymptotic (?:methods?|expansions?)", r"dynamic equations on time scales", r"difference equations?", r"recurrence relations?",
        r"differential inclusions?", r"impulsive", r"integro-differential", r"lie symmetries", r"CS:EQUADIFF", r"differential (?:and|&) difference equations?", r"Hamiltonian (?:systems?|ODEs?|dynamics)", r"limit cycles?", r"Lyapunov functions?", r"invariant manifolds?", r"nonlinear oscillations?", r"geometric singular perturbation", r"slow-?fast", r"canard", r"Riccati", r"Duffing", r"van der Pol", r"Lotka-Volterra", r"mathematical (?:models?|modelling) (?:of|in) (?:ODE|dynamics)", r"existence (?:and|&) (?:uniqueness|multiplicity) of solutions", r"positive solutions?", r"upper and lower solutions", r"shooting method", r"Fuchsian (?:equations?|systems?)", r"Hill'?s equation", r"Mathieu"]),
    "math.analysis.pde": ("math.analysis", "Partial differential equations (general)", [
        r"partial differential equations?", r"CS:PDEs?", r"CS:PDE", r"weak solutions?", r"well-?posedness",
        r"blow-?up", r"global (?:existence|regularity)", r"calder(?:ó|o)n problem",
        r"inverse (?:problems?|scattering|boundary)", r"homogeni[sz]ation", r"hamilton-jacobi",
        r"mean[- ]field games?", r"ginzburg-landau",
        r"PDE (?:analysis|methods?|theory|and (?:geometry|probability|applications))", r"quasi-?linear",
        r"semilinear", r"singular (?:limits?|perturbations? of PDE)",
        r"asymptotic (?:behaviou?r|stability) (?:of|for) (?:solutions|PDE)", r"long[- ]time (?:behaviou?r|dynamics)",
        r"attractors? (?:for|of) (?:PDE|dissipative)", r"dissipative (?:PDE|equations?|systems?)",
        r"stochastic (?:PDEs?|partial)", r"CS:SPDEs?", r"Cauchy problems?"]),
    "math.analysis.elliptic": ("math.analysis", "Elliptic & parabolic PDE", [
        r"elliptic (?:equations?|PDE|operators?|regularity|systems?|problems?|and parabolic|boundary)",
        r"parabolic (?:equations?|PDE|regularity|systems?|problems?|and hyperbolic|flows?)", r"free boundary",
        r"stefan problem", r"regularity (?:theory|of solutions|for)", r"viscosity solutions?", r"schauder",
        r"de giorgi", r"harnack", r"nonlocal (?:equations?|operators?|problems?|diffusion|PDE)",
        r"fractional laplacian", r"p-laplac\w+", r"reaction[- ]diffusion", r"allen-cahn", r"cahn-hilliard",
        r"porous medium", r"heat (?:equations?|kernels?|flows? (?:on|of|for) (?:manifolds?|metrics|maps|graphs))", r"keller-segel", r"chemotaxis",
        r"degenerate (?:elliptic|parabolic|equations?)", r"fully nonlinear", r"Neumann problems?",
        r"Dirichlet problems?", r"obstacle problems?", r"transmission problems?", r"elliptic (?:and|&) parabolic",
        r"Monge-Amp(?:è|e)re equations?", r"Krylov-Safonov", r"(?:quasilinear|semilinear) (?:elliptic|parabolic)",
        r"Hele-Shaw", r"thin[- ]film equations?", r"fast diffusion"]),
    "math.analysis.waves": ("math.analysis", "Dispersive & wave equations", [
        r"hyperbolic (?:equations?|PDE|conservation laws|systems?|problems?|and dispersive|PDE)",
        r"dispersive (?:equations?|PDE|estimates?|dynamics|and wave|flows?|blow-?up)", r"nonlinear schr(?:ö|o)dinger",
        r"wave equations?", r"kdv", r"conservation laws?", r"schr(?:ö|o)dinger (?:evolution|flow)",
        r"scattering theory", r"strichartz", r"maxwell'?s? equations",
        r"einstein (?:equations?|constraint) (?:as|in) PDE", r"shock waves?", r"riemann problem",
        r"Hamiltonian PDEs?", r"nonlinear waves?", r"solitary waves?", r"Zakharov (?:systems?|equations?)", r"Klein-Gordon",
        r"Dirac equations?", r"Hartree(?![- ]Fock)", r"Gross-Pitaevskii", r"Schr(?:ö|o)dinger-Poisson",
        r"Benjamin-Ono", r"Camassa-Holm", r"Burgers", r"Korteweg", r"wave maps?",
        r"nonlinear (?:dispersive|Klein-Gordon|wave) equations?", r"soliton resolution", r"modified scattering",
        r"quasilinear wave", r"Kadomtsev-Petviashvili", r"systems of conservation laws",
        r"hyperbolic (?:and|&) dispersive", r"Chern-Simons-Schr(?:ö|o)dinger"]),
    "math.analysis.fluids": ("math.analysis", "Fluid & kinetic PDE", [
        r"navier[- ]stokes", r"euler equations?", r"boltzmann (?:equations?|PDEs?)", r"vlasov",
        r"kinetic (?:equations?|theory)", r"compressible (?:flows?|Euler|Navier)",
        r"incompressible (?:Euler|Navier|flows? (?:and|&) PDE)", r"magneto-?hydrodynamics (?:equations?|PDE)",
        r"water waves?", r"Euler-(?:Poisson|Korteweg|alignment)", r"Landau (?:equation|damping)",
        r"Boussinesq (?:equations?|system)", r"quasi-?geostrophic", r"Hall-MHD", r"active scalars?",
        r"Muskat (?:problem|equation)", r"Oldroyd", r"Stokes (?:equations?|system)", r"Cucker-Smale",
        r"aggregation[- ]diffusion", r"kinetic (?:models?|PDEs?)", r"mean[- ]field limits?"]),
    "math.analysis.calculus": ("math.analysis", "Calculus of variations", [
        r"calculus of variations",
        r"variational (?:methods?|problems?|principles?|analysis|calculus|inequalit\w+|models?|convergence|approach)",
        r"gradient flows?", r"gamma-?convergence", r"Γ-convergence", r"minimal (?:surfaces?|hypersurfaces?)",
        r"isoperimetric", r"optimal (?:shapes?|design)", r"shape optimi[sz]ation", r"free discontinuity",
        r"regularity of minimi\w+", r"plateau'?s? problem", r"mountain pass", r"critical point theory", r"lusternik",
        r"ekeland", r"quasi-?convex\w*", r"poly-?convex", r"elastic (?:energies|materials)", r"obstacle problems?",
        r"dirichlet principle", r"minimi[sz]ers?", r"minimi[sz]ation (?:problems?|of)",
        r"energy (?:minimi[sz]ers?|methods?|functionals?)", r"Euler-Lagrange", r"Young measures?",
        r"phase transitions? (?:and|&) (?:minimal|variational)", r"Modica-Mortola",
        r"Ginzburg-Landau (?:functionals?|vortices)", r"concentration[- ]compactness",
        r"optimal (?:Sobolev|constants?)", r"sharp inequalit\w+", r"Sobolev inequalities",
        r"rearrangement inequalit\w+", r"Steiner symmetri[sz]ation", r"calculus of variations (?:and|&) PDEs?",
        r"nonlinear elasticity"]),
    "math.analysis.ot": ("math.analysis", "Optimal transport", [
        r"optimal transport\w*", r"monge-kantorovich", r"wasserstein", r"mass transport", r"Brenier", r"Kantorovich",
        r"Schrödinger bridges?", r"entropic (?:regulari[sz]ation|optimal transport)", r"Sinkhorn",
        r"(?:unbalanced|martingale|multi-marginal|computational|semi-discrete) (?:optimal )?transport",
        r"displacement convexity", r"Benamou-Brenier"]),
    "math.analysis.approx": ("math.analysis", "Approximation theory & special functions", [
        r"approximation theory", r"special functions?", r"orthogonal polynomials?", r"jacobi polynomials?", r"hypergeometric", r"q-(?:special|hypergeometric)", r"bessel", r"gamma function", r"polynomial (?:approximation|interpolation|inequalit\w+)", r"splines?", r"radial basis", r"chebyshev", r"pad(?:é|e)", r"rational approximation", r"interpolation (?:theory|nodes)", r"szeg(?:ő|o)", r"riemann-hilbert (?:problems?|approach|analysis)",
        r"hermite", r"laguerre", r"askey", r"orthogonal (?:functions?|systems?|expansions?)", r"moment problems?", r"stieltjes", r"numerical approximation", r"n-widths?", r"optimal recovery", r"kolmogorov widths?", r"sampling (?:and|&) interpolation", r"CS:OPSFA", r"CS:IWOTA", r"zeros of (?:orthogonal|special)", r"Meixner", r"Krawtchouk", r"Wilson polynomials?", r"Racah", r"elliptic functions?", r"Appell", r"Lommel", r"hypergeometric (?:series|functions?|identities|orthogonal)", r"Ramanujan-type", r"summation formulas?", r"basic hypergeometric", r"umbral", r"generating functions? (?:and|&) special", r"orthogonal (?:and|&) special", r"Lauricella", r"Heun", r"Airy", r"Mittag-Leffler functions?", r"WKB", r"uniform asymptotic", r"exponential asymptotics", r"hyperasymptotics?"]),
    "math.analysis.inverse": ("math.analysis", "Integral equations, transforms & inverse problems", [
        r"integral equations?", r"integral transforms?",
        r"inverse (?:problems?|scattering|spectral|boundary value|source|eigenvalue|obstacle)", r"tomograph\w+",
        r"radon (?:transform|inversion)", r"regulari[sz]ation (?:methods?|theory|of ill-posed)", r"ill-?posed",
        r"imaging (?:inverse|and inverse)", r"electrical impedance", r"abel (?:integral|transform|equation)",
        r"volterra", r"fredholm (?:integral|equations?)", r"singular integral equations?",
        r"convolution (?:equations?|operators?)", r"wiener-hopf", r"boundary integral", r"layer potentials?",
        r"laplace transforms?", r"mellin", r"hilbert transforms?", r"scattering (?:theory|transform|inverse)",
        r"integral operators?", r"photoacoustic", r"x-ray transform", r"carleman estimates?", r"unique continuation",
        r"Landweber", r"Tikhonov", r"data assimilation", r"parameter identification", r"inverse (?:and|&) ill-posed",
        r"calderón", r"seismic inversion", r"full waveform inversion", r"geophysical inverse", r"deconvolution",
        r"integral geometry", r"geodesic ray transforms?", r"travel time tomography", r"boundary rigidity",
        r"lens rigidity"]),
    "math.analysis.potential": ("math.analysis", "Potential theory & pluripotential theory", [
        r"potential theory", r"pluripotential", r"green (?:functions?|kernels?|potentials?)", r"harmonic measure", r"dirichlet problems?", r"balayage", r"newtonian potential", r"subharmonic", r"martin boundary", r"riesz (?:potentials?|capacity|energy)", r"polar sets?", r"fine topology", r"potential (?:kernels?|operators?|analysis)", r"Brownian motion and potential", r"logarithmic potentials?", r"equilibrium measures?", r"energy (?:minimi[sz]ation|problems?) on", r"Fekete points?", r"transfinite diameter", r"weighted potential", r"external fields?", r"Coulomb gases", r"Frostman", r"Wiener criterion", r"regular points", r"Poisson (?:kernels?|integrals?)", r"nontangential", r"Hardy spaces? (?:and|&) potential"]),

    # ── Probability & statistics ───────────────────────────────────────────────
    "math.probability.theory": ("math.probability", "Probability theory & stochastic processes (general)", [
        r'probability (?:theory|measures?|distributions?|and statistics|limit theorems?|inequalit\w+|and (?:combinatorics|analysis|geometry)|seminar|colloquium|school)', r'stochastic (?:processes?|control|dynamics|models?|geometry|systems?|methods)', r'random (?:graphs?|media|processes|permutations?|polynomials?|fields?|sets?|measures?|dynamics)', r'brownian (?:motion|sheet|bridge|excursions?|sheets?)', r'martingales?', r'markov (?:decision|random fields?|models?)', r'gaussian (?:processes?|fields?|measures?|analysis)', r'large deviations?', r'limit theorems?', r'poisson (?:processes?|point|random)', r'branching (?:processes?|Brownian)', r'interacting particle systems?', r'exclusion process', r'l(?:é|e)vy processes?', r'jump (?:processes|diffusions|Markov processes)', r'heavy[- ]tailed', r'concentration (?:of measure|inequalit\w+)', r"stein'?s method", r'extreme value', r'point processes?', r'hydrodynamic limits?', r'metastability', r'random (?:schr(?:ö|o)dinger|operators?)', r'anderson (?:localization|model)', r'disordered (?:systems?|media)', r'Gibbs (?:measures?|states?|point processes?)', r'universality (?:in|of) (?:random|probability)', r'probabilistic (?:methods?|analysis|techniques)', r'stochastic (?:optimi[sz]ation|approximation|games?)', r'mathematical (?:finance|statistical physics)']),
    "math.probability.stochastic": ("math.probability", "Stochastic analysis, SDEs & SPDEs", [
        r'stochastic (?:analysis|calculus|differential equations?|partial differential|PDEs?|integration|quantization)', r'stochastic (?:filtering|volatility)', r'it(?:ô|o)', r'malliavin', r'rough paths?', r'regularity structures?', r'CS:SPDEs?', r'SDEs?', r'CS:SDE', r'stochastic (?:Navier|Burgers|heat|wave)', r'BSDEs?', r'backward stochastic', r'mckean-vlasov', r'propagation of chaos', r'diffusions', r'diffusion (?:processes|approximation)', r'nonlinear (?:filtering|expectations?)', r'mean[- ]field (?:limits?|models?|interacting)']),
    "math.probability.walks": ("math.probability", "Random walks, Markov chains & mixing", [
        r'random walks?', r'markov (?:chains?|processes?|operators?|semigroups?)', r'markov chain monte carlo (?:convergence|mixing)', r'branching random walks?', r'random walks? in random (?:environments?|media|scenery)', r'hitting times?', r'glauber dynamics', r'card shuffling', r'spectral gaps? (?:of|for) markov', r'mixing times?', r'cutoff phenomenon', r'coupling (?:methods?|from the past)']),
    "math.probability.geometry": ("math.probability", "Random geometry: SLE, percolation, random maps & trees", [
        r'random (?:trees?|maps?|planar maps?|surfaces|tilings?|geometry|geometries|growth|interfaces)', r'gaussian free field', r'gaussian multiplicative chaos', r'conformal loop ensembles?', r'CS:CLE', r'CS:LQG', r'brownian (?:map|sphere|plane|loop soups?)', r'loop soups?', r'dimer models?', r'uniform spanning (?:trees?|forests?)', r'spanning trees and forests', r'percolation', r'first[- ]passage percolation', r'schramm-loewner', r'CS:SLE', r'CS:KPZ', r'kardar-parisi-zhang', r'last passage', r'liouville quantum gravity', r'random (?:cluster|loop|conformal|planar) (?:models?|maps?)', r'critical (?:percolation|random)', r'Ising (?:model|and Potts)', r'lattice spin systems']),
    "math.probability.rmt": ("math.probability", "Random matrices & free probability", [
        r"random matri(?:x|ces)", r"random matrix theory", r"CS:RMT", r"free probability", r"dyson (?:brownian|index|model)", r"eigenvalue (?:statistics|distributions?|spacings?|fluctuations?|gaps?)", r"universality (?:of|in) (?:eigenvalue|local|random matrix)", r"determinantal point processes?", r"coulomb gases", r"log-?gases", r"β-?ensembles?", r"tracy-widom", r"CS:GUE", r"CS:GOE", r"orthogonal polynomial ensembles?", r"spiked (?:models?|matri\w+|covariance)", r"sample covariance", r"marchenko-pastur", r"high-dimensional (?:random|probability)", r"gaussian ensembles?", r"circular ensembles?", r"zeros of random polynomials?", r"free (?:convolution|cumulants?|entropy|independence)", r"large (?:random )?matrices", r"matrix models?", r"random (?:regular )?graphs? (?:spectra|eigenvalues)", r"non-?hermitian random", r"Ginibre", r"circular law", r"deformed Wigner", r"Gaussian (?:unitary|orthogonal|symplectic)", r"quantum chaos and random", r"level (?:spacing|repulsion|statistics)"]),
    # ── Statistics (its own branch since 2026-11-10; it keeps Probability's profile weights) ──
    "math.stat.mathstat": ("math.stat", "Mathematical statistics & inference", [
        r'mathematical statistics', r'statistical (?:inference|theory|modell?ing|estimation|testing|decision theory|computing|science)', r'hypothesis testing', r'estimation (?:theory|problems?|and (?:inference|testing))', r'sampling (?:methods|theory|designs?)', r'monte carlo (?:sampling|integration|methods)', r'bootstrap (?:methods?|confidence|resampling|estimators?|inference)', r'multivariate (?:analysis|statistics|methods?)', r'functional data', r'econometrics', r'likelihood', r'sequential (?:analysis|testing|methods?|monte carlo)', r'semi-?parametric', r'extreme value (?:statistics|theory)', r'statistics (?:and|&) (?:data science|machine learning|probability)', r'uncertainty quantification', r'CS:UQ', r'CS:JSM', r'statistical (?:and|&) (?:applied|computational)', r'robust statistics', r'order statistics', r'sample surveys?', r'statistical quality', r'reliability (?:theory|analysis|engineering) ||| software', r'stochastic modell?ing (?:and|&) statistics', r'applied (?:statistics|probability and statistics)', r'conformal prediction', r'multiple testing', r'false discovery', r'mixture models?', r'statistical (?:network|graph) analysis', r'missing data']),
    "math.stat.bayes": ("math.stat", "Bayesian statistics & computation", [
        r'bayesian (?:statistics|inference|nonparametrics?|modell?ing|optimi[sz]ation)', r'CS:MCMC', r'CS:ISBA', r'approximate bayesian', r'CS:ABC', r'variational inference', r'gaussian process (?:regression|models?)', r'simulation[- ]based inference', r'CS:SBI', r'bayesian (?:computation|methods?|analysis|hierarchical|model selection)', r'variational bayes', r'markov chain monte carlo', r'hamiltonian monte carlo', r'sequential monte carlo', r'posterior (?:sampling|inference|contraction|distributions?)', r'prior (?:elicitation|distributions?|specification)', r'likelihood-free', r"bayesian"]),
    "math.stat.highdim": ("math.stat", "High-dimensional & nonparametric statistics", [
        r'high[- ]dimensional (?:statistics|inference|regression)', r'non-?parametric (?:statistics|estimation|regression|inference|methods?|testing)', r'(?:linear|logistic|quantile|ridge|lasso) regression', r'empirical process\w*', r'minimax', r'sparse (?:regression|estimation|models?|learning)', r'high[- ]dimensional data', r'lasso', r'density estimation', r'kernel (?:density|smoothing)', r'covariance (?:matrix )?estimation', r'model selection', r'shrinkage (?:estimat\w+|priors?)', r'statistical (?:optimal transport|learning in high dimensions)']),
    "math.stat.timeseries": ("math.stat", "Time series, spatial & spatio-temporal statistics", [
        r'time series (?:analysis|models?)', r'spatial statistics', r'change[- ]?point', r'time series (?:methods|forecasting|econometrics)', r'spatio-?temporal (?:statistics|models?|data|modell?ing)', r'geostatistics', r'kriging', r'state[- ]space models?', r'CS:ARIMA', r'statistical forecasting', r'functional time series', r'point pattern analysis']),
    "math.stat.causal": ("math.stat", "Causal inference & design of experiments", [
        r'causal inference', r'experimental design', r'design of experiments', r'causal (?:discovery|effects?|models?|machine learning)', r'treatment effects?', r'instrumental variables?', r'randomi[sz]ed (?:controlled )?(?:trials?|experiments?)', r'potential outcomes', r'propensity scores?', r'observational studies', r'CS:A/B test\w*']),
    "math.stat.bio": ("math.stat", "Biostatistics & epidemiological methods", [
        r'bio-?statistics', r'survival analysis', r'clinical trials? statistics', r'statistical (?:design|analysis) of clinical trials', r'statistical (?:genetics?|genomics|epidemiology)', r'genome-wide association', r'CS:GWAS', r'epidemiological (?:methods|statistics)', r'medical statistics', r'pharmacometrics', r'statistics (?:for|in) (?:biology|genomics|medicine)']),
    "math.stat.physical": ("math.stat", "Statistics in the physical sciences & astrostatistics", [
        r'astro-?statistics', r'cosmostatistics', r'statistics (?:for|in) (?:astronomy|physics|cosmology|particle physics|climate|the physical sciences)', r'CS:PhyStat', r'statistical (?:methods|techniques|challenges|issues) (?:in|for) (?:astronomy|astrophysics|cosmology|physics|particle physics|high[- ]energy physics)', r'school of statistics', r'statistical data analysis']),
    "math.mathphys.qm": ("math.mathphys", "Mathematical quantum mechanics & spectral theory", [
        r"mathematical (?:quantum mechanics|aspects of quantum|quantum theory|physics of quantum)", r"schr(?:ö|o)dinger operators?", r"spectral theory (?:in|of) (?:mathematical|quantum)", r"quantum (?:spin systems?|many-body (?:systems?|physics|problems?) (?:and|rigorous))", r"many-body quantum mechanics", r"rigorous (?:quantum|many-body|results)", r"bose gases", r"gross-pitaevskii", r"hartree (?:equations?|dynamics|theory)",
        r"stability of matter", r"semiclassical analysis", r"semi-?classical (?:analysis|methods|limits?|approximations?|Schr)", r"scattering (?:theory|matrix) (?:in|of) quantum", r"quantum graphs?", r"Lieb-Robinson", r"quantum (?:spin|lattice) systems? (?:and|&) (?:operator|C\*)", r"Anderson (?:model|localization) (?:and|in)", r"random Schr(?:ö|o)dinger", r"magnetic (?:Schr(?:ö|o)dinger|Laplacian|fields? and spectral)", r"Landau levels?", r"Aharonov-Bohm", r"spectral (?:properties|gaps?|asymptotics) of (?:Schr|quantum)", r"Pauli (?:operators?|equation)", r"Dirac (?:operators?|Hamiltonians?|equation) (?:and|in)", r"relativistic (?:quantum|Schr)", r"quantum (?:ergodicity|chaos) (?:and|&) (?:mathematical|spectral)", r"Weyl (?:law|asymptotics)", r"eigenvalue (?:bounds|asymptotics) (?:for|of)", r"Lieb-Thirring", r"Hardy-Lieb-Thirring", r"Hardy-type inequalit\w+", r"quantum (?:ergodic|unique ergodicity)", r"mathematical (?:methods|physics) of quantum", r"Bose-Einstein condensation (?:and|&) rigorous", r"adiabatic (?:theorems?|theory|approximation)", r"Born-Oppenheimer", r"N-body (?:quantum|Schr)", r"quantum (?:mean[- ]field|Hartree|dynamics) (?:and|&) rigorous"]),
    "math.mathphys.statmech": ("math.mathphys", "Rigorous statistical mechanics", [
        r"rigorous (?:statistical|results in) (?:mechanics|physics)", r"mathematical (?:statistical (?:mechanics|physics)|physics of (?:statistical|phase))", r"statistical mechanics: a rigorous", r"lattice (?:models?|spin systems?|gauge) (?:and|&)? ?(?:rigorous|phase)", r"gibbs (?:measures?|states?|ensembles?)", r"cluster expansions?", r"phase (?:transitions?|coexistence) (?:in|for) (?:lattice|rigorous|spin)",
        r"ising (?:model|models?) (?:rigorous|and|in)", r"potts", r"XY model", r"Berezinskii", r"Kosterlitz-Thouless", r"reflection positivity", r"infrared bounds?", r"Mermin-Wagner", r"Pirogov-Sinai", r"spin glasses? (?:rigorous|mathematical)", r"Sherrington-Kirkpatrick", r"Parisi", r"replica (?:symmetry breaking|method) (?:rigorous|mathematical)", r"thermodynamic (?:limit|formalism|pressure)", r"correlation (?:inequalit\w+|functions? (?:and|in) (?:rigorous|lattice))", r"FKG", r"random (?:cluster|current|loop) (?:model|representation)", r"conformal invariance (?:in|of) (?:statistical|critical)", r"2D (?:Ising|critical|statistical)", r"dimer (?:models?|configurations?)", r"six-vertex", r"vertex models?", r"integrable (?:statistical|lattice) models?", r"Bethe (?:ansatz|lattice)", r"quantum (?:Ising|lattice|spin) (?:models?|systems?)", r"Hubbard model (?:rigorous|and)", r"mathematical (?:aspects|foundations) of statistical"]),
    "math.mathphys.qft": ("math.mathphys", "Mathematical QFT, TQFT & vertex algebras", [
        r"constructive (?:quantum field|QFT)", r"algebraic quantum field", r"conformal nets?", r"vertex (?:operator )?algebras?", r"mathematical (?:quantum field theory|aspects of (?:quantum field|QFT|gauge|string)|gauge theory|string theory)", r"rigorous (?:quantum field|QFT|gauge)", r"yang-mills (?:existence|mass gap)", r"mass gap", r"topological (?:quantum )?field theor\w+ (?:and|&) (?:geometry|mathematical|invariants?)", r"extended TQFTs?", r"factorization algebras?", r"locally covariant", r"quantum fields? (?:on|in) curved", r"curved spacetimes?", r"Hadamard states?", r"renormali[sz]ation (?:and|&) (?:Hopf|operads?|mathematical)", r"perturbative (?:algebraic|constructive)", r"Epstein-Glaser", r"BV[- ]formalism", r"Batalin-Vilkovisky", r"deformation quantization", r"geometric (?:quantization|Langlands) (?:and|&) (?:physics|QFT)", r"Kapustin-Witten", r"mathematics of (?:quantum field|string|gauge)", r"Coulomb branch", r"Higgs branch", r"symplectic duality", r"Seiberg-Witten (?:theory|geometry|curves?)", r"Nekrasov", r"AGT correspondence", r"Gaiotto", r"mathematics (?:and|&) (?:physics) of (?:gauge|strings?)"]),
    "math.mathphys.integrable": ("math.mathphys", "Integrable systems & solitons", [
        r"integrable (?:systems?|hierarch\w+|models?|PDEs?|equations?|lattices?|Hamiltonian|geometry|probability|quantum)", r"integrability", r"solitons?", r"soliton (?:theory|equations?|solutions?)", r"painlev(?:é|e) (?:equations?|transcendents?|property|test)", r"riemann-hilbert (?:problems?|method|approach)", r"yang-baxter", r"quantum (?:groups?|integrable)", r"lax (?:pairs?|representation|equations?)", r"kdv (?:hierarchy|equations?)", r"toda (?:lattice|hierarchy)", r"inverse scattering", r"tau[- ]functions?", r"isomonodromic?", r"isomonodromy", r"spectral curves?", r"Frobenius manifolds?", r"Gromov-Witten (?:and|&) integrable", r"Hitchin (?:systems?|fibrations?)", r"Calogero", r"Ruijsenaars", r"Hirota", r"Kadomtsev", r"bi-?Hamiltonian", r"Poisson (?:structures?|brackets?) (?:and|&) integrable", r"symmetries (?:and|&) integrability", r"discrete (?:integrable|Painlev)", r"cluster (?:integrable|algebras? and integrable)", r"Bethe (?:ansatz|equations?|roots?)", r"quantum (?:inverse scattering|spectral curves?)", r"exactly solvable", r"Sine-Gordon", r"Sinh-Gordon", r"nonlinear Schr(?:ö|o)dinger (?:hierarchy|integrable)", r"Boussinesq", r"Darboux", r"Bäcklund", r"Hamiltonian reductions?"]),
    "math.mathphys.relativity": ("math.mathphys", "Mathematical relativity & geometric analysis of spacetime", [
        r"mathematical (?:general )?relativity", r"(?:cauchy|initial value) problem (?:for|in) (?:the )?einstein", r"cosmic censorship", r"black hole (?:stability|uniqueness|interiors?)", r"stability of (?:minkowski|kerr|black holes?|de Sitter|solitons? in)", r"einstein (?:equations?|constraint equations?|field equations?|manifolds?|metrics?)", r"positive mass", r"penrose (?:inequality|conjecture|singularity)", r"trapped surfaces?", r"apparent horizons?", r"constant mean curvature", r"asymptotically (?:flat|hyperbolic|AdS)", r"initial data sets?", r"gluing (?:constructions?|initial)",
        r"geometric analysis (?:in|of|and) (?:general relativity|spacetime|gravity)", r"Lorentzian (?:geometry|manifolds?|causality)", r"causal (?:structure|theory|boundary)", r"global hyperbolicity", r"spacetime (?:geometry|singularities|inequalit\w+)", r"hawking (?:area|singularity)", r"wave (?:equations?|maps?) on (?:curved|black|Kerr|Schwarzschild)", r"decay (?:of|for) (?:waves?|solutions?) (?:on|in) (?:Kerr|Schwarzschild|black)", r"Price'?s law", r"quasi-?local (?:mass|energy)", r"conformal (?:methods|compactification) in relativity", r"Bondi", r"null infinity", r"Friedrich", r"Christodoulou", r"shock (?:formation|waves?) (?:in|for) (?:relativistic|Euler)", r"relativistic (?:fluids?|Euler|kinetic|Boltzmann|Vlasov)", r"Einstein-Vlasov", r"Einstein-Maxwell", r"Einstein-Dirac", r"Einstein-scalar", r"mathematical (?:aspects|problems?) (?:of|in) (?:gravitation|general relativity|cosmology)"]),

    # ── Dynamical systems ──────────────────────────────────────────────────────
    "math.dyn.ergodic": ("math.dyn", "Ergodic theory & topological dynamics", [
        r"ergodic (?:theory|theorems?|properties|averages?|decomposition)", r"ergodic(?:ity)?",
        r"measure[- ]preserving", r"invariant measures?", r"furstenberg",
        r"entropy (?:theory|of|in) (?:dynamical|ergodic|systems|measure)",
        r"bernoulli (?:shifts?|systems?|processes)", r"unique ergodicity",
        r"mixing (?:properties|systems?|rates?|flows?)", r"subshifts?", r"surjunctiv\w+", r"symbolic dynamics",
        r"shifts? of finite type", r"topological dynamics", r"minimal (?:systems?|flows?|sets?|homeomorphisms?)",
        r"billiards?", r"Zd[- ]actions?", r"group actions? (?:and|on) (?:measure|dynamical)", r"orbit equivalence",
        r"measurable dynamics", r"Kakutani", r"cutting and stacking", r"substitution (?:systems?|dynamical|tilings?)",
        r"aperiodic (?:order|tilings?)", r"quasi-?crystals? (?:and|&) dynamics",
        r"entropy (?:and|&) (?:dimension|dynamics)", r"measure[- ]theoretic entropy", r"Kolmogorov-Sinai",
        r"joinings?", r"disjointness", r"Sarnak", r"Möbius (?:disjointness|randomness)"]),
    "math.dyn.hyperbolic": ("math.dyn", "Hyperbolic dynamics & Hamiltonian systems", [
        r"hyperbolic (?:dynamics|dynamical systems?|flows?|sets?|measures?|attractors?)", r"anosov", r"partially hyperbolic", r"thermodynamic formalism", r"SRB (?:measures?|states?)", r"pesin", r"lyapunov exponents?", r"uniform hyperbolicity", r"horseshoes?", r"attractors?", r"strange attractors?", r"structural stability", r"dominated splittings?", r"geodesic flows?", r"hamiltonian dynamics", r"CS:KAM", r"arnold diffusion", r"celestial mechanics", r"n-body problem", r"three-body problem", r"twist maps?", r"area-preserving", r"aubry-mather", r"diffeomorphisms", r"stable manifolds?", r"normal(?:ly)? hyperbolic", r"rotation numbers?", r"circle (?:maps?|diffeomorphisms|homeomorphisms)", r"dynamical zeta", r"ruelle", r"transfer operators?", r"resonances? (?:for|of) (?:flows?|Anosov|dynamical)", r"Smale", r"homoclinic", r"heteroclinic", r"Lorenz (?:attractor|flow|system)", r"chaotic (?:attractors?|hyperbolic)", r"statistical (?:properties|laws) (?:of|for) (?:dynamical|chaotic)", r"decay of correlations", r"central limit theorems? (?:for|in) (?:dynamical|chaotic)", r"Axiom A", r"expanding maps?", r"Markov partitions?", r"Hénon", r"intermittent (?:maps?|dynamics)", r"billiards? (?:and|&) (?:chaos|hyperbolic)", r"Hamiltonian (?:systems?|chaos|dynamics) (?:and|&) (?:KAM|stability)", r"Nekhoroshev", r"symplectic dynamics", r"invariant tori"]),
    "math.dyn.complex": ("math.dyn", "Complex & holomorphic dynamics", [
        r"complex dynamics", r"holomorphic dynamics", r"julia sets?", r"fatou", r"mandelbrot", r"rational (?:maps?|dynamics)", r"polynomial dynamics", r"siegel disks?", r"iteration of (?:rational|holomorphic|entire|polynomials?)", r"quasi-?conformal (?:dynamics|surgery)", r"renormali[sz]ation (?:in|of) (?:complex|unimodal|dynamics)", r"unimodal maps?", r"bifurcation locus", r"p-adic dynamics", r"non-?archimedean dynamics", r"berkovich dynamics", r"dynamics of (?:polynomials|rational|entire|holomorphic|meromorphic)",
        r"several complex variables dynamics", r"h(?:é|e)non", r"b(?:ö|o)ttcher", r"Kleinian (?:groups?|dynamics)", r"Teichm(?:ü|u)ller (?:and|&) complex dynamics", r"Thurston (?:equivalence|obstruction|maps?)", r"Cantor (?:Julia|bouquet)", r"parabolic (?:dynamics|implosion)", r"Fatou coordinates", r"holomorphic (?:flows?|foliations?|motions?)", r"Lattès", r"postcritically finite", r"dynamical (?:uniform|Mordell)", r"arithmetic (?:and|&) complex dynamics", r"Montel (?:theorem|and)", r"critical (?:orbits?|points?) (?:and|&) dynamics", r"external rays?", r"laminations?"]),
    "math.dyn.homogeneous": ("math.dyn", "Homogeneous & arithmetic dynamics", [
        r"ratner", r"homogeneous dynamics", r"teichm(?:ü|u)ller dynamics", r"translation surfaces?",
        r"interval exchange", r"flows? on (?:homogeneous|surfaces|moduli)", r"arithmetic dynamics",
        r"diophantine (?:and|&) dynamics", r"unipotent (?:flows?|dynamics|orbits?)",
        r"equidistribution (?:of|in) (?:orbits|homogeneous|horospheres|periodic)", r"Oppenheim conjecture",
        r"Veech (?:surfaces?|groups?)", r"Masur-Veech", r"SL\(2,\s?R\)",
        r"dynamics on (?:homogeneous|moduli|the moduli) spaces?",
        r"dynamical (?:Mordell-Lang|Manin-Mumford|Galois|moduli|degrees?)", r"preperiodic points?",
        r"canonical heights?", r"(?:p-adic|non-archimedean) dynamics",
        r"(?:dynamics|dynamical systems) over (?:number fields|function fields|finite fields)", r"horocycle flows?",
        r"Diophantine approximation (?:and|&|on) (?:homogeneous|dynamics|manifolds)", r"shrinking targets?"]),
    "math.dyn.general": ("math.dyn", "Dynamical systems (general)", [
        r"dynamical systems?", r"discrete dynamical systems?", r"difference equations? and (?:discrete )?dynamical", r"topological entropy", r"iterated (?:maps?|function)", r"cellular automata", r"random dynamical systems?", r"stochastic dynamical", r"skew products?", r"poincar(?:é|e) (?:maps?|sections?|recurrence)", r"koopman", r"data[- ]driven (?:dynamical|modell?ing of dynamics)", r"dynamical systems (?:and|&) (?:ergodic|applications|ODE|topology|geometry|number theory)", r"dynamics (?:and|&) (?:geometry|topology|number theory|group)", r"smooth dynamics", r"low[- ]dimensional dynamics", r"one-dimensional dynamics", r"interval maps?", r"CS:EQUADIFF", r"bifurcations? (?:of|in) (?:maps?|dynamical)", r"conjugacy", r"semi[- ]?conjugacy", r"invariants? (?:of|for) dynamical", r"fixed points? (?:and|&) periodic", r"periodic (?:orbits?|points?)", r"orbit (?:growth|counting|closures)", r"(?<!quantum )chaos (?:in|and|theory)", r"dynamics (?:of|on) (?:networks?|graphs?)", r"nonautonomous (?:dynamical|systems?)", r"skew[- ]product", r"asymptotic dynamics"]),

    # ── Combinatorics ──────────────────────────────────────────────────────────
    "math.comb.algebraic": ("math.comb", "Algebraic combinatorics", [
        r"algebraic combinatorics", r"symmetric functions?", r"young tableaux", r"schur (?:functions?|polynomials?)", r"macdonald polynomials?", r"schubert (?:calculus|polynomials?|varieties)", r"catalan (?:numbers?|objects?|structures?)", r"coxeter combinatorics", r"hopf algebras? in combinatorics", r"matroids?", r"polytopes? (?:and|&) combinatorics", r"ehrhart", r"permutation (?:patterns?|statistics)", r"lattice paths?",
        r"bijective", r"plethysm", r"kostka", r"littlewood-richardson", r"representation theory of the symmetric", r"algebraic graph theory", r"association schemes?", r"chromatic (?:polynomials?|symmetric)", r"tutte", r"root systems?", r"crystal graphs?", r"dimers?", r"total positivity", r"positroids?", r"grassmannian (?:combinatorics|cells)", r"CS:FPSAC", r"algebraic and (?:geometric|enumerative) combinatorics", r"poset (?:topology|theory|combinatorics)", r"order polytopes", r"flag (?:complexes|varieties) (?:and|&) combinatorics", r"cluster (?:algebras?|combinatorics) (?:and|&) combinatorics", r"Hecke (?:algebras?|combinatorics)", r"tableaux", r"RSK", r"Robinson-Schensted", r"symmetric (?:groups?|functions?) and combinatorics", r"noncrossing", r"associahedr\w+", r"Stanley (?:symmetric|-Reisner)", r"Cohen-Macaulay (?:posets?|complexes)", r"Gelfand-Tsetlin", r"alternating sign matrices", r"CS:ASM", r"six-vertex (?:and|&) (?:combinatorics|ASM)"]),
    "math.comb.enumerative": ("math.comb", "Enumerative & analytic combinatorics", [
        r"enumerative combinatorics", r"generating functions?", r"asymptotic enumeration", r"analytic combinatorics", r"combinatorial (?:enumeration|species|identities|sequences|structures|designs?|methods|objects|interpretations?|proofs?)", r"bijections?", r"counting (?:problems?|formulas?|lattice|structures)", r"q-analogs?", r"lattice (?:walks|paths)", r"pattern (?:avoidance|avoiding)", r"permutation patterns?", r"combinatorics on words", r"automatic sequences", r"integer (?:partitions?|sequences?)", r"random combinatorial", r"CS:AofA", r"combinatorial (?:and|&) (?:probabilistic|analytic)", r"words? (?:combinatorics|avoiding)", r"Fibonacci", r"Stirling numbers?", r"Eulerian (?:numbers?|polynomials?)", r"tilings? (?:and|&) (?:enumeration|counting)", r"WZ (?:method|pairs?)", r"holonomic", r"D-finite", r"experimental mathematics", r"creative telescoping", r"computer algebra (?:and|&) combinatorics", r"CS:FPSAC", r"urn models?", r"Pólya"]),
    "math.comb.extremal": ("math.comb", "Extremal & probabilistic combinatorics, Ramsey theory", [
        r"extremal (?:combinatorics|graph theory|set theory|problems?|and probabilistic)", r"probabilistic (?:combinatorics|method)", r"ramsey (?:theory|numbers?|problems?)", r"tur(?:á|a)n", r"szemer(?:é|e)di", r"regularity (?:lemma|method)", r"random graphs?", r"graph limits?", r"graphons?", r"hypergraphs?", r"erd(?:ő|o)s", r"additive combinatorics", r"sum-?free", r"sidon", r"lov(?:á|a)sz local lemma", r"container method", r"discrepancy", r"VC[- ]dimension", r"polynomial method", r"zarankiewicz", r"sperner", r"set systems?", r"intersecting families?", r"kruskal-katona", r"van der waerden", r"hales-jewett", r"combinatorial number theory", r"latin squares?", r"block designs?", r"finite (?:geometr\w+|projective planes?)", r"steiner systems?", r"hadamard matrices", r"random structures?", r"CS:Eurocomb", r"combinatorics (?:and|&) (?:probability|number theory|geometry|computing)", r"graph (?:Ramsey|Turán)", r"saturation (?:numbers?|problems?)", r"forbidden (?:subgraphs?|configurations?|induced)", r"Sidorenko", r"flag algebras?", r"entropy (?:method|in combinatorics)", r"probabilistic (?:and|&) extremal", r"thresholds? (?:for|in) (?:random|graph)", r"phase transitions? (?:in|of) random graphs?", r"giant components?", r"Erd(?:ő|o)s-R(?:é|e)nyi", r"random (?:geometric|regular|hyper)graphs?", r"combinatorial (?:probability|Nullstellensatz)", r"Kahn-Kalai", r"sunflower (?:lemma|conjecture|theorem)", r"cap sets?", r"Kakeya (?:sets? )?(?:over|in) finite", r"coloring problems?"]),
    "math.comb.graph": ("math.comb", "Graph theory", [
        r"graph theory", r"spectral graph theory", r"graph (?:coloring|colouring|minors?|embeddings?|invariants?|algorithms?|decompositions?|labell?ings?|isomorphism|reconstruction|homomorphisms?|polynomials?|searching|drawing|connectivity|structure|products?|operations?|partitioning|packing|covering|spectra)", r"chromatic number", r"planar graphs?", r"hamilton(?:ian)? (?:cycles?|paths?|graphs?)", r"(?:perfect|maximum|maximal|stable|bipartite|graph) matchings?", r"matchings", r"matching theory", r"network flows?", r"treewidth", r"expanders?", r"cayley graphs?", r"laplacian eigenvalues? of graphs?", r"perfect graphs?", r"chordal", r"directed graphs?", r"digraphs?",
        r"regular graphs?", r"graphs? on surfaces?", r"cycle (?:covers?|double covers?)", r"eulerian", r"flows? in graphs", r"tree (?:decompositions?|width)", r"cliques?", r"independent sets?", r"graph (?:and|&) (?:hypergraph|network)", r"discrete (?:mathematics|structures)", r"graphs? (?:and|&) (?:matroids?|combinatorics|geometry)", r"signed graphs?", r"graph (?:theory|algorithms) (?:and|&) (?:applications|combinatorial)", r"extremal graph", r"intersection graphs?", r"interval graphs?", r"line graphs?", r"cubic graphs?", r"snarks?", r"Cheeger", r"graph (?:spectra|eigenvalues?)", r"adjacency (?:matri\w+|spectrum)", r"vertex (?:cover|coloring|connectivity|transitive)", r"edge (?:coloring|colouring|connectivity|disjoint)", r"circulant", r"strongly regular", r"distance[- ]regular", r"graph (?:energy|Laplacians?)", r"resistance (?:distance|networks?)", r"zero forcing", r"graph (?:rigidity|burning|pebbling)", r"pursuit[- ]evasion", r"cops and robbers", r"Ramanujan graphs?"]),

    # ── Logic, foundations & category theory ───────────────────────────────────
    "math.logic.logic": ("math.logic", "Mathematical logic (general)", [
        r"(?:mathematical|symbolic|modal|classical|intuitionistic|linear|first-order|higher-order|temporal|categorical|computability|substructural|dynamic|epistemic|non-?classical|many-valued|fuzzy|paraconsistent|relevance|deontic) logic",
        r"logic colloquium", r"g(?:ö|o)del", r"foundations of mathematics",
        r"formal (?:languages?|verification|systems?)", r"philosophy of mathematics", r"CS:LICS",
        r"logic (?:and|&) (?:computation|computer science|applications|foundations|games?|algebra|topology)",
        r"Ramsey (?:theory|numbers?) (?:in|and) logic"]),
    "math.logic.model": ("math.logic", "Model theory", [
        r"model theory", r"o-?minimal\w*", r"stability theory", r"hrushovski", r"definable sets?",
        r"finite model theory", r"nonstandard analysis", r"Löwenheim", r"Skolem", r"infinitary", r"ultrapowers?",
        r"Scott analysis", r"model[- ]theoretic", r"neostability", r"NIP (?:theories|structures|groups|fields)",
        r"continuous logic", r"abstract elementary classes", r"pseudo-?finite (?:fields?|structures?|groups?)",
        r"tame (?:geometry|topology)", r"Zilber", r"ultraproducts?"]),
    "math.logic.sets": ("math.logic", "Set theory", [
        r"set theory", r"large cardinals?", r"descriptive set theory", r"axiomatic set theory",
        r"continuum hypothesis", r"determinacy", r"inner models?", r"cardinal (?:arithmetic|characteristics)",
        r"Borel (?:equivalence|complexity|combinatorics)", r"cardinal invariants", r"PCF theory", r"Martin'?s axiom",
        r"proper forcing", r"Suslin", r"projective determinacy", r"Woodin", r"consistency strength",
        r"axiom of choice", r"ZFC", r"forcing axioms?", r"iterated forcing", r"(?:set-theoretic|Cohen) forcing",
        r"forcing (?:and|&|in) (?:set theory|large cardinals?)",
        r"(?:inaccessible|measurable|supercompact|strongly compact|Woodin) cardinals?",
        r"Borel (?:reducibility|sets)", r"infinite combinatorics",
        r"set-theoretic (?:methods|combinatorics|aspects)"]),
    "math.logic.computability": ("math.logic", "Computability & proof theory", [
        r"proof theory", r"computability(?: theory)?", r"recursion theory", r"reverse mathematics",
        r"ordinal analysis", r"decidab\w+", r"satisfiability", r"recursive functions?", r"turing degrees",
        r"computable (?:analysis|structures?|model theory)", r"algorithmic randomness", r"kolmogorov complexity",
        r"Hilbert'?s (?:programme|program)", r"proof complexity", r"bounded arithmetic",
        r"(?:Peano|Heyting|weak|second-order) arithmetics?", r"realizability", r"Weihrauch",
        r"computable (?:functions?|reducibility|mathematics)", r"degrees of unsolvability", r"halting problem",
        r"incompleteness theorems?", r"provability logic", r"computable structure theory"]),
    "math.logic.formal": ("math.logic", "Type theory, proof assistants & formalised mathematics", [
        r"constructive (?:mathematics|type theory|analysis)", r"type theory", r"homotopy type theory", r"univalent (?:foundations|type theory|mathematics|universes?)", r"univalence",
        r"lambda calculus", r"curry-howard", r"proof assistants?", r"CS:Lean", r"CS:Coq", r"CS:Isabelle",
        r"interactive theorem proving", r"formali[sz]ation (?:of mathematics|in Lean)",
        r"proof (?:verification|assistants?) (?:for|in) mathematics", r"formali[sz]ed mathematics",
        r"autoformali[sz]ation", r"mathlib", r"CS:Agda", r"CS:Rocq", r"HOL Light", r"Metamath", r"dependent types?",
        r"cubical type theory", r"CS:TYPES", r"CS:ITP", r"CS:CICM",
        r"Lean (?:4|prover|theorem prover|community|together)", r"theorem provers?",
        r"(?:automated|interactive|machine-assisted) theorem proving", r"formal (?:proofs?|mathematics)"]),
    "math.logic.category": ("math.logic", "Category theory & higher categories", [
        r"category theory", r"higher categor\w+", r"∞-categor\w+", r"infinity[- ]categor\w+", r"topos\w*", r"toposes", r"sheaf theory", r"monoidal categor\w+", r"operads?", r"2-categor\w+", r"bicategor\w+", r"enriched categor\w+", r"adjoint functors?", r"monads?", r"kan extensions?", r"derived (?:algebraic geometry|categor\w+)", r"triangulated categor\w+", r"string diagrams?", r"applied category theory", r"CS:ACT\s+20\d\d", r"categorif\w+", r"categorical (?:algebra|semantics|logic|quantum mechanics|structures?|methods|approach|foundations?|homotopy|aspects)", r"model categor\w+", r"homotopy theory of categories", r"dg[- ]categor\w+", r"tensor categor\w+", r"fusion categor\w+", r"higher algebra", r"factorization algebras?", r"spectral algebraic geometry", r"synthetic (?:geometry|mathematics|differential)", r"condensed mathematics", r"pro-?(?:é|e)tale", r"grothendieck (?:topolog\w+|construction|universes?|fibrations?)", r"yoneda", r"CS:SYCO", r"CS:CALCO", r"CS:MFPS", r"limits? and colimits?", r"universal properties?", r"representable functors?", r"locally presentable", r"accessible categor\w+", r"abelian categor\w+", r"Grothendieck categor\w+", r"stable ∞", r"cartesian closed", r"lawvere", r"fibrations?(?: (?:of|and) categor\w+)", r"internal (?:categor\w+|logic)", r"double categor\w+", r"(?:co)?algebras? for (?:a )?(?:co)?monads?", r"Hopf (?:monads?|categor\w+)", r"cobordism hypothesis", r"categorical (?:and|&) (?:topological|geometric)", r"multicategor\w+"]),

    # ── Numerical analysis ────────────────────────────────────────────────────
    "math.numeric.analysis": ("math.numeric", "Numerical analysis & scientific computing (general)", [
        r"numerical (?:analysis|mathematics|schemes?|approximation|integration|methods for (?:ODEs?|SDEs?|differential))",
        r"error estimates?", r"structure[- ]preserving", r"geometric (?:numerical )?integration",
        r"symplectic integrators?", r"time[- ]stepping", r"stiff (?:problems?|ODEs?|systems?)", r"runge-kutta",
        r"quadrature", r"computational (?:mathematics|science|PDEs?|methods|engineering|physics (?:and|&) numerical)",
        r"scientific computing", r"automatic differentiation", r"verified (?:computing|numerics?|computations?)",
        r"interval arithmetic", r"CS:ICIAM", r"CS:ENUMATH", r"CS:FoCM", r"scientific machine learning",
        r"physics[- ]informed", r"neural (?:PDE|operators?|solvers?|networks? for PDE)",
        r"numerical (?:methods|analysis) for (?:SDE|ODE|fractional|stochastic|integral|inverse|optimal)"]),
    "math.numeric.pde": ("math.numeric", "Numerical PDE & finite elements", [
        r"finite (?:element|difference|volume) (?:methods?|approximations?|analysis|schemes?|discretizations?)",
        r"CS:FEM", r"discontinuous galerkin", r"spectral methods?", r"multigrid", r"domain decomposition",
        r"mesh (?:generation|adaptation|refinement)", r"adaptive (?:finite element|mesh)", r"a posteriori",
        r"boundary element", r"meshfree", r"isogeometric", r"level set methods?", r"CS:ICOSAHOM", r"CS:WCCM",
        r"CS:ECCOMAS", r"conservation laws? (?:numerics|schemes?|solvers?)", r"Riemann solvers?", r"WENO",
        r"approximation (?:of|and) (?:PDE|solutions?)", r"mixed finite element", r"virtual element",
        r"hybrid high-order", r"polytopal", r"numerical methods for (?:PDEs?|partial)",
        r"numerical (?:methods|analysis) for PDE",
        r"(?:continuous|Petrov-|hybridi[sz]able |space-time )?Galerkin (?:methods?|schemes?|discreti[sz]ations?|approximations?)",
        r"hp-(?:FEM|finite elements?|adaptivity)", r"finite elements?", r"finite element exterior calculus",
        r"FEniCS", r"Firedrake", r"FreeFEM", r"Nitsche'?s? method", r"cut finite elements?", r"CutFEM",
        r"fictitious domain", r"asymptotic[- ]preserving", r"well-balanced (?:schemes?|methods?)",
        r"numerical (?:PDEs?|solution of (?:PDEs?|partial))", r"discreti[sz]ation of (?:PDEs?|partial)",
        r"high-order (?:methods|schemes|discreti[sz]ations?)"]),
    "math.numeric.linalg": ("math.numeric", "Numerical linear algebra & high-performance computing", [
        r"iterative (?:methods?|solvers?)", r"krylov (?:subspaces?|methods?|solvers?)", r"preconditioners?",
        r"tensor (?:decompositions|train)", r"low[- ]rank (?:approximation|methods?|matrices|tensor)",
        r"randomi[sz]ed (?:numerical linear algebra|algorithms? for|methods?)",
        r"matrix (?:computations?|functions?)", r"eigenvalue (?:problems?|algorithms?|computations?|solvers?)",
        r"high[- ]performance (?:numerical|scientific)", r"floating[- ]point", r"rounding errors?",
        r"fast (?:multipole|Fourier|solvers?)", r"numerical (?:multi)?linear algebra",
        r"sparse (?:linear|matrix|solvers?)", r"(?:applied|computational) linear algebra", r"Lanczos", r"Arnoldi",
        r"GMRES", r"conjugate gradients?", r"mixed[- ]precision (?:algorithms?|arithmetic|computing|linear algebra)",
        r"communication[- ]avoiding", r"PETSc|ScaLAPACK|LAPACK|Trilinos|hypre",
        r"exascale (?:algorithms?|numerics|solvers?)",
        r"parallel (?:numerical|linear algebra|solvers?|preconditioners?|in time)", r"hierarchical matri(?:x|ces)",
        r"structured matri(?:x|ces)", r"matrix (?:equations?|nearness)", r"singular value decompositions?",
        r"Householder Symposium"]),
    "math.numeric.uq": ("math.numeric", "Uncertainty quantification & data assimilation", [
        r"uncertainty quantification", r"reduced[- ](?:order|basis)", r"model (?:reduction|order reduction)",
        r"Monte Carlo (?:and|&) (?:quasi-Monte Carlo|numerical)", r"quasi-Monte Carlo", r"sparse grids?",
        r"high-dimensional (?:integration|approximation|PDE)", r"data assimilation", r"polynomial chaos",
        r"stochastic (?:Galerkin|collocation)", r"multi-?level Monte Carlo", r"Bayesian inverse problems?",
        r"ensemble Kalman", r"(?:3D|4D)-?Var", r"variational data assimilation",
        r"Gaussian process (?:emulat\w+|surrogates?)", r"rare[- ]event (?:simulation|estimation|sampling)",
        r"global sensitivity analysis", r"Sobol (?:indices|sequences?)"]),
    "math.numeric.symbolic": ("math.numeric", "Computer algebra & experimental mathematics", [
        r"computer algebra", r"symbolic (?:computation|computing|methods|integration|summation)", r"CS:ISSAC",
        r"SageMath",
        r"computational (?:algebra|algebraic geometry|number theory|group theory|commutative algebra|topology|geometry|combinatorics)",
        r"experimental mathematics", r"computer[- ]assisted (?:proofs?|mathematics)",
        r"computer[- ]aided (?:proofs?|mathematics)", r"algorithmic (?:algebra|number theory|algebraic geometry)",
        r"polynomial (?:system|solving|algorithms?)",
        r"gr(?:ö|o)bner (?:bases?|methods?) (?:and|in) (?:computation|algorithms?)",
        r"cylindrical algebraic decomposition", r"real algebraic geometry (?:algorithms?|computation)",
        r"computational (?:and|&) (?:experimental|computer)", r"mathematical software",
        r"mathematics and (?:AI|machine learning|computers?)", r"AI (?:for|in) mathematics",
        r"machine learning (?:for|in) (?:pure )?mathematics", r"data[- ]driven (?:mathematics|discovery)",
        r"conjecture (?:generation|discovery)"]),

    # ── Optimisation, control & games ─────────────────────────────────────────
    "math.optim.optimisation": ("math.optim", "Optimisation (general)", [
        r"optimi[sz]ation (?:theory|methods?|algorithms?|problems?|techniques|models?|approaches|applications?)",
        r"optimi[sz]ation,? (?:and|&) (?:image processing|control|inverse problems|games?|statistics|numerical analysis|variational)",
        r"linear programming", r"CS:ISMP", r"mathematical programming", r"decision (?:analysis|theory)",
        r"multi-?objective", r"online (?:learning|optimi[sz]ation|convex)",
        r"optimi[sz]ation (?:and|&) (?:control|machine learning|data science|applications)"]),
    "math.optim.convex": ("math.optim", "Continuous & convex optimisation", [
        r"convex (?:optimi[sz]ation|analysis|programming|and (?:nonconvex|nonsmooth)|relaxations?)",
        r"nonlinear (?:programming|optimi[sz]ation)", r"semidefinite (?:programming|optimi[sz]ation|relaxations?)",
        r"CS:SDP", r"stochastic (?:optimi[sz]ation|programming|approximation|gradient)", r"robust optimi[sz]ation",
        r"interior[- ]point", r"first[- ]order methods?", r"variational analysis", r"non-?smooth", r"bilevel",
        r"complementarity", r"derivative[- ]free", r"global optimi[sz]ation",
        r"conic (?:optimi[sz]ation|programming)", r"sum[- ]of[- ]squares",
        r"moment (?:and|&) polynomial optimi[sz]ation", r"polynomial optimi[sz]ation", r"nonconvex", r"proximal",
        r"ADMM", r"Frank-Wolfe", r"accelerated (?:methods?|gradient)", r"minimax (?:optimi[sz]ation|problems?)",
        r"saddle[- ]point (?:problems?|optimi[sz]ation)", r"variational inequalit\w+", r"equilibrium problems?",
        r"(?:continuous|smooth|large-scale) optimi[sz]ation", r"(?:Newton|quasi-Newton|trust[- ]region) methods?",
        r"augmented Lagrangian", r"optimi[sz]ation on manifolds", r"Riemannian optimi[sz]ation",
        r"monotone operators?", r"operator splitting", r"(?:Bregman|mirror) descent", r"Kurdyka-(?:Ł|L)ojasiewicz"]),
    "math.optim.discrete": ("math.optim", "Discrete optimisation & operations research", [
        r"integer (?:programming|linear programming|optimi[sz]ation)", r"combinatorial optimi[sz]ation", r"CS:IPCO",
        r"operations research", r"submodular", r"network (?:flows?|optimi[sz]ation|design)", r"scheduling",
        r"logistics", r"supply chains?", r"queueing", r"metaheuristics?",
        r"evolutionary (?:algorithms?|computation|optimi[sz]ation)", r"polyhedral combinatorics",
        r"matroid (?:optimi[sz]ation|theory and optimi[sz]ation)", r"approximation algorithms?",
        r"travelling salesman", r"traveling salesman", r"discrete optimi[sz]ation", r"combinatorial algorithms?",
        r"randomi[sz]ed (?:algorithms?|rounding)", r"graph algorithms?", r"online algorithms?", r"flow algorithms?",
        r"vehicle routing", r"facility location", r"knapsack", r"bin packing", r"cutting stock", r"timetabling",
        r"matching algorithms?", r"operational research", r"mixed[- ]integer",
        r"branch[- ]and[- ](?:bound|cut|price)", r"cutting planes?", r"column generation",
        r"(?:inventory|lot[- ]sizing|routing) problems?", r"CS:IFORS", r"CS:INFORMS", r"management science",
        r"revenue management", r"assignment problems?"]),
    "math.optim.control": ("math.optim", "Control theory & systems", [
        r"control theory", r"optimal control", r"stochastic control", r"control systems?", r"mathematical systems theory", r"systems (?:and|&) control", r"controllability", r"observability", r"kalman", r"model predictive", r"hamilton-jacobi-bellman", r"robust control", r"nonlinear control", r"networked control", r"H-?infinity", r"dynamic programming", r"riccati", r"differential games?", r"distributed (?:control|optimization|estimation)", r"hybrid systems?", r"CS:MTNS", r"CS:IFAC", r"CS:NOLCOS", r"port-?Hamiltonian", r"passivity", r"Lyapunov (?:stability|methods?|functions?)", r"adaptive control", r"sliding mode", r"reinforcement learning (?:and|&) control", r"data-driven control", r"control (?:barrier|Lyapunov)", r"PDE control", r"boundary control", r"infinite[- ]dimensional (?:systems?|control)", r"distributed parameter systems?", r"system identification", r"quantum control", r"geometric control", r"sub-?Riemannian (?:control|geometry and control)", r"Pontryagin"]),
    "math.optim.game": ("math.optim", "Game theory & mathematical economics", [
        r"game theory", r"mathematical economics", r"mechanism design", r"auctions?", r"nash", r"cooperative games?",
        r"evolutionary (?:game|dynamics) (?:theory|and)", r"stochastic games?", r"social choice", r"voting",
        r"matching (?:markets?|theory)", r"market (?:design|equilibrium)", r"general equilibrium",
        r"algorithmic game theory", r"differential games?", r"mean[- ]field games?", r"bargaining", r"fair division",
        r"econometrics", r"optimal stopping", r"contract theory", r"information (?:design|economics)",
        r"social (?:networks? (?:and|&) (?:games|economics))", r"Shapley", r"core (?:and|&) (?:nucleolus|stability)",
        r"repeated games?", r"signaling games?", r"potential games?", r"congestion games?", r"price of anarchy",
        r"learning in games", r"fictitious play", r"replicator dynamics",
        r"games? (?:and|&) (?:economic|decisions?|behaviou?r)", r"rational (?:choice|agents?)",
        r"utility (?:theory|maximi[sz]ation)"]),
    "math.optim.finance": ("math.optim", "Mathematical finance & insurance", [
        r"mathematical finance", r"financial mathematics", r"stochastic finance", r"option pricing",
        r"derivatives pricing", r"risk (?:measures?|theory)", r"portfolio (?:theory|optimi[sz]ation|selection)",
        r"actuarial", r"insurance mathematics", r"quantitative finance", r"stochastic calculus (?:and|in) finance",
        r"volatility", r"arbitrage", r"credit risk", r"(?:quantitative|mathematical) risk management",
        r"XVA", r"market microstructure", r"(?:insurance|actuarial) (?:science|risk|and finance)", r"ruin theory",
        r"longevity risk", r"Bachelier (?:Finance Society|World Congress|Congress)", r"financial (?:engineering|econometrics|derivatives)",
        r"(?:term structure|interest rate) models?", r"Black-Scholes", r"(?:stochastic|optimal) portfolio"]),

    # ── Applied & interdisciplinary mathematics ───────────────────────────────
    "math.applied.biology": ("math.applied", "Mathematical biology & medicine", [
        r"mathematical (?:biology|medicine|ecology|neuroscience|epidemiology|immunology|physiology|oncology|modell?ing in (?:biology|medicine|neuroscience|ecology|epidemiology))", r"epidemic (?:modell?ing|models?|dynamics|theory|spread)", r"population (?:dynamics|models?|genetics|biology)", r"biological (?:modell?ing|systems|networks|pattern|models?|dynamics|processes)", r"systems biology", r"computational (?:biology|neuroscience|systems biology|medicine)", r"reaction[- ]diffusion", r"pattern formation", r"morphogenesis", r"cancer (?:modell?ing|dynamics|growth|models?)", r"infectious (?:disease|diseases) (?:dynamics|modell?ing|models?)",
        r"phylogenet\w+", r"bio-?mathematics", r"neural (?:fields?|dynamics|systems|models?|mass)", r"cell (?:dynamics|signalling|biology (?:and|&) mathematics)", r"CS:SMB", r"CS:ESMTB", r"CS:ECMTB", r"mathematical (?:and|&) (?:computational|theoretical) (?:biology|neuroscience)", r"theoretical (?:biology|ecology|neuroscience|immunology|epidemiology)", r"ecological (?:models?|modell?ing|dynamics)", r"evolutionary (?:dynamics|game theory)", r"gene regulatory networks?", r"chemical reaction (?:networks?|systems?|kinetics?)", r"biochemical (?:networks?|systems?|reaction|kinetics)", r"stochastic (?:gene|biochemical|chemical|population|epidemic)", r"spatial (?:epidemiology|ecology|models? in (?:biology|ecology))", r"within[- ]host", r"disease (?:dynamics|modell?ing)", r"COVID-19 (?:modell?ing|dynamics)", r"physiolog\w+ (?:modell?ing|models?)", r"cardiac modell?ing", r"tumou?r (?:growth|modell?ing|models?|dynamics)", r"pharmacokinetics", r"pharmacodynamics", r"drug (?:discovery|delivery) (?:modell?ing|models?)", r"neurodynamics", r"computational (?:and|&) mathematical (?:biology|neuroscience)", r"CS:ICSB"]),
    "math.applied.mechanics": ("math.applied", "Mathematical mechanics & continuum mechanics", [
        r"continuum mechanics", r"solid mechanics", r"mathematical fluid", r"mathematical (?:modell?ing|theory) of (?:fluids?|elasticity|continua|materials|mechanics)", r"homogeni[sz]ation", r"mechanics of (?:materials|solids|continua|structures?|fluids?)", r"analytical mechanics", r"classical mechanics", r"celestial mechanics", r"lagrangian mechanics", r"variational mechanics", r"geometric mechanics", r"nonlinear elasticity", r"multi-?phase flow", r"mathematical models? (?:of|in) (?:fluid|elastic|material|continuum)", r"euler equations?", r"thermodynamics of continua", r"mixture theory", r"CS:ICIAM", r"CS:ESMC", r"CS:EUROMECH", r"CS:ICTAM", r"CS:WCCM", r"CS:IUTAM", r"CS:ESMC", r"mathematical (?:aspects|problems?|theory) of (?:continuum|elasticity|plates?|shells?|fluid|mechanics)", r"asymptotic (?:analysis|methods?) (?:in|for|of) (?:mechanics|elasticity|thin|shells?|fluid)", r"dimension reduction (?:in|for) (?:elasticity|mechanics|thin)", r"gamma-convergence (?:in|for) (?:mechanics|elasticity|thin|material)", r"micromagnetics", r"liquid crystals? (?:and|&) (?:analysis|PDEs?|mathematical|variational)", r"Landau-de Gennes", r"Ericksen-Leslie", r"geophysical (?:fluid|flows?) (?:and|&) mathematical", r"mathematical (?:analysis|aspects) of (?:Navier|Euler|incompressible|compressible)", r"mathematical (?:problems?|theory) (?:in|of) (?:fluid|geophysical)", r"hydrodynamic (?:stability|instabilit\w+) (?:mathematical|rigorous)", r"inviscid limit", r"vanishing viscosity", r"boundary layers? (?:theory|analysis|and)", r"Prandtl", r"turbulence (?:theory|mathematical)", r"mathematical (?:theory|analysis) of turbulence", r"Onsager conjecture", r"convex integration", r"wild solutions?", r"non-?uniqueness"]),
    "math.applied.imaging": ("math.applied", "Mathematical imaging & signal processing", [
        r"mathematical (?:image|signal) (?:processing|analysis)", r"compressed sensing", r"graph signal processing",
        r"(?:mathematical|variational|PDE[- ]based) (?:methods (?:in|for) )?image (?:processing|analysis)",
        r"image processing (?:and|&) (?:inverse problems|calculus of variations|PDEs?|optimi[sz]ation)",
        r"(?:calculus of variations|optimi[sz]ation|inverse problems),? (?:and|&) image processing",
        r"mathematical imaging", r"imaging (?:science|sciences|mathematics)",
        r"mathematics (?:of|in|for) (?:imaging|signal processing)", r"compressive sensing", r"phase retrieval",
        r"total variation (?:denoising|regulari[sz]ation|minimi[sz]ation)", r"mathematical signal processing",
        r"sampling theory", r"frame theory", r"CS:SSVM", r"shape (?:analysis|spaces)", r"mathematics of (?:\w+ )?imaging"]),
    "math.applied.info": ("math.applied", "Information theory", [
        r"(?<!quantum )information theory", r"source coding", r"shannon (?:theory|entropy|capacity)", r"CS:ISIT",
        r"entropy (?:and|&) (?:information|compression)", r"data compression", r"rate[- ]distortion",
        r"estimation (?:and|&) information", r"information[- ]theoretic", r"channel capacity", r"CS:ITW",
        r"(?:broadcast|wiretap|multiple[- ]access|interference) channels?", r"lossless compression",
        r"universal (?:coding|compression)", r"(?:age|value) of information"]),
    "math.applied.modelling": ("math.applied", "Applied mathematics & mathematical modelling", [
        r"mathematical (?:modell?ing|methods|sciences|models?)",
        r"applied (?:mathematics|analysis|probability|topology|algebra|category|geometry|harmonic|and computational)",
        r"industrial mathematics", r"mathematics (?:for|in) industry", r"study group",
        r"differential equations (?:and|in) applications", r"applications of mathematics",
        r"mathematics of (?:data|information|imaging|machine learning|networks|planet earth|climate|finance|deep learning|AI|signal)",
        r"inverse problems", r"uncertainty quantification", r"geometry of data", r"topological data analysis",
        r"mathematics of deep learning", r"mathematical aspects of (?:deep|machine) learning", r"CS:ICIAM",
        r"CS:ECMI",
        r"applied (?:and|&) (?:computational|industrial|interdisciplinary|engineering) (?:mathematics|sciences?)",
        r"engineering mathematics",
        r"mathematical (?:analysis|problems?) (?:in|of) (?:engineering|applications|science)",
        r"interdisciplinary (?:mathematics|applications)",
        r"mathematics (?:and|&) (?:its applications|applications|engineering|technology|society|industry)",
        r"nonlinear (?:analysis|science|phenomena) (?:and|&) applications",
        r"mathematical (?:and|&) (?:computational|statistical|numerical) (?:modelling|methods|sciences|aspects)",
        r"networks? (?:and|&) (?:applied|complex) mathematics", r"graph learning",
        r"mathematics (?:of|for) (?:AI|data)", r"mathematical foundations of (?:data|machine|AI|deep)"]),

    # ── Mathematics education & history ───────────────────────────────────────
    "math.edu.education": ("math.edu", "Mathematics education & outreach", [
        r"mathematics (?:education|teaching|learning|pedagogy|curriculum|olympiads?|competitions?|outreach|popularisation|popularization|communication|textbooks?|teachers?|classroom|students?|instruction|assessment|research)",
        r"teaching (?:mathematics|of mathematics|calculus|statistics|linear algebra|proof|probability)",
        r"math(?:s)? (?:circles?|olympiad|camps?|festival|day|competitions?|education|clubs?|fairs?|exhibitions?|teachers?|outreach)",
        r"mathematical (?:olympiad|circles?|education|literacy|community|culture|thinking|competitions?|talent|festivals?)",
        r"school (?:mathematics|math)", r"undergraduate (?:mathematics|research in mathematics)",
        r"teachers? (?:of|in) mathematics", r"CS:ICME", r"CS:IMO", r"CS:CERME", r"CS:ICMI",
        r"mathematics (?:and|&) (?:art|music|culture|society|literature|design|architecture|games?)",
        r"recreational mathematics", r"women in mathematics", r"gender (?:and|in) mathematics",
        r"diversity (?:in|and) mathematics", r"mathematics (?:and|&) (?:gender|equity|inclusion)", r"CS:EWM",
        r"CS:AWM", r"mathematical (?:modell?ing|problem solving) (?:education|competitions?|in the classroom)",
        r"learning (?:mathematics|mathematical|calculus|algebra|geometry)",
        r"mathematics (?:and|&) (?:technology|computing) (?:in|for) education", r"CS:ATCM",
        r"mathematics (?:anxiety|attitudes|motivation|beliefs)",
        r"mathematical (?:practices|reasoning|proof) (?:education|in school)",
        r"proof (?:and|&) (?:proving|reasoning) (?:in|and) (?:education|school)", r"CS:ICTMT"]),
    "math.edu.history": ("math.edu", "History & philosophy of mathematics", [
        r"history of mathematics", r"philosophy of mathematics", r"CS:HPM", r"mathematics history",
        r"mathematics (?:and|&) philosophy", r"history (?:and|&) philosophy of (?:mathematics|logic)",
        r"historians? of mathematics",
        r"history of (?:algebra|geometry|calculus|statistics|probability|logic|number theory|analysis|topology|mathematical \w+)",
        r"(?:ancient|medieval|Babylonian|Egyptian|Greek|Islamic|Mayan|Vedic) mathematics", r"Kerala school",
        r"mathematical heritage", r"epistemology of mathematics", r"CS:BSHM",
        r"philosophy of (?:logic|mathematical practice)"]),
}

# A topic marked "(general)" gives way to a narrower topic of the same area: "Elliptic PDE" is
# filed under Elliptic & parabolic PDE, not also under PDE (general). Same idea as a field's
# general bucket giving way to a specific sub-field (classify.GENERALS). Added 2026-11-10 (M3c).
NARROWER = {
    "math.logic.logic": ["math.logic.model", "math.logic.sets", "math.logic.computability", "math.logic.formal"],
    "math.analysis.pde": ["math.analysis.elliptic", "math.analysis.waves", "math.analysis.fluids"],
    "math.probability.theory": ["math.probability.stochastic", "math.probability.walks", "math.probability.geometry",
                                "math.probability.rmt"],
    "math.dyn.general": ["math.dyn.ergodic", "math.dyn.hyperbolic", "math.dyn.complex", "math.dyn.homogeneous"],
    "math.numeric.analysis": ["math.numeric.pde", "math.numeric.linalg", "math.numeric.uq"],
    "math.optim.optimisation": ["math.optim.convex", "math.optim.discrete"],
}
