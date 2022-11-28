import csv
from csvw.dsv import UnicodeDictReader
from collections import defaultdict



def add_existing(wordlist, conceptlist, doculect):
    out_list = []

    concepts = defaultdict()
    with UnicodeDictReader(conceptlist, delimiter='\t') as reader:
        for line in reader:
            concepts[line['SPANISH']] = [
                line["CONCEPTICON_ID"],
                line['CONCEPTICON_GLOSS']
            ]

    with UnicodeDictReader(wordlist, delimiter='\t') as doc:
        for idx in doc:
            # print(idx)
            if idx["Gloss"] in concepts:
                # print(idx["CONCEPT"])
                # print(concepts[idx["CONCEPT"]][0])

                out_list.append([
                    "",
                    doculect,
                    concepts[idx["Gloss"]][0],
                    concepts[idx["Gloss"]][1],
                    idx["Value"]
                ])

    return out_list


doculect = "Sharanahua"
wordlist = "../../../zariquieyisconahua/raw/archive/full_extraction.tsv"
conceptlist = "../missing/missing_" + doculect + ".tsv"

output = add_existing(wordlist, conceptlist, doculect)

out_path = "../additions/auto_" + doculect + ".tsv"
with open(out_path, 'w', encoding="utf8") as file:
    writer = csv.writer(file, delimiter="\t")
    writer.writerows(output)
