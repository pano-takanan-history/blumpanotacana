"""
Module computes the occurrences of concepts and
filters the conceptlist according to a certain threshold.
"""
import csv
import re
from collections import Counter
from pathlib import Path
from csvw.dsv import UnicodeDictReader
from lingpy import Wordlist
from lingpy.compare.sanity import average_coverage
from lingpy.compare.util import mutual_coverage_check


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
        "language_glottocode"
        ),
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


unique_combinations = []
count_parameters = {}
for entry in wordlist:
    if wordlist[entry, "core"] == "1":
        comb = [wordlist[entry, "doculect"], wordlist[entry, "concepticon_gloss"]]
        if comb not in unique_combinations:
            unique_combinations.append(comb)

            count_parameters[comb[1]] = count_parameters.get(comb[1], 0) + 1

filtered_params = []
for concept in count_parameters:
    if count_parameters[concept] > 10:
        filtered_params.append(concept)

language_count = {}
D = {0: [c for c in wordlist.columns]}  # defines the header
for idx in wordlist:
    if wordlist[idx, "concepticon_gloss"] in filtered_params:
        if wordlist[idx, "core"] == "1":
            wordlist[idx, "doculect"] = re.sub("_IDS", "", wordlist[idx, "doculect"])

            if wordlist[idx, "doculect"] in language_count:
                language_count[wordlist[idx, "doculect"]] += 1
            else:
                language_count[wordlist[idx, "doculect"]] = 1

            D[idx] = [wordlist[idx, c] for c in D[0]]


wlnew = Wordlist(D)
print(
    f"Wordlist has {wlnew.width} languages and {len(filtered_params)} concepts across {len(wlnew)} rows."
    )

# Mutual coverage
for i in range(wlnew.height, 0, -1):
    if mutual_coverage_check(wlnew, i):
        print(
            "Minimal mutual coverage is at {0} concept pairs.".format(i))
        break

# average coverage
print('{0:.2f}'.format(average_coverage(wlnew)))

conceptlist = "etc/concepts.tsv"
concepts_out = []
with UnicodeDictReader(conceptlist, delimiter='\t') as reader:
    for line in reader:
        concepts[line["CONCEPTICON_ID"]] = line['CONCEPTICON_GLOSS']
        concepts_out.append([
            line["CONCEPTICON_ID"],
            line["CONCEPTICON_GLOSS"],
            line["ENGLISH"],
            line["SPANISH"],
            line["PORTUGUESE"]
        ])

# output structure
filtered = [[
    "CONCEPTICON_ID",
    "CONCEPTICON_GLOSS",
    "ENGLISH",
    "SPANISH",
    "PORTUGUESE"
]]

# custom additions below threshold
protected = [
    "SPIDER WEB",
    "TREE STUMP",
    "WAVE",
    "MENSTRUATE",
    "VULVA",
    "SUCKLE (BREASTFEED, NURSE)",
    "TRAP (CATCH)",
    "BETWEEN",
    "BLOOM",
    "CLOUDY",
    "VAGINA",
    "DEAD"
]

for item in concepts_out:
    if item[1] not in filtered_params and item[1] not in protected:
        filtered.append(item)

with open('raw/scripts/filtered_concepts.tsv', 'w', encoding="utf8") as csvfile:
    writer = csv.writer(csvfile, delimiter="\t")
    writer.writerows(filtered)
