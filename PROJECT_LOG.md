# Project log: where Event Horizon 2.0 stands

One page to see the whole project at once: what works, what is being changed, what is
still wrong, what was decided and why, and how the numbers moved. Every pull request
updates it.

Other documents go deeper: [ROADMAP.md](ROADMAP.md) (the long-term plan),
[RUNBOOK.md](RUNBOOK.md) (incidents and how to fix them), [TAXONOMY.md](TAXONOMY.md)
(fields and topics), [INSTITUTES.md](INSTITUTES.md) (sources checked and why some wait).

*Last updated: 2026-11-10*

---

## 1. At a glance

| Area | State | Numbers (latest measurement) |
|---|---|---|
| Site | Live, refreshed daily and on every change to `main` | https://astrophysicist-abhi26.github.io/event-horizon-2.0/ · the daily run is scheduled for 08:00 IST but GitHub starts it 6–8 hours late (it ran at 14:30–15:30 IST on 7–9 Nov) |
| Events | Healthy | 1,434 upcoming events (2026-11-09) |
| Sources | 70 entries in `institutes.yaml` (14 parked) plus 9 global feeds | Parked ones and reasons: `institutes.yaml`, RUNBOOK |
| Health alerts | #50 open (2026-11-10): IISER Kolkata Physical Sciences (read timeouts since 2026-11-09) and IIT Bhubaneswar School of Basic Sciences (connection timeout). It replaced #48; IISc Mathematics and ICTP Indico recovered | Both show their last good events ("stale"); a source broken for 7 days raises a chronic alert, then park it |
| Disciplines | Physics · Astronomy & cosmology · Mathematics · Computer science · AI & ML | 54 sub-fields, 132 topics |
| Physics | 13 branches, 67 topics | to be measured |
| Astronomy & cosmology | 10 sub-fields, no topic level | to be measured |
| Mathematics | 15 branches, 65 topics: **being reworked (M1, M2 done; M3, M4 next)** | 376 maths events (2026-11-10, after M2); French maths Indico 68% to a specific branch |
| Computer science | 8 branches, no topics yet | 220 events; 0% with a topic |
| AI & ML | 8 branches, no topics yet | 154 events; 0% with a topic |
| Profiles | 14 ranking profiles | — |
| Tests | All pass | 163 (2026-11-10) |

## 2. Workstreams

✅ done · 🔄 in progress · ⏭️ next · 🗓️ planned · 💤 offered, not scheduled

| ID | Workstream | Status | Pull request |
|---|---|---|---|
| M1 | Maths precision: placeholder slots, no embedding guesses on French or name-only titles, maths keywords that tag physics events | ✅ | [#49](https://github.com/Astrophysicist-Abhi26/event-horizon-2.0/pull/49) |
| M2 | French keywords; series names count like titles (max 3 branches); maths-only sources fall back to "General mathematics"; legacy words out of "General mathematics" (X-6) | ✅ | [#51](https://github.com/Astrophysicist-Abhi26/event-horizon-2.0/pull/51) |
| M3 | Maths depth: Statistics branch, about 33 new topics, information theory / finance / history moved; speed-up of the keyword matcher first (P-9) | ⏭️ | — |
| M4 | Maths sources, each probed first: NCM, ATM, TIFR, TIFR-CAM, ISI, IISER/IIT maths, KSoM; RMS/IMS on the watchlist; AMS, EMS, MathMeetings, INI, Fields, MFO, CIRM, HIM, ESI, Lorentz | 🗓️ | — |
| C1 | Computer science: about 40 topics and Indian CSE sources | 🗓️ | — |
| A1 | AI & ML: topics | 🗓️ | — |
| DS | Statistics & Data Science discipline (shares Statistics with Maths, databases with CS, ML theory with AI) | 🗓️ | — |
| F1 | Calendar (.ics) export per profile | 💤 | — |
| F2 | "Wrong field?" button on each event | 💤 | — |
| F3 | Weekly digest | 💤 | — |
| F4 | Deadlines view | 💤 | — |

## 3. Decisions

| ID | Date | Decision | Why |
|---|---|---|---|
| D-1 | 2026-11-10 | Statistics becomes its own maths branch now (in M3) | It will be shared with the Data Science discipline later |
| D-2 | 2026-11-10 | Split PDE into elliptic & parabolic, dispersive & wave, fluid & kinetic, plus a general PDE topic | PDE is the largest maths topic and dominates the French seminars |
| D-3 | 2026-11-10 | Move information theory to Applied maths; split finance from game theory and history from education | They were filed in the wrong place |
| D-4 | 2026-11-10 | Drop placeholder slots such as "Séminaire des doctorants: TBA ENS" | Same rule as the existing "TBA" filter |
| D-5 | 2026-11-10 | Series names count like titles, but a series that names more than 3 branches goes to the general bucket | The organisers' own label is strong evidence; broad series would over-tag |
| D-6 | 2026-11-10 | Maths-only sources fall back to "General mathematics & colloquia" | Known to be maths, branch unknown |
| D-7 | 2026-11-10 | No embedding guess for French or name-only titles; a multilingual model only if needed later | The English-only model guessed wrong on 13 of 14 such maths events |
| D-8 | 2026-11-10 | Sources: Indian national bodies first (NCM, ATM, TIFR, TIFR-CAM, ISI), then AMS, EMS and the European institutes | Agreed order |
| D-9 | open | Should the pure-mathematics profile weight Statistics below Probability (40 vs 60)? Until decided, Statistics inherits Probability's weights | To be settled in M3 |
| D-10 | 2026-11-10 | Work in small pull requests, a few fixes at a time, each with a before/after report on the live data | Your instruction |
| D-11 | 2026-11-07 | Logo R2 (tilted black hole) | Your choice from the round-5 study |
| D-12 | 2026-11-05 | No Source filter on the site; fields shown as a vertical list; colourful field map with curved labels | Your feedback on the interface |
| D-13 | 2026-11-05 | Respect robots.txt (feeds are exempt); link out, never copy pages; removal requests via an issue form | Legal and etiquette review |

## 4. Open problems, pitfalls and inconsistencies

**Q** = data quality (measured), **X** = inconsistency in code or docs, **P** = pitfall to watch.
Status: 🔴 open · 🔄 being fixed · ✅ fixed (kept for the record).

| ID | Problem | Evidence | Plan | Status |
|---|---|---|---|---|
| Q-1 | Holiday and TBA slots reach the site as "<series>: Férié", "…: TBA ENS", "…: -" | Probe 2026-11-09. Cause: the Indico reader took "Férié" for a speaker's name and prefixed the series, so the junk filter no longer matched | M1 | ✅ |
| Q-2 | The embedding model guesses on French titles and bare speaker names | 14 maths events tagged by it alone; 13 wrong, 11 of them "Number theory" | M1 | ✅ |
| Q-3 | Maths tags on physics events | 8 of a sample of 45 branch-only maths events were not maths (EPS-HEP, ICDMS, a topological-matter talk) | M1 | ✅ |
| Q-4 | French maths Indico mostly unclassified | 81 of 229 classified (35%); the keywords are English | M2: specific branch 25% → 68% of French maths Indico; nothing left unclassified | ✅ |
| Q-5 | A series name in the description counts only 0.5, below the 1.0 threshold | "Séminaire de Géométrie Complexe: Hadrien Notarantonio" gets nothing | M2: series names count like titles | ✅ |
| Q-6 | Real maths missing a topic | Jump processes, intersection local times, uniform spanning trees, Santaló inequality | M3 | 🔴 |
| Q-7 | CS and AI have no topic level | 0% of 220 and 154 events | C1, A1 | 🔴 |
| Q-8 | Odd non-maths tags seen in passing | "Securing the Immersive Web" → reinforcement learning; "Data-Driven Modeling of Social Behavior" → astronomy | Audit during C1/A1 | 🔴 |
| Q-9 | The embedding model files many astronomy conferences under "Stars & planets" by default | "eSPACE 2027", "The right of seeing the stars: sustainable astronomy" → stellar (probe 2026-11-10) | Astronomy audit, later | 🔴 |
| Q-10 | A deadline sentence published as an event | "The last date to submit your abstract is Monday, 5 October 2026." | Small noise fix, later | 🔴 |
| Q-11 | Physics keyword "gravity" tags fluid dynamics | "Global well-posedness for … gravity water waves" → gravitation | Physics audit, later | 🔴 |
| Q-12 | INSPIRE's own category "Math and Math Physics" puts broad HEP conferences under Mathematics | Tux quantum-gravity workshop, Loop-the-Loop, LACES, Symmetry 2027 carry maths tags without any maths word | M1: measure how INSPIRE uses it, then weigh it | ✅ |
| X-1 | Coding & information theory sits under Number theory | taxonomy_math.py | M3 (D-3) | 🔴 |
| X-6 | "General mathematics" still holds words for areas that now have their own branch (combinatorics, logic, set theory, dynamical systems, game theory, information theory…) | taxonomy.py `math.other` | M2: moved to Combinatorics, Logic, Dynamics, Optimisation, Numerical, Education | ✅ |
| X-2 | Finance inside "Game theory, economics & finance"; education and history in one topic | taxonomy_math.py | M3 (D-3) | 🔴 |
| X-3 | RUNBOOK said `requirements.txt` is not pinned; it has been pinned since PR #31 | RUNBOOK | M1 | ✅ |
| X-4 | RUNBOOK listed the researchseminars.org timeouts twice | RUNBOOK | M1 | ✅ |
| X-5 | ROADMAP step 5 did not say maths is in progress | ROADMAP | M1 | ✅ |
| P-1 | Common words (group, ring, field, category, measure, graph, network, model, knot, bundle) also appear in physics and CS titles | 24 physics/CS/AI titles that must get no maths tag (`tests/test_maths_precision.py`) | Extend the set in M2–M3 | 🔄 |
| P-2 | A broad series name can hit many branches | "Géométrie, Algèbre, Dynamique et Topologie" | M2: a series naming more than 3 branches counts for General mathematics | ✅ |
| P-3 | Splitting a topic narrows a visitor's saved selection | — | Old ids stay as the general bucket; the site maps old ids to new ones (M3) | 🔴 |
| P-4 | Statistics/ML double tags raise such events in ML profiles | — | Intended; the cosmology-ml parity test must stay unchanged (M3) | 🔴 |
| P-5 | The new Statistics branch needs embedding examples; the classifier recalibrates itself | — | Labelled examples in M3; check the health line after merging | 🔴 |
| P-6 | About 98 maths topics crowd the outer ring of the field map | — | Check at phone width; show topics after clicking a discipline if needed (M3) | 🔴 |
| P-7 | Test titles used to write patterns are no longer a fair test | — | M2: dev/held-out split by event id; held-out scored once (see section 6). Repeat for M3 | 🔄 |
| P-8 | New sources: JavaScript pages, terms of use, duplicates across aggregators, a flood of conferences in "explore" | — | Probe each source before enabling it (M4) | 🔴 |
| P-9 | Classification time grows with the number of patterns (4,849 now) | Measured 2026-11-10: about 120 ms for one event with a 3,000-character description, because every pattern is tried on its own | Merge each topic's patterns into one regex before M3 adds more | 🔴 |
| Q-13 | Broad INSPIRE meetings get a tag for every box they tick | EPS-HEP 2027 → Astronomy and Gravitation as well as particle physics | Physics/astronomy audit, later | 🔴 |
| Q-14 | The embedding guard removed a few right guesses until M2 lands | "Séminaire de Probabilités" speakers (Irene Marcovici, Julien Barre) lost Probability; "Dynamique du billard dans un prisme" lost Geometry | M2: all three are back (series and French keywords) | ✅ |
| Q-15 | A source-level fallback can misfile an off-subject event | "6th Smilei user & training workshop" (plasma simulation code) → General mathematics | Rare; correct by a keyword when seen | 🔴 |
| Q-16 | Some real maths titles still lack a topic or get only the series' branch | "Limits of uniform spanning trees" → statistics (series MAD-Stat), "Surjonctivité des sous-décalages" → geometry (series) | M3 topics | 🔴 |
| P-10 | Cryptography is split between maths (number theory) and CS (security). M1 sends bare "cryptography" to CS only; words like "encryption" and "hash functions" still tag maths too | — | Finish in C1 | 🔴 |
| O-1 | Two old remote branches, `claude/actions-bump-test` and `claude/fix-noise`, could not be deleted from here | — | Delete them on GitHub (Branches page) | 🔴 |

## 5. Change log

| Date | PR | What changed |
|---|---|---|
| 2026-11-10 | #51 (M2, deployed by run #71 at 06:28 UTC) | French maths keywords (~200 patterns); series names count like titles, more than 3 branches → General mathematics; maths-only sources fall back to General mathematics; legacy words moved out of General mathematics; "TBA (speaker)" placeholders; tests 153 → 163 |
| 2026-11-10 | #49 (M1, deployed by run #70 at 06:01 UTC) | 51 placeholder slots dropped (Indico "Férié", "TBA ENS", "…: -"); Indico training and outreach categories skipped; no embedding guesses on French, non-Latin or speaker-name titles; 16 maths patterns narrowed ("field theory", "cryptography", "diffusion", "topological", "curvature" …) with a new "unless" context rule; INSPIRE's maths box weak on meetings that tick 4+ boxes; tests 142 → 153; this log; RUNBOOK and ROADMAP corrected |
| 2026-11-07 | #46 | Logo R2; maths in titles typeset; titles in other scripts behind a switch |
| 2026-11-06 | #43 | Shorter watchlist notes; Symmetry 2027 in person (likely) |
| 2026-11-06 | #41 | Placeholder, holiday, exam and cancelled entries dropped; no embedding guesses on bare names |
| 2026-11-06 | #32 | GitHub Actions versions updated (Dependabot) |
| 2026-11-05 | #40 | Wider layout, vertical field list, colourful map, no Source filter, quieter health alerts |
| 2026-11-05 | #39 | DESC's Google Calendar and the CADC RSS read as feeds |
| 2026-11-05 | #37 | Field browser with shared branches, relevance explained, robots.txt, removal requests |
| 2026-11-05 | #36 | DESY Indico parked (403 Forbidden) |
| 2026-11-05 | #34 | Three-level physics and maths taxonomy, new profiles, worldwide sources |
| 2026-11-05 | #31 | Renamed to Event Horizon 2.0; dependencies pinned; Dependabot; subject-coverage audit |
| 2026-11-05 | #30 | Daily refresh kept alive: date-proof test, non-blocking alerts, self-closing health alerts |
| 2026-10-25 | #23 | 12 more IIT and IISER sources |
| 2026-10-25 | #21 | 19 Indian institute sources |
| 2026-10-13 | #11–#15 | CMI source; embedding classifier fix; health alerts close themselves; NCM-4 form |
| 2026-09-25 | #1–#7 | Project docs, MIT licence, live site, science-poster background with typeset equations |

## 6. Measurements over time

Measured on the live site's events by a temporary probe (removed before each merge).

| Date | Events | Maths events with a topic | French maths Indico classified | Maths tags from the embedding alone that are right | CS with a topic | AI with a topic | Tests |
|---|---|---|---|---|---|---|---|
| 2026-11-09 (baseline) | 1,434 | 270 / 383 (70%) | 81 / 229 (35%) | 1 / 14 | 0% | 0% | 142 |
| 2026-11-10 before M1 ¹ | 1,434 | 231 / 309 (74%) | 77 / 229 (34%) | 18 tagged | 0% | 0% | 142 |
| 2026-11-10 after M1 ¹ | 1,383 | 201 / 263 (76%) | 58 / 182 (32%) | 5 tagged, 3–4 right | 0% | 0% | 153 |
| 2026-11-10 before M2 ² | 1,373 | 193 / 254 (75%) | 57 / 178 (32%); specific branch 44 (25%) | — | 0% | 0% | 153 |
| 2026-11-10 after M2 ² | 1,370 | 256 / 376 (68%) | 137 / 175 by keywords (78%), 175 with the fallback (100%); specific branch 119 (68%) | — | 0% | 0% | 163 |

¹ Same live events re-classified by the old and the new code with the same embedding results. Organisers' declared
codes are not stored in `events.json`, so neither run has them; that is why these numbers differ from the baseline.
M1 removes wrong tags (50 maths tags gone, 1 added, no physics or astronomy tag lost); the share of French events
classified rises only with M2.

² Re-classified from the live data after M1 was deployed (old code = M1, new code = M2). The share of maths events with a
topic falls because 122 more events now count as maths, most of them only at the General mathematics level (fallback
or a broad series); topics for them come with M3. **Held-out half** of the French maths Indico (74 events, written
without looking at them, scored once): specific branch 50 (68%), tagged by keywords 57 (77%), the rest by the
fallback; checked by hand, 73 of 74 right at branch level (wrong: "6th Smilei user & training workshop", a plasma
simulation code, fell back to General mathematics). Caveat: the ~95 series names were all seen beforehand.

**Targets for the maths work:** maths events with a topic ≥ 85%; French maths Indico
classified ≥ 80% (≥ 60% to a specific branch); embedding-only maths tags ≥ 90% right or not
given; no maths tags on the known physics events; held-out maths titles: branch ≥ 95%,
topic ≥ 85%; no off-topic title tagged maths.

## How to keep this log

With every pull request: update the status in section 2, the problems in section 4 (new rows
for anything found, ✅ for anything fixed), add a row to sections 5 and 6, and record any
decision in section 3. Incidents (something broke) still go to RUNBOOK.md.
