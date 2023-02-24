import attr
from collections import defaultdict
import pathlib
from clldutils.misc import slug
from pylexibank import Dataset as BaseDataset
from pylexibank import progressbar as pb
from pylexibank import Concept


@attr.s
class CustomConcept(Concept):
    Spanish_Gloss = attr.ib(default=None)
    Portuguese_Gloss = attr.ib(default=None)


class Dataset(BaseDataset):
    dir = pathlib.Path(__file__).parent
    id = "blumpanotacana"
    concept_class = CustomConcept

    def cmd_makecldf(self, args):
        # add bib
        args.writer.add_sources()
        args.log.info("added sources")

        # add concept
        concepts = {}
        for concept in self.concepts:
            idx = slug(concept["ENGLISH"])
            args.writer.add_concept(
                    ID=idx,
                    Name=concept["ENGLISH"],
                    Spanish_Gloss=concept["SPANISH"],
                    Portuguese_Gloss=concept["PORTUGUESE"],
                    Concepticon_ID=concept["CONCEPTICON_ID"],
                    Concepticon_Gloss=concept["CONCEPTICON_GLOSS"]
                    )
            concepts[concept["CONCEPTICON_GLOSS"]] = idx
        args.log.info("added concepts")

        # add language
        languages = {}
        sources = defaultdict()
        for language in self.languages:
            args.writer.add_language(
                    ID=language["ID"],
                    Name=language["Name"],
                    Glottocode=language["Glottocode"]
                    )
            languages[language["ID"]] = language["Name"]
            sources[language["ID"]] = language["Source"]
        args.log.info("added languages")

        # read in data
        data = self.raw_dir.read_csv(
            "raw.tsv", delimiter="\t", dicts=True
        )
        # add data
        idx = 1
        for entry in pb(data, desc="cldfify", total=len(data)):
            print(entry)
            args.writer.add_forms_from_value(
                ID=idx,
                Parameter_ID=concepts[entry["CONCEPTICON_GLOSS"]],
                Language_ID=entry["DOCULECT"],
                Value=entry["VALUE"],
                Source=sources[entry["DOCULECT"]]
            )
