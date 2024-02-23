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

prepare_gb:
	git clone https://github.com/grambank/grambank --branch v1.0.3 grambank
	cldf createdb grambank/cldf/StructureDataset-metadata.json grambank.sqlite3

combine:
	python s_combine.py