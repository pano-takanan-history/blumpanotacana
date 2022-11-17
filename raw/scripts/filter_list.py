import csv
from csvw.dsv import UnicodeDictReader
from lingpy import Wordlist


concepts = {}
PATH = "etc/concepts.tsv"
with UnicodeDictReader(PATH, delimiter='\t') as reader:
    for line in reader:
        concepts[line["CONCEPTICON_GLOSS"]] = line['CONCEPTICON_ID']


blumpanotacana = Wordlist("raw/Amahuaca.tsv")

filtered_list = [[
    "ID", "DOCULECT", "CONCEPTICON_ID", "CONCEPTICON_GLOSS", "SPANISH", "FORM"
    ]]
ID = 0

for idx, toks in blumpanotacana.iter_rows('form'):
    # print(idx, toks)
    # print(blumpanotacana[idx])
    if blumpanotacana[idx][1] in concepts:
        # print(blumpanotacana[idx])
        ID += 1
        entry = [
            ID,
            "Amahuaca",
            concepts[blumpanotacana[idx][1]],
            blumpanotacana[idx][1],
            blumpanotacana[idx][3],
            blumpanotacana[idx][2]
        ]
        filtered_list.append(entry)

with open('raw/Amahuaca_filtered.tsv', 'w', encoding="utf8") as file:
    writer = csv.writer(file, delimiter="\t")
    writer.writerows(filtered_list)
