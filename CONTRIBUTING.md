# Contributing

Thank you for helping. Most contributions are one small edit to a YAML file. You don't need
to know the scraper code.

## Quick ways to help (no code)

- **An event you heard about by email or poster:** open an **Add event** issue. It appears
  on the site within minutes and disappears when the issue is closed. Only issues opened by
  the repository's owner, members or collaborators are published; a maintainer publishes
  someone else's issue by adding the `verified` label (this keeps strangers from pinning
  links to the site).
- **A source we should read:** open a **Suggest a source** issue with the page or calendar
  link.
- **A research profile for your field:** open a **Research profile** issue listing the
  topics that matter, roughly in order.
- **A mislabelled event:** open an issue with the event title and the topic it should have.

## Adding or tuning a research profile

Profiles live in [`scraper/profiles.yaml`](scraper/profiles.yaml). A minimal profile:

```yaml
  my-field:                        # id: lowercase, used in the link ?p=my-field
    label: Soft & biological physics
    blurb: Soft matter, active matter and biological physics first; then statistical physics.
    focus: [phys.condmat]          # optional: what the "focus" button and sort mean
    focus_label: soft matter
    interests:                     # field or sub-field -> weight 0-100
      phys.condmat: 100
      math.probability: 40
      physics: 30                  # every other physics sub-field
    places: {bengaluru: 10, india: 5}
    types: {School: 5, Workshop: 5}
```

Rules worth knowing:

- For each tag, the **most specific** node listed wins: `physics: 30` together with
  `phys.condmat: 100` gives condensed matter 100 and all other physics 30.
- Topics that are not listed, not even through their field, score **0**. Location and event
  type never make an off-topic event relevant.
- Level names can replace numbers: `top` 100, `very_high` 85, `high` 70, `medium` 45,
  `low` 20, `avoid` −40.
- The fields are cosmo, astro, ai, cs, math and physics; all sub-fields are listed in
  [`scraper/taxonomy.py`](scraper/taxonomy.py) (`FIELDS`, `SUBFIELDS`).
- **Profiles are named after research areas, never after people.**

Then run the tests (below). A typo, such as an unknown topic, region, event type or key,
fails with a message that says what is wrong.

## Adding a source

Institute pages and calendars go in [`scraper/institutes.yaml`](scraper/institutes.yaml).
Each entry picks an adapter with `kind`:

| kind | Use for |
|---|---|
| `ical` / `google_calendar` | any public calendar feed (preferred: it doesn't break when the page is redesigned) |
| `indico` | an Indico server (JSON export, falling back to the public iCal feed) |
| `wp_events` | WordPress sites using "The Events Calendar" |
| `labelled_list` | pages listing each talk as a list item with `Date:` / `Time:` / `Venue:` lines |
| `table` | an HTML table with a header row (Title, Speaker, Date, Venue …); columns are found by their header words |
| `rss` | an RSS feed whose item titles start with the date (Joomla JEvents) |

Optional keys for any entry: `include` / `exclude` (a regex on the title: keep only, or
drop, matching items, e.g. a notice board's tenders) and `title_in_description` (for
calendars that name an entry after its speaker and put the real title in a "Title:" line),
and `title_label` (for pages whose headings are generic, such as "International Conference",
with the full name after a label like "Details:"). `default_field` (for a source that lists one
subject only: an event no keyword tags is filed in that bucket, such as `math.other` for General
mathematics) and, for Indico servers, `skip_categories` (regexes on the category name for
categories that are not research events, such as staff training).
| `listing` | an HTML page that lists upcoming events (last resort) |

Check a new entry against the live site before opening a pull request:

```bash
python scraper/doctor.py "<part of the source name>"
```

It prints how many events the source returns and the next three upcoming ones. If the site
blocks automated visitors or needs JavaScript, say so in the pull request; such sources are
kept with `enabled: false` and a comment explaining why.

Global aggregators (INSPIRE, researchseminars.org and so on) live in
[`scraper/sources.py`](scraper/sources.py).

## Fixing a mislabelled event

Add `["the event title", correct.subfield]` to [`scraper/labels.yaml`](scraper/labels.yaml).
The embedding classifier learns from these examples on the next run, and the tests use them
to check classification accuracy. For a whole class of mistakes, add or adjust a keyword
rule in `RULES` in [`scraper/taxonomy.py`](scraper/taxonomy.py).

## Running the tests

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m pytest -q tests
```

The tests are offline and take a few seconds. They also run automatically on every pull
request.

## Pull requests

- Keep each pull request to one change: a profile, a source, or a fix.
- Never commit `docs/events.json`: the workflow builds it and publishes it with the site.
- Describe what you checked (for example the `doctor.py` output for a new source).

## Adding or fixing a topic

Events are tagged on three levels: field, sub-field, topic (for example Physics, High-energy
theory & QFT, String theory). The topics are defined in two plain files:

* `scraper/taxonomy_physics.py` and `scraper/taxonomy_math.py`: each topic has an id, a
  label and a list of keyword patterns. A pattern is a regular expression matched on whole
  words, ignoring case; a `CS:` prefix makes it case-sensitive (for acronyms).
* `tests/coverage_data.py`: titles with the topic they must get, and titles that must get no
  science tag at all.

To fix a missed event: add a pattern for its wording to the right topic, add the title to
`HELD_OUT` in `tests/coverage_data.py`, and run `python -m pytest -q tests/test_coverage.py`.
Keep patterns specific: a bare common word ("sensors", "mixing", "partitions") tags
unrelated events, and `OFF_TOPIC` is there to catch that.

When a word means something else in a known context, add that context after ` ||| `: the
word then counts only if the same text does not also mention the context. For example
`topolog\w* ||| insulators?|quantum matter` keeps "topology of manifolds" in mathematics but
leaves "topological insulators" to condensed matter. Titles that must get no maths tag at all
are listed in `tests/test_maths_precision.py`.

French keywords live in `scraper/taxonomy_math_fr.py`. Write them with their accents; they are
made accent-tolerant automatically. Use French words or phrases only: a word that is also
English ("inference", "optimisation") would tag English events too, and
`tests/test_maths_m2.py` checks a list of English titles for that.

The seminar series a talk belongs to (an Indico category such as "Séminaire de Géométrie
Complexe") counts like the title. A series naming more than three branches of one field counts
only for that field's general bucket.

To add a new topic, put it in the right file under its sub-field. A profile can weight a topic
by its id in `scraper/profiles.yaml`; otherwise it takes the weight of its sub-field.

