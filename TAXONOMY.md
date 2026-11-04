# Subject coverage: physics and mathematics

What Event Horizon 2.0 can recognise today, area by area, and what is missing. Written 2026-11-04 as the start of the plan to cover **every branch of physics and mathematics** before any other subject.

## How this was measured

A draft list of 117 areas was written (physics, astronomy and cosmology, and the top-level areas of the Mathematics Subject Classification, with a few minor ones merged), each with 1 to 3 realistic event titles (the topics you named have several phrasings). Each title was run through the classifier **on the title alone**, which is the stricter case: real events usually also carry a description. An area is:

* ✅ **covered**: every sample title got a specific sub-field of the right field;
* ◐ **partly**: some titles did, or the title only reached the catch-all bucket ("Physics (other)", "Other mathematics"), where it cannot be filtered or ranked by topic;
* ❌ **missing**: no sample title was recognised.

Three samples per area is a spot check, not a proof; "covered" means the samples worked. The list itself is a draft: add or remove areas freely, and the audit can be re-run.

## Result

| | Areas | Share |
|---|---|---|
| ✅ covered | 59 | 50% |
| ◐ partly | 37 | 31% |
| ❌ missing | 21 | 17% |

By title: 169 of 250 sample titles (67%) were tagged correctly.

**The bigger limit is granularity, not recall.** The site has 39 sub-fields in total: 6 for physics (gravitation, high-energy theory & QFT, quantum, condensed matter, fluids/plasma, other) and 8 for mathematics (number theory, topology, algebra, geometry, probability & statistics, mathematical physics, analysis & PDE, other). So string theory, conformal field theory and scattering amplitudes all land in one bucket ("High-energy theory & QFT"), and elliptic curves, cryptography and modular forms in another ("Number theory"). You cannot yet filter or rank by these finer topics, whatever the recall.

## Physics · Strings, fields & gravity

| Area | Status | Not recognised (title → what it got) |
|---|---|---|
| String theory | ◐ | “Strings 2027” → nothing |
| AdS/CFT and holography | ✅ |  |
| Conformal field theory & bootstrap | ✅ |  |
| Quantum field theory | ✅ |  |
| Scattering amplitudes | ◐ | “Amplitudes 2027” → nothing |
| Supersymmetry & supergravity | ✅ |  |
| Quantum gravity | ✅ |  |
| Black holes & information paradox | ✅ |  |
| Swampland & string phenomenology | ◐ | “String Compactifications and Moduli Stabilisation” → math.geometry |
| Topological QFT & Chern–Simons | ✅ |  |
| Integrable systems & Yang–Baxter | ✅ |  |
| Lattice field theory | ◐ | “Lattice 2027: Symposium on Lattice Field Theory” → nothing |
| Effective field theory | ✅ |  |
| Generalized symmetries & anomalies | ◐ | “Generalized Global Symmetries and Anomalies” → nothing |
| Resurgence & non-perturbative methods | ❌ | “Resurgence, Transseries and Non-perturbative Effects” → nothing |
| General relativity & numerical relativity | ✅ |  |
| Modified gravity | ✅ |  |
| Gravitational waves | ✅ |  |

## Physics · Particles & nuclei

| Area | Status | Not recognised (title → what it got) |
|---|---|---|
| Particle phenomenology / BSM | ◐ | “Workshop on New Physics Searches” → phys.general |
| Neutrino physics | ✅ |  |
| Flavour physics | ❌ | “Flavour Physics and CP Violation” → phys.general; “B Physics and Rare Decays Workshop” → phys.general |
| Collider physics / LHC | ✅ |  |
| Dark matter (particle) | ✅ |  |
| Heavy-ion & QGP | ◐ | “Quark Matter 2027: Heavy-Ion Collisions” → nothing |
| Hadron physics / QCD | ◐ | “Proton Structure and Parton Distribution Functions” → nothing |
| Nuclear physics | ❌ | “Nuclear Structure and Reactions Conference” → phys.general; “School on Nuclear Astrophysics and Nucleosynthesis” → astro.stellar; “Nuclear Theory: Ab Initio Methods” → phys.general |
| Accelerator & detector physics | ❌ | “Particle Accelerator Conference” → nothing; “Detector Instrumentation and Silicon Sensors Workshop” → nothing |
| Astroparticle & cosmic rays | ✅ |  |

## Physics · Quantum & optics

| Area | Status | Not recognised (title → what it got) |
|---|---|---|
| Quantum information & computation | ◐ | “Workshop on Quantum Algorithms and Complexity” → cs.theory |
| Quantum foundations | ◐ | “Conference on the Measurement Problem” → nothing |
| Open quantum systems & thermodynamics | ✅ |  |
| Quantum optics & photonics | ◐ | “Nonlinear Optics and Ultrafast Lasers” → phys.general; “Plasmonics and Metamaterials Workshop” → nothing |
| Atomic, molecular & ultracold | ❌ | “Ultracold Atoms and Molecules Workshop” → nothing; “Atomic Clocks and Precision Metrology” → phys.general; “Cold Atom Quantum Simulators” → nothing |
| Quantum technologies & sensing | ✅ |  |

## Physics · Condensed matter & statistical

| Area | Status | Not recognised (title → what it got) |
|---|---|---|
| Strongly correlated systems | ◐ | “Strongly Correlated Electron Systems” → nothing |
| Topological matter | ✅ |  |
| Quantum magnetism & many-body | ✅ |  |
| 2D materials & nanoscience | ❌ | “Graphene and Two-Dimensional Materials” → nothing; “Moiré Physics and Twisted Bilayers” → phys.general; “Nanoscience and Nanotechnology Symposium” → nothing |
| Electronic structure / DFT / computational | ◐ | “Density Functional Theory and Materials Modelling” → nothing |
| Soft matter & polymers | ◐ | “Liquid Crystals Conference” → nothing |
| Active matter & biophysics | ✅ |  |
| Statistical mechanics & phase transitions | ◐ | “Critical Phenomena and the Renormalization Group” → nothing |
| Spintronics & magnetism | ◐ | “Semiconductor Physics and Devices” → phys.general |

## Physics · Plasma, fluids & applied

| Area | Status | Not recognised (title → what it got) |
|---|---|---|
| Plasma physics & fusion | ✅ |  |
| Fluid dynamics & turbulence | ✅ |  |
| Nonlinear dynamics & chaos | ❌ | “Nonlinear Dynamics and Chaos” → math.other; “Complex Systems and Network Science Workshop” → nothing |
| Climate, atmosphere & geophysics | ◐ | “Seismology and Geophysics Conference” → nothing |
| Medical & radiation physics | ❌ | “Medical Physics and Radiation Therapy Conference” → phys.general |
| Acoustics & mechanics | ❌ | “Acoustics and Vibration Symposium” → phys.general; “Classical Mechanics and Nonlinear Waves” → nothing |
| Energy & materials physics | ❌ | “Photovoltaics and Solar Energy Materials” → nothing; “Physics of Batteries and Energy Storage” → phys.general |
| History, philosophy & teaching of physics | ❌ | “Physics Education Conference” → phys.general; “History and Philosophy of Physics Workshop” → phys.general |
| Econophysics & interdisciplinary | ❌ | “Econophysics and Social Dynamics” → nothing; “Physics of Information and Computation” → phys.general |

## Physics · Astronomy & cosmology

| Area | Status | Not recognised (title → what it got) |
|---|---|---|
| Cosmology | ◐ | “Cosmology from Home” → cosmo.general; “Neighbourhood Cosmology Meeting” → cosmo.general |
| Galaxies & AGN | ✅ |  |
| Stars & stellar evolution | ✅ |  |
| Exoplanets & planetary science | ✅ |  |
| Solar & heliophysics | ✅ |  |
| Interstellar medium & astrochemistry | ◐ | “Astrochemistry and Astrobiology” → nothing |
| Observational astronomy & instruments | ◐ | “Radio Astronomy and Square Kilometre Array Science” → astro.general |
| Pulsars & compact objects | ✅ |  |

## Mathematics · Foundations & discrete

| Area | Status | Not recognised (title → what it got) |
|---|---|---|
| Mathematical logic & set theory | ❌ | “Logic Colloquium: Model Theory and Set Theory” → math.other; “Workshop on Computability and Proof Theory” → cs.theory, math.other |
| Combinatorics | ◐ | “Extremal and Probabilistic Combinatorics Workshop” → math.other; “Enumerative Combinatorics and Symmetric Functions” → math.other |
| Graph theory | ❌ | “Graph Theory and Ramsey Theory Workshop” → math.other; “Spectral Graph Theory Seminar” → math.other |
| Discrete & convex geometry | ◐ | “Polytopes and Lattice Packings” → nothing |
| Order, lattices & universal algebra | ✅ |  |
| Category theory | ◐ | “Workshop on Topos Theory” → nothing |

## Mathematics · Number theory

| Area | Status | Not recognised (title → what it got) |
|---|---|---|
| Analytic number theory | ✅ |  |
| Algebraic number theory | ✅ |  |
| Elliptic curves & arithmetic geometry | ◐ | “Seminar: Rational Points on Curves” → nothing |
| Modular & automorphic forms | ✅ |  |
| Additive & Diophantine number theory | ✅ |  |
| Cryptography (mathematical) | ✅ |  |
| Coding theory & information theory | ◐ | “Information Theory and Error-correcting Codes” → math.other |

## Mathematics · Algebra

| Area | Status | Not recognised (title → what it got) |
|---|---|---|
| Commutative algebra | ✅ |  |
| Noncommutative rings & modules | ✅ |  |
| Group theory | ✅ |  |
| Lie algebras & representation theory | ✅ |  |
| Field & Galois theory | ✅ |  |
| Linear & multilinear algebra | ✅ |  |
| K-theory & homological algebra | ✅ |  |
| Hopf algebras & quantum groups | ✅ |  |

## Mathematics · Geometry & topology

| Area | Status | Not recognised (title → what it got) |
|---|---|---|
| Algebraic geometry | ✅ |  |
| Differential geometry | ✅ |  |
| Symplectic & contact geometry | ✅ |  |
| Complex & Kähler geometry | ◐ | “Several Complex Variables” → nothing |
| Algebraic topology & homotopy | ✅ |  |
| Low-dimensional topology & knots | ✅ |  |
| Differential topology & manifolds | ◐ | “Foliations and Characteristic Classes” → nothing |
| General topology | ✅ |  |
| Euclidean & non-Euclidean geometry | ✅ |  |
| Tropical & combinatorial geometry | ✅ |  |
| Lie groups & homogeneous spaces | ◐ | “Discrete Subgroups and Arithmetic Groups” → nothing |

## Mathematics · Analysis

| Area | Status | Not recognised (title → what it got) |
|---|---|---|
| Real analysis & measure theory | ◐ | “Fractals and Hausdorff Dimension” → nothing |
| Complex analysis | ◐ | “Riemann Surfaces and Entire Functions” → nothing |
| Harmonic analysis | ◐ | “Wavelets and Time-Frequency Analysis” → nothing |
| Functional analysis & Banach spaces | ✅ |  |
| Operator theory & operator algebras | ✅ |  |
| Ordinary differential equations | ◐ | “Seminar: Boundary Value Problems for ODEs” → nothing |
| Partial differential equations | ✅ |  |
| Dynamical systems & ergodic theory | ◐ | “Hyperbolic Dynamics and Thermodynamic Formalism” → nothing; “Complex Dynamics and Julia Sets” → nothing |
| Calculus of variations & optimal transport | ✅ |  |
| Approximation & special functions | ◐ | “Orthogonal Polynomials Workshop” → nothing |
| Integral equations & transforms | ✅ |  |
| Potential theory & several complex variables | ❌ | “Potential Theory and Pluripotential Theory” → nothing |
| Difference equations & dynamics on graphs | ❌ | “Difference Equations and Discrete Dynamical Systems” → math.other |

## Mathematics · Probability, statistics & applied

| Area | Status | Not recognised (title → what it got) |
|---|---|---|
| Probability theory | ✅ |  |
| Mathematical statistics | ✅ |  |
| Numerical analysis & scientific computing | ✅ |  |
| Optimisation & operations research | ❌ | “Convex Optimization and Operations Research” → ai.theory, math.other; “Combinatorial Optimization Workshop” → math.other |
| Game theory & mathematical economics | ◐ | “Game Theory and Mathematical Economics” → math.other |
| Control theory & systems | ❌ | “Control Theory and Mathematical Systems” → math.other |
| Mathematical biology | ❌ | “Mathematical Biology and Epidemic Modelling” → math.other; “Mathematical Modelling in Neuroscience” → math.other |
| Mathematical physics | ✅ |  |
| Mechanics & continuum mechanics | ◐ | “Continuum Mechanics and Elasticity” → nothing |
| Theoretical computer science (maths side) | ◐ | “Computational Complexity and Algorithms” → nothing |
| Mathematics education & history | ❌ | “Mathematics Education Conference” → math.other; “History of Mathematics Workshop” → math.other |
| Data science / applied mathematics (general) | ❌ | “Applied Mathematics Colloquium” → math.other; “Mathematical Modelling Workshop for Industry” → math.other |

## Proposed next step: a finer two-level tree

1. **Split the 14 physics and mathematics sub-fields into about 120 topics**, following the arXiv archives for physics (hep-th, hep-ph, hep-ex, hep-lat, gr-qc, quant-ph, cond-mat's sections, nucl-th/ex, physics.*) and the Mathematics Subject Classification (MSC2020) for mathematics. Examples: *High-energy theory* → string theory, AdS/CFT & holography, conformal field theory, quantum field theory, scattering amplitudes, supersymmetry & supergravity, quantum gravity, lattice field theory; *Number theory* → analytic, algebraic, arithmetic geometry & elliptic curves, modular & automorphic forms, cryptography. Existing profile settings keep working because every new topic sits under the sub-field it came from.
2. **Fill the ❌ and ◐ rows above** with keyword rules, the arXiv/INSPIRE codes the organisers attach, and example titles for the embedding classifier.
3. **Add the sources that publish these events**, for example IPMU, ICTP, Simons, MSRI/SLMath, Isaac Newton Institute, Oberwolfach, BIRS, CIRM, IHES, and the Indian mathematics societies; see INSTITUTES.md for the Indian side.
4. **A regression test** per area, using these same titles, so coverage cannot silently shrink.

History, education and outreach events would stay together under one "education & history" topic per field, to keep the list usable.
