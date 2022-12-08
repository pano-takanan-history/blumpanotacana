import csv
import itertools
from lingpy import Alignments, Wordlist
from lingrex.copar import CoPaR
from lingrex.util import add_structure


bpt_data = Wordlist('raw/analysis/bpt-lexstat.tsv')

# create Alignments object from Wordlist object
almsB = Alignments(bpt_data, ref="cogid", transcription="ipa")

almsB.align()
add_structure(almsB)
copB = CoPaR(almsB, ref="cogid", transcription="ipa")
copB.get_sites()
copB.cluster_sites()
copB.sites_to_pattern()


dic_langs = {}
for _, vals in copB.clusters.items():
    if len(vals) > 1:
        for x in vals:
            for item in copB.msa["cogid"][x[0]]["ID"]:
                # print(copB[item])
                COGID = str(copB[item, "cogid"])
                if COGID in dic_langs:
                    if copB[item, "doculect"] not in dic_langs[COGID]:
                        dic_langs[COGID].append(copB[item, "doculect"])
                else:
                    dic_langs[COGID] = [copB[item, "doculect"]]

interest = [
    "Moseten",
    # "Chipaya",
    # "Movima"
    ]

final_list = []
for key in dic_langs:
    if len(dic_langs[key]) > 1:
        for lang in interest:
            if lang in dic_langs[key]:
                if [len(dic_langs[key]), key, dic_langs[key]] not in final_list:
            # print(len(dic_langs[key]), key, dic_langs[key])
                    final_list.append([
                        len(dic_langs[key]), key, dic_langs[key]
                    ])

# list(product(*dictionary.values()))
unique_names = set(itertools.chain.from_iterable(dic_langs))
# Get all combinations of pairs
all_pairs = list(itertools.combinations(unique_names, 2))
# Create the dictionary
result = {pair: len([x for x in unique_names if set(pair) <= set(x)]) for pair in all_pairs}

with open('raw/analysis/language_table.csv', 'w', encoding="utf8") as file:
    writer = csv.writer(file)
    writer.writerows(final_list)
