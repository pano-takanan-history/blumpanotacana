import csv
from csvw.dsv import UnicodeDictReader
from collections import defaultdict


def find_missing_data(lang, conceptlist, wordlist):
    """
    This function computes the missing data for a wordlist
    given a mapped conceptlist.
    """
    concepts = defaultdict()
    with UnicodeDictReader(conceptlist, delimiter='\t') as reader:
        for line in reader:
            concepts[line["CONCEPTICON_ID"]] = [
                line['CONCEPTICON_GLOSS'],
                line['ENGLISH'],
                line['SPANISH'],
                line['PORTUGUESE']
            ]

    data = defaultdict()
    with open(wordlist, 'r', encoding="utf8") as doc:
        raw_data = csv.reader(doc, delimiter="\t")
        for item in raw_data:
            # check if lang is in data
            if item[1] not in data:
                # add concepticon GLOSS to lang
                data[item[1]] = [item[2]]
            else:
                data[item[1]].append(item[2])

    missing_concepts = [[
        "DOCULECT", "CONCEPTICON_ID", "CONCEPTICON_GLOSS",
        "ENGLISH", "SPANISH", "PORTUGUESE", "FORM"
        ]]

    for concept in concepts:
        if concept not in data[lang]:
            entry = [
                lang,
                concept,
                concepts[concept][0],
                concepts[concept][1],
                concepts[concept][2],
                concepts[concept][3],
                ""
                ]
            missing_concepts.append(entry)

    return missing_concepts
# for entry in missing_concepts:
#     print(entry)


LANG = "Araona"
CONCEPTS = "etc/concepts.tsv"
DATA = 'raw/raw.tsv'

missing_data = find_missing_data(LANG, CONCEPTS, DATA)
PATH = "raw/missing_" + str(LANG) + ".tsv"

with open(PATH, 'w', encoding="utf8") as file:
    writer = csv.writer(file, delimiter="\t")
    writer.writerows(missing_data)
