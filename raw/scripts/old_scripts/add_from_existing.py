import csv
from csvw.dsv import UnicodeDictReader
from collections import defaultdict
from lingpy import Wordlist


def add_existing_dic(wordlist, conceptlist, doculect):
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


def add_existing_ids(wordlist, conceptlist, doculect):
    out_list = []

    concepts = defaultdict()
    with UnicodeDictReader(conceptlist, delimiter='\t') as reader:
        for line in reader:
            concepts[line['CONCEPTICON_GLOSS']] = [
                line["CONCEPTICON_ID"]
            ]

    doc = Wordlist(wordlist)
    for idx in doc:
        # print(doc[idx])
        if doc[idx, "CONCEPTICON_GLOSS"] in concepts and doc[idx, "DOCULECT"] == doculect:
            print(doc[idx, "CONCEPTICON_GLOSS"])
            # print(concepts[doc[idx, "CONCEPT"]][0])

            out_list.append([
                "",
                doculect,
                concepts[doc[idx, "CONCEPTICON_GLOSS"]][0],
                doc[idx, "CONCEPTICON_GLOSS"],
                doc[idx, "FORM"]
            ])

    return out_list


doculect = "Sharanahua"
conceptlist = "raw/missing/missing_" + doculect + ".tsv"

# wordlist = "../scottsharanahua/raw/full_extraction.tsv"
# output = add_existing_dic(wordlist, conceptlist, doculect)

wordlist = "raw/archive/additions/ids_import.tsv"
output = add_existing_ids(wordlist, conceptlist, doculect)

out_path = "raw/missing/auto_" + doculect + ".tsv"
with open(out_path, 'w', encoding="utf8") as file:
    writer = csv.writer(file, delimiter="\t")
    writer.writerows(output)
