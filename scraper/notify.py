"""
Health alerts as GitHub issues. Run by the workflow after the site is built:

    python scraper/notify.py

* notify/health.md exists (a source broke, or has been broken for a week):
  open a new `health` issue, then close the older ones ("superseded"). The new
  issue is created first, so a failed call never leaves the repository without an alert.
* otherwise: close every open `health` issue whose named sources (the `- **Name**`
  lines) are all working again.

GitHub's API fails now and then ("Something went wrong while executing your query"),
so every call is retried. This script never fails the workflow: the site must be
published even if an alert could not be posted.
"""
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTIFY_DIR = os.path.join(ROOT, "notify")
LABELS = ("health", "add-event")


def gh(*args, tries=4, delay=3):
    """Run the GitHub CLI; retry with growing pauses. -> stdout, or None if it kept failing."""
    for i in range(tries):
        r = subprocess.run(["gh", *args], capture_output=True, text=True)
        if r.returncode == 0:
            return r.stdout
        print(f"gh {' '.join(args[:2])} failed ({i + 1}/{tries}): {(r.stderr or r.stdout).strip()[:200]}")
        if i < tries - 1:
            time.sleep(delay * (i + 1))
    return None


def listed_sources(body):
    """Source names an alert body points at: its `- **Name** — ...` lines."""
    return re.findall(r"^- \*\*(.+?)\*\*", body or "", re.M)


def resolved(body, bad):
    """True when none of the sources the alert names is broken any more. An alert
    with no recognisable names (an old format) closes only when nothing is broken."""
    names = listed_sources(body)
    return not any(n in bad for n in names) if names else not bad


def open_alerts():
    out = gh("issue", "list", "--label", "health", "--state", "open", "--json", "number,body")
    return json.loads(out) if out else []


def main():
    health_md = os.path.join(NOTIFY_DIR, "health.md")
    bad_json = os.path.join(NOTIFY_DIR, "bad.json")
    if not os.path.exists(bad_json):
        print("no notify/bad.json (the scrape did not finish): nothing to do")
        return
    bad = set(json.load(open(bad_json)))
    for label in LABELS:
        gh("label", "create", label, "--color", "0E8A16", "--force", tries=1)
    today = time.strftime("%Y-%m-%d", time.gmtime())
    old = open_alerts()
    if os.path.exists(health_md):
        if gh("issue", "create", "--label", "health", "--title", f"Source health alert — {today}",
              "--body-file", health_md) is None:
            print("could not post the alert; the old alerts stay open")
            return
        for it in old:
            gh("issue", "close", str(it["number"]), "--comment",
               f"Superseded by the notice of {today}.")
        return
    for it in old:
        if resolved(it.get("body"), bad):
            gh("issue", "close", str(it["number"]), "--comment",
               "Every source named in this alert is returning events again. Closing it.")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:        # never block publishing
        print(f"notify failed: {exc.__class__.__name__}: {exc}")
    sys.exit(0)
