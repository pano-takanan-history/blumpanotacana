import csv
from pathlib import Path
from lingpy import Wordlist
from collections import Counter

concepts = Counter()

wordlist = Wordlist.from_cldf(
    Path("cldf", "cldf-metadata.json").as_posix(),
    columns=(
        "form",
        "segments",
        "language_id",
        "language_family",
        "language_core",
        "concept_name",
        "concept_concepticon_id",
        "concept_concepticon_gloss",
        "language_glottocode"),
    namespace=(
        ("language_core", "core"),
        ("language_id", "doculect"),
        ("language_glottocode", "glottocode"),
        ("language_family", "family"),
        ("concept_name", "concept"),
        ("concept_concepticon_gloss", "concepticon_gloss"),
        ("concept_concepticon_id", "concepticon_id"),
        )
    )


D = {0: [c for c in wordlist.columns]}  # defines the header
for idx in wordlist:
    if wordlist[idx, "core"] == 1:
        D[idx] = [wordlist[idx, c] for c in D[0]]
        concepts[wordlist[idx, "concepticon_gloss"]] += 1

    # print(wordlist[idx])

wlnew = Wordlist(D)
print(concepts)

with open('concepts.tsv', 'w', encoding="utf8") as csvfile:
    writer = csv.writer(csvfile, delimiter="\t")
    for key, value in concepts.items():
        writer.writerow([key] + [value])
