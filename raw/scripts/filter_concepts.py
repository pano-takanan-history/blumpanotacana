import csv
from csvw.dsv import UnicodeDictReader
from collections import defaultdict


def filter_concepts(conceptlist, filter, data):
    exclude = defaultdict()
    with UnicodeDictReader(filter, delimiter='\t') as reader:
        for line in reader:
            exclude[line["CONCEPTICON_ID"]] = line['CONCEPTICON_GLOSS']

    concepts = defaultdict()
    concepts_out = [[
        "CONCEPTICON_ID",
        "CONCEPTICON_GLOSS",
        "ENGLISH",
        "SPANISH",
        "PORTUGUESE"
    ]]

    with UnicodeDictReader(conceptlist, delimiter='\t') as reader:
        for line in reader:
            if line["CONCEPTICON_ID"] not in exclude:
                concepts[line["CONCEPTICON_ID"]] = line['CONCEPTICON_GLOSS']
                concepts_out.append([
                    line["CONCEPTICON_ID"],
                    line["CONCEPTICON_GLOSS"],
                    line["ENGLISH"],
                    line["SPANISH"],
                    line["PORTUGUESE"]
                ])

    filtered = [[
        "ID",
        "DOCULECT",
        "CONCEPTICON_ID",
        "CONCEPTICON_GLOSS",
        "VALUE"
    ]]

    excluded = [[
        "ID",
        "DOCULECT",
        "CONCEPTICON_ID",
        "CONCEPTICON_GLOSS",
        "VALUE"
    ]]

    with open(data, 'r', encoding="utf8") as doc:
        raw_data = csv.reader(doc, delimiter="\t")
        for item in raw_data:
            print(item)
            if item[2] in concepts:
                filtered.append(item)
            else:
                excluded.append(item)

    return filtered, excluded, concepts_out


conceptlist = "etc/concepts.tsv"
fil_concepts = "etc/old/excluded_concepts.tsv"
data = "raw/filtered_raw_new.tsv"

filtered, excluded, concepts = filter_concepts(conceptlist, fil_concepts, data)

with open("raw/filtered_raw_new.tsv", 'w', encoding="utf8") as file:
    writer = csv.writer(file, delimiter="\t")
    writer.writerows(filtered)

with open("raw/archive/excluded_data.tsv", 'w', encoding="utf8") as file:
    writer = csv.writer(file, delimiter="\t")
    writer.writerows(excluded)

# with open("etc/concepts.tsv", 'w', encoding="utf8") as file:
#     writer = csv.writer(file, delimiter="\t")
#     writer.writerows(concepts)
