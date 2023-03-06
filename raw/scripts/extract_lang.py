"""
Module extracts data from a specific language
"""
from collections import Counter
from pathlib import Path
from lingpy import Wordlist


concepts = Counter()

wordlist = Wordlist.from_cldf(
    Path("cldf", "cldf-metadata.json").as_posix(),
    columns=(
        "form",
        "segments",
        "language_id",
        "concept_name",
        "concept_concepticon_id",
        "concept_concepticon_gloss",
        ),
    namespace=(
        ("language_id", "doculect"),
        ("language_glottocode", "glottocode"),
        ("concept_name", "concept"),
        ("concept_concepticon_gloss", "concepticon_gloss"),
        ("concept_concepticon_id", "concepticon_id"),
        )
    )

D = {0: [c for c in wordlist.columns]}  # defines the header
for idx in wordlist:
    if wordlist[idx, "doculect"] == "Kaxarari":
        D[idx] = [wordlist[idx, c] for c in D[0]]

wlnew = Wordlist(D)
wlnew.output('tsv', filename='kaxarari')
