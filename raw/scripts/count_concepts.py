import csv
import re
from pathlib import Path
from lingpy import Wordlist
from collections import Counter
from lingpy.compare.sanity import average_coverage

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


# D = {0: [c for c in wordlist.columns]}  # defines the header
# for idx in wordlist:
#     # print(wordlist[idx, "core"])
#     if wordlist[idx, "core"] == 1:
#         print("wup")
#     D[idx] = [wordlist[idx, c] for c in D[0]]
#     concepts[wordlist[idx, "concepticon_gloss"]] += 1
# wlnew = Wordlist(D)

unique_combinations = []
count_parameters = {}
for entry in wordlist:
    if wordlist[entry, "core"] == "1":
        comb = [wordlist[entry, "doculect"], wordlist[entry, "concepticon_gloss"]]
        if comb not in unique_combinations:
            unique_combinations.append(comb)

            count_parameters[comb[1]] = count_parameters.get(comb[1], 0) + 1
# print(concepts)

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

# print(language_count)
wlnew = Wordlist(D)
print(
    f"Wordlist has {wlnew.width} languages and {len(filtered_params)} concepts across {len(wlnew)} rows."
    )

from lingpy.compare.util import mutual_coverage_check
for i in range(wlnew.height, 0, -1):
    if mutual_coverage_check(wlnew, i):
        print(
            "Minimal mutual coverage is at {0} concept pairs.".format(i))
        break
from lingpy.compare.sanity import average_coverage
print('{0:.2f}'.format(average_coverage(wlnew)))

# with open('raw/scripts/concepts.tsv', 'w', encoding="utf8") as csvfile:
#     writer = csv.writer(csvfile, delimiter="\t")
#     for key, value in count_parameters.items():
#         writer.writerow([key] + [value])
