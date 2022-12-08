from __future__ import unicode_literals, print_function, division
from lingpy import Wordlist, LexStat, Alignments
from lingpy.convert.strings import write_nexus
from lexibank_blumpanotacana import Dataset as BPT
from lingpy.sequence.sound_classes import ipa2tokens

# load the wordlist
ds = BPT()

# wl = Wordlist.from_cldf(
#     str(ds.cldf_dir.joinpath("cldf-metadata.json").as_posix()),
#     # columns to be loaded from CLDF set
#     columns=(
#         "language_id",
#         "concept_name",
#         "segments",
#         "form"
#         ),
#     # a list of tuples of source and target
#     namespace=(
#         ("language_id", "doculect"),
#         ("concept_name", "concept")
#         )
#     )

# # count number of languages, number of rows, number of concepts
# print(
#     "Wordlist has {0} languages and {1} concepts across {2} rows.".format(
#         wl.width, wl.height, len(wl)))

# # for i in range(324, 0, -1):
# #     if mutual_coverage_check(wl, i):
# #         print("Minimal mutual coverage is at {0} concept pairs (AMC: {1:.2f}).".format(
# #             i, average_coverage(wl)))
# #         break


# wl.add_entries('segments', 'form', ipa2tokens)

# lex = LexStat(wl, segments='segments', check=False)
# lex.get_scorer(runs=10000)
# lex.cluster(method='lexstat', threshold=0.55, ref="infomap", cluster_method='infomap')
# lex.output('tsv', filename='raw/analysis/bpt-lexstat')

wl = Wordlist("raw/analysis/bpt-lexstat.tsv")
nexus = write_nexus(wl, ref='infomap', mode='splitstree', filename='raw/analysis/bpt_auto.nex')
