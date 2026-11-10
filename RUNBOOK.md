# Runbook: known problems and how to fix them fast

Every real incident so far, newest first. If something breaks, look for its symptom here
first. Add a row when a new kind of problem appears (and a test, if it can recur).

**Where to look.** Actions tab → *Update events* (a red run = the site was not refreshed) ·
Issues labelled `health` (a source stopped working) · the *Source health* panel at the bottom
of the site · `python scraper/doctor.py "<part of a source name>"` (tests one source live).

## Quick symptom table

| Symptom | Most likely cause | Do this |
|---|---|---|
| Run is red at **Run tests**; no deploy | A test depends on today's date (see I-1) or a library update broke a test | Open the run → the failing test name. Date-related: fix the fixture, never skip the test |
| Run is red at **Notify**; no deploy | (fixed, I-2) GitHub API hiccup while posting an alert | Re-run the workflow. If it recurs, check `scraper/notify.py` and the step's `continue-on-error` |
| Run is green but the site looks old | A deploy was skipped, or the browser cached | Check the run's *deploy* job; hard refresh (Ctrl/Cmd+Shift+R) once |
| `health` issue about one source | That site is down, redesigned or blocks us | `doctor.py "<name>"`; fix the entry in `institutes.yaml`, or `enabled: false` to park it |
| `health` issue never closes | (fixed, I-3) | It closes itself once none of its named sources is broken |
| Source shows `stale` | It failed; yesterday's events are shown instead | Same as above. Stale data is kept for the events' lifetime only |
| A run takes more than ~10 minutes | Unreachable hosts or very slow pages | Look at the per-source seconds in the log; park or fix the slow source |
| Strange events at the top of the site | Someone used the *Add event* form (see I-4) | Close the issue; only your own issues, or ones labelled `verified`, are published |
| Garbled text such as `Itâs` | Page declares no charset (I-9) | Already handled in `common.get`; check the page's encoding if it recurs |

## Incident log

| ID | Date | Symptom | Root cause | Fix | Prevent / detect |
|---|---|---|---|---|---|
| I-1 | 2026-10-30 → 11-01 | Daily run failed at *Run tests*; the site was not refreshed for 3 days | A test built a fake conference "today + 60 days" and wrote its dates without the year of the end date. When that window crossed 31 Dec ("December 29 – January 1, 2026") it parsed as past | The fixture now writes both years; a test round-trips every day of the year | Tests must not depend on the calendar date. `tests/test_ai_cs.py::test_date_text_round_trips_every_day_of_the_year`. Sweeping the suite under faked dates found no others (see PR) |
| I-2 | 2026-11-04 | Scrape succeeded, but the run was red and the deploy skipped | The *Notify* step failed on a GitHub API error ("Something went wrong while executing your query") and the deploy job depends on the update job | Alerts moved into `scraper/notify.py`: every call retried, never exits non-zero; the step is `continue-on-error`. A new alert is posted before the old one is closed | An alert can never block publishing. `tests/test_ops_nov2026.py` |
| I-3 | 2026-10 → 11 | Alert #29 (IISc, 502) stayed open after IISc recovered; IIT Bombay failed for 10 days with no open alert | The old rule closed alerts only when *no* source anywhere was broken, and each new alert replaced the older one while listing only the *new* failures | An alert now lists every broken source; it closes when none of the sources it names is broken; a source broken for 7 days raises one alert (`bad_since` in `events.json` health) | `notify/bad.json`; tests in `test_ops_nov2026.py` |
| I-4 | found 2026-11-04 | (latent) anyone could publish a pinned event | "Add event" issues from any GitHub user were read; the issue template applies the label automatically | Only issues by the owner, members or collaborators are published; an outsider's issue appears after a maintainer adds the `verified` label | `SI._trusted_issue` and its tests |
| I-5 | 2026-10-25 → | IIT Bombay Mathematics: `ConnectTimeout` every run, two sources × ~50 s | The host does not answer connections from GitHub's runners (it did on 2026-10-25). Either the server is down, or the institute now blocks traffic from abroad or from cloud providers (common after a security incident); from outside we cannot tell which | A host that fails to connect is skipped for the rest of the run (`common._DEAD_HOSTS`); both sources parked (`enabled: false`) on 2026-11-04 | Open the two links from a phone or campus network: if they load, the site blocks cloud servers and stays parked; if not, it is down. `python scraper/doctor.py --all "IIT Bombay Math"` re-tests |
| I-6 | 2026-11 | IISc Mathematics: `404 Seminars2027.html` | From November the source also tries next year's page, which does not exist yet; the whole source errored | The look-ahead page is optional; the current year's page is still required | `_collect` in `sources_india.py`; test in `test_ops_nov2026.py` |
| I-7 | 2026-10-12 | Embedding classifier switched itself off; 93 of 681 events unclassified | New AI/CS topics had no labelled examples; three titles carried old labels | Relabelled; examples added (PR #13) | Source health panel shows classifier status; watch for "calibration failed" in the run log |
| I-8 | 2026-10-12 | A dead host cost 12 minutes per run | 90 s timeout × retries on researchseminars.org | Connect timeout 10 s (PR #13) | Per-source seconds in the log |
| I-9 | 2026-10-25 | `Itâs` in IIT Madras titles | Page names no charset; `requests` assumed ISO-8859-1 | Encoding taken from the bytes | `common.get` |
| I-10 | 2026-10-13 | The link `…github.io/event-horizon-2.0/` gave 404 | The address follows the *repository* name, which was still `research-horizon` | The repository was renamed to `event-horizon-2.0` (Settings → General → Repository name), so that address now works; the code, README and site links were updated to match | After any rename: GitHub redirects the repository's old *github.com* address, but not the old *github.io* site address; the next run starts without yesterday's "first seen" dates | README, site |
| I-11 | 2026-10-13 | Health alert #12 never closed | No auto-close existed (PR #14); later replaced by I-3 | — | — |
| I-12 | 2026-10-25 | Temporary probe files reached `main` | PR merged while a temporary commit was on its branch | Removed in PR #23 | Never push temporary files to a branch with an open PR; check `git diff main` before merging |
| I-13 | 2026-11-04 | Physics and mathematics events fell into a few broad topics, so string theory, conformal field theory and amplitudes could not be told apart; about a third of sample titles got no topic | The taxonomy had 6 physics and 8 mathematics sub-fields | Three-level taxonomy (field, sub-field, topic) with 132 topics; physics and mathematics areas re-measured (TAXONOMY.md) | `tests/test_coverage.py` fails if held-out coverage drops or an off-topic title gets a science tag |

## Standing known limitations (not bugs)

* *researchseminars.org* (talks and conferences) does not answer GitHub's runners (three timeouts in a row on 2026-11-05). It stays in *Source health* with its last good events but never raises an alert (`UNRELIABLE` in `scraper/scrape.py`).
* A page that loads and lists nothing because nothing is scheduled (ARIES seminars) is marked `empty_ok: true` in `institutes.yaml`; it then counts as healthy.

* Pages a site's `robots.txt` asks automated tools not to read are skipped (status *error*,
  message "the site's robots.txt asks automated tools not to read …"). That is the site's
  choice; do not work around it. `EH_ROBOTS=report` lists what would be skipped without skipping.
* A source marked *needed a browser user agent* in `events.json` health refused our named agent
  and answered an ordinary browser's. Review such sources now and then; drop one if its owner objects.

* Sources whose pages are built by JavaScript, protected by Cloudflare, or have no dates cannot
  be read. They are listed with reasons in [INSTITUTES.md](INSTITUTES.md).
* Several servers (IIA, TIFR, IIT Jodhpur) send incomplete certificate chains, so certificate
  checking is relaxed for exactly those sources (`insecure_ok: true`). The data is public.
* Library versions are pinned in `requirements.txt` (since PR #31). Dependabot proposes updates
  as pull requests once a week, and each one runs the tests before it can be merged.
* The scan takes 8–9 minutes because sources run one after another.

## How to add a row

Symptom (what you saw) · root cause (what was actually wrong) · fix (the change) · prevent/detect
(the test or log line that would catch it next time). Keep it factual and short.
