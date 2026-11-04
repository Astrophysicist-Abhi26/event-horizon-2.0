"""
Physics topics: the third level of the taxonomy (field -> sub-field -> topic).

UMBRELLAS   new sub-fields, carved out of what used to be "Physics (other)" and
            friends: id -> (field, label, inherits). `inherits` is the older
            sub-field whose profile weight an event keeps until a profile
            lists the new one, so no ranking changes by surprise.
TOPICS      topic id -> (sub-field, label, [keyword patterns]).

Patterns follow taxonomy.RULES: case-insensitive, word-bounded; a "CS:" prefix
makes one case-sensitive (acronyms). Titles are short and plain, so patterns
name the subject the way a conference title does.
"""

UMBRELLAS = {
    "phys.hep":     ("physics", "Particle physics: phenomenology & experiment", "phys.hepth"),
    "phys.nuclear": ("physics", "Nuclear & heavy-ion physics", "phys.general"),
    "phys.amo":     ("physics", "Atomic, molecular & optical physics", "phys.general"),
    "phys.applied": ("physics", "Materials, devices & instrumentation", "phys.general"),
    "phys.complex": ("physics", "Nonlinear dynamics & complex systems", "phys.general"),
    "phys.cosmo":   ("physics", "Cosmology", None),
    "phys.meta":    ("physics", "History, philosophy & education of physics", "phys.general"),
}

TOPICS = {
    # ── High-energy theory & QFT ───────────────────────────────────────────────
    "phys.hepth.string": ("phys.hepth", "String theory", [
        r"string theor\w*", r"superstring\w*", r"CS:Strings\s+20\d\d", r"strings? (?:and|&) (?:fields|branes|geometry)",
        r"D-?branes?", r"(?:string|M|F)-theory", r"heterotic", r"worldsheet", r"string (?:dualit\w+|perturbation|field|cosmology|phenomenology)",
        r"type II[AB]?", r"string (?:and|&) M[- ]theory", r"topological strings?"]),
    "phys.hepth.holography": ("phys.hepth", "AdS/CFT & holography", [
        r"holograph\w*", r"CS:AdS\d?\s*/\s*CFT\d?", r"gauge\s*/\s*gravity", r"gauge-gravity", r"ryu-takayanagi",
        r"CS:AdS\d?", r"celestial holography", r"de Sitter holography"]),
    "phys.hepth.cft": ("phys.hepth", "Conformal field theory & bootstrap", [
        r"conformal (?:field theor\w*|bootstrap|symmetry|blocks?|invariance|manifolds?|anomal\w+|perturbation theory)",
        r"CS:CFTs?", r"(?:modular |numerical |analytic )?bootstrap", r"Virasoro", r"minimal models?",
        r"vertex operator algebras?", r"two-dimensional (?:conformal|CFT)", r"2d CFT", r"conformal nets?"]),
    "phys.hepth.qft": ("phys.hepth", "Quantum field theory", [
        r"quantum field theor\w*", r"CS:QFTs?", r"gauge theor\w*", r"yang-mills", r"path integrals?",
        r"feynman (?:diagrams?|integrals?|rules)", r"(?:non-?perturbative|perturbative) (?:QFT|quantum field)",
        r"renormali[sz]ation", r"large[- ]N", r"strongly coupled (?:gauge|field)", r"confinement", r"chiral symmetry breaking"]),
    "phys.hepth.amplitudes": ("phys.hepth", "Scattering amplitudes", [
        r"scattering amplitudes?", r"CS:Amplitudes?\s+20\d\d", r"amplituhedr\w*", r"positive geometr\w+",
        r"on-shell (?:methods?|recursion|diagrams?)", r"unitarity methods?", r"celestial amplitudes?",
        r"form factors?", r"S-matrix", r"double copy", r"soft theorems?", r"cluster algebras? (?:and|in) (?:amplitudes|scattering)",
        r"Feynman integrals?", r"Landau singularit\w+"]),
    "phys.hepth.susy": ("phys.hepth", "Supersymmetry & supergravity", [
        r"supersymmetr\w*", r"CS:SUSY", r"supergravit\w*", r"supermultiplets?", r"superconformal", r"BPS (?:states?|bounds?|spectrum)",
        r"supermanifolds?", r"superspace", r"N\s*=\s*[1-8]\s+(?:supersymmetric|gauge|SCFT|theor\w+)"]),
    "phys.hepth.swampland": ("phys.hepth", "Swampland & string phenomenology", [
        r"swampland", r"string[- ]pheno(?:menology)?", r"string (?:phenomenology|landscape|vacua|model building|compactifications?)",
        r"(?:string|flux|heterotic|Calabi-Yau|F-theory) compactifications?", r"moduli stabili[sz]ation",
        r"flux (?:vacua|compactifications?|landscape)", r"string (?:cosmology|inflation)", r"de Sitter (?:vacua|space in string)",
        r"Calabi-Yau (?:compactifications?|manifolds?|threefolds?|fourfolds?)", r"F-theory"]),
    "phys.hepth.tqft": ("phys.hepth", "Topological QFT & Chern-Simons", [
        r"topological (?:quantum )?field theor\w*", r"CS:TQFTs?", r"chern[- ]simons", r"topological (?:string|twist|recursion)\w*",
        r"seiberg-witten", r"donaldson(?:-thomas)? (?:theory|invariants?)", r"knot invariants?", r"invariants of (?:knots|manifolds|3-manifolds)",
        r"reshetikhin-turaev", r"Witten-Reshetikhin", r"extended (?:topological|TQFT)", r"quantum topology"]),
    "phys.hepth.integrable": ("phys.hepth", "Integrability & Yang-Baxter", [
        r"integrab\w+ (?:in|and|of) (?:gauge|string|AdS|field|quantum|holograph\w*)", r"quantum integrable", r"integrable (?:systems?|models?|field theor\w+|spin chains?|hierarch\w+|quantum)",
        r"yang-baxter", r"bethe ansatz", r"thermodynamic bethe", r"painlev(?:é|e)", r"lax pairs?",
        r"quantum inverse scattering", r"spectral curves?", r"cluster integrable", r"Toda"]),
    "phys.hepth.lattice": ("phys.hepth", "Lattice field theory", [
        r"lattice (?:QCD|gauge theor\w*|field theor\w*|simulations?|regulari[sz]ation|calculations?|Monte Carlo|methods)",
        r"CS:Lattice\s+20\d\d", r"lattice (?:and|&) continuum", r"finite[- ]density (?:QCD|lattice)", r"sign problem",
        r"quantum link", r"hamiltonian lattice"]),
    "phys.hepth.eft": ("phys.hepth", "Effective field theory", [
        r"effective field theor\w*", r"CS:EFTs?", r"chiral perturbation theory", r"CS:SMEFT", r"CS:HEFT", r"heavy quark effective",
        r"soft[- ]collinear effective", r"CS:SCET", r"non-?relativistic (?:QCD|effective)", r"EFT (?:methods|techniques)"]),
    "phys.hepth.symmetries": ("phys.hepth", "Generalized symmetries & anomalies", [
        r"generali[sz]ed (?:global )?symmetr\w*", r"non-?invertible symmetr\w*", r"higher[- ](?:form|group|categorical) symmetr\w*",
        r"categorical symmetr\w*", r"anomal(?:y|ies)(?! detection)", r"'t Hooft anomal\w*", r"anomaly (?:matching|inflow|cancellation)",
        r"symmetry (?:fractionali[sz]ation|protected|topological|defects?)", r"topological defects? (?:and|in) (?:quantum|field)",
        r"(?:global|gauge) symmetr(?:y|ies) (?:and|in) quantum gravity", r"SPT (?:phases|order)"]),
    "phys.hepth.nonpert": ("phys.hepth", "Resurgence & non-perturbative methods", [
        r"resurgence", r"trans-?series", r"borel (?:summation|resummation|plane)", r"non-?perturbative (?:effects?|methods?|physics|aspects|string|QFT|corrections|phenomena)",
        r"instantons?", r"renormalons?", r"exact WKB", r"large order", r"asymptotic series", r"Stokes (?:phenomenon|phenomena|lines)"]),

    # ── Gravitation & general relativity ───────────────────────────────────────
    "phys.gr.classical": ("phys.gr", "General relativity & numerical relativity", [
        r"general relativity", r"numerical relativity", r"einstein (?:equations?|field equations?|gravity|constraint)",
        r"cosmic censorship", r"(?:cauchy|initial value) problem (?:in|for) (?:general relativity|Einstein)", r"mathematical (?:general )?relativity",
        r"spacetime singularit\w+", r"asymptotically (?:flat|AdS|de Sitter|anti-de Sitter)", r"penrose (?:inequality|conjecture)",
        r"positive mass theorem", r"stability of (?:Minkowski|Kerr|black holes?)", r"Kerr (?:stability|black hole|metric)",
        r"CS:GR\s+(?:20\d\d|and)", r"gravitation (?:and|&) (?:cosmology|relativity)", r"CS:GRG", r"relativity (?:and|&) gravitation"]),
    "phys.gr.waves": ("phys.gr", "Gravitational waves", [
        r"gravitational[- ]waves?", r"CS:GWs?", r"LIGO", r"Virgo", r"KAGRA", r"CS:LISA", r"pulsar timing arrays?", r"CS:PTAs?", r"binary (?:black hole|neutron star|compact) (?:mergers?|coalescences?|inspirals?|systems?)", r"compact binar\w+",
        r"Einstein Telescope", r"Cosmic Explorer", r"inspiral\w*", r"ringdown", r"extreme mass[- ]ratio", r"CS:EMRIs?",
        r"gravitational (?:wave )?(?:astronomy|astrophysics|detectors?|lensing)", r"stochastic (?:gravitational[- ]wave )?background"]),
    "phys.gr.bh": ("phys.gr", "Black holes: thermodynamics & information", [
        r"black[- ]holes? (?:information|thermodynamics|microstates?|entropy|evaporation|perturbations?|spectroscopy|shadows?|physics|mergers?|mechanics|solutions?|horizons?|hair|complementarity)",
        r"information (?:paradox|loss|problem)", r"hawking (?:radiation|temperature|effect)", r"page curve", r"quantum extremal", r"entanglement islands?",
        r"firewalls?", r"quasi-?normal modes?", r"event horizons?", r"bekenstein", r"fuzzballs?", r"black hole (?:and|&) (?:string|quantum)",
        r"microstates", r"Penrose process", r"superradian\w+"]),
    "phys.gr.modified": ("phys.gr", "Modified gravity", [
        r"modified (?:theories of )?gravity", r"CS:f\(R\)", r"teleparallel", r"massive gravity", r"scalar-tensor", r"horndeski",
        r"gauss-bonnet", r"einstein-cartan", r"lovelock", r"bi-?metric", r"beyond (?:horndeski|general relativity)", r"alternative theories of gravity",
        r"MOND", r"f\(R\) gravity", r"f\(R,\s*T\)", r"emergent gravity", r"extended theories of gravity", r"Brans-Dicke", r"tests of (?:general relativity|gravity)", r"CS:TeVeS"]),
    "phys.gr.quantum": ("phys.gr", "Quantum gravity", [
        r"quantum gravity", r"loop quantum", r"asymptotic safety", r"causal (?:dynamical triangulations?|set theor\w+|sets?)",
        r"spin[- ]?foams?", r"group field theory", r"canonical quantum gravity", r"planck[- ]scale", r"emergent (?:gravity|spacetime)",
        r"dynamical triangulations?", r"quantum (?:spacetime|geometry|cosmology)", r"non-?commutative (?:geometry|spacetime)s? (?:and|in) (?:physics|gravity)",
        r"minimal length", r"generali[sz]ed uncertainty", r"Wheeler-DeWitt", r"quantum reference frames?"]),

    # ── Particle physics ───────────────────────────────────────────────────────
    "phys.hep.bsm": ("phys.hep", "Beyond the Standard Model & phenomenology", [
        r"beyond the standard model", r"CS:BSM", r"new physics", r"particle phenomenolog\w*", r"CS:Phenomenology\s+20\d\d",
        r"phenomenology (?:of|and|symposium|workshop)", r"(?:grand|great) unifi\w+", r"leptoquarks?", r"dark sectors?", r"naturalness", r"hierarchy problem", r"CS:GUTs?", r"extended (?:Higgs|scalar) sectors?", r"two[- ]Higgs[- ]doublet", r"vector[- ]like", r"standard model (?:extensions?|and beyond)",
        r"particle physics (?:phenomenology|theory)", r"physics beyond", r"search(?:es)? for new (?:physics|particles?)", r"new (?:particles?|physics) searches"]),
    "phys.hep.neutrino": ("phys.hep", "Neutrino physics", [
        r"neutrinos?", r"neutrino (?:oscillations?|mass(?:es)?|physics|telescopes?|experiments?)", r"CS:DUNE", r"Hyper-?Kamiokande", r"CS:JUNO",
        r"IceCube", r"neutrino-?less double beta", r"double beta decay", r"leptogenesis", r"sterile neutrinos?", r"mass ordering", r"KATRIN",
        r"CS:NOvA", r"CS:T2K", r"majorana (?:neutrinos?|mass)"]),
    "phys.hep.flavour": ("phys.hep", "Flavour physics & CP violation", [
        r"flavou?r (?:physics|anomal\w+|symmetr\w+|changing|violation|puzzle)", r"CP[- ]violation", r"CS:CKM", r"CS:PMNS", r"B[- ]physics", r"rare (?:B[- ])?decays?",
        r"(?:B|D|K)[- ]meson (?:mixing|decays?|physics)", r"muon g-?2", r"lepton flavou?r", r"charm physics", r"kaons?", r"baryon number violation",
        r"electric dipole moments?", r"CS:EDMs?", r"CS:LHCb", r"Belle\s*II", r"CS:BaBar", r"heavy[- ]flavou?r", r"b-?hadrons?", r"tau (?:physics|lepton)"]),
    "phys.hep.collider": ("phys.hep", "Collider physics & the Higgs", [
        r"colliders?", r"CS:LHC", r"large hadron collider", r"CS:HL-LHC", r"higgs (?:boson|physics|portal|sector|couplings?|production)",
        r"future (?:circular )?colliders?", r"CS:FCC", r"muon colliders?", r"CS:ILC", r"CS:CEPC", r"electroweak (?:physics|precision|symmetry breaking|phase transitions?)",
        r"top[- ]quarks?", r"jets? (?:physics|substructure|algorithms?)", r"parton showers?", r"monte carlo (?:event )?generators?", r"event generators?", r"proton[- ]proton collisions?", r"hadron colliders?", r"lepton colliders?", r"precision (?:physics|measurements) at",
        r"standard model (?:measurements|precision|physics)", r"CS:HEP", r"high[- ]energy physics (?:experiments?|conference)"]),
    "phys.hep.hadron": ("phys.hep", "Hadron physics & QCD", [
        r"hadron\w*", r"CS:QCD", r"quantum chromodynamics", r"parton distribution\w*", r"CS:PDFs?", r"proton (?:structure|spin|radius|mass)", r"nucleon (?:structure|spin|mass)",
        r"quarkonium", r"exotic hadrons?", r"tetraquarks?", r"pentaquarks?", r"chiral symmetry", r"deep[- ]inelastic", r"electron[- ]ion collider", r"CS:EIC",
        r"transverse[- ]momentum[- ]dependent", r"CS:TMDs?", r"generali[sz]ed parton", r"CS:GPDs?", r"QCD (?:at|in|and) (?:high|finite|low)", r"perturbative QCD",
        r"nucleon", r"glueballs?", r"gluons?", r"quarks?"]),
    "phys.hep.dm": ("phys.hep", "Dark matter (particle physics)", [
        r"dark matter (?:direct|indirect|detection|candidates?|models?|searches?|particles?|physics)", r"direct detection", r"CS:WIMPs?", r"axions?",
        r"axion[- ]like", r"ultra-?light dark matter", r"fuzzy dark matter", r"dark photons?", r"feebly[- ]interacting", r"CS:FIMPs?", r"freeze-?(?:in|out)",
        r"dark matter and", r"hidden sectors?", r"dark (?:sector|force|radiation)"]),
    "phys.hep.accel": ("phys.hep", "Accelerators & detectors", [
        r"(?:particle )?accelerators?", r"accelerator (?:physics|science|technology)", r"beam (?:dynamics|physics|instrumentation|diagnostics|cooling)",
        r"synchrotron\w*", r"cyclotron\w*", r"linacs?", r"linear accelerators?", r"storage rings?", r"free[- ]electron lasers?", r"plasma wakefield", r"laser[- ]plasma accelerat\w+",
        r"detector (?:instrumentation|physics|development|technolog\w+|R&D)", r"(?:silicon|pixel|gaseous|semiconductor) (?:sensors?|detectors?|trackers?)",
        r"calorimet\w+", r"particle detectors?", r"radiation detectors?", r"photo-?detectors?", r"scintillat\w+", r"trigger (?:and|&) data acquisition", r"CS:DAQ",
        r"readout electronics", r"CS:SiPMs?", r"silicon photomultipliers?", r"cryogenic detectors?", r"instrumentation (?:for|in) (?:high[- ]energy|particle|nuclear)",
        r"superconducting (?:magnets?|RF|cavit\w+)", r"vacuum (?:technology|systems?)", r"cryogenics"]),
    "phys.hep.astropart": ("phys.hep", "Astroparticle & cosmic rays", [
        r"astro-?particle", r"cosmic[- ]rays?", r"gamma[- ]ray (?:astronomy|astrophysics|bursts?|sources?)", r"high[- ]energy neutrinos?",
        r"multi-?messenger", r"ultra-?high[- ]energy", r"cherenkov (?:telescopes?|array|light)", r"CS:CTA", r"pierre auger", r"CS:HAWC", r"CS:LHAASO", r"air showers?",
        r"extensive air", r"cosmic (?:ray|accelerators)", r"CS:ICRC", r"TeV (?:gamma|astronomy|sources?)", r"astroparticle physics", r"underground (?:physics|laborator\w+)",
        r"neutrino astronomy"]),

    # ── Nuclear & heavy-ion ────────────────────────────────────────────────────
    "phys.nuclear.structure": ("phys.nuclear", "Nuclear structure & reactions", [
        r"nuclear (?:structure|theory|physics|reactions?|forces?|matter|many-body|shell model|density functional|data|fission|fusion|excitations?|models?|spectroscopy|decay)", r"shell[- ]model", r"neutron[- ]rich", r"radioactive (?:ion )?beams?", r"exotic nuclei", r"halo nuclei", r"super-?heavy (?:elements?|nuclei)",
        r"isotopes? (?:production|separation)", r"CS:FAIR", r"CS:FRIB", r"nuclear physics (?:symposium|conference|school)",
        r"ab initio (?:nuclear|nuclear structure)", r"coupled[- ]cluster (?:nuclear|nuclei)", r"nucleon[- ]nucleon", r"neutron (?:physics|capture|skins?)", r"alpha (?:decay|clustering)"]),
    "phys.nuclear.astro": ("phys.nuclear", "Nuclear astrophysics", [
        r"nuclear astro\w*", r"nucleosynthesis", r"r-process", r"s-process", r"p-process", r"stellar (?:nucleosynthesis|burning)", r"dense matter",
        r"neutron[- ]star (?:matter|equation of state|crust|interiors?|mergers?)", r"equation of state (?:of|for) (?:dense|neutron|nuclear)", r"cosmic (?:abundances|chemical evolution)",
        r"big[- ]bang nucleosynthesis", r"nuclear reaction rates?", r"weak interactions? (?:in|and) (?:stars|astrophys\w+)", r"supernova (?:nucleosynthesis|neutrinos?)"]),
    "phys.nuclear.heavyion": ("phys.nuclear", "Heavy-ion collisions & QGP", [
        r"heavy[- ]ions?(?: collisions?| physics| beams?)?", r"quark[- ]gluon plasma", r"CS:QGP", r"quark matter", r"relativistic heavy", r"CS:RHIC", r"ultra-?relativistic",
        r"QCD (?:phase diagram|matter|critical point|thermodynamics)", r"color glass condensate", r"jet quenching", r"hot (?:and|&) dense (?:QCD|matter)", r"strangeness",
        r"CS:ALICE", r"initial state (?:physics|fluctuations)", r"hydrodynamics of (?:the )?(?:QGP|heavy)", r"collective flow"]),
    "phys.nuclear.experiment": ("phys.nuclear", "Nuclear experiment & applications", [
        r"nuclear (?:experiments?|instrumentation|techniques?|applications?|medicine|reactors?|energy|waste|safety|security|forensics?|chemistry|analytical|methods)",
        r"gamma[- ]ray spectroscopy", r"accelerator mass spectrometry", r"ion[- ]beam (?:analysis|techniques?|applications?|modification)", r"radiochemistry",
        r"radiation (?:physics|effects|damage|protection|detection)", r"radioactivity", r"fusion reactions?", r"reactor physics", r"neutron (?:sources?|scattering|activation|imaging|beams?)",
        r"spallation", r"nuclear (?:fuel|engineering)", r"transmutation", r"isotope (?:applications|production)"]),

    # ── Quantum physics ────────────────────────────────────────────────────────
    "phys.quantum.info": ("phys.quantum", "Quantum information & computation", [
        r"quantum (?:information|computing|computation|algorithms?|complexity|communication|cryptography|key distribution|networks?|error[- ]correct\w+|codes?|channels?|resource theor\w+|supremacy|advantage|entanglement|machine learning|circuits?|walks?|protocols?|speed[- ]?up|software|programming|compil\w+|verification|learning theory|Shannon|data|states?|private)",
        r"entanglement (?:entropy|measures?|theory|witnesses?|and|in)", r"qubits?", r"CS:QKD", r"tensor networks?", r"CS:NISQ", r"fault[- ]tolerant", r"error[- ]correcting",
        r"quantum (?:and|&) classical (?:complexity|computation)", r"quantum (?:cryptography|simulation|algorithms?) (?:and|&)", r"Hamiltonian (?:simulation|complexity)", r"quantum information (?:and|&)",
        r"stabili[sz]er (?:codes?|formalism|states?)", r"CS:QMA", r"CS:BQP", r"magic states?", r"quantum (?:cloud|computers?)"]),
    "phys.quantum.foundations": ("phys.quantum", "Quantum foundations", [
        r"foundations of quantum (?:mechanics|theory|physics)", r"quantum foundations", r"bell (?:nonlocality|inequalit\w+|tests?|theorem|experiments?|scenarios?)",
        r"measurement problem", r"interpretations? of quantum", r"many[- ]worlds", r"bohmian", r"pilot[- ]wave", r"contextuality", r"collapse models?", r"quantum reality",
        r"wigner'?s friend", r"CS:QBism", r"schr(?:ö|o)dinger'?s cat", r"nonlocality", r"quantum (?:measurement|causality|reference frames?|logic|time|theory of measurement)",
        r"causal (?:structure|inference|models?) (?:and|in) quantum", r"indefinite causal", r"time in quantum", r"quantum paradoxes?", r"decoherence (?:and|&) (?:measurement|the measurement)",
        r"philosophy of quantum", r"retrocausal\w*"]),
    "phys.quantum.open": ("phys.quantum", "Open quantum systems & quantum thermodynamics", [
        r"open quantum (?:systems?|dynamics|many-body)", r"lindblad\w*", r"decoheren\w+", r"quantum thermodynamics", r"quantum (?:heat engines?|thermal machines?|batteries|refrigerators?|work)",
        r"non-?markovian", r"dissipative (?:quantum|dynamics|phase|systems?)", r"quantum (?:trajectories|jumps)", r"quantum master equations?", r"system[- ]bath",
        r"quantum Brownian", r"thermali[sz]ation (?:in|of) (?:closed )?quantum", r"eigenstate thermali[sz]ation", r"CS:ETH", r"quantum fluctuation (?:theorems?|relations?)",
        r"quantum (?:stochastic|many-body) (?:dynamics|thermodynamics)", r"Floquet", r"quantum (?:chaos|ergodicity|scars)", r"Krylov complexity",
        r"out[- ]of[- ]equilibrium quantum", r"non-?equilibrium quantum", r"quantum quench\w*"]),
    "phys.quantum.tech": ("phys.quantum", "Quantum technologies, sensing & devices", [
        r"quantum (?:technolog\w+|sensing|sensors?|metrology|devices?|memor\w+|simulators?|hardware|photonics|engineering|optomechanics|materials|networks?|internet|dots?|transducers?|clocks?|imaging|radar|magnetometr\w+|gravimet\w+|annealing)",
        r"superconducting (?:qubits?|circuits?|quantum)", r"circuit QED", r"trapped[- ]ions?", r"rydberg (?:atoms?|arrays?|states?|quantum)", r"NV[- ]cent(?:er|re)s?", r"nitrogen[- ]vacancy",
        r"spin[- ]qubits?", r"photonic quantum", r"quantum (?:technologies) (?:and|&)", r"transmon", r"flux qubits?", r"Josephson (?:junctions?|parametric|devices?)", r"CS:SQUIDs?",
        r"single[- ]photon (?:sources?|detectors?)", r"quantum emitters?", r"silicon (?:qubits?|quantum)", r"topological qubits?", r"cryogenic (?:electronics|quantum)", r"quantum (?:control|state engineering)",
        r"entanglement (?:distribution|swapping)", r"quantum repeaters?", r"quantum (?:enhanced|advantage in) (?:sensing|metrology)"]),

    # ── Atomic, molecular & optical physics ────────────────────────────────────
    "phys.amo.cold": ("phys.amo", "Ultracold atoms & quantum gases", [
        r"ultra-?cold (?:atoms?|molecules?|gases|quantum gases|fermions?|bosons?|matter|neutral|atomic)", r"cold[- ]atoms?(?: (?:physics|experiments?|simulators?|quantum|systems?))?",
        r"bose[- ]einstein condensat\w+", r"CS:BECs?", r"optical lattices", r"degenerate (?:fermi|quantum) gases", r"quantum gases", r"atom (?:optics|interferometr\w+|chips?|lasers?)",
        r"laser cooling", r"magneto-?optical traps?", r"feshbach", r"cold molecules?", r"dipolar (?:gases|quantum|atoms|molecules)", r"quantum degenerate", r"superfluid (?:helium|fermi|gases)",
        r"Rydberg (?:atoms?|physics)", r"atomic (?:Bose|Fermi)", r"cold atom quantum simulat\w+", r"quantum simulators? with (?:atoms|ions)", r"trapped (?:atoms|gases)", r"bose gas"]),
    "phys.amo.atomic": ("phys.amo", "Atomic & molecular physics, precision measurement", [
        r"atomic (?:physics|structure|collisions?|spectroscopy|and molecular|, molecular|clocks?|processes|theory|data|transitions?)", r"molecular (?:physics|spectroscopy|dynamics|collisions?|beams?|ions?|clocks?)",
        r"CS:AMO", r"atomic,? molecular,? (?:and|&) optical", r"optical clocks?", r"precision (?:spectroscopy|metrology|measurements?|tests?|physics)", r"frequency (?:combs?|standards?|metrology)",
        r"time (?:and|&) frequency", r"atom[- ]ion", r"ion traps?", r"electron (?:EDM|electric dipole)", r"fundamental constants", r"highly charged ions", r"positronium", r"antihydrogen",
        r"antimatter", r"atomic clocks? (?:and|&)", r"clock comparisons?", r"variation of fundamental", r"molecular (?:structure|spectra)", r"collision (?:physics|dynamics|processes)",
        r"electron[- ]impact", r"photo-?ionization", r"photo-?dissociation", r"spectroscopy of (?:atoms|molecules|ions)", r"atomic (?:and|&) (?:nuclear|plasma)", r"interatomic"]),
    "phys.amo.qoptics": ("phys.amo", "Quantum optics", [
        r"quantum optics", r"cavity (?:QED|optomechanics|quantum electrodynamics)", r"optomechanic\w+", r"squeezed (?:light|states?|vacuum)", r"single[- ]photons?",
        r"entangled photons?", r"quantum light", r"fock states?", r"photon (?:statistics|blockade|pairs?|number)", r"cavity (?:photons?|quantum)", r"quantum (?:electrodynamics|nonlinear optics)",
        r"spontaneous parametric", r"CS:SPDC", r"quantum (?:coherence|interference)", r"hong-ou-mandel", r"boson sampling", r"coherent (?:states?|control)", r"light[- ]matter (?:interaction|coupling)",
        r"polaritons?", r"strong coupling (?:cavity|light)", r"waveguide QED", r"giant atoms"]),
    "phys.amo.photonics": ("phys.amo", "Photonics, nonlinear optics & metamaterials", [
        r"photonic\w*", r"integrated (?:photonics|optics)", r"silicon photonics", r"nonlinear optic\w+", r"optical (?:fibers?|fibres?|communications?|devices?|sensors?|materials?|coherence|metrology|trapping|tweezers?|physics|engineering|sciences?|imaging|networks?|waveguides?|resonators?|microscopy)",
        r"optics (?:and|&) photonics", r"fib(?:er|re) (?:lasers?|optics|sensors?)", r"plasmonic\w*", r"metamaterials?", r"metasurfaces?", r"nano-?photonic\w*", r"topological photonics",
        r"biophotonics", r"biomedical optics", r"optical (?:and|&) (?:photonic|quantum)", r"CS:OSA", r"CS:SPIE", r"CS:CLEO", r"optics (?:20\d\d|conference|symposium|workshop|school)", r"holography (?:and|&) imaging",
        r"photonic (?:crystals?|integrated|devices?|materials?|circuits?)", r"light[- ]matter", r"liquid crystal (?:optics|photonics)", r"microresonators?", r"optical (?:computing|neural)"]),
    "phys.amo.ultrafast": ("phys.amo", "Lasers & ultrafast science", [
        r"ultra-?fast (?:optics|lasers?|phenomena|dynamics|science|spectroscopy|processes|electron|imaging|physics)", r"femtosecond", r"attosecond", r"high[- ]harmonic generation",
        r"terahertz", r"THz", r"laser (?:physics|science|technology|systems?|spectroscopy|matter interactions?|ablation|processing|applications|materials)", r"intense (?:laser|fields?)", r"strong[- ]field",
        r"extreme (?:ultraviolet|light)", r"CS:XUV", r"x-?ray (?:lasers?|free[- ]electron|pulses?)", r"pump[- ]probe", r"time[- ]resolved (?:spectroscopy|measurements?|dynamics)", r"lasers? (?:and|&) (?:optics|photonics)",
        r"high[- ]power lasers?", r"ultrashort", r"mode[- ]locked", r"optical frequency", r"laser[- ]induced"]),

    # ── Condensed matter ───────────────────────────────────────────────────────
    "phys.condmat.correlated": ("phys.condmat", "Strongly correlated systems & superconductivity", [
        r"(?:strongly|highly) correlated", r"correlated (?:electrons?|systems?|materials?|matter|quantum|oxides?|metals?)", r"high[- ](?:Tc|temperature) superconduct\w+",
        r"(?:unconventional|topological|iron-based|nickelate|cuprate|heavy[- ]fermion) superconduct\w+", r"hubbard", r"mott", r"heavy[- ]fermions?", r"cuprates?", r"iron[- ]based", r"nickelates?",
        r"kondo", r"quantum critical\w*", r"non-?fermi liquids?", r"strange metals?", r"charge[- ]density waves?", r"pair(?:ing|ed) (?:symmetry|states?|mechanisms?)", r"superfluid\w*", r"kagome",
        r"density waves?", r"superconduct\w+", r"fermi liquids?", r"electron[- ]phonon", r"electronic (?:correlations?|phases?)", r"quantum (?:materials|phases)", r"CS:DMFT", r"dynamical mean[- ]field",
        r"doped (?:Mott|insulators?)", r"stripe (?:order|phases?)", r"pseudo-?gap", r"BCS", r"CS:BCS-BEC"]),
    "phys.condmat.topological": ("phys.condmat", "Topological matter", [
        r"topological (?:insulators?|semimetals?|superconductors?|phases?|matter|order|materials?|quantum matter|bands?|states?|photonics|phase transitions?|quantum|metals?|physics|crystalline|invariants?|defects?)",
        r"quantum hall", r"fractional quantum hall", r"majorana", r"weyl (?:semimetals?|fermions?|points?|physics)", r"dirac (?:semimetals?|materials?|fermions?|cones?)", r"anyons?", r"non-?abelian (?:anyons?|statistics|states?)",
        r"berry (?:phase|curvature|connection)", r"chern (?:insulators?|numbers?|bands?)", r"fractional chern", r"skyrmions?", r"topological (?:and|&) (?:correlated|quantum)",
        r"bulk[- ]boundary", r"edge (?:states?|modes?)", r"anomalous hall", r"spin hall", r"quantum spin hall", r"higher[- ]order topological", r"topological (?:mechanics|acoustics|circuits?)", r"fractionali[sz]ation",
        r"symmetry[- ]protected topological", r"CS:SPT", r"band topology", r"non-?hermitian (?:topology|physics|systems)", r"parity[- ]time"]),
    "phys.condmat.magnetism": ("phys.condmat", "Magnetism & spin systems", [
        r"(?:quantum|frustrated|itinerant|molecular|low-dimensional|anti-?ferro|ferro|ferri)-?magnet\w*", r"spin (?:liquids?|ice|glass\w*|chains?|waves?|systems?|dynamics|textures?|transport|orbit|current|pumping|torque|ladders?|models?|Hall)",
        r"magnons?", r"magnetic (?:materials?|order|frustration|skyrmions?|domain\w*|properties|thin films?|oxides?|semiconductors?|anisotropy|resonance|nanostructures?|memor\w+|fields? (?:and|in)|insulators?|phases?|excitations?|dynamics)",
        r"multiferroics?", r"ferromagnet\w*", r"antiferromagnet\w*", r"spintronics?", r"spin[- ]orbit", r"ferroelectric\w*", r"quantum spin", r"altermagnet\w*", r"spin[- ]caloritronics?", r"spin valves?",
        r"magnetoresistance", r"magneto-?optic\w*", r"magnetism (?:and|&)", r"magnetic (?:and|&) (?:electronic|superconducting)", r"CS:MMM", r"ferroics?", r"Heisenberg (?:model|magnets?)",
        r"exchange (?:interactions?|bias|coupling)", r"Dzyaloshinskii"]),
    "phys.condmat.lowdim": ("phys.condmat", "2D materials & low-dimensional systems", [
        r"graphene", r"two[- ]dimensional (?:materials?|electron(?:ic)? systems?|systems?|crystals?|semiconductors?|magnets?|superconductors?)", r"2D (?:materials?|systems?|electron|crystals?|magnets?|semiconductors?|heterostructures?|van der waals)",
        r"van der waals (?:materials?|heterostructures?|magnets?|crystals?)", r"moir(?:é|e)", r"twisted (?:bilayer|graphene|moir(?:é|e)|double|trilayer|materials?)", r"transition[- ]metal dichalcogenides?", r"CS:TMDCs?", r"CS:TMDs",
        r"monolayers?", r"bilayers?", r"mxenes?", r"nano-?tubes?", r"excitons?", r"atomically thin", r"heterostructures?", r"quantum wells?", r"quantum wires?", r"one[- ]dimensional (?:systems?|conductors?|quantum)",
        r"Luttinger liquids?", r"phosphorene", r"silicene", r"borophene", r"flat bands?", r"magic[- ]angle", r"layered (?:materials?|compounds?|crystals?)", r"low[- ]dimensional (?:systems?|materials?|physics|magnets?)"]),
    "phys.condmat.computational": ("phys.condmat", "Electronic structure & computational materials physics", [
        r"density functional theory", r"CS:DFT", r"electronic structure", r"first[- ]principles", r"ab[- ]initio (?:calculations?|simulations?|molecular dynamics|materials|methods|studies)", r"molecular dynamics",
        r"quantum monte carlo", r"tight[- ]binding", r"computational (?:condensed matter|materials?|physics|chemistry|science|methods)", r"materials? (?:modell?ing|simulations?|informatics|discovery|design|by design|theory|genome|screening)",
        r"machine[- ]learning (?:potentials?|force fields?|interatomic|for materials|in materials)", r"many-body perturbation theory", r"GW approximation", r"wannier", r"phonons?", r"lattice dynamics", r"CS:DMRG", r"density matrix renormali[sz]ation", r"exact diagonali[sz]ation", r"variational monte carlo", r"neural[- ]network (?:quantum states?|wave ?functions?)",
        r"time[- ]dependent density", r"CS:TDDFT", r"hybrid functionals?", r"(?:crystal|structure) prediction", r"Car-Parrinello", r"quantum chemistry (?:and|&) materials"]),
    "phys.condmat.soft": ("phys.condmat", "Soft matter & polymers", [
        r"soft (?:matter|condensed matter|materials?)", r"complex fluids?", r"polymers?", r"polymer (?:physics|science|dynamics|melts?|solutions?|networks?|brushes|gels?)", r"colloid\w*", r"liquid crystals?",
        r"gels?", r"granular (?:matter|media|materials?|flows?|physics)", r"glass transition", r"glassy (?:dynamics|systems?|materials?|liquids?|states?)", r"jamming", r"foams?", r"emulsions?",
        r"surfactants?", r"self-?assembl\w+", r"rheology", r"viscoelastic\w*", r"wetting", r"microfluidic\w*", r"capillar\w+", r"elastic(?:ity)? (?:of|in) soft", r"amorphous (?:solids?|materials?)",
        r"disordered (?:solids?|materials?|media)", r"biopolymers?", r"DNA (?:origami|nanotechnology)", r"complex (?:media|materials)", r"soft (?:and|&) biological", r"mechanical metamaterials?",
        r"nematics?", r"smectics?", r"cholesteric"]),
    "phys.condmat.active": ("phys.condmat", "Active matter & biological physics", [
        r"active (?:matter|fluids?|particles?|systems?|nematics?|gels?|turbulence|colloids?|Brownian)", r"self-propelled", r"swimmers?", r"flocking", r"collective (?:motion|behaviou?r|dynamics|cell)", r"motility",
        r"bacterial (?:suspensions?|turbulence|colonies|swimming|motility)", r"biological physics", r"biophysics", r"cell (?:mechanics|migration|motility|biophysics)", r"cytoskeleton", r"living (?:matter|systems?)",
        r"statistical physics of (?:living|biological|life)", r"protein (?:folding|dynamics|physics|aggregation|structure)", r"DNA (?:mechanics|physics|dynamics)", r"single[- ]molecule", r"morphogenesis",
        r"tissue (?:mechanics|dynamics|physics)", r"physics of (?:life|living|biology)", r"molecular motors?", r"membrane (?:biophysics|proteins?|dynamics)", r"biological (?:networks?|matter|membranes?|systems? physics|fluids?)",
        r"chromatin", r"phase separation (?:in|of) (?:cells|biological)", r"biomolecular condensates?"]),
    "phys.condmat.stat": ("phys.condmat", "Statistical mechanics & phase transitions", [
        r"statistical (?:mechanics|physics|field theor\w+)", r"phase transitions?", r"renormali[sz]ation group", r"universality class\w*",
        r"disordered systems?", r"spin glass\w*", r"ising", r"potts", r"percolation", r"large deviations?", r"fluctuation (?:theorems?|relations?|theory)", r"quantum (?:phase transitions?|criticality|critical)", r"lattice (?:models?|gases|systems?)", r"equilibrium (?:statistical|phases?)", r"order[- ]disorder", r"mean[- ]field (?:theory|models?|approach)", r"CS:RG", r"thermodynamic limit", r"gibbs", r"information (?:and|&) statistical", r"coarsening", r"boltzmann (?:equation|statistics)",
        r"random (?:field|bond|energy) models?", r"replica", r"complexity (?:landscapes?|of energy)", r"disordered (?:and|&) (?:complex|glassy)"]),
    "phys.condmat.noneq": ("phys.condmat", "Non-equilibrium & stochastic thermodynamics", [
        r"non-?equilibrium (?:statistical|dynamics|steady states?|phase|physics|systems?|processes|fluctuations?|transitions?)", r"stochastic thermodynamics", r"driven[- ]dissipative",
        r"langevin", r"fokker-planck", r"anomalous diffusion", r"first[- ]passage", r"reaction[- ]diffusion", r"CS:KPZ", r"kardar", r"stochastic (?:processes|dynamics|resetting|models?) (?:in|of) physics", r"resetting",
        r"hydrodynamics (?:of|and) (?:interacting|many-body|quantum)", r"generali[sz]ed hydrodynamics", r"thermal transport", r"heat (?:transport|conduction|engines?|flow)", r"fluctuating hydrodynamics",
        r"many[- ]body localization", r"(?:anderson|many-body|quantum|weak|strong) localization", r"ergodicity breaking", r"thermali[sz]ation", r"out[- ]of[- ]equilibrium",
        r"exclusion process", r"brownian (?:motion|particles?|dynamics)", r"stochastic (?:thermodynamics|heat)", r"information (?:thermodynamics|engines?)", r"maxwell'?s demon", r"Landauer"]),
    "phys.condmat.meso": ("phys.condmat", "Mesoscopic & quantum transport", [
        r"mesoscopic", r"nanoscale (?:transport|physics|electronics)", r"quantum transport", r"quantum dots?", r"single[- ]electron", r"coulomb blockade", r"josephson", r"quantum point contacts?",
        r"molecular (?:electronics|junctions?)", r"thermoelectric\w*", r"electron (?:transport|interferometr\w+|optics)", r"quantum (?:interference|coherence) (?:in|of) (?:electrons|conductors?)",
        r"weak localization", r"universal conductance", r"Andreev", r"proximity effect", r"nano-?(?:wires?|devices?|electronics|mechanical|junctions?)", r"hybrid (?:superconductor|semiconductor|devices?)",
        r"charge (?:transport|pumping|noise|sensing)", r"shot noise", r"noise (?:in|and) (?:electronic|quantum|mesoscopic)", r"nanoscale (?:devices?|junctions?)", r"quantum (?:rings?|wires?|Hall (?:devices?|effect in))"]),

    # ── Materials, devices & instrumentation ───────────────────────────────────
    "phys.applied.semi": ("phys.applied", "Semiconductor physics & devices", [
        r"semiconductors?", r"semiconductor (?:physics|devices?|materials?|heterostructures?|nanostructures?|lasers?|technolog\w+|optics|processing|fabrication|industry|manufacturing)",
        r"(?:thin[- ]film )?transistors?", r"oxide (?:electronics|interfaces?|semiconductors?|heterostructures?)", r"wide[- ]band-?gap", r"GaN", r"gallium nitride", r"silicon carbide", r"CS:SiC",
        r"perovskites?", r"quantum wells?", r"heterojunctions?", r"opto-?electronic\w*", r"CS:LEDs?", r"light[- ]emitting", r"photodetectors?", r"micro-?electronics", r"memristors?", r"neuromorphic (?:devices?|hardware|computing|materials)",
        r"ferroelectric (?:memor\w+|devices?|transistors?|thin)", r"devices? physics", r"CS:MOSFETs?", r"nano-?electronics", r"flexible electronics", r"organic (?:electronics|semiconductors?|photovoltaics|LEDs?)", r"III-V", r"compound semiconductors?"]),
    "phys.applied.energy": ("phys.applied", "Energy materials & devices", [
        r"photovoltaic\w*", r"solar (?:cells?|energy|materials?|fuels?|photovoltaics|power|panels?|thermal|harvesting|conversion)", r"batter(?:y|ies)", r"energy (?:storage|materials?|harvesting|conversion|devices?|technolog\w+|science|systems?|research|transition|and environment)",
        r"supercapacitors?", r"fuel cells?", r"thermoelectrics?", r"hydrogen (?:storage|production|energy|economy)", r"photo-?catalysis", r"electro-?catalysis", r"sustainable (?:energy|materials?|technolog\w+)",
        r"renewable energy", r"clean energy", r"energy (?:efficiency|harvesters?)", r"energy (?:and|&) (?:sustainability|climate)"]),
    "phys.applied.nano": ("phys.applied", "Nanoscience, thin films & surfaces", [
        r"nano-?science", r"nano-?technolog\w+", r"nano-?materials?", r"nano-?(?:structures?|particles?|wires?|tubes?|crystals?|scale|devices?|electronics|mechanics|composites?|fabrication|lithography|medicine|sensors?|engineering|biotechnology|photonics)",
        r"nanoscale", r"thin[- ]films?", r"surface (?:science|physics|chemistry|engineering|states?|analysis|phenomena)", r"interfaces?(?: (?:and|&) surfaces?)", r"scanning (?:probe|tunn?elling|electron) (?:microscop\w+|spectroscop\w+)",
        r"CS:STM", r"CS:AFM", r"atomic force", r"epita\w+", r"molecular beam epitaxy", r"CS:MBE", r"chemical vapou?r deposition", r"CS:CVD", r"sputtering", r"thin film (?:deposition|growth|technology|devices?|physics)",
        r"lithography", r"atomic layer deposition", r"CS:ALD", r"functionali[sz]ed? (?:surfaces?|nanomaterials)", r"quantum dots? (?:and|&) nano", r"nano (?:and|&) (?:micro|bio)", r"micro[- ]?(?:and|&)? ?nano",
        r"self-assembled (?:monolayers?|nano)", r"plasmonic nano", r"nanofabrication", r"pulsed laser deposition", r"CS:PLD", r"2D (?:and|&) nano", r"carbon (?:nanotubes?|nanostructures?|materials?|dots?)", r"fullerenes?"]),
    "phys.applied.materials": ("phys.applied", "Materials research & characterisation", [
        r"materials? (?:science|physics|research|characteri[sz]ation|engineering|chemistry|modell?ing|processing|synthesis|properties|technology|testing|for)", r"advanced materials?", r"functional materials?", r"quantum materials?",
        r"crystal (?:growth|structure|physics|chemistry|engineering)", r"crystallograph\w+", r"x-?ray (?:diffraction|scattering|spectroscopy|absorption|imaging|crystallography|photoelectron|fluorescence|techniques|physics|science)",
        r"neutron (?:scattering|diffraction|sources?|spectroscopy|imaging|techniques|science)", r"synchrotron (?:radiation|light|facilit\w+|techniques|science|applications?|beamlines?)", r"synchrotrons?",
        r"(?:electron|transmission|scanning|cryo) (?:electron )?microscopy", r"cryo-?EM", r"spectroscop\w+ (?:techniques|methods|and imaging)", r"raman", r"photoemission", r"CS:ARPES", r"muon spin", r"magnetometry",
        r"high[- ]pressure (?:physics|science|research|studies)", r"superconducting materials?", r"ceramics?", r"alloys?", r"metals? (?:and|&) alloys", r"glass (?:materials?|science)", r"composites?", r"biomaterials?",
        r"polymers? (?:science|materials)", r"thermal (?:properties|analysis|transport in materials)", r"mechanical (?:properties|behaviou?r|testing)", r"fracture", r"corrosion", r"tribology", r"additive manufacturing", r"3D printing",
        r"metallurgy", r"powder (?:diffraction|metallurgy)", r"characteri[sz]ation (?:techniques|methods|of)", r"materials? (?:and|&) (?:devices?|interfaces?|processes)", r"solid[- ]state (?:physics|chemistry|science|materials)",
        r"inorganic (?:materials?|solids?)", r"crystal engineering", r"amorphous", r"phase (?:diagrams?|stability|transformations?)", r"grain boundar\w+", r"defects? (?:in|and) (?:solids?|crystals?|materials?)", r"dielectrics?", r"piezoelectric\w*"]),
    "phys.applied.instr": ("phys.applied", "Instrumentation, sensors & metrology", [
        r"instrumentation", r"sensing (?:technolog\w+|applications?)", r"metrology", r"spectrometers?", r"detectors? (?:and|&) (?:sensors?|instrumentation)",
        r"instruments? (?:and|&) (?:methods|techniques|measurements?)", r"cryogenic (?:techniques|engineering|systems)", r"vacuum (?:science|technology|physics)", r"signal (?:acquisition|conditioning)",
        r"imaging (?:techniques|systems|physics|technolog\w+|methods)", r"microscopy (?:techniques|and imaging)", r"data acquisition", r"experimental (?:techniques|methods|physics|setups?)", r"laboratory (?:physics|techniques)", r"low[- ]temperature (?:physics|techniques|measurements)",
        r"cryostats?", r"magnetic (?:field )?(?:sensors?|measurements?)", r"optical (?:instruments?|instrumentation)", r"telescope (?:instrumentation|optics)", r"adaptive optics", r"interferometers?", r"photon (?:counting|detection)"]),
    "phys.applied.medical": ("phys.applied", "Medical & radiation physics", [
        r"medical (?:physics|imaging|instrumentation|devices?|technology|radiation|applications? of)", r"radio-?therapy", r"radiation (?:therapy|oncology|dosimetry|safety|biology|protection)", r"dosimetry", r"nuclear medicine", r"CS:MRI",
        r"ultrasound", r"biomedical (?:optics|physics|imaging|engineering|applications?|instrumentation|devices?|sciences?)", r"health physics", r"tomography", r"CS:PET", r"CS:SPECT", r"X-ray imaging", r"proton (?:therapy|beams? therapy)", r"hadron therapy",
        r"ion[- ]beam therapy", r"brachytherapy", r"diagnostic (?:imaging|radiology)", r"radiology", r"radiopharmaceutic\w+", r"medical (?:and|&) (?:biological|health) physics", r"CS:AAPM", r"CS:IOMP", r"clinical (?:physics|applications?|dosimetry)", r"imaging (?:in|for) (?:medicine|healthcare|biology)",
        r"optical coherence tomography", r"CS:OCT", r"photoacoustic", r"neuro-?imaging", r"biosensors?", r"lab[- ]on[- ]a[- ]chip", r"point[- ]of[- ]care"]),
    "phys.applied.mech": ("phys.applied", "Acoustics, vibration & mechanics", [
        r"acoustic\w*", r"vibrations?", r"phononic\w*", r"ultrasonic\w*", r"sound (?:waves?|propagation|and vibration|fields?)", r"wave (?:propagation|physics|mechanics|phenomena)", r"classical mechanics", r"nonlinear waves?", r"elasticity", r"solid mechanics", r"structural (?:dynamics|health|mechanics|vibration)", r"seismic (?:waves|isolation|metamaterials)",
        r"underwater acoustics", r"musical acoustics", r"architectural acoustics", r"psychoacoustics", r"waves? in (?:solids|elastic|media)", r"rigid[- ]body", r"lagrangian (?:and|&) hamiltonian (?:mechanics|dynamics)",
        r"analytical mechanics", r"mechanics (?:of|and) (?:solids|materials|structures)", r"celestial mechanics", r"orbital (?:mechanics|dynamics)"]),

    # ── Fluids, plasma & climate ───────────────────────────────────────────────
    "phys.fluids.fluids": ("phys.fluids", "Fluid dynamics", [
        r"fluid (?:dynamics|mechanics|flows?|physics|structure interaction|instabilit\w+)", r"CS:CFD", r"computational fluid", r"hydrodynamic\w*", r"multi-?phase (?:flows?|fluids?)", r"boundary layers?", r"viscous (?:flows?|fluids?)",
        r"vortex|vortices|vorticity", r"flow (?:instabilit\w+|control|physics|visuali[sz]ation|stability)", r"free[- ]surface", r"stratified (?:flows?|fluids?|turbulence)", r"rotating (?:flows?|fluids?|convection)", r"aerodynamics", r"hydrodynamic stability",
        r"lattice boltzmann", r"combustion", r"reacting flows?", r"fluid[- ]structure", r"convection", r"rayleigh-b(?:é|e)nard", r"rayleigh-taylor", r"thermal convection", r"bubbles?", r"sprays?", r"jets? (?:and|&) wakes?",
        r"flows? (?:in|through) (?:porous|channels?|pipes?)", r"porous media", r"gravity currents?", r"shock waves?", r"compressible (?:flows?|fluids?)", r"gas dynamics", r"rarefied (?:gas|flows?)", r"hydromagnetic", r"flows? (?:in|of) (?:fluids|liquids?)", r"liquid (?:metals?|helium|jets?|films?)", r"interfacial (?:flows?|dynamics|phenomena)", r"Marangoni", r"CS:ICTAM"]),
    "phys.fluids.turbulence": ("phys.fluids", "Turbulence", [
        r"turbulen\w+", r"kolmogorov", r"intermittency", r"energy cascades?", r"reynolds (?:number|stress|averaged)", r"large[- ]eddy", r"CS:LES", r"CS:DNS", r"shear flows?", r"wall[- ]bounded", r"passive scalars?", r"scalar mixing",
        r"homogeneous (?:isotropic )?turbulence", r"two-dimensional turbulence", r"quantum turbulence", r"wave turbulence", r"magnetohydrodynamic turbulence", r"transition to turbulence", r"inertial range", r"structure functions?",
        r"lagrangian (?:turbulence|statistics|tracers?)", r"particle[- ]laden", r"turbulent (?:flows?|transport|mixing|convection|combustion|boundary)", r"eddy", r"CS:RANS", r"closure (?:models?|problem)"]),
    "phys.fluids.plasma": ("phys.fluids", "Plasma physics", [
        r"plasma\w*", r"magneto-?hydrodynamic\w*", r"CS:MHD", r"dusty plasmas?", r"laser[- ]plasma", r"plasma (?:physics|astrophysics|turbulence|instabilit\w+|waves?|processes|science|simulations?|technolog\w+|applications?|sources?|diagnostics|etching|medicine|propulsion|chemistry)",
        r"vlasov", r"kinetic plasma", r"gyro-?kinetic\w*", r"alfv(?:é|e)n", r"magnetic reconnection", r"dynamo", r"space plasmas?", r"solar wind", r"magnetospher\w+", r"ionospher\w+", r"space weather", r"heliospher\w+", r"particle[- ]in[- ]cell", r"CS:PIC",
        r"low[- ]temperature plasma", r"atmospheric[- ]pressure plasma", r"non-?thermal plasma", r"plasma (?:and|&) (?:fusion|astro)", r"astrophysical plasmas?", r"relativistic plasmas?", r"collisionless", r"shocks? (?:in|and) plasma", r"magnetized plasma", r"ion (?:and|&) electron"]),
    "phys.fluids.fusion": ("phys.fluids", "Fusion energy & confinement", [
        r"fusion (?:energy|plasmas?|research|reactors?|science|devices?|power|technology|experiments?|materials?)", r"controlled fusion", r"inertial (?:confinement )?fusion", r"CS:ITER", r"magnetic confinement", r"CS:ICF", r"burning plasmas?", r"plasma[- ]facing",
        r"divertors?", r"tokamaks?", r"stellarators?", r"CS:DEMO", r"neutron (?:wall loads?|irradiation)", r"CS:MCF", r"tritium", r"deuterium", r"compact fusion", r"z-?pinch", r"laser fusion", r"CS:NIF", r"plasma confinement", r"transport in (?:tokamaks?|fusion)", r"edge (?:plasma|localized modes?)", r"CS:ELMs?", r"disruptions?"]),
    "phys.fluids.climate": ("phys.fluids", "Climate, atmosphere & ocean physics", [
        r"climate (?:dynamics|science|physics|change|model\w*|variability|system|sensitivity|prediction|projections?|impacts?|extremes?|risk|adaptation|and weather)", r"atmospheric (?:physics|science|dynamics|chemistry|boundary layer|aerosols?|model\w*|processes|electricity|waves?|convection|radiation|turbulence|general circulation)",
        r"ocean\w*", r"monsoons?", r"weather (?:prediction|forecasting|and climate|extremes?)", r"geophysical fluid dynamics", r"CS:GFD", r"cryosphere", r"glaciers?", r"sea[- ]ice", r"remote sensing", r"earth system", r"numerical weather", r"paleo-?climat\w+",
        r"cloud (?:physics|microphysics|dynamics|processes)", r"aerosols?", r"precipitation", r"tropical (?:cyclones?|meteorology|dynamics)", r"mesoscale", r"meteorolog\w+", r"hydrometeor\w+", r"radiative (?:transfer|forcing)", r"greenhouse", r"El Ni(?:ñ|n)o", r"CS:ENSO", r"ocean[- ]atmosphere",
        r"land[- ]atmosphere", r"carbon cycle", r"global (?:warming|change)", r"regional climate", r"climate (?:modelling|data)", r"tropospher\w+", r"stratospher\w+", r"middle atmosphere", r"upper atmosphere", r"air (?:quality|pollution)", r"atmospheric (?:and|&) (?:ocean\w*|space)"]),
    "phys.fluids.earth": ("phys.fluids", "Geophysics & solid-earth physics", [
        r"geophysic\w+", r"seismolog\w+", r"earthquakes?", r"tectonic\w*", r"geodynamic\w*", r"geodesy", r"hydrolog\w+", r"tsunamis?", r"volcan\w+", r"mantle (?:convection|dynamics)", r"geomagnet\w+", r"paleomagnet\w+", r"gravity (?:and|&) magnetic (?:fields?|methods)",
        r"solid[- ]earth", r"earth (?:interior|sciences?|structure|physics|observation|and planetary|surface processes?)", r"planetary (?:interiors?|geophysics|science)", r"geo-?sciences?", r"exploration geophysics", r"crustal", r"lithosphere", r"reservoir (?:physics|characteri[sz]ation)",
        r"groundwater", r"geo-?mechanics?", r"rock (?:physics|mechanics)", r"fault (?:mechanics|zones?|slip)", r"seismic (?:hazard|imaging|tomography|data|waves?|analysis|monitoring|sources?)", r"CS:GPS", r"gnss", r"satellite (?:geodesy|gravimetry)", r"glaciology", r"CS:AGU", r"CS:EGU"]),

    # ── Nonlinear dynamics & complex systems ───────────────────────────────────
    "phys.complex.nonlinear": ("phys.complex", "Nonlinear dynamics & chaos", [
        r"nonlinear (?:dynamics|science|physics|phenomena|systems?|oscillat\w+|waves?|dynamical|processes)", r"chaos", r"chaotic", r"bifurcations?", r"synchroni[sz]ation", r"attractors?", r"lyapunov", r"limit cycles?", r"pattern formation", r"excitable",
        r"coupled oscillators?", r"time[- ]series (?:analysis|and)", r"strange attractors?", r"reservoir computing", r"nonlinear (?:and|&) (?:complex|statistical)", r"dynamics (?:of|in) (?:complex|nonlinear)", r"spatio-?temporal (?:chaos|patterns?|dynamics)", r"turing patterns?",
        r"breathers?", r"chimera states?", r"delay (?:systems?|dynamics|differential)", r"noise[- ]induced", r"stochastic resonance", r"tipping points?", r"critical transitions?", r"early warning (?:signals?|indicators?)", r"multistability", r"hysteresis", r"intermittency", r"Hamiltonian chaos",
        r"quantum chaos", r"dynamical systems (?:in|and) physics", r"nonlinear (?:optics|lattices|Schr(?:ö|o)dinger)", r"solitons? (?:and|&)"]),
    "phys.complex.networks": ("phys.complex", "Complex systems & network science", [
        r"complex (?:systems?|networks?|adaptive|dynamics|phenomena|matter|and|systems science)", r"network (?:science|theory|dynamics|physics|geometry|resilience|robustness|controllability)", r"small[- ]world", r"scale[- ]free", r"temporal networks?",
        r"multi-?layer networks?", r"higher[- ]order (?:networks?|interactions?)", r"hypergraphs? (?:and|in) (?:physics|dynamics)", r"percolation (?:on|in) networks?", r"cascading failures?", r"network (?:medicine|neuroscience|biology|ecology)", r"self-?organi[sz]ed criticality", r"emergent (?:phenomena|behaviou?r|properties)", r"neural networks? (?:and|&) (?:physics|dynamics)", r"physics of (?:learning|computation|information)",
        r"statistical physics of (?:information|learning|complex|networks?|computation|inference)", r"information (?:physics|theory (?:and|&) (?:physics|complexity))", r"entropy (?:in|of) (?:complex|networks?)", r"complex (?:systems|network) (?:school|conference|workshop)", r"network\w* (?:epidemics|spreading)"]),
    "phys.complex.socio": ("phys.complex", "Econophysics, sociophysics & epidemics", [
        r"econo-?physics", r"social dynamics", r"physics of (?:epidemics|society|social)", r"epidemics? (?:and|&) social", r"socio-?physics", r"opinion dynamics", r"epidemic (?:spreading|dynamics|models?|modell?ing|processes|forecasting|control|threshold)", r"contagion", r"agent[- ]based", r"(?:stock|market) (?:dynamics|fluctuations|microstructure)", r"wealth (?:distribution|inequality|and income)", r"income (?:distribution|inequality)",
        r"evolutionary dynamics", r"ecological (?:dynamics|models?|networks?|complexity)", r"computational social science", r"language (?:dynamics|evolution)", r"cultural (?:evolution|dynamics)", r"cooperation (?:and|&) (?:evolution|games)",
        r"pandemic (?:modell?ing|spread|dynamics)", r"public health (?:modell?ing|physics)", r"physics of (?:society|finance|economics|social)", r"quantitative (?:social|finance)", r"complex (?:socio|socio-economic|economic) systems?", r"mathematical (?:sociology|economics)"]),

    # ── History, philosophy & education ────────────────────────────────────────
    "phys.meta.education": ("phys.meta", "Physics education & outreach", [
        r"physics (?:education|teaching|pedagog\w+|outreach|olympiads?|curriculum|learning|textbooks?|laboratory|demonstrations?|communication|popularisation|popularization|students?)", r"teaching (?:physics|science|of physics)", r"(?:undergraduate|school|college) physics", r"physics teachers?", r"learning (?:physics|science)",
        r"women in (?:physics|science|astronomy)", r"diversity (?:in|and) (?:physics|science|astronomy)", r"physics (?:careers|students|olympiad)", r"CS:IPhO", r"CS:IYPT", r"public (?:understanding|engagement) of science", r"science (?:museums?|centres?|exhibitions?)", r"hands-on (?:physics|science)",
        r"inquiry[- ]based", r"low[- ]cost (?:physics|experiments|science)", r"CS:NCERT", r"CS:HBCSE"]),
    "phys.meta.history": ("phys.meta", "History & philosophy of physics", [
        r"(?:history|philosophy|foundations|sociology|ethics) (?:and|&|of) (?:physics|science|astronomy|cosmology|relativity|quantum)", r"history of (?:physics|science|astronomy|quantum|relativity|cosmology|modern physics)",
        r"philosophy of (?:physics|science|space|time|quantum|cosmology|mind|nature)",
        r"einstein (?:centenary|legacy|lecture|memorial)", r"scientific revolutions?", r"epistemology (?:of|and) (?:physics|science)", r"metaphysics", r"conceptual (?:foundations|problems)",
        r"\d+ years of (?:\w+ ){0,3}(?:relativity|quantum|physics|the)", r"CS:HOPOS", r"time and (?:space|physics)", r"arrow of time", r"nature of time", r"reduction(?:ism)? (?:and|&) emergence"]),
}
