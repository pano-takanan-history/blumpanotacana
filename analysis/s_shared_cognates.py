"""
Producing heatmaps for comparison of shared cognacy.
"""
import argparse
import re
import matplotlib as mpl
from lingpy import LexStat, Alignments, Wordlist
from lingpy.convert.plot import plot_heatmap
from lingpy.read.qlc import reduce_alignment
from lingpy.sequence.sound_classes import tokens2class
from lingrex.copar import CoPaR
from lingrex.util import prep_wordlist


def clean_slash(x):
    """Cleans slash annotation from EDICTOR."""
    cleaned = []
    for segment in x:
        if "/" in segment:
            after_slash = re.split("/", segment)[1]
            cleaned.append(after_slash)
        else:
            cleaned.append(segment)

    return cleaned


def shared_cog(lng_a, lng_b, wlist):
    """Computes the shared cognates between languages."""
    cognate_pairs = 501
    same_cogid = 0

    pairs = (lng_a, lng_b) if (lng_a, lng_b) in wlist.pairs else (lng_b, lng_a)
    for idx_a, idx_b in wlist.pairs[pairs]:
        if wlist[idx_a, 'cogid'] == wlist[idx_b, 'cogid']:
            same_cogid += 1

    if same_cogid != 0 and cognate_pairs != 0:
        shared_cognates = same_cogid/cognate_pairs
    else:
        shared_cognates = 0
    print(lng_a, lng_b, shared_cognates)
    return shared_cognates


def create_plot(setting="cognate", only_pano=True):
    wl = Wordlist.from_cldf(
        "../cldf/cldf-metadata.json",
        # columns to be loaded from CLDF set
        columns=(
            "language_id",
            "language_core",
            "language_subgroup",
            "concept_name",
            "cognacy",
            "segments",
            "form"
            ),
        # a list of tuples of source and target
        namespace=(
            ("language_id", "doculect"),
            ("language_subgroup", "subgroup"),
            ("concept_name", "concept"),
            ("segments", "tokens"),
            ("cognacy", "cogid")
            )
        )

    # Select Pano subset only
    if only_pano is True:
        D = {0: list(wl.columns)}
        for idx in wl:
            if wl[idx, "subgroup"] == "Pano":
                D[idx] = [wl[idx, c] for c in D[0]]
        wl = Wordlist(D)

    wl = prep_wordlist(wl)
    alms = Alignments(wl, ref="cogid", transcription="tokens")

    dct = {}
    for idx, msa in alms.msa["cogid"].items():
        msa_reduced = []
        for site in msa["alignment"]:
            reduced = reduce_alignment([site])[0]
            reduced = clean_slash(reduced)
            msa_reduced.append(reduced)
        for i, row in enumerate(msa_reduced):
            dct[msa["ID"][i]] = row

    alms.add_entries("tokens", dct,
                    lambda x: " ".join([y for y in x if y != "-"]),
                    override=True)
    alms.add_entries("alignment", dct,
                    lambda x: " ".join([y for y in x]),
                    override=True)
    alms.add_entries("structure", "tokens",
                    lambda x: tokens2class(x.split(" "), "cv"))

    alms.output("tsv", filename="bpt_alg")
    #######

    cop = CoPaR("bpt_alg.tsv", transcription="form", ref="cogid", min_refs=3)
    cop.get_sites()
    cop.cluster_sites()
    cop.sites_to_pattern()
    cop.calculate("tree")
    TREE = str(cop.tree)

    cop_wl = LexStat(cop)
    matrix = [[0 for i in cop_wl.language] for j in cop_wl.language]

    description = "Shared cognacy between language pairs"

    visited = []
    for j, lang_a in enumerate(cop_wl.language):
        for k, lang_b in enumerate(cop_wl.language):
            if (lang_a, lang_b) not in visited:
                if j < k:
                    matrix[j][k] = shared_cog(lang_a, lang_b, cop_wl)
                    matrix[k][j] = shared_cog(lang_a, lang_b, cop_wl)
                elif j == k:
                    matrix[j][k] = 1
            visited.append((lang_a, lang_b))

    outputname = "shared_" + setting

    plot_heatmap(cop_wl, filename=outputname, tree=TREE,
                 vmin=0.0, vmax=0.25, cmap=mpl.colormaps['viridis'],
                 colorbar_label=description, matrix=matrix,
                 )


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-pano",
                        action='store_true',
                        help="Choose if you want to compute the heatmaps only for Panoan languages.")
    args = parser.parse_args()
    create_plot("cognates", only_pano=args.pano)
