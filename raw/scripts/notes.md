# Thesis notes

## To-Do's

ICHL reminder 01.12.2022

## Abstracts for conferences

- Abstract 1: Regularity Checks (ICHL?)
- Abstract 2: Deep family links of Panoan, correspondences with Pano-Tac

## blumpanotacana

- possible add: 158 PUT ON, PREGNANT, NIPPLE
- possible: ceramic vessels and related adjectives
- notable exclusions for second round: Family relationships

## To-Do: Reading list

- Mattis: Partial Cognacy --> Schweikhard & List 2019
- Mattis: Fuzzy Reconstructions --> Auch mit Nathaniel
- Mattis: Interlinear Glossing
- Spielman et al: Claimed link between Yamonaman languages and P-T
check Brinton's comments on Tacana, Aymara, Pano, and Moseten

## Whom-to-thank

Mattis List
Roberto Zariquiey
Isaac Stead
Simon Greenhill (recommendations on BEAST analysis)
Christiane Bageritz, Josephine Finckh, Diana Scheffler (Library)
Iren Hartmann (organisation)
Adam Tellmann (Input on Panoan long/short forms)
Carlos and Zoe

Idea for copying structure of thesis: Otero_2018, Annika, Pache 2018

## Unclassified notes

--> kakataibo tiene gramática muy distinta al Shipibo
--> Fleck: Kapanawa y Shipibo son "dialectos"
--> Roberto: solo léxico, gramática muy distinta
--> bastante reportes entre Shipibos y Kakataibos hasta 1930
--> leave Kakataibo out of prior

Roberto confirms Chacobo+Pacahuara prior

## Timeline and plans

Possible communities for fieldwork: Kaxararí (too ambitious?), Headwaters group

- Ziel: Magna cum Laude
- [ ] Paper 1: Database (28.02.2023)
  - [ ] Finish database (31.12.2022)
    - [x] Kaufmans concept list + cognates of Girard/Oliveira
    - [x] also adding cognates of Suárez?
    - [x] Tacana data
    - [x] Mayoruna data
    - [ ] Pano data
      - [x] preliminary concept list (04.11)
      - [x] code to find missing data
      - [x] code to add Spanish and English glosses to my list
      - [x] Ferreira 2005: Matis (11.11)
        - [ ] ß is ʂ
      - [x] Loos 1998: Capanahua (18.11)
      - [x] Hyde 1980: Amahuaca (25.11)
      - [ ] Cashinawa (30.11)
      - [ ] Compute mutual coverage for 400+ languages to finalize ideas where to do Fieldwork (2.12)
    - [ ] Ortho-profiles (9.12)
    - [ ] Lexibank datasets (16.12)
- [ ] Paper 2: Check regularity of reconstructions (31.07.2023)
  - [ ] finish Proto-Panoan data
  - [ ] finish Proto-Tacanan data
  - [ ] Write code to assess regularity
  - [ ] output irregular patterns with ID of root form
- [ ] Paper 3: Sound correspondences for P-T and Moseten, Movima, Yuracare, Chipaya, Yaninama (31.12.2023)
  - [ ] get all data
  - [ ] fill holes in coverage
  - [ ] Analyze sound correspondences
  - [ ] Sound correspondences between those groups
- [ ] Paper 4: Study about deep family relationships (31.05.2024)
  - [ ] Reconstruction of Proto-Pano-Tacana
  - [ ] Comparison with at least: Mosetén, Yuracaré, Movima, Canichana (body-part prefixes!), Ayoreo, Uro, Yaminama
  - [ ] Canichana: Cardús p. 316, also extensive list in Heath 1883
- [ ] Other timelines
  - [x] GATA paper (SUBMIT THIS THING PLEASE)
  - [ ] DoReCo lengthening (31.03.2023)

## Calibrations

- Amawaka narratives: migration from the north, near border Ecuador/Peru; Urarina spoke Panoan language before
- Archaeological evidence for Ucayali arrival of Panoan speakers around 300 DC (Lathrap, Myers, etc), but unclear which groups exactly

Test hypothesis: Collapse of Conibo-Cashinahua Cumancaya state around 1000 AD (Lathrap 1985)

Izaguirre 1922: MRCA of Mayoruna, Shipiubo, Kakataibo, and Amaguacas, at least 250 years ago

## Possible small studies

Tovar 1961, p. 76: movima as chibcha language

Note: Remo of Carvalho call their language "Nucuyni"; same branch as Nukuini, possible relation between both?

## Summary of available bibliography

- Sapibokona, Reyesano and Maropa are probably the same
- Tiatinagua == Ese Ejja
Farabee p. 154: Tiatinagua have various names: Atsahuaca, Yamiaca, Guarayo, Huarayo

Tiatinawa: Farabee 1922; different from Tiatinagua by Crequi Montfort, based un unpublished material frm Nordenskioeld --> those are Chamik, subdivision of Takanan (Huarayo)
Warisa: Pater Noster on Teza (1868), closely related to Sapibokona complex (Girard 1971)
Warisa/Guariza == Reyesano, so not needed to go for this

Huarayo has no ethnic value, applied "to all savages"

Who are the canawarys?
who are the senssis? There is same data in one of the books...  --> tessmann
location of tribes in Brinton 1901, page 292

## Workflow for dic conversion

1. <https://pdf2doc.com/>
2. Convert from doc to html in LibreOffice

### Tacana

Lyon 1975: Only Arasa from Nordenskiöld might be Tacana, Atsahuaca is Pano
Confusion because of toponyms used by different groups
check atawaka and Yamiaka in Crequi-Monfort and Rivet 1913: 46-78, for more terms than Nordenskiöld

Martius: Colina (--> Marubo)
Jakway: Marubo (--> Colina)?

Notes:

- c̆
- v for  ̶b̶
- d for strikethrough d because other is only dz

## CL-tools

### cldfbench commands with version

`--concepticon-version=v3.0.0 --glottolog-version=v4.6 --clts-version=v2.2.0`

`cldfbench lexibank.init_profile lexibank_scottsharanahua.py --clts-version=v2.2.0`

`cldfbench lexibank.check_phonotactics lexibank_crossandean.py`
`cldfbench lexibank.check_profile lexibank_crossandean.py --noprofile --clts-version=v2.2.0`

### Create conceptlist from raw dictionary with `getcl`

`conceptlist --data=cldf/Dictionary-metadata.json --conceptlist=Key-2016-1310 --concepticon-version=v3.0.0 --language=es --output=raw/wordlist.tsv`

1. Parse dictionary
2. Create FormTable with wordlist.tsv
3. run ids_lookup
4. Fix mappings
5. Look-up manually

## EDICTOR notes

mac os: shifting left/right through alt+ctrl+ arrow shifts the table at the same time
right click on cogid: alignment
right click notes: larger window
!e/a  we expect e, but data has /a/

## Notes for using the cluster

ssh cdlce1
/data/users/blum --> für git repos. daten
/home/blum --> config dateien

default config script
source ~/shh_default

### see info on all nodes

`sinfo --Node --long`

### send script to slurm

`sbatch SCRIPT.sh`

### see result

`tail output.out`

move from remote to local:

`scp blum@cdlce1:/data/users/blum/pano-full3.log .?`

From local to remote:

`scp data/consonant_data.csv blum@cdlce1:/data/users/blum/consonant_lengthening/data/consonant_data.csv`

### MPCDF account

fblum: VVsw6J7gP3cVHWh!
blum: hwLf1aBMEz

### running tasks

`squeue -u blum`

### cancel tasks

`scancel JOBID`

## Test for Python packages

`pytest -s --cov=lingreg --cov-report=html tests/`

## Glottolog API for Python

```Python
from pyglottolog import Glottolog

# see https://calc.hypotheses.org/2225 to avoid having to pass the path!
G = Glottolog("path2glottologdata")

for language in my_list_of_language_codes:
    lng = G.languoid(language)
    print(lng.name, lng.latitude)
```

What's this?

```Python
from csvw.dsv import UnicodeReader
# also test this: UnicodeDictReader

with UnicodeReader("file") as reader:
    for row in reader:
        print(row)
```

## Tips for BEAST analysis

### Simon

if you’re calibrating with a tip date then you should use a bdsky with serial sampling, or a fossilised birth death (FBD).

becomeUninfectious should be a measure of how long the lineages survive after splitting. When I’ve used it in the past, I’ve just set it to have a lognormal with a mean of zero and a s.d. of 1 or 1.25.

However, if you use the `BDSParam` version (which should be available in BEAUTi now) you won’t need to worry about it but can put priors on rho (sampling proportion) and birth and death instead.

Konstantin Hoffman and I have a tutorial here that talks about this (<https://taming-the-beast.org/tutorials/LanguagePhylogenies/>) which might be a good starting point.

You could also use a FBD model, which should also be in beast, and it’s what we used in the Sagart et al 2019 Sino-Tibetan paper (the xml files are in the supplement for that, so you could just do what we did there).

Re (c) — yes, but it might be a bit weird, if your sample is 450y, you could assume that the age of the split above it is > 450y, so you could enforce that split with a calibration forcing it older than that.  FBD might be the easiest strategy.

Hope this helps, let me know if you get stuck. Would be keen to see what the results look like.

### contacTrees

After following the tutorial and running the model, annotate the trees, run the following command in BEAST/bin

`./applauncher ContactreesAnnotator -threshold 50 your_results.trees your_results.summary.tree`

For plotting the results, run the following command:

`python -m contacTreesIE.plotting.plot_contact_edges --trees <path_to_tree_sample> --summary_tree <path_to_summary_tree> --data <path_to_data_csv> --output <paht_to_output_directory>`

However, this needs fixing in the plot_contact_edges, which currently loads only Indo-European languages and thus causes errors.

## Dynamic programming

### Memoization recipe

How to solve Dynamic Programming tasks:

0. Think about the problem as a tree
1. Make it work
   1. implement tree using recursion (call function within the function)
2. Make it efficient
   1. add memo object
   2. add base case to return memo values
