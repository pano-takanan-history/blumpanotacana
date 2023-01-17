import csv
from csvw.dsv import UnicodeDictReader
from pathlib import Path
from lingpy import Wordlist


concepts = {}
PATH = "etc/concepts.tsv"
with UnicodeDictReader(PATH, delimiter='\t') as reader:
    for line in reader:
        concepts[line["CONCEPTICON_GLOSS"]] = line['CONCEPTICON_ID']


addition = Wordlist.from_cldf(
    Path("../zariquieyisconahua", "cldf", "cldf-metadata.json").as_posix(),
    columns=(
        "form",
        "segments",
        "language_id",
        "language_family",
        "concept_name",
        "concept_concepticon_id",
        "concept_concepticon_gloss",
        "language_glottocode"),
    namespace=(
        ("language_id", "doculect"),
        ("language_glottocode", "glottocode"),
        ("language_family", "family"),
        ("concept_name", "concept"),
        ("concept_concepticon_gloss", "concepticon_gloss"),
        ("concept_concepticon_id", "concepticon_id"),
        )
    )
new_data = []
for idx in addition:
    if addition[idx, "concepticon_gloss"] in concepts:
        new_data.append([
            "",
            addition[idx, "doculect"],
            addition[idx, "concepticon_id"],
            addition[idx, "concepticon_gloss"],
            addition[idx, "form"]
        ])


with open('raw/bptfiltered.tsv', 'w', encoding="utf8") as file:
    writer = csv.writer(file, delimiter="\t")
    writer.writerows(new_data)
