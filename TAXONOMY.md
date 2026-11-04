# Subject coverage: physics and mathematics

What Event Horizon 2.0 recognises, area by area. The taxonomy has three levels: **field → sub-field → topic**, with 132 topics under the physics and mathematics sub-fields (the full list is below), and a few new sub-fields carved out of the old catch-alls. Re-measured on 2026-11-04 after adding them.

## How the site shows it

The site groups the taxonomy into five disciplines: **Physics**, **Astronomy & Astrophysics**
(cosmology is a branch of it), **Mathematics**, **Computer science** and **AI & machine
learning**. Three branches are *shared*, listed under two disciplines with the same topics and the
same count: Gravitation & GR and Cosmology (Physics and Astronomy), and Mathematical physics
(Physics and Mathematics). Branches follow a fixed order (physics from fundamental theory through
matter at growing scales to applied topics; mathematics roughly in MSC order), and each
discipline's catch-all ("General … & colloquia") comes last. This grouping is presentation only
(`DISPLAY` and `SHARED` in `scraper/taxonomy.py`); tagging and ranking use the ids below.

## How it is measured

* **Area samples.** 117 areas (physics, astronomy and cosmology, and the top-level areas of the Mathematics Subject Classification), each with 1 to 3 event titles; `tests/coverage_data.py` and the audit tables below. The classifier is run on the **title alone**, the stricter case. A title is right when it gets the expected *topic*.
* **Held-out titles.** 110 further titles written without looking at the keyword rules: 108 matched on the first try and two needed a rule each (all 110 match now). `tests/test_coverage.py` fails if this falls below 96%.
* **Off-topic titles.** 40 titles from other subjects (administration, engineering, biology, computer science) must get no physics, mathematics, astronomy or cosmology tag. A few older catch-all rules still tag the words "water", "statistics" and "fluid"; they are left as they were.
* A sample of 3 titles per area is a spot check, not a proof. Real titles and descriptions will show more gaps; each one found is added as a rule and a test.

## Result

| | Before (2026-11-04 morning) | Now |
|---|---|---|
| Areas where every sample title gets the expected topic | 59 of 117 | 115 of 117 |
| Areas partly covered | 37 | 2 |
| Areas not recognised | 21 | 0 |
| Sample titles on the right topic | 169 of 250 (right *field*, not topic) | 248 of 250 (right *topic*) |

## Gravitation and cosmology under both fields

Gravitation & GR events are tagged **Physics → Gravitation** and also **Astronomy & cosmology → Gravitation & GR**; cosmology events are tagged **Astronomy & cosmology** and also **Physics → Cosmology**. Someone who follows only one of the two fields therefore sees all of it. The second tag is a mirror: it makes the event visible and ranked in the other field, but never counts as a second subject, so a profile's score for the event does not change.

## The topics

### Physics

* **Gravitation & GR** (`phys.gr`): General relativity & numerical relativity; Gravitational waves; Black holes: thermodynamics & information; Modified gravity; Quantum gravity
* **High-energy theory & QFT** (`phys.hepth`): String theory; AdS/CFT & holography; Conformal field theory & bootstrap; Quantum field theory; Scattering amplitudes; Supersymmetry & supergravity; Swampland & string phenomenology; Topological QFT & Chern-Simons; Integrability & Yang-Baxter; Lattice field theory; Effective field theory; Generalized symmetries & anomalies; Resurgence & non-perturbative methods
* **Quantum physics** (`phys.quantum`): Quantum information & computation; Quantum foundations; Open quantum systems & quantum thermodynamics; Quantum technologies, sensing & devices
* **Condensed matter & stat mech** (`phys.condmat`): Strongly correlated systems & superconductivity; Topological matter; Magnetism & spin systems; 2D materials & low-dimensional systems; Electronic structure & computational materials physics; Soft matter & polymers; Active matter & biological physics; Statistical mechanics & phase transitions; Non-equilibrium & stochastic thermodynamics; Mesoscopic & quantum transport
* **Fluids, plasma & climate** (`phys.fluids`): Fluid dynamics; Turbulence; Plasma physics; Fusion energy & confinement; Climate, atmosphere & ocean physics; Geophysics & solid-earth physics
* **General physics & colloquia** (`phys.general`)
* **Particle physics: phenomenology & experiment** (`phys.hep`): Beyond the Standard Model & phenomenology; Neutrino physics; Flavour physics & CP violation; Collider physics & the Higgs; Hadron physics & QCD; Dark matter (particle physics); Accelerators & detectors; Astroparticle & cosmic rays
* **Nuclear & heavy-ion physics** (`phys.nuclear`): Nuclear structure & reactions; Nuclear astrophysics; Heavy-ion collisions & QGP; Nuclear experiment & applications
* **Atomic, molecular & optical physics** (`phys.amo`): Ultracold atoms & quantum gases; Atomic & molecular physics, precision measurement; Quantum optics; Photonics, nonlinear optics & metamaterials; Lasers & ultrafast science
* **Materials, devices & instrumentation** (`phys.applied`): Semiconductor physics & devices; Energy materials & devices; Nanoscience, thin films & surfaces; Materials research & characterisation; Instrumentation, sensors & metrology; Medical & radiation physics; Acoustics, vibration & mechanics
* **Nonlinear dynamics & complex systems** (`phys.complex`): Nonlinear dynamics & chaos; Complex systems & network science; Econophysics, sociophysics & epidemics
* **Cosmology** (`phys.cosmo`)
* **History, philosophy & education of physics** (`phys.meta`): Physics education & outreach; History & philosophy of physics

### Mathematics

* **Number theory** (`math.nt`): Analytic number theory; Algebraic number theory; Elliptic curves & arithmetic geometry; Modular & automorphic forms, Langlands; Additive & Diophantine number theory; Cryptography (mathematical); Coding theory & information theory
* **Topology** (`math.topology`): Algebraic topology & homotopy theory; Low-dimensional topology & knot theory; Differential & geometric topology, manifolds; General & set-theoretic topology
* **Algebra & representation theory** (`math.algebra`): Commutative algebra; Noncommutative rings & modules; Group theory; Lie algebras & representation theory; Hopf algebras, quantum groups & tensor categories; Field & Galois theory, polynomials; Linear & multilinear algebra; Homological algebra & K-theory; Universal algebra, lattices & semigroups
* **Geometry** (`math.geometry`): Algebraic geometry; Differential & Riemannian geometry; Symplectic & contact geometry; Complex & Kähler geometry; Convex & discrete geometry; Lie groups & homogeneous spaces; Tropical & toric geometry
* **Probability & statistics** (`math.probability`): Probability theory & stochastic processes; Random matrices & free probability; Mathematical statistics & data analysis
* **Mathematical physics** (`math.mathphys`): Mathematical quantum mechanics & spectral theory; Rigorous statistical mechanics; Mathematical QFT, TQFT & vertex algebras; Integrable systems & solitons; Mathematical relativity & geometric analysis of spacetime
* **Analysis & PDE** (`math.analysis`): Real analysis, measure theory & fractals; Complex analysis & function theory; Harmonic analysis & Fourier analysis; Functional analysis & operator theory; Operator algebras & noncommutative geometry; Ordinary differential equations; Partial differential equations; Calculus of variations & optimal transport; Approximation theory & special functions; Integral equations, transforms & inverse problems; Potential theory & pluripotential theory
* **General mathematics & colloquia** (`math.other`)
* **Logic, foundations & category theory** (`math.logic`): Mathematical logic & set theory; Category theory & higher categories
* **Combinatorics & discrete mathematics** (`math.comb`): Algebraic combinatorics; Enumerative & analytic combinatorics; Extremal & probabilistic combinatorics, Ramsey theory; Graph theory
* **Dynamical systems & ergodic theory** (`math.dyn`): Ergodic theory & topological dynamics; Hyperbolic dynamics & Hamiltonian systems; Complex & holomorphic dynamics; Dynamical systems (general)
* **Numerical analysis & scientific computing** (`math.numeric`): Numerical analysis & scientific computing; Computer algebra & experimental mathematics
* **Optimisation, control & games** (`math.optim`): Optimisation & operations research; Control theory & systems; Game theory, economics & finance
* **Applied & interdisciplinary mathematics** (`math.applied`): Mathematical biology & medicine; Mathematical mechanics & continuum mechanics; Applied mathematics & mathematical modelling
* **Mathematics education & history** (`math.edu`): Mathematics education & history

## Audit by area

Samples that reached the expected topic / samples tried.


**Physics · Strings, fields & gravity**

| Area | Samples right |
|---|---|
| String theory | 3 / 3 ✅ |
| AdS/CFT and holography | 3 / 3 ✅ |
| Conformal field theory & bootstrap | 3 / 3 ✅ |
| Quantum field theory | 3 / 3 ✅ |
| Scattering amplitudes | 2 / 2 ✅ |
| Supersymmetry & supergravity | 2 / 2 ✅ |
| Quantum gravity | 2 / 2 ✅ |
| Black holes & information paradox | 2 / 2 ✅ |
| Swampland & string phenomenology | 2 / 2 ✅ |
| Topological QFT & Chern–Simons | 2 / 2 ✅ |
| Integrable systems & Yang–Baxter | 2 / 2 ✅ |
| Lattice field theory | 2 / 2 ✅ |
| Effective field theory | 2 / 2 ✅ |
| Generalized symmetries & anomalies | 2 / 2 ✅ |
| Resurgence & non-perturbative methods | 1 / 1 ✅ |
| General relativity & numerical relativity | 2 / 2 ✅ |
| Modified gravity | 2 / 2 ✅ |
| Gravitational waves | 2 / 2 ✅ |

**Physics · Particles & nuclei**

| Area | Samples right |
|---|---|
| Particle phenomenology / BSM | 3 / 3 ✅ |
| Neutrino physics | 2 / 2 ✅ |
| Flavour physics | 2 / 2 ✅ |
| Collider physics / LHC | 3 / 3 ✅ |
| Dark matter (particle) | 2 / 2 ✅ |
| Heavy-ion & QGP | 2 / 2 ✅ |
| Hadron physics / QCD | 2 / 2 ✅ |
| Nuclear physics | 3 / 3 ✅ |
| Accelerator & detector physics | 2 / 2 ✅ |
| Astroparticle & cosmic rays | 2 / 2 ✅ |

**Physics · Quantum & optics**

| Area | Samples right |
|---|---|
| Quantum information & computation | 3 / 3 ✅ |
| Quantum foundations | 2 / 2 ✅ |
| Open quantum systems & thermodynamics | 2 / 2 ✅ |
| Quantum optics & photonics | 3 / 3 ✅ |
| Atomic, molecular & ultracold | 3 / 3 ✅ |
| Quantum technologies & sensing | 2 / 2 ✅ |

**Physics · Condensed matter & statistical**

| Area | Samples right |
|---|---|
| Strongly correlated systems | 2 / 2 ✅ |
| Topological matter | 2 / 2 ✅ |
| Quantum magnetism & many-body | 2 / 2 ✅ |
| 2D materials & nanoscience | 3 / 3 ✅ |
| Electronic structure / DFT / computational | 2 / 2 ✅ |
| Soft matter & polymers | 3 / 3 ✅ |
| Active matter & biophysics | 3 / 3 ✅ |
| Statistical mechanics & phase transitions | 3 / 3 ✅ |
| Spintronics & magnetism | 2 / 2 ✅ |

**Physics · Plasma, fluids & applied**

| Area | Samples right |
|---|---|
| Plasma physics & fusion | 2 / 2 ✅ |
| Fluid dynamics & turbulence | 3 / 3 ✅ |
| Nonlinear dynamics & chaos | 2 / 2 ✅ |
| Climate, atmosphere & geophysics | 2 / 2 ✅ |
| Medical & radiation physics | 1 / 1 ✅ |
| Acoustics & mechanics | 2 / 2 ✅ |
| Energy & materials physics | 2 / 2 ✅ |
| History, philosophy & teaching of physics | 2 / 2 ✅ |
| Econophysics & interdisciplinary | 2 / 2 ✅ |

**Physics · Astronomy & cosmology**

| Area | Samples right |
|---|---|
| Cosmology | 3 / 3 ✅ |
| Galaxies & AGN | 2 / 2 ✅ |
| Stars & stellar evolution | 2 / 2 ✅ |
| Exoplanets & planetary science | 2 / 2 ✅ |
| Solar & heliophysics | 1 / 1 ✅ |
| Interstellar medium & astrochemistry | 2 / 2 ✅ |
| Observational astronomy & instruments | 1 / 2 ◐ |
| Pulsars & compact objects | 2 / 2 ✅ |

**Mathematics · Foundations & discrete**

| Area | Samples right |
|---|---|
| Mathematical logic & set theory | 2 / 2 ✅ |
| Combinatorics | 3 / 3 ✅ |
| Graph theory | 2 / 2 ✅ |
| Discrete & convex geometry | 2 / 2 ✅ |
| Order, lattices & universal algebra | 1 / 1 ✅ |
| Category theory | 2 / 2 ✅ |

**Mathematics · Number theory**

| Area | Samples right |
|---|---|
| Analytic number theory | 3 / 3 ✅ |
| Algebraic number theory | 2 / 2 ✅ |
| Elliptic curves & arithmetic geometry | 3 / 3 ✅ |
| Modular & automorphic forms | 2 / 2 ✅ |
| Additive & Diophantine number theory | 2 / 2 ✅ |
| Cryptography (mathematical) | 3 / 3 ✅ |
| Coding theory & information theory | 2 / 2 ✅ |

**Mathematics · Algebra**

| Area | Samples right |
|---|---|
| Commutative algebra | 2 / 2 ✅ |
| Noncommutative rings & modules | 1 / 1 ✅ |
| Group theory | 2 / 2 ✅ |
| Lie algebras & representation theory | 3 / 3 ✅ |
| Field & Galois theory | 1 / 1 ✅ |
| Linear & multilinear algebra | 2 / 2 ✅ |
| K-theory & homological algebra | 2 / 2 ✅ |
| Hopf algebras & quantum groups | 1 / 1 ✅ |

**Mathematics · Geometry & topology**

| Area | Samples right |
|---|---|
| Algebraic geometry | 3 / 3 ✅ |
| Differential geometry | 3 / 3 ✅ |
| Symplectic & contact geometry | 2 / 2 ✅ |
| Complex & Kähler geometry | 2 / 2 ✅ |
| Algebraic topology & homotopy | 2 / 2 ✅ |
| Low-dimensional topology & knots | 2 / 2 ✅ |
| Differential topology & manifolds | 2 / 2 ✅ |
| General topology | 1 / 1 ✅ |
| Euclidean & non-Euclidean geometry | 2 / 2 ✅ |
| Tropical & combinatorial geometry | 1 / 1 ✅ |
| Lie groups & homogeneous spaces | 2 / 2 ✅ |

**Mathematics · Analysis**

| Area | Samples right |
|---|---|
| Real analysis & measure theory | 2 / 2 ✅ |
| Complex analysis | 2 / 2 ✅ |
| Harmonic analysis | 2 / 2 ✅ |
| Functional analysis & Banach spaces | 2 / 2 ✅ |
| Operator theory & operator algebras | 3 / 3 ✅ |
| Ordinary differential equations | 2 / 2 ✅ |
| Partial differential equations | 3 / 3 ✅ |
| Dynamical systems & ergodic theory | 3 / 3 ✅ |
| Calculus of variations & optimal transport | 2 / 2 ✅ |
| Approximation & special functions | 2 / 2 ✅ |
| Integral equations & transforms | 1 / 1 ✅ |
| Potential theory & several complex variables | 1 / 1 ✅ |
| Difference equations & dynamics on graphs | 1 / 1 ✅ |

**Mathematics · Probability, statistics & applied**

| Area | Samples right |
|---|---|
| Probability theory | 3 / 3 ✅ |
| Mathematical statistics | 2 / 3 ◐ |
| Numerical analysis & scientific computing | 2 / 2 ✅ |
| Optimisation & operations research | 2 / 2 ✅ |
| Game theory & mathematical economics | 2 / 2 ✅ |
| Control theory & systems | 1 / 1 ✅ |
| Mathematical biology | 2 / 2 ✅ |
| Mathematical physics | 3 / 3 ✅ |
| Mechanics & continuum mechanics | 2 / 2 ✅ |
| Theoretical computer science (maths side) | 2 / 2 ✅ |
| Mathematics education & history | 2 / 2 ✅ |
| Data science / applied mathematics (general) | 2 / 2 ✅ |

## What is still missing

* **Astronomy and cosmology topics.** This pass added topics for physics and mathematics only; astronomy and cosmology keep their original sub-fields (galaxies, stars, high-energy astrophysics, dark energy, large-scale structure, CMB, dark matter).
* **Real-world checking.** The rules were checked on written titles. The first daily runs on live events will show which real titles are missed or mis-tagged; those become new rules and tests.
* **Sources.** Topics only help if events reach the site: sources for string theory, mathematics institutes and the international conference series are the next step (see the pull request).
