# Analysis: How to replicate the code from the paper

This folder contains a series of files that have been used for the database paper. The necessary commands are all stored in a Makefile, that can be run directly from the command line. We present three features:

1. Creating a tsv-wordlist from the data
2. Compute the coverage and synonymy across languages
3. Create heatmaps of shared cognacy and shared regularity

## Create the wordlist

The first command, `make wordlist`, creates a tsv-based wordlist that can be used with EDICTOR (<www.digling.org/edictor>). You can also open the data directly in EDICTOR using the following link: <https://lingulist.de/edev/?file=blumpanotacana.tsv&preview=500&basics=DOCULECT|CONCEPT|TOKENS|COGIDS&publish=true>

You may use this link to visualize the data, but you will not be able to manipulate any annotations online.

Note: If you don't have pyedictor installed set, you can do so running the command `pip install pyedictor` from the command line.

## Compute the coverage of concepts

Running the command `make coverage` runs the script `s_compute_coverage`, that presents a count of synonymy and coverage of concepts across all languages in the database.

## Shared cognates across languages

Finally, the command `make heatmap` creates a heatmap visualizing the amount of shared cognacy between languages. For a better understandable visualization, we showcase this for the Panoan languages only. If you want to run this for the whole dataset, you can remove the `-pano` argument from the Makefile.

## Map of all languages

The R-Script `map.R` adds the code that was used to create the map `fig_map.png`.
