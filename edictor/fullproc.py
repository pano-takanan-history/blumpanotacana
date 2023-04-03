from lingpy import Wordlist, LexStat, Alignments
from lingpy.compare.partial import Partial
from lexibase.lexibase import LexiBase


def run(wordlist):

    D = {0: wordlist.columns}
    for idx in wordlist:
        D[idx] = [wordlist[idx, h] for h in D[0]]
    wl = Wordlist(D)

    lex = Partial(wl, segments='tokens', check=False)
    lex.partial_cluster(method='sca', threshold=0.4, ref="cogids")

    lex = Alignments(lex, ref="cogids")
    lex.align(ref="cogids")

    lex = LexStat(lex)
    lex.get_scorer(runs=10000)
    lex.cluster(threshold=0.55, method="lexstat", cluster_method="infomap", ref="cogid")

    D = {0: wordlist.columns+["cogids", "cogid", "alignment"]}
    for idx in lex:
        D[idx] = [lex[idx, h] for h in D[0]]

    wl = Wordlist(D)
    lex = LexiBase(wl, dbase="blumpanotacana.sqlite3")
    lex.create("blumpanotacana")

    return wl
