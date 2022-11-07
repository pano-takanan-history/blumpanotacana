import csv
from cldfcatalog import Config
from csvw.dsv import UnicodeDictReader
from collections import defaultdict

repos = Config.from_file().get_clone('concepticon')
paths = {p.stem.split('-')[1]: p for p in repos.joinpath(
    'mappings').glob('map-*.tsv')}
mappings = {}

for language, path in paths.items():
    mappings[language] = defaultdict(set)

PATH_ES = "../../../git_resources/concepticon-data/mappings/map-es.tsv"
PATH_PT = "../../../git_resources/concepticon-data/mappings/map-pt.tsv"

list_maps = [
    (PATH_ES, "es"),
    (PATH_PT, "pt")
    ]

for lang in list_maps:
    with UnicodeDictReader(lang[0], delimiter='\t') as reader:
        for line in reader:
            # print(line)
            gloss = line['GLOSS'].split('///')[1]
            mappings[lang[1]][line['ID']] = gloss

# print(mappings)
# for x in mappings["es"]:
#     print(x, mappings["es"][x])
# for x in mappings["pt"]:
#     print(x, mappings["pt"][x])

ptdata = defaultdict(list)


concept_dic = {}
with open(
    '../../../git_resources/concepticon-data/concepticondata/concepticon.tsv',
    mode='r', encoding="utf8"
    ) as file:
    data = csv.reader(file, delimiter="\t")
    for line in data:
        concept_dic[line[0]] = line[1]
# print(concept_dic)


mapped_concepts = [
    ["CONCEPTICON_ID", "CONCEPTICON_GLOSS", "ENGLISH", "SPANISH", "PORTUGUESE"]
    ]

with UnicodeDictReader('concepts_old.tsv', delimiter='\t') as reader:
    for i, line in enumerate(reader):
        if line['CONCEPTICON_ID'] in mappings['es']:
            line["SPANISH"] = mappings['es'][line['CONCEPTICON_ID']]
        else:
            line["SPANISH"] = ""

        if line['CONCEPTICON_ID'] in mappings['pt']:
            # print(line)
            line["PORTUGUESE"] = mappings['pt'][line['CONCEPTICON_ID']]
        else:
            line["PORTUGUESE"] = ""
        entry = []
        for x in line:
            entry.append(line[x])

        mapped_concepts.append(entry)

with open('concepts.tsv', 'w', encoding="utf8") as file:
    writer = csv.writer(file, delimiter='\t')
    writer.writerows(mapped_concepts)
