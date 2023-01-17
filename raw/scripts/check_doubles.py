import csv
from pathlib import Path
from lingpy import Wordlist

concepts = [
	"680", "2030"
	"1920", "2374"
	"1228", "3603"
	"1879", "3472"
	"1309", "1828"
	"785", "3188"
	"763", "2613"
	"1586", "1587", "2124"
	"1415", "2271"
	"750", "2866", "1280"
	"2117", "1784"
	"2486", "602"
	"143", "1726", "2324"
	"3603", "1228"
	"3452", "1198"
	"3913", "879"
	"1229", "2112", "2113"
]

wordlist = Wordlist.from_cldf(
    Path("cldf", "cldf-metadata.json").as_posix(),
    columns=(
        "form",
        "doculect",
        "language_core",
        "concept_concepticon_id",
        "concept_concepticon_gloss",
        "concept"
        ),
    namespace=(
        ("language_core", "core"),
        ("concept_concepticon_gloss", "concepticon_gloss"),
        ("concept_concepticon_id", "concepticon_id"),
        )
    )

analyze = []
for entry in wordlist:
    print(wordlist[entry, "concepticon_id"])
    if wordlist[entry, "core"] == "1" and wordlist[entry, "concepticon_id"] in concepts:
        print(wordlist[entry, "concepticon_id"])
        analyze.append(wordlist[entry])

with open("raw/check_concepts.tsv", 'w', encoding="utf8") as file:
    writer = csv.writer(file, delimiter="\t")
    writer.writerows(analyze)
