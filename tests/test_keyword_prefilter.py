"""The per-sub-field prefilter (2026-11-10) must not change a single keyword hit."""
import os
from collections import defaultdict

import yaml

import classify as C
import coverage_data as D
import taxonomy as T


def reference(text):
    """keyword_hits without the prefilter: every pattern tried."""
    hits = defaultdict(list)
    for sf, pats in T.COMPILED.items():
        for p in pats:
            m = p.search(text)
            if m:
                hits[sf].append(m.group(0))
    return hits


def _texts():
    out = []
    for name in dir(D):
        val = getattr(D, name)
        if isinstance(val, (list, tuple, dict)):
            items = val.items() if isinstance(val, dict) else val
            for it in items:
                for x in (it if isinstance(it, (list, tuple)) else [it]):
                    if isinstance(x, str) and len(x) > 6:
                        out.append(x)
    labels = yaml.safe_load(open(os.path.join(os.path.dirname(T.__file__), "labels.yaml")))
    out += [t for t, _ in labels]
    out += ["Séminaire de Géométrie Complexe", "Statistique - Probabilités - Optimisation et Contrôle",
            "Workshop on Geometric Phase, Berry Curvature and Topological Phenomena",
            "CS:LDPC codes and Lean formalisation", "AI for science", "The 44th International Symposium on Lattice Field Theory"]
    return out


def test_prefilter_gives_exactly_the_same_hits():
    texts = _texts()
    assert len(texts) > 400
    # long descriptions too: groups of 25 titles joined into one text
    texts += [". ".join(texts[i:i + 25]) for i in range(0, len(texts), 25)]
    for t in texts:
        assert dict(C.keyword_hits(t)) == dict(reference(t)), t
