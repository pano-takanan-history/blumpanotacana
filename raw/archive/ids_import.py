"""
Download and convert data from IDS for PanoTacanan languages.
"""
from pathlib import Path
from lingpy import Wordlist
from lingpy.compare.util import mutual_coverage_check


wl = Wordlist.from_cldf(
    Path("../../git_resources/idssegmented", "cldf", "cldf-metadata.json").as_posix(),
    columns=(
        "form",
        "segments",
        "language_name",
        "language_family",
        "concept_name",
        "concept_concepticon_id",
        "concept_concepticon_gloss",
        "language_glottocode"),
    namespace=(
        ("language_name", "doculect"),
        ("language_glottocode", "glottocode"),
        ("language_family", "family"),
        ("concept_name", "concept"),
        ("concept_concepticon_gloss", "concepticon_gloss"),
        ("concept_concepticon_id", "concepticon_id"),
        )
)

FAM = {"Pano-Tacanan"}
LANGS = {"Mosetén", "Movima", "Chipaya"}
EXCLUDE = {
    "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY",
    "FRIDAY", "SATURDAY", "SUNDAY",
    "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN",
    "EIGHT", "NINE", "TEN", "ELEVEN", "TWELVE", "HUNDRED",
    "THOUSAND", "FIRST", "SECOND", "THIRD", "HORSE"
    }

D = {0: [c for c in wl.columns]}  # defines the header
for idx in wl:
    if (wl[idx, "family"] in FAM or wl[idx, "doculect"] in LANGS):
        if wl[idx, "concepticon_gloss"] not in EXCLUDE:
            D[idx] = [wl[idx, c] for c in D[0]]

wlnew = Wordlist(D)

wlnew.output(
    'tsv',
    filename='raw/ids_import'
    )

print(f"Wordlist has {wlnew.width} languages and {wlnew.height} concepts across {len(wlnew)} rows.")

for i in range(wlnew.height, 0, -1):
    if mutual_coverage_check(wlnew, i):
        print(
            f"Minimal mutual coverage is at {i} concept pairs.")
        break
