from collections import defaultdict
from pathlib import Path
from lingpy import Wordlist
from lingpy.compare.sanity import average_coverage
from lingpy.compare.util import mutual_coverage_check


pth = Path(".")
wl = Wordlist.from_cldf(
    pth.joinpath("cldf", "cldf-metadata.json"),
    # columns to be loaded from CLDF set
    columns=(
        "language_id",
        "language_core",
        "concept_name",
        "segments",
        "form"
        ),
    # a list of tuples of source and target
    namespace=(
        ("language_id", "doculect"),
        ("concept_name", "concept"),
        ("segments", "tokens")
        )
    )

syns = defaultdict()
lang_count = defaultdict()
covered = []
for item in wl:
    checkup = [
        wl[item, "doculect"],
        wl[item, "concept"]
        ]
    if wl[item, "doculect"] != "Kaxararidasdas":
        if checkup[0] not in syns:
            syns[checkup[0]] = 0
            lang_count[checkup[0]] = 0
        if checkup in covered:
            syns[checkup[0]] = syns[checkup[0]] + 1
        else:
            lang_count[checkup[0]] = lang_count[checkup[0]] + 1
            covered.append(checkup)

covs = 0
syno = 0
for x in syns:
    coverage = round((lang_count[x] / 501), 2)
    covs += coverage
    synonyms = round(((syns[x]+lang_count[x]) / lang_count[x]), 2)
    syno += synonyms
    print("---")
    print("Language:", x)
    print("Total coverage", coverage)
    print("Synonyms:", synonyms)

print("---")
print("Coverage:", covs/21)
print("Synonyms:", syno/21)
print("Average:", '{0:.2f}'.format(average_coverage(wl)))
for i in range(wl.height, 0, -1):
    if mutual_coverage_check(wl, i):
        print(
            "Minimal mutual coverage is at {0} concept pairs.".format(i))
        break
