import csv
from csvw.dsv import UnicodeDictReader
from collections import defaultdict


langs = defaultdict()
with UnicodeDictReader("etc/languages.tsv", delimiter='\t') as reader:
    for line in reader:
        langs[line["ID"]] = [
            line['ID']
        ]

stays = []
excluded = []
with open("raw/filtered_raw_new.tsv", 'r', encoding="utf8") as doc:
    raw_data = csv.reader(doc, delimiter="\t")
    count = 0
    for item in raw_data:
        if item[1] in langs:
            count += 1
            item[0] = count
            stays.append(item)

        else:
            excluded.append(item)

# print(stays)

with open("raw/filtered_raw_new.tsv", 'w', encoding="utf8") as file:
    writer = csv.writer(file, delimiter="\t")
    writer.writerows(stays)

with open("raw/archive/further_exclusions.tsv", 'w', encoding="utf8") as file:
    writer = csv.writer(file, delimiter="\t")
    writer.writerows(excluded)
