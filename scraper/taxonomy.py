"""
Event Horizon 2.0 taxonomy: everything that decides *what an event is about*.

How much an event matters is NOT decided here: that is a property of a research
profile (scraper/profiles.yaml), so the same tagged events can be ranked
differently for different researchers.

Structure
---------
FIELDS      top-level fields, in display order
SUBFIELDS   sub-field id -> (parent field, label)
RULES       sub-field id -> list of regex patterns (word-boundary safe)
DECLARED    subject codes that *organisers* attach to events (arXiv-style
            researchseminars topics, INSPIRE categories, ai-deadlines tags)
            -> sub-fields. Declared codes are the most trustworthy evidence.
PROTOTYPES  one-paragraph descriptions of each sub-field, used by the
            embedding classifier (Option B) to catch events with no keywords.
"""

import re

# ---------------------------------------------------------------------------
# Fields and sub-fields
# ---------------------------------------------------------------------------
FIELDS = {
    "cosmo":   "Cosmology",
    "astro":   "Astrophysics",
    "ai":      "AI / ML",
    "cs":      "Computer science",
    "math":    "Mathematics",
    "physics": "Physics",
}

# id: (parent field, label). Display order follows this table.
SUBFIELDS = {
    "cosmo.de":      ("cosmo", "Dark energy & expansion"),
    "cosmo.lss":     ("cosmo", "Large-scale structure & surveys"),
    "cosmo.early":   ("cosmo", "CMB & early universe"),
    "cosmo.dm":      ("cosmo", "Dark matter"),
    "cosmo.general": ("cosmo", "General cosmology"),

    "ai.science":    ("ai", "ML for science"),
    "ai.theory":     ("ai", "ML theory & optimisation"),
    "ai.genai":      ("ai", "Generative models & LLMs"),
    "ai.nlp":        ("ai", "Language & speech"),
    "ai.vision":     ("ai", "Computer vision & multimodal"),
    "ai.rl":         ("ai", "Reinforcement learning & agents"),
    "ai.trust":      ("ai", "Safety, fairness & interpretability"),
    "ai.general":    ("ai", "General AI & ML"),

    "cs.theory":     ("cs", "Algorithms & theory of computation"),
    "cs.systems":    ("cs", "Systems, networks & HPC"),
    "cs.security":   ("cs", "Security & cryptography"),
    "cs.pl":         ("cs", "Programming languages & software"),
    "cs.data":       ("cs", "Databases, data mining & retrieval"),
    "cs.hci":        ("cs", "HCI, graphics & visualisation"),
    "cs.robotics":   ("cs", "Robotics"),
    "cs.general":    ("cs", "General computer science"),

    "astro.he":       ("astro", "High-energy, compact objects & GW"),
    "astro.galactic": ("astro", "Galaxies & AGN"),
    "astro.stellar":  ("astro", "Stars, Sun & planets"),
    "astro.general":  ("astro", "General astronomy & colloquia"),

    "math.nt":        ("math", "Number theory"),
    "math.topology":  ("math", "Topology"),
    "math.algebra":   ("math", "Algebra & representation theory"),
    "math.geometry":  ("math", "Geometry"),
    "math.probability": ("math", "Probability"),
    "math.mathphys":  ("math", "Mathematical physics"),
    "math.analysis":  ("math", "Analysis & PDE"),
    "math.other":     ("math", "General mathematics & colloquia"),

    "phys.gr":       ("physics", "Gravitation & GR"),
    "phys.hepth":    ("physics", "High-energy theory & QFT"),
    "phys.quantum":  ("physics", "Quantum physics"),
    "phys.condmat":  ("physics", "Condensed matter & stat mech"),
    "phys.fluids":   ("physics", "Fluids, plasma & climate"),
    "phys.general":  ("physics", "General physics & colloquia"),
}


# ---------------------------------------------------------------------------
# Keyword rules. All patterns are case-insensitive and word-bounded unless the
# pattern says otherwise. Patterns starting with "CS:" are case-sensitive
# (for acronyms like AI, SBI, DESI that collide with ordinary words).
# ---------------------------------------------------------------------------
W = r"\b"
RULES = {
    "cosmo.general": [
        r"cosmolog\w*", r"cosmic (?:web|expansion|history|structure)",
        r"big bang", r"lambda-?cdm", r"CS:ΛCDM", r"CS:LCDM", r"friedmann",
        r"CS:FLRW", r"standard model of cosmology", r"primordial universe",
    ],
    "cosmo.de": [
        r"dark energy", r"cosmic acceleration", r"accelerat\w* expansion",
        r"hubble (?:tension|constant|parameter)", r"CS:H_?0 tension",
        r"expansion history", r"quintessence", r"phantom (?:crossing|dark|divide|regime)",
        r"CS:w0-?wa", r"CS:w_0", r"dynamical dark", r"modified gravity",
        r"CS:f\(R\)", r"horndeski", r"type ia supernova\w*", r"supernova cosmology",
        r"cosmic chronometer\w*", r"distance ladder",
    ],
    "cosmo.early": [
        r"inflation(?:ary)?", r"cosmic microwave background", r"CS:CMB",
        r"primordial", r"early universe", r"reioni[sz]ation", r"21[- ]?cm",
        r"cosmic dawn", r"dark ages", r"baryogenesis", r"non-?gaussianit\w*",
        r"cosmological collider", r"big bang nucleosynthesis", r"CS:BBN",
        r"planck (?:data|satellite|mission|collaboration)", r"b-modes?",
        r"stochastic gravitational[- ]wave background",
    ],
    "cosmo.lss": [
        r"large[- ]scale structure", r"CS:LSS", r"baryon acoustic", r"CS:BAO",
        r"galaxy (?:clustering|survey\w*|bias)", r"redshift[- ]space", r"CS:RSD",
        r"weak (?:gravitational )?lensing", r"cosmic shear", r"CS:DESI",
        r"CS:Euclid", r"CS:LSST", r"rubin observatory", r"CS:S8", r"sigma_?8",
        r"matter power spectrum", r"halo model", r"n-body", r"cosmological simulation\w*",
        r"structure formation", r"intensity mapping", r"peculiar velocit\w*",
        r"field-level", r"CS:Roman Space Telescope",
    ],
    "cosmo.dm": [
        r"dark matter", r"CS:WIMPs?", r"axion\w*", r"sterile neutrino\w*",
        r"fuzzy dark", r"primordial black holes?", r"CS:PBHs?", r"dark sector",
    ],

    "ai.general": [
        r"machine learning", r"deep learning", r"neural networks?",
        r"artificial intelligence", r"CS:AI", r"representation learning",
        r"data science", r"graph neural", r"CS:GNNs?", r"CS:ML",
        r"neural information processing", r"learning representations",
        r"CS:NeurIPS", r"CS:ICML", r"CS:ICLR", r"CS:AAAI", r"CS:IJCAI",
        r"pattern recognition", r"neural computation", r"geometric deep learning",
        r"federated learning", r"continual learning", r"lifelong learning",
        r"self-supervised", r"knowledge representation", r"automated planning",
        r"evolutionary computation", r"genetic (?:algorithms?|programming)",
    ],
    "ai.genai": [
        r"CS:LLMs?", r"large language models?", r"language models?",
        r"transformers?(?! (?:substation|winding))", r"generative (?:models?|AI|modell?ing)",
        r"CS:GenAI", r"diffusion models?", r"score-based", r"foundation models?",
        r"agentic", r"(?:AI|LLM) agents?", r"prompt(?:ing| engineering)", r"in-context learning",
        r"variational auto-?encoders?", r"CS:VAEs?", r"CS:GANs?", r"generative adversarial",
        r"text-to-(?:image|video|speech)", r"CS:RAG", r"retrieval-augmented",
        r"CS:GPT", r"chatbots?", r"CS:COLM",
    ],
    "ai.nlp": [
        r"natural language(?: processing| understanding| generation)?", r"CS:NLP",
        r"computational linguistics", r"machine translation", r"speech (?:recognition|processing|synthesis)",
        r"spoken language", r"question answering", r"text (?:mining|classification|summari[sz]ation)",
        r"sentiment analysis", r"information extraction", r"CS:ACL", r"CS:EMNLP",
        r"CS:NAACL", r"CS:EACL", r"CS:COLING", r"CS:CoNLL", r"CS:LREC",
        r"interspeech", r"CS:ICASSP", r"multilingual", r"low-resource languages?",
    ],
    "ai.vision": [
        r"computer vision", r"image (?:recognition|segmentation|generation|analysis|processing|understanding)",
        r"object detection", r"visual (?:recognition|understanding|computing)",
        r"video (?:understanding|analysis|generation)", r"3-?d (?:vision|reconstruction)",
        r"multimodal", r"multi-modal", r"vision[- ]language", r"CS:CVPR", r"CS:ICCV",
        r"CS:ECCV", r"CS:WACV", r"CS:BMVC", r"CS:ICVGIP", r"CS:ACCV", r"CS:3DV",
        r"medical image\w*", r"biometrics?", r"face recognition", r"document analysis",
        r"neural radiance", r"CS:NeRFs?", r"gaussian splatting", r"remote sensing",
    ],
    "ai.rl": [
        r"reinforcement learning", r"CS:RL", r"sequential decision\w*", r"decision[- ]making under uncertainty",
        r"multi-?agent systems?", r"autonomous agents", r"Markov decision", r"CS:MDPs?",
        r"policy (?:gradient|optimi[sz]ation|learning)", r"imitation learning",
        r"offline RL", r"CS:AAMAS", r"CS:RLC", r"CS:ICAPS", r"game[- ]playing",
    ],
    "ai.trust": [
        r"(?:AI|ML) safety", r"safe (?:AI|machine learning|reinforcement learning)",
        r"(?:AI|value|model) alignment", r"interpretab\w*", r"explainab\w*", r"CS:XAI", r"fairness",
        r"responsible (?:AI|machine learning)", r"trustworthy (?:AI|machine learning|ML)",
        r"adversarial (?:examples?|attacks?|robustness)", r"CS:FAccT",
        r"privacy-preserving", r"differential(?:ly)? priva\w*", r"mechanistic interpretability", r"AI ethics",
        r"ethics (?:of|in) (?:AI|artificial intelligence)", r"AI governance", r"AI policy",
    ],
    "ai.theory": [
        r"learning theory", r"statistical learning", r"generali[sz]ation (?:bounds?|error|theory)",
        r"CS:PAC", r"kernel methods?", r"stochastic gradient", r"CS:SGD",
        r"neural tangent", r"(?:theory|mathematics) of (?:deep|machine) learning",
        r"deep learning theory", r"high-dimensional statistic\w*", r"sample complexity",
        r"online learning", r"bandits?", r"kolmogorov[- ]arnold", r"CS:KANs?",
        r"overparameteri[sz]\w*", r"implicit bias", r"compressed sensing",
        r"sparse recovery", r"bayesian (?:deep learning|neural)", r"optimal transport",
        r"mean[- ]field (?:limit|theory) of (?:neural|deep)",
        r"(?:non-?)?convex optimi[sz]ation", r"optimi[sz]ation (?:for|in) (?:machine|deep) learning",
        r"CS:COLT", r"CS:ALT", r"CS:AISTATS", r"CS:UAI", r"probabilistic (?:machine learning|AI|modell?ing)",
        r"gaussian processes?", r"neural scaling laws?", r"theory of (?:transformers|neural networks|generali[sz]ation)",
    ],
    "ai.science": [
        r"(?:machine learning|deep learning|neural networks?|CS_INLINE_AI|artificial intelligence) "
        r"(?:for|in|and|meets)(?: and (?:for|in))? (?:the )?(?:science|physics|astronomy|astrophysics|cosmology|"
        r"physical sciences|astro\w*|space|the universe|fundamental physics)",
        r"CS:ML4PS", r"CS:AI4Science", r"ai for science", r"scientific machine learning",
        r"CS:SciML", r"physics[- ]informed", r"CS:PINNs?", r"neural operators?",
        r"simulation[- ]based inference", r"CS:SBI", r"likelihood[- ]free",
        r"emulat(?:or|ors|ion)", r"surrogate models?", r"neural (?:posterior|density|likelihood) estimat\w*",
        r"normali[sz]ing flows?", r"differentiable (?:simulation|programming|physics)",
        r"symbolic regression", r"data-driven discovery", r"astroinformatics",
        r"astrostatistic\w*", r"cosmostatistic\w*",
    ],

    "cs.theory": [
        r"(?:design and analysis of|theory of|efficient|graph|approximation|online|streaming|parallel|combinatorial) algorithms?",
        r"algorithmic(?! trading)", r"(?:computational )?complexity theor\w*", r"computational complexity", r"complexity (?:and|&) algorithms?",
        r"theory of computation", r"theoretical computer science", r"CS:TCS",
        r"computability", r"randomi[sz]ed algorithms?",
        r"data structures?", r"computational geometry",
        r"quantum (?:algorithms?|complexity)", r"automata", r"formal languages",
        r"CS:STOC", r"CS:FOCS", r"CS:SODA", r"CS:ICALP", r"CS:FSTTCS", r"CS:SoCG", r"CS:CCC",
        r"CS:APPROX", r"CS:RANDOM", r"CS:ITCS", r"CS:STACS", r"CS:ESA", r"CS:MFCS",
        r"algorithmic game theory", r"mechanism design", r"(?:P|NP)-hard\w*", r"NP-complete\w*",
        r"pseudorandom\w*", r"property testing", r"sublinear", r"parameteri[sz]ed complexity",
        r"distributed computing", r"CS:PODC", r"CS:DISC",
    ],
    "cs.systems": [
        r"operating systems?", r"distributed systems?", r"computer systems?", r"cloud computing",
        r"computer architecture", r"high[- ]performance computing", r"CS:HPC", r"supercomput\w*",
        r"parallel (?:computing|programming|algorithms?)", r"CS:GPUs?", r"hardware accelerators?",
        r"computer networks?", r"wireless (?:networks?|communications?)",
        r"internet of things", r"CS:IoT", r"edge computing", r"embedded systems?",
        r"storage systems?", r"datacenters?", r"data cent(?:er|re)s?", r"(?:VLSI|chip|hardware) design",
        r"CS:VLSI", r"CS:FPGAs?", r"CS:MLSys", r"(?:ML|AI) systems", r"CS:OSDI", r"CS:SOSP",
        r"CS:NSDI", r"CS:SIGCOMM", r"CS:INFOCOM", r"CS:MobiCom", r"CS:ASPLOS", r"CS:ISCA",
        r"CS:MICRO", r"CS:HPCA", r"CS:EuroSys", r"CS:COMSNETS", r"CS:HiPC",
        r"cyber-?physical", r"real-time systems?", r"CS:5G", r"CS:6G",
    ],
    "cs.security": [
        r"cryptograph\w*", r"cryptolog\w*", r"(?:cyber|computer|network|information|systems?) security",
        r"cybersecurity", r"security and privacy", r"privacy", r"malware", r"blockchains?",
        r"zero-knowledge", r"homomorphic encryption", r"post-quantum", r"encryption",
        r"CS:CRYPTO", r"CS:EUROCRYPT", r"CS:ASIACRYPT", r"CS:INDOCRYPT", r"CS:CCS",
        r"CS:NDSS", r"CS:USENIX Security", r"CS:CHES", r"CS:TCC", r"CS:PETS",
        r"formal security", r"side[- ]channels?", r"secure (?:computation|systems?)",
    ],
    "cs.pl": [
        r"programming languages?", r"type (?:theory|systems?)", r"compilers?",
        r"program (?:analysis|synthesis|verification)", r"formal (?:methods|verification)",
        r"model checking", r"software engineering", r"software (?:testing|systems?|verification)",
        r"functional programming", r"concurrency theory", r"semantics of programming",
        r"CS:POPL", r"CS:PLDI", r"CS:ICFP", r"CS:OOPSLA", r"CS:CAV", r"CS:LICS",
        r"CS:ICSE", r"CS:FSE", r"CS:ESEC", r"CS:ISSTA", r"CS:ETAPS", r"CS:TACAS",
        r"proof assistants?", r"CS:Coq", r"CS:Rocq", r"CS:Isabelle", r"CS:Agda",
        r"logic in computer science", r"static analysis", r"code generation",
    ],
    "cs.data": [
        r"databases?", r"data management", r"data mining", r"knowledge discovery",
        r"information retrieval", r"recommender systems?", r"recommendation systems?",
        r"web search", r"search engines?", r"knowledge graphs?", r"big data",
        r"CS:SIGMOD", r"CS:VLDB", r"CS:ICDE", r"CS:PODS", r"CS:KDD", r"CS:SIGKDD",
        r"CS:SIGIR", r"CS:WSDM", r"CS:CIKM", r"CS:ICDM", r"CS:ECIR", r"CS:RecSys",
        r"CS:CODS", r"CS:COMAD", r"semantic web", r"data engineering", r"social networks? analysis",
        r"world wide web",
    ],
    "cs.hci": [
        r"human[- ]computer interaction", r"CS:HCI", r"user interfaces?", r"user experience",
        r"interaction design", r"ubiquitous computing", r"accessibility",
        r"computer graphics", r"CS:SIGGRAPH", r"visuali[sz]ation", r"virtual reality",
        r"augmented reality", r"mixed reality", r"CS:VR", r"CS:AR", r"CS:CHI", r"CS:UIST",
        r"CS:CSCW", r"CS:IUI", r"rendering", r"geometry processing", r"animation",
        r"computational design", r"CS:EuroVis", r"CS:Eurographics", r"video games?", r"game design",
    ],
    "cs.robotics": [
        r"robot\w*", r"autonomous (?:vehicles?|systems?|driving|navigation)", r"self-driving",
        r"drones?", r"CS:UAVs?", r"legged locomotion", r"motion planning",
        r"CS:SLAM", r"CS:ICRA", r"CS:IROS", r"CS:RSS", r"CS:CoRL", r"control systems?",
        r"embodied (?:AI|intelligence)", r"humanoids?",
    ],
    "cs.general": [
        r"computer science", r"computational thinking", r"CS:ACM",
        r"CS:IEEE Computer Society", r"informatics", r"research software", r"quantum computing",
        r"signal processing", r"information systems?", r"CS:CSE", r"CS:EECS",
        r"bioinformatics", r"computational biology",
    ],

    "astro.general": [
        r"astronom\w*", r"astrophysic\w*", r"astro-?chemistry", r"astro-?biology", r"telescopes?", r"observator(?:y|ies)",
        r"astroparticle", r"radio astronomy", r"CS:SKA", r"sky surveys?", r"CS:IAU",
        r"space mission\w*", r"astrometr\w*", r"spectroscop\w* survey",
    ],
    "astro.galactic": [
        r"galax(?:y|ies)", r"galactic", r"CS:AGNs?", r"active galactic", r"quasars?",
        r"interstellar medium", r"CS:ISM", r"circumgalactic", r"milky way",
        r"star formation", r"intracluster", r"galaxy clusters?", r"star clusters?",
    ],
    "astro.stellar": [
        r"stellar", r"exoplanet\w*", r"planetary (?:system|science|formation)\w*",
        r"protoplanetary", r"asteroseismolog\w*", r"solar (?:physics|flares?|wind|corona|dynamo|system)",
        r"heliophys\w*", r"white dwarfs?", r"binary stars?", r"supernova(?:e|s)?",
        r"nucleosynthesis", r"small bodies", r"comets?", r"asteroids?", r"space weather",
        r"massive stars?", r"stars and planets", r"CS:Aditya",
    ],
    "astro.he": [
        r"black holes?", r"neutron stars?", r"pulsars?", r"magnetars?",
        r"gamma[- ]rays?", r"x-ray (?:astronomy|binar\w*|sources?|observ\w*)",
        r"cosmic rays?", r"gravitational[- ]waves?", r"CS:LIGO", r"CS:LISA",
        r"fast radio bursts?", r"CS:FRBs?", r"astrophysical transients", r"time[- ]domain",
        r"tidal disruption", r"kilonova\w*", r"compact objects?", r"accretion",
        r"CS:GRBs?", r"multi-?messenger", r"relativistic jets?",
        r"(?:hybrid|compact|quark|strange|neutron) stars?", r"dense matter", r"relativistic astrophysics",
    ],

    "math.nt": [
        r"number theor\w*", r"arithmetic (?:geometry|statistics|topology|of)",
        r"modular forms?", r"automorphic", r"CS:L-functions?", r"l-functions?",
        r"zeta (?:functions?|values)", r"diophantine", r"galois representations?",
        r"elliptic curves?", r"p-adic", r"iwasawa", r"langlands", r"class field",
        r"eisenstein", r"abelian variet\w*", r"(?:cubic|quadratic|number) fields",
        r"analytic number", r"sieve methods?", r"mahler measure", r"modularity",
        r"primes?(?! minister)", r"hecke", r"shimura", r"ramanujan", r"stark units?",
        r"(?:cubic|quadratic|abelian|galois|cyclotomic) extensions?", r"additive bases",
        r"h-bases", r"arithmetic statistics", r"CS:CM-types?", r"complex multiplication",
    ],
    "math.topology": [
        r"topolog\w*(?! (?:insulator|phase|order|matter|superconduct|quantum|photonic|materials|states?|bands?|semimetal|defects?|solitons?|charges?|excitations?|edge|phenomena|magnon|qubits?|protection|crystalline)) ||| (?:quantum|topological|condensed|soft|active) matter|insulators?|semimetals?|superconduct\w*|quantum hall|berry|photonic\w*|materials?|band structures?|magnon\w*|qubits?|isolants?|matière",
        r"homotop\w*", r"homolog\w*", r"cohomolog\w*", r"knots?(?! per)", r"knot theory",
        r"manifolds?", r"CS:TQFTs?", r"cobordism", r"fundamental groups?",
        r"mapping class", r"[34]-manifolds?", r"sheaf|sheaves", r"persistent homology",
        r"loop spaces?",
    ],
    "math.algebra": [
        r"algebras?(?! for tensors)", r"algebraic(?! (?:geometry|topology|number))", r"group theor\w*",
        r"group (?:schemes?|actions?|representations?|cohomology)",
        r"(?:finite|lie|free|discrete|abelian|reductive|algebraic|quantum) groups?",
        r"representation theor\w*", r"commutative algebra", r"noncommutative",
        r"rings? and modules", r"lie (?:algebras?|groups?|theory)", r"category theor\w*",
        r"categorical", r"hopf", r"quivers?", r"homological algebra", r"galois theory",
        r"cluster algebras?", r"operads?", r"koszul", r"vertex operator", r"2-groups?",
    ],
    "math.geometry": [
        r"(?<!quantum )(?<!spacetime )(?<!band )geometr(?:y|ies|ic)(?! deep learning| phases?| optics| frustration) ||| berry|topological (?:phases?|matter|insulators?)", r"algebraic geometry", r"differential geometry",
        r"riemannian", r"symplectic", r"calabi[- ]yau", r"moduli(?! (?:stabili[sz]ation|fields?|problem|inflation|decay))", r"(?<!berry )(?<!spacetime )curvature(?! perturbations?| radiation| of spacetime) ||| berry|inflation\w*|cosmolog\w*|black holes?",
        r"minimal surfaces?", r"hodge", r"k(?:ä|a)hler", r"mirror symmetry", r"(?<!dirac )(?<!weyl )(?<!majorana )spinors?(?![- ]helicity)",
        r"(?<!magnetic )monopoles?(?! searches?| production| dark matter)", r"orbifolds?", r"varieties", r"surfaces of",
    ],
    "math.analysis": [
        r"(?:functional|harmonic|complex|real|fourier|microlocal|spectral|nonlinear|numerical) analysis",
        r"partial differential equations?", r"CS:PDEs?", r"differential equations?",
        r"operator (?:algebras?|theory)", r"heat kernels?", r"dirichlet forms?", r"sobolev",
        r"inequalit(?:y|ies)", r"dispersive", r"navier[- ]stokes", r"calculus of variations",
        r"approximation theory", r"integral (?:equations?|representations?)", r"analytification",
        r"amenab\w*", r"ergodic", r"schr(?:ö|o)dinger equations?", r"blow-?up",
    ],
    "math.probability": [
        r"probabilit\w*", r"stochastic\w*(?! (?:gravitational|GW|background|inflation))", r"random (?:matri\w*|walks?|graphs?|fields?|processes)",
        r"brownian", r"markov", r"martingales?",
        r"large deviations?", r"percolation", r"extreme values?",
        r"fokker[- ]planck", r"(?<!quantum )(?<!diffusion )(?<!variational )monte carlo(?! event generators?| generators?)",
        r"spin glass\w*",
    ],
    # Statistics is its own branch since 2026-11-10; these words were under "Probability & statistics"
    "math.stat": [
        r"(?<!quantum )(?<!anyonic )(?<!fractional )(?<!exchange )(?<!counting )(?<!photon )(?<!Bose-Einstein )(?<!Fermi-Dirac )statistic\w*(?! (?:mechanic|physic|field theor))",
        r"bayesian", r"statistical inference", r"causal inference", r"regression", r"uncertainty quantification",
    ],
    "math.mathphys": [
        r"mathematical physics", r"integrable (?:systems?|models?|hierarch\w*)",
        r"lax (?:pairs?|representation)", r"conformal field theor\w*", r"vertex algebras?",
        r"CS:TQFTs?", r"mathematical relativity", r"spectral theory",
        r"quantum field theor\w* (?:mathematic\w*|rigorous)",
    ],
    "math.other": [r"mathemat\w*"],
    # These words were under General mathematics before the branches below existed (moved 2026-11-10)
    "math.comb": [r"combinatori\w*", r"graph theor\w*", r"posets?"],
    "math.logic": [r"mathematical logic", r"model theory", r"set theory", r"g(?:ö|o)del", r"incompleteness",
                   r"proof theory", r"formal(?:i[sz]ed|i[sz]ation)? (?:proofs?|mathematics)", r"theorem prov\w*", r"CS:Lean"],
    "math.dyn": [r"dynamical systems?", r"(?<!quantum )(?<!polynomial )(?<!propagation of )chaos(?! (?:in|and) (?:black holes?|quantum|many-body))"],
    "math.optim": [r"game theory", r"optimal control", r"convex optimi[sz]ation"],
    "math.numeric": [r"numerical methods?"],
    "math.edu": [r"history of mathematics"],

    "phys.gr": [
        r"general relativity", r"gravitation\w*", r"gravity", r"spacetimes?", r"space-time",
        r"einstein", r"wormholes?", r"numerical relativity", r"quantum gravity",
        r"tidal deformation", r"geodesics?", r"black holes?", r"CS:gr-qc",
    ],
    "phys.hepth": [
        r"string theor\w*", r"string field", r"worldsheet", r"superstrings?",
        r"quantum field theor\w*", r"CS:QFTs?", r"gauge theor\w*", r"supersymmetr\w*",
        r"CS:SUSY", r"holograph\w*", r"CS:AdS", r"CS:CFTs?", r"conformal (?:field|bootstrap)",
        r"scattering amplitudes?", r"infrared divergences?", r"generali[sz]ed symmetr\w*",
        r"higher[- ]form symmetr\w*", r"higher symmetr\w*", r"particle physics",
        r"high[- ]energy physics", r"CS:HEP", r"phenomenolog\w*", r"colliders?",
        r"CS:LHC", r"neutrinos?", r"standard model", r"beyond the standard model",
        r"CS:BSM", r"effective field theor\w*", r"CS:EFTs?", r"CS:QCD", r"hadron\w*",
        r"swampland", r"anomal(?:y|ies) (?:inflow|matching)", r"nambu",
    ],
    "phys.quantum": [
        r"quantum (?:information|computing|computation|matter|many-body|chaos|optics|"
        r"mechanics|entanglement|technolog\w*|devices?|sensing|simulation|thermodynamics)",
        r"entanglement", r"qubits?", r"open quantum", r"decoherence", r"semiclassical",
        r"classical and quantum",
    ],
    "phys.condmat": [
        r"condensed matter", r"spin glass\w*", r"statistical (?:mechanics|physics)",
        r"phase transitions?", r"topological (?:insulators?|phases?|matter|order)",
        r"superconduct\w*", r"(?:frustrated|quantum|itinerant) magnetism", r"magnetic materials", r"spin (?:chains?|liquids?|systems?)",
        r"soft matter", r"active matter", r"living matter", r"polymers?",
        r"biological physics", r"biophysics", r"non-?equilibrium", r"many-body",
        r"glass(?:es|y)?(?! ceiling)", r"fluctuation theory", r"quantum matter",
    ],
    "phys.fluids": [
        r"turbulen\w*", r"fluids?", r"plasmas?", r"hydrodynamic\w*",
        r"magnetohydrodynamic\w*", r"CS:MHD", r"convection",
        r"(?<!normalizing )(?<!normalising )flows?(?! matching|-based| models?) ||| (?:ricci|curvature|gradient|geometric|unipotent|geodesic|horocycle|harmonic map|calabi|yamabe|willmore|teichm(?:ü|u)ller|wasserstein|homogeneous|translation|hamiltonian) flows?", r"climate (?:dynamics|physics|model\w*|chaos)", r"atmospher\w*",
        r"ocean\w*", r"stochasticity", r"diffusion(?! models?| and flow|-based)",
    ],
    "phys.general": [
        r"physics", r"optic(?:s|al)", r"photon\w*", r"lasers?",
        r"nuclear (?:physics|structure|theory|matter)", r"atomic", r"acoustic\w*",
        r"polari[sz]ation", r"caustics", r"water",
    ],
}

# ---------------------------------------------------------------------------
# Declared subject codes -> sub-fields (with evidence weight)
# Codes are normalised: lowercase, '.', '-', ' ' -> '_'.
# ---------------------------------------------------------------------------
STRONG, MEDIUM, WEAK = 1.5, 1.0, 0.6

_ARXIV_MATH = {
    "nt": "math.nt",
    "at": "math.topology", "gt": "math.topology", "gn": "math.topology",
    "kt": "math.topology",
    "ra": "math.algebra", "ac": "math.algebra.comm", "rt": "math.algebra.lie",
    "gr": "math.algebra.group", "qa": "math.algebra.hopf", "ct": "math.logic.category",
    "ag": "math.geometry", "dg": "math.geometry", "mg": "math.geometry",
    "sg": "math.geometry", "cv": "math.analysis",
    "ap": "math.analysis.pde", "ca": "math.analysis.ode", "fa": "math.analysis.functional",
    "oa": "math.analysis.opalg", "sp": "math.analysis.functional", "na": "math.numeric",
    "pr": "math.probability", "st": "math.stat",
    "mp": "math.mathphys",
    "ds": "math.dyn", "co": "math.comb", "lo": "math.logic", "oc": "math.optim",
    "it": "math.applied.info", "gm": "math.other", "ho": "math.edu",
}


# arXiv computer-science / EESS categories (researchseminars.org uses the same codes)
_ARXIV_CS = {
    "cs_lg": "ai.general", "cs_ai": "ai.general", "cs_ne": "ai.general",
    "cs_cv": "ai.vision", "eess_iv": "ai.vision",
    "cs_cl": "ai.nlp", "cs_sd": "ai.nlp", "eess_as": "ai.nlp",
    "cs_ma": "ai.rl",
    "cs_cc": "cs.theory", "cs_ds": "cs.theory", "cs_fl": "cs.theory", "cs_cg": "cs.theory",
    "cs_dm": "cs.theory", "cs_gt": "cs.theory",
    "cs_dc": "cs.systems", "cs_os": "cs.systems", "cs_ni": "cs.systems", "cs_ar": "cs.systems",
    "cs_pf": "cs.systems", "cs_et": "cs.systems",
    "cs_cr": "cs.security",
    "cs_pl": "cs.pl", "cs_se": "cs.pl", "cs_lo": "cs.pl",
    "cs_db": "cs.data", "cs_ir": "cs.data", "cs_dl": "cs.data", "cs_si": "cs.data",
    "cs_hc": "cs.hci", "cs_gr": "cs.hci", "cs_mm": "cs.hci",
    "cs_ro": "cs.robotics",
    "cs_na": "math.analysis", "cs_it": "math.applied.info",
}

# Topic tags of the CS aggregators: huggingface/ai-deadlines tags, ccf-deadlines
# areas ("ccf_<area>") and awesome-mlss school topics ("mlss_<topic>").
_CODES = {}
for _sf, _w, _codes in [
    ("ai.theory", STRONG, ["stat_ml", "cs_lg_theory", "optimization_methods", "learning_theory",
                           "mlss_theory"]),
    ("ai.general", STRONG, ["machine_learning", "deep_learning", "representation_learning",
                            "lifelong_learning", "knowledge_representation", "reasoning",
                            "mlss_ml", "mlss_kr", "mlss_cogsci", "mlss_neuro", "mlss_eml",
                            "mlss_health", "mlss_econai", "mlss_ds"]),
    ("ai.genai", STRONG, ["large_language_models", "mlss_genai"]),
    ("ai.nlp", STRONG, ["natural_language_processing", "speech", "mlss_nlp", "mlss_sp"]),
    ("ai.vision", STRONG, ["computer_vision", "image_processing", "pattern_recognition",
                           "visual_information_processing", "mlss_cv"]),
    ("ai.rl", STRONG, ["reinforcement_learning", "mlss_rl", "mlss_ap", "mlss_ai4games"]),
    ("ai.trust", STRONG, ["fairness", "mlss_rai"]),
    ("ai.science", STRONG, ["mlss_ml4science", "mlss_bio"]),
    ("ai.general", MEDIUM, ["ccf_ai", "mlss_quantum"]),
    ("phys.quantum", MEDIUM, ["mlss_quantum"]),
    ("cs.theory", STRONG, ["ccf_ct"]),
    ("cs.systems", STRONG, ["ccf_ds", "ccf_nw", "mlss_hw"]),
    ("cs.security", STRONG, ["ccf_sc"]),
    ("cs.pl", STRONG, ["ccf_se", "software_engineering"]),
    ("cs.data", STRONG, ["ccf_db", "data_mining", "web_search", "information_retrieval",
                         "information_systems", "knowledge_graphs", "recommendation",
                         "retrieval", "web_mining", "content_analysis",
                         "semantics_and_knowledge", "mlss_dm", "mlss_recsys"]),
    ("cs.hci", STRONG, ["ccf_cg", "ccf_hi", "computer_graphics", "human_computer_interaction",
                        "mlss_cg", "mlss_hci"]),
    ("cs.robotics", STRONG, ["robotics", "mlss_ro"]),
    ("cs.general", MEDIUM, ["ccf_mx", "signal_processing"]),
    ("math.other", MEDIUM, ["mlss_log"]),
]:
    for _c in _codes:
        _CODES.setdefault(_c, []).append((_sf, _w))


# A meeting that ticks four or more INSPIRE categories is a broad one (EPS-HEP ticks 11, the AIP
# Congress 16). Its "Math and Math Physics" box then says little about the programme, so it only
# supports other maths evidence. Focused ones keep it: MITP "Strings, Symmetries, and
# Singularities" ticks two boxes (seen on 2026-11-10).
BROAD_DECLARED = 4


def declared_evidence(codes):
    """-> list of (subfield, weight) for all the codes declared on one event."""
    codes = [c for c in codes or [] if c]
    out = []
    for code in codes:
        for sf, w in declared_codes(code):
            if sf == "math.mathphys" and len(codes) >= BROAD_DECLARED:
                w = WEAK
            out.append((sf, w))
    return out


def declared_codes(code):
    """Map one declared subject code -> list of (subfield, weight)."""
    raw = str(code).strip()
    if raw.startswith("field:"):             # chosen by YOU in watchlist.yaml
        f = raw[6:].strip()
        if f in SUBFIELDS:
            return [(f, STRONG)]
        if f in FIELDS:
            return [(next(s for s, v in SUBFIELDS.items()
                          if v[0] == f and s.endswith((".general", ".other"))), STRONG)]
        raw = f
    c = re.sub(r"[.\- ]+", "_", raw.lower())
    out = []
    # arXiv-style math codes: math_NT, math.NT
    m = re.match(r"^math_([a-z]{2})$", c)
    if m and m.group(1) in _ARXIV_MATH:
        return [(_ARXIV_MATH[m.group(1)], STRONG)]
    if c in ("math", "mathematics"):
        return [("math.other", WEAK)]
    if c in ("math_ph", "math_mp", "physics_math_ph", "math_and_math_physics"):
        return [("math.mathphys", STRONG)]
    # astro
    if c in ("astro_ph_co", "astro_co", "physics_astro_ph_co", "cosmology",
             "cosmology_and_nongalactic_astrophysics"):
        return [("cosmo.general", STRONG), ("astro.general", WEAK)]
    if c in ("astro_ph_ga", "astro_ga", "physics_astro_ph_ga"):
        return [("astro.galactic", STRONG)]
    if c in ("astro_ph_he", "astro_he", "physics_astro_ph_he"):
        return [("astro.he", STRONG)]
    if c in ("astro_ph_sr", "astro_ph_ep", "astro_sr", "astro_ep",
             "physics_astro_ph_sr", "physics_astro_ph_ep"):
        return [("astro.stellar", STRONG)]
    if c in ("astro_ph_im", "astro_im", "physics_astro_ph_im"):
        return [("astro.general", STRONG)]
    if c.startswith("astro") or c == "astrophysics":
        return [("astro.general", STRONG)]
    # physics
    if c in ("gr_qc", "physics_gr_qc", "general_relativity"):
        return [("phys.gr", STRONG)]
    if c == "gravitation_and_cosmology":           # INSPIRE category
        return [("phys.gr", STRONG), ("cosmo.general", WEAK)]
    if c in ("hep_th", "physics_hep_th", "theory_hep"):
        return [("phys.hepth", STRONG)]
    if c in ("hep_ph", "physics_hep_ph", "phenomenology_hep", "hep_ex", "experiment_hep"):
        return [("phys.hep", STRONG)]
    if c in ("hep_lat", "lattice"):
        return [("phys.hepth.lattice", STRONG)]
    if c in ("experiment_nucl", "theory_nucl", "nucl_th", "nucl_ex"):
        return [("phys.nuclear", STRONG)]
    if c in ("accelerators", "physics_acc_ph"):
        return [("phys.hep.accel", STRONG)]
    if c in ("instrumentation", "physics_ins_det"):
        return [("phys.applied.instr", STRONG), ("phys.hep.accel", WEAK)]
    if c in ("physics_atom_ph", "physics_atm_clus"):
        return [("phys.amo.atomic", STRONG)]
    if c == "physics_optics":
        return [("phys.amo.photonics", STRONG)]
    if c == "physics_med_ph":
        return [("phys.applied.medical", STRONG)]
    if c == "physics_comp_ph":
        return [("phys.condmat.computational", STRONG)]
    if c in ("physics_soc_ph",):
        return [("phys.complex.socio", STRONG)]
    if c in ("physics_bio_ph", "q_bio"):
        return [("phys.condmat.active", STRONG)]
    if c == "physics_ed_ph":
        return [("phys.meta.education", STRONG)]
    if c in ("physics_hist_ph", "physics_soc_ph_history"):
        return [("phys.meta.history", STRONG)]
    if c in ("physics_chem_ph", "physics_app_ph"):
        return [("phys.applied.materials", MEDIUM)]
    if c == "physics_geo_ph":
        return [("phys.fluids.earth", STRONG)]
    if c == "physics_ao_ph":
        return [("phys.fluids.climate", STRONG)]
    if c == "physics_plasm_ph":
        return [("phys.fluids.plasma", STRONG)]
    if c == "physics_flu_dyn":
        return [("phys.fluids.fluids", STRONG)]
    if c in ("general_physics", "physics_gen_ph"):
        return [("phys.general", MEDIUM)]
    if c in ("quant_ph", "physics_quant_ph", "quantum_physics"):
        return [("phys.quantum", STRONG)]
    _cm = {"soft": "phys.condmat.soft", "stat_mech": "phys.condmat.stat", "str_el": "phys.condmat.correlated",
           "supr_con": "phys.condmat.correlated", "mes_hall": "phys.condmat.meso",
           "mtrl_sci": "phys.applied.materials", "dis_nn": "phys.condmat.stat",
           "quant_gas": "phys.amo.cold", "other": "phys.condmat"}
    m = re.match(r"^(?:physics_)?cond_mat_(\w+)$", c)
    if m and m.group(1) in _cm:
        return [(_cm[m.group(1)], STRONG)]
    if c.startswith(("cond_mat", "physics_cond_mat")) or c == "condensed_matter":
        return [("phys.condmat", STRONG)]
    if c == "nlin_si":
        return [("math.mathphys.integrable", STRONG), ("phys.hepth.integrable", MEDIUM)]
    if c in ("nlin_cd", "nlin_ps", "nlin_ao", "nlin_cg"):
        return [("phys.complex.nonlinear", STRONG)]
    if c.startswith("nlin"):
        return [("phys.complex.nonlinear", MEDIUM)]
    if c in ("physics",):
        return [("phys.general", WEAK)]
    if c == "data_analysis_and_statistics":        # INSPIRE category
        return [("math.probability", WEAK)]
    # CS / stats / AI
    if c in _CODES:
        return list(_CODES[c])
    m = re.match(r"^(?:cs|eess)_([a-z]{2})$", c)
    if m and m.group(0) in _ARXIV_CS:
        return [(_ARXIV_CS[m.group(0)], STRONG)]
    if c in ("stat", "stat_th", "stat_me", "stat_ap", "stat_co", "math_st"):
        return [("math.stat", STRONG)]
    if c.startswith(("cs_", "eess_")) or c in ("cs", "computer_science"):
        return [("cs.general", MEDIUM)]
    return out


# ---------------------------------------------------------------------------
# Embedding prototypes (Option B). A few sentences that describe what an
# event on this sub-field *sounds like*. Negative classes absorb events that
# are about something else entirely, so they don't get forced into a field.
# ---------------------------------------------------------------------------
PROTOTYPES = {
    "cosmo.de": "dark energy, cosmic acceleration, Hubble tension, expansion history of the universe, modified gravity, supernova cosmology, DESI BAO constraints on w0 wa",
    "cosmo.lss": "large-scale structure of the universe, galaxy clustering, weak lensing, cosmic shear, redshift surveys, cosmological N-body simulations, matter power spectrum",
    "cosmo.early": "cosmic microwave background, inflation, primordial non-Gaussianity, reionization, 21-cm cosmology, early universe physics",
    "cosmo.dm": "dark matter particles, axions, primordial black holes, dark matter halos and direct detection",
    "cosmo.general": "cosmology conference, physical cosmology, the standard cosmological model, observational cosmology",
    "ai.science": "machine learning for physics and astronomy, simulation-based inference, neural emulators, AI for science, physics-informed neural networks",
    "ai.theory": "theory of deep learning, statistical learning theory, generalization bounds, optimization, kernel methods, learning theory",
    "ai.genai": "large language models, generative models, diffusion models, foundation models, transformers, LLM agents, generative AI",
    "ai.nlp": "natural language processing, computational linguistics, machine translation, speech recognition, question answering",
    "ai.vision": "computer vision, image recognition, object detection, video understanding, multimodal vision-language models, 3D reconstruction",
    "ai.rl": "reinforcement learning, sequential decision making, multi-agent systems, planning, bandits and control, imitation learning",
    "ai.trust": "AI safety, alignment, interpretability, fairness, privacy and robustness of machine learning, responsible AI",
    "ai.general": "machine learning conference, deep learning, neural networks, representation learning, artificial intelligence research",
    "cs.theory": "algorithms, computational complexity, theoretical computer science, approximation and randomized algorithms, data structures",
    "cs.systems": "operating systems, distributed systems, computer architecture, networking, high-performance computing, cloud and edge computing",
    "cs.security": "computer security, cryptography, privacy, network security, malware, blockchain, secure systems",
    "cs.pl": "programming languages, compilers, type systems, formal verification, model checking, software engineering",
    "cs.data": "databases, data management, data mining, information retrieval, recommender systems, web search, knowledge graphs",
    "cs.hci": "human-computer interaction, user interfaces, computer graphics, visualization, virtual and augmented reality",
    "cs.robotics": "robotics, autonomous vehicles, robot learning, manipulation and locomotion, motion planning, drones",
    "cs.general": "computer science department seminar, computing research, informatics, signal processing, information systems",
    "astro.he": "black holes, neutron stars, pulsars, gravitational wave astronomy, gamma-ray bursts, high-energy astrophysics, transients",
    "astro.galactic": "galaxy formation and evolution, active galactic nuclei, interstellar medium, star formation, galaxy clusters",
    "astro.stellar": "stellar physics, the Sun, solar flares, exoplanets, planetary systems, asteroseismology, supernovae",
    "astro.general": "astronomy and astrophysics meeting, telescopes, observatories, sky surveys, radio astronomy",
    "math.nt": "number theory, modular forms, L-functions, elliptic curves, Galois representations, arithmetic geometry, primes",
    "math.topology": "algebraic topology, low-dimensional topology, homotopy theory, knots, manifolds, cohomology",
    "math.algebra": "algebra, representation theory, group theory, Lie algebras, category theory, commutative algebra",
    "math.geometry": "differential geometry, algebraic geometry, symplectic geometry, moduli spaces, Riemannian geometry",
    "math.probability": "probability theory, stochastic processes, random matrices, Brownian motion, mathematical statistics, Bayesian inference",
    "math.mathphys": "mathematical physics, integrable systems, conformal field theory, rigorous quantum field theory",
    "math.analysis": "analysis, partial differential equations, harmonic analysis, functional analysis, operator theory",
    "math.other": "combinatorics, mathematical logic, dynamical systems, graph theory, discrete mathematics",
    "phys.gr": "general relativity, gravitation, spacetime geometry, black hole physics, numerical relativity, quantum gravity",
    "phys.hepth": "string theory, quantum field theory, particle physics, holography, scattering amplitudes, gauge theories",
    "phys.quantum": "quantum information, quantum computing, entanglement, quantum many-body physics, quantum optics",
    "phys.condmat": "condensed matter physics, statistical mechanics, soft matter, active matter, phase transitions, superconductivity",
    "phys.fluids": "fluid dynamics, turbulence, plasma physics, magnetohydrodynamics, climate and atmospheric physics",
    "phys.general": "physics colloquium, optics, lasers, atomic and nuclear physics",
}
NEGATIVE_PROTOTYPES = {
    "neg.bio": "biology, medicine, genomics, neuroscience, cell biology, clinical research, ecology",
    "neg.chem": "chemistry, materials synthesis, catalysis, batteries, chemical engineering",
    "neg.eng": "power systems, electrical machines, civil and mechanical engineering, manufacturing, construction, automotive industry",
    "neg.admin": "committee meeting, foundation day, cultural event, open day, inauguration ceremony, administrative announcement, alumni event",
    "neg.humanities": "history, philosophy, economics, social sciences, education policy, arts and culture",
}


# ---------------------------------------------------------------------------
# Topics: the third level (field -> sub-field -> topic)
#
# taxonomy_physics.py and taxonomy_math.py define about 130 topics and a few new
# sub-fields. An event is tagged with the most specific node that matches; every
# ancestor counts for filters and profile weights (see ancestors()). The embedding
# classifier knows only the original sub-fields (PROTOTYPES), so adding topics
# cannot disturb its calibration.
# ---------------------------------------------------------------------------
from taxonomy_math import TOPICS as _MATH_TOPICS, UMBRELLAS as _MATH_UMBRELLAS      # noqa: E402
from taxonomy_math import NARROWER as _MATH_NARROWER                               # noqa: E402
from taxonomy_physics import TOPICS as _PHYS_TOPICS, UMBRELLAS as _PHYS_UMBRELLAS    # noqa: E402

PARENT_SF = {}      # topic id -> its sub-field
INHERITS = {}       # new sub-field -> older sub-field whose profile weight it keeps
MIRRORS = {         # shown under two fields on purpose (see mirror_tags)
    "cosmo.gravity": "Gravitation & GR",
    "phys.cosmo": "Cosmology",
}

_added = {}
_added["cosmo.gravity"] = ("cosmo", MIRRORS["cosmo.gravity"])
INHERITS["cosmo.gravity"] = "phys.gr"
for _id, (_field, _label, _inh) in {**_PHYS_UMBRELLAS, **_MATH_UMBRELLAS}.items():
    _added[_id] = (_field, _label)
    if _inh:
        INHERITS[_id] = _inh
_added["phys.cosmo"] = ("physics", MIRRORS["phys.cosmo"])
for _id, (_sf, _label, _pats) in {**_PHYS_TOPICS, **_MATH_TOPICS}.items():
    assert _sf in SUBFIELDS or _sf in _added, (_id, _sf)
    _added[_id] = ((SUBFIELDS.get(_sf) or _added[_sf])[0], _label)
    PARENT_SF[_id] = _sf
    RULES[_id] = list(_pats)
SUBFIELDS.update(_added)


def _display_order():
    """Fields in their order; inside a field each sub-field is followed by its topics."""
    out = {}
    for f in FIELDS:
        tops = [sf for sf, v in SUBFIELDS.items() if v[0] == f and sf not in PARENT_SF]
        for sf in tops:
            out[sf] = SUBFIELDS[sf]
            for t, up in PARENT_SF.items():
                if up == sf:
                    out[t] = SUBFIELDS[t]
    return out


# a "(general)" topic -> the narrower topics of its area it gives way to (taxonomy_math.NARROWER)
NARROWER = {g: set(ns) for g, ns in _MATH_NARROWER.items()}
for _g, _ns in NARROWER.items():
    assert _g in PARENT_SF and _ns <= set(PARENT_SF), (_g, _ns)
    assert {PARENT_SF[n] for n in _ns} == {PARENT_SF[_g]}, _g     # same branch

_ordered = _display_order()
assert len(_ordered) == len(SUBFIELDS)
SUBFIELDS.clear()
SUBFIELDS.update(_ordered)


# ---------------------------------------------------------------------------
# Compilation helpers
# ---------------------------------------------------------------------------
class _Unless:
    """"word ||| context": the word counts only when the same text does not also mention the
    context. For common words that mean something else nearby: "topological" in a title about
    quantum matter or insulators is condensed matter, not topology."""

    def __init__(self, pattern, unless):
        self.pattern, self.unless = pattern, unless

    def search(self, text):
        m = self.pattern.search(text)
        return None if m is None or self.unless.search(text) else m


def _compile(pattern):
    if " ||| " in pattern:
        word, unless = pattern.split(" ||| ", 1)
        return _Unless(_compile(word), re.compile(W + "(?:" + unless + ")" + W, re.I))
    if pattern.startswith("CS:"):
        return re.compile(W + pattern[3:] + W)
    pattern = pattern.replace("CS_INLINE_AI", "AI")
    return re.compile(W + "(?:" + pattern + ")" + W, re.I)


# French keywords for mathematics (and a little physics and AI): taxonomy_math_fr.py
from taxonomy_math_fr import FRENCH as _FRENCH, fold as _fold      # noqa: E402
for _sf, _pats in _FRENCH.items():
    assert _sf in SUBFIELDS, _sf
    RULES[_sf] = list(RULES.get(_sf, [])) + [_fold(p) for p in _pats]

COMPILED = {sf: [_compile(p) for p in pats] for sf, pats in RULES.items()}


def _prefilter_part(pattern):
    """The same match as _compile(pattern), ignoring case and any ||| context: a superset."""
    word = pattern.split(" ||| ", 1)[0]
    if word.startswith("CS:"):
        return "(?:" + W + word[3:] + W + ")"
    return "(?:" + W + "(?:" + word.replace("CS_INLINE_AI", "AI") + ")" + W + ")"


# One combined regex per sub-field and topic that matches whenever any of its patterns could
# (2026-11-10). keyword_hits tries the individual patterns only after it matches, which gives the
# same result about 10x faster: most texts mention few of the ~200 sub-fields and topics.
PREFILTER = {sf: re.compile("|".join(_prefilter_part(p) for p in pats), re.I) for sf, pats in RULES.items()}


def parent(sf):
    """The FIELD of a sub-field or topic."""
    return SUBFIELDS[sf][0]


def label(node):
    return FIELDS[node] if node in FIELDS else SUBFIELDS[node][1]


def is_node(node):
    """A taxonomy node a profile may weight: a field, a sub-field or a topic."""
    return node in FIELDS or node in SUBFIELDS


def ancestors(node):
    """The node itself, then what it belongs to, most specific first, ending with its
    field: topic -> sub-field -> (the older sub-field it inherits from) -> field."""
    if node in FIELDS:
        return [node]
    out, seen = [node], {node}
    nxt = PARENT_SF.get(node) or INHERITS.get(node)
    while nxt and nxt not in seen:
        out.append(nxt)
        seen.add(nxt)
        nxt = PARENT_SF.get(nxt) or INHERITS.get(nxt)
    out.append(SUBFIELDS[node][0])
    return out


def mirror_key(tag):
    """'gr' for gravitation tags, 'cosmo' for cosmology tags, else None. A tag and its
    mirror share a key, so a profile never counts one subject as two fields."""
    if tag == "cosmo.gravity" or "phys.gr" in ancestors(tag)[:-1] and tag not in FIELDS:
        return "gr"
    if tag == "phys.cosmo" or (tag in SUBFIELDS and parent(tag) == "cosmo"):
        return "cosmo"
    return None


def is_mirror(tag):
    return tag in MIRRORS


def mirrored(a, b):
    ka = mirror_key(a)
    return ka is not None and ka == mirror_key(b) and parent(a) != parent(b)


def mirror_tags(tags):
    """Gravitation belongs to Physics and to Astronomy & cosmology; cosmology to both
    as well, so someone who follows only one of the two still sees all of it."""
    extra = []
    if any(mirror_key(t) == "gr" and not is_mirror(t) for t in tags):
        extra.append("cosmo.gravity")
    if any(mirror_key(t) == "cosmo" and not is_mirror(t) for t in tags):
        extra.append("phys.cosmo")
    return [t for t in extra if t not in tags]


ORDER = {sf: i for i, sf in enumerate(SUBFIELDS)}   # display order of sub-fields


def export_for_frontend():
    """The site builds its field/sub-field/topic filter from this, so the taxonomy is
    defined in exactly one place. `chain` gives, for every node, what to look up in a
    profile's weights (itself, its sub-field, what that inherits, its field)."""
    return {
        "fields": [{"id": f, "label": lbl,
                    "subfields": [{"id": sf, "label": v[1], "parent": PARENT_SF.get(sf)}
                                  for sf, v in SUBFIELDS.items() if v[0] == f]}
                   for f, lbl in FIELDS.items()],
        "chain": {sf: ancestors(sf) for sf in SUBFIELDS},
        "mirrors": sorted(MIRRORS),
        "display": display_tree(),
        "migrations": MIGRATIONS,
    }


# When a branch or topic is split or moved, a visitor's saved selection is widened to what the
# old id used to cover. Each entry applies once, to selections saved before its version.
MIGRATIONS = [
    {"version": "2026-11-10", "map": {
        "b:math.probability": ["b:math.probability", "b:math.stat"],
        "t:math.probability.stat": ["b:math.stat"],
        "t:math.probability.theory": ["t:math.probability.theory", "t:math.probability.stochastic",
                                      "t:math.probability.walks", "t:math.probability.geometry"],
    }},
    # M3c: 24 more maths topics; each old topic widens to the topics its keywords went to
    {"version": "2026-11-10-m3c", "map": {
        "t:math.logic.logic": ["t:math.logic.logic", "t:math.logic.model", "t:math.logic.sets",
                               "t:math.logic.computability", "t:math.logic.formal"],
        "t:math.algebra.group": ["t:math.algebra.group", "t:math.algebra.ggt"],
        "t:math.algebra.rings": ["t:math.algebra.rings", "t:math.algebra.quivers"],
        "t:math.algebra.lie": ["t:math.algebra.lie", "t:math.algebra.quivers"],
        "t:math.geometry.algebraic": ["t:math.geometry.algebraic", "t:math.geometry.moduli",
                                      "t:math.geometry.enumerative"],
        "t:math.geometry.complex": ["t:math.geometry.complex", "t:math.geometry.moduli"],
        "t:math.geometry.lie": ["t:math.geometry.lie", "t:math.geometry.moduli"],
        "t:math.geometry.diff": ["t:math.geometry.diff", "t:math.geometry.analysis"],
        "t:math.topology.algebraic": ["t:math.topology.algebraic", "t:math.topology.applied"],
        "t:math.analysis.pde": ["t:math.analysis.pde", "t:math.analysis.elliptic", "t:math.analysis.waves",
                                "t:math.analysis.fluids"],
        "t:math.analysis.calculus": ["t:math.analysis.calculus", "t:math.analysis.ot"],
        "t:math.dyn.ergodic": ["t:math.dyn.ergodic", "t:math.dyn.homogeneous"],
        "t:math.numeric.analysis": ["t:math.numeric.analysis", "t:math.numeric.pde", "t:math.numeric.linalg",
                                    "t:math.numeric.uq"],
        "t:math.numeric.symbolic": ["t:math.numeric.symbolic", "t:math.logic.formal"],
        "t:math.optim.optimisation": ["t:math.optim.optimisation", "t:math.optim.convex", "t:math.optim.discrete"],
        "t:math.optim.game": ["t:math.optim.game", "t:math.optim.finance"],
        "t:math.applied.modelling": ["t:math.applied.modelling", "t:math.applied.imaging"],
        "t:math.nt.coding": ["t:math.nt.coding", "t:math.applied.info", "t:math.applied.imaging"],
        "t:math.edu.education": ["t:math.edu.education", "t:math.edu.history"],
    }},
]


# ---------------------------------------------------------------------------
# What the site shows: five disciplines, each a list of branches, each with its
# topics. This is presentation only; tagging and scoring use the ids above.
# A shared branch ("@gr", ...) is one branch listed under two disciplines: same
# id, same topics, same count, so ticking it in one place ticks it in the other.
# ---------------------------------------------------------------------------
SHARED = {
    "@gr": {"label": "Gravitation & GR", "base": "phys.gr", "extra": ["cosmo.gravity"]},
    "@cosmology": {"label": "Cosmology", "base": None,
                   "topics": ["cosmo.early", "cosmo.de", "cosmo.lss", "cosmo.dm", "cosmo.general"],
                   "extra": ["phys.cosmo"]},
    "@mathphys": {"label": "Mathematical physics", "base": "math.mathphys", "extra": []},
}
DISPLAY = [
    # Each discipline starts with its catch-all ("0": colloquia and broad talks), then the
    # branches. Physics: fundamental theory, then matter from small scales to large, then
    # applied and human topics. Mathematics: roughly the order of the Mathematics Subject
    # Classification.
    ("physics", "Physics", "physics",
     ["phys.general", "phys.hepth", "@gr", "phys.hep", "phys.nuclear", "phys.amo", "phys.quantum",
      "phys.condmat", "phys.applied", "phys.fluids", "phys.complex", "@mathphys",
      "@cosmology", "phys.meta"]),
    ("astro", "Astronomy & Astrophysics", "astro",
     ["astro.general", "@cosmology", "@gr", "astro.he", "astro.galactic", "astro.stellar"]),
    ("math", "Mathematics", "math",
     ["math.other", "math.logic", "math.comb", "math.nt", "math.algebra", "math.geometry",
      "math.topology", "math.analysis", "math.dyn", "math.probability", "math.stat", "@mathphys",
      "math.numeric", "math.optim", "math.applied", "math.edu"]),
    ("cs", "Computer science", "cs",
     ["cs.general", "cs.theory", "cs.systems", "cs.security", "cs.pl", "cs.data", "cs.hci",
      "cs.robotics"]),
    ("ai", "AI & machine learning", "ai",
     ["ai.general", "ai.science", "ai.theory", "ai.genai", "ai.nlp", "ai.vision", "ai.rl",
      "ai.trust"]),
]


def _topics_of(sf):
    return [t for t, p in PARENT_SF.items() if p == sf]


def _branch(key):
    if key in SHARED:
        spec = SHARED[key]
        base = spec["base"]
        topic_ids = spec.get("topics") or _topics_of(base)
        own = [base] if base else []
        return {"id": key, "label": spec["label"], "shared": True,
                "members": own + topic_ids + spec["extra"],
                "topics": [{"id": t, "label": SUBFIELDS[t][1]} for t in topic_ids]}
    topic_ids = _topics_of(key)
    return {"id": key, "label": SUBFIELDS[key][1], "shared": False,
            "members": [key] + topic_ids,
            "topics": [{"id": t, "label": SUBFIELDS[t][1]} for t in topic_ids]}


def display_tree():
    """Disciplines -> branches -> topics, with the tag ids each branch stands for."""
    return [{"id": d, "label": label, "color": color, "branches": [_branch(k) for k in keys]}
            for d, label, color, keys in DISPLAY]
