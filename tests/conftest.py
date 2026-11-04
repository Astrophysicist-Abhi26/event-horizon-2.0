import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "scraper"))

# Tests replace the network with fakes; robots.txt checks are tested on their own
# (tests/test_robots.py), so they do not ask the fakes for robots.txt files.
os.environ.setdefault("EH_ROBOTS", "off")
