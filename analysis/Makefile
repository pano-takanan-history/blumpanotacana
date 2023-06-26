wordlist:
	edictor wordlist --name=d_blumpanotacana --data=../cldf/cldf-metadata.json --preprocessing=s_realign.py --addon="language_subgroup:subgroup","cognacy:cogid","partial_cognacy:cogids","morphemes:morphemes","borrowing:borrowing","comment:note"

wordlist-auto:
	edictor wordlist --name=d_bpt-auto --data=../cldf/cldf-metadata.json --preprocessing=s_autocogid.py --addon="cognacy:cogid","Partial_Cognacy:cogids","alignment:alignment"

coverage:
	python s_compute_coverage.py
