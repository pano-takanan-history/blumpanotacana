from __future__ import unicode_literals, print_function, division
from lingpy import Wordlist, LexStat, Alignments
from lexibank_blumpanotacana import Dataset as BPT
from lingpy.compare.partial import Partial
from lexibase.lexibase import LexiBase


# load the wordlist
ds = BPT()

wl = Wordlist.from_cldf(
    str(ds.cldf_dir.joinpath("cldf-metadata.json").as_posix()),
    # columns to be loaded from CLDF set
    columns=(
        "language_id",
        "language_family",
        "language_subgroup",
        "concept_name",
        "segments",
        "form",
        "value",
        "comment",
        "source"
        ),
    # a list of tuples of source and target
    namespace=(
        ("language_id", "doculect"),
        ("language_family", "family"),
        ("language_subgroup", "subgroup"),
        ("concept_name", "concept"),
        ("segments", "tokens")
        )
    )


# count number of languages, number of rows, number of concepts
print(
    "Wordlist has {0} languages and {1} concepts across {2} rows.".format(
        wl.width, wl.height, len(wl)))

lex = Partial(wl, segments='tokens', check=False)
lex.partial_cluster(method='sca', threshold=0.55, ref="cogids")

lex = Alignments(lex, ref="cogids")
lex.align(ref="cogids")

lex = LexStat(lex, segments='tokens', check=False)
lex.get_scorer(runs=10000)
lex.cluster(method='lexstat', threshold=0.55, ref="cogid")

lex = LexiBase(lex, dbase="edictor/blumpanotacana.sqlite3")
lex.create("blumpanotacana")
lex.output('tsv', filename='edictor/blumpanotacana')
