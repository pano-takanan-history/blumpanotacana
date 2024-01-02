wordlist:
	edictor wordlist --name=d_blumpanotacana --data=../cldf/cldf-metadata.json --preprocessing=s_realign.py --addon="language_subgroup:subgroup","cognacy:cogid","partial_cognacy:cogids","morphemes:morphemes","borrowing:borrowing","comment:note"

coverage:
	python s_compute_coverage.py

heatmap:
	python s_shared_cognates.py

map:
	Rscript map.R

patterns:
	make patterns
