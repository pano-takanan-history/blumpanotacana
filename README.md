# CLDF dataset derived from Blum et al.'s "A comparative wordlist for studying long-distance relationships in the Americas (forthcoming).

## How to cite

If you use these data please cite
- the original source
  > Blum, Frederic and Barrientos, Carlos and Zariquiey, Roberto and List, Johann-Mattis.
- the derived dataset using the DOI of the [particular released version](../../releases/) you were using

## Description


Comparative wordlist for Panoan and Tacanan languages, as well as a selection of language isolates that have been hypothesized to be related to Pano-Tacanan.

This dataset is licensed under a CC-BY-4.0 license

## Notes

### Convert the data to SQL to integrate other datasets

To ease the integration with other datasets, we recommend to convert the dataset to SQL. This is easily done by running the following command from pycldf:

`cldf createdb cldf/cldf-metadata.json blumpanotacana.sqlite3`

As an example, you can easily integrate the data from Grambank. As a pre-requisite, please clone Grambank (Zenodo) and create the sqlite-database in the same way as presented above. In order to now retrieve the data of the languages that are both in this dataset and in Grambank, you can use the following code in `sqlite3`:

```SQL
attach 'blumpanotacana.sqlite3' as db1;
attach '../grambank/grambank.sqlite' as db2;

SELECT count(a.cldf_glottocode) FROM
  db1.LanguageTable a
INNER JOIN
  db2.LanguageTable b 
ON 
  a.cldf_glottocode = b.cldf_glottocode;
```

As you can see from the output, 15 of the 21 languages in the dataset are coded for Grambank. If you want to retrieve the Grambank features for those languages, you can run the following command:

```SQL
SELECT * FROM
  db1.LanguageTable a
INNER JOIN
  db2.ValueTable b 
ON 
  a.cldf_glottocode = b.cldf_languageReference;
```



## Statistics


![Glottolog: 100%](https://img.shields.io/badge/Glottolog-100%25-brightgreen.svg "Glottolog: 100%")
![Concepticon: 100%](https://img.shields.io/badge/Concepticon-100%25-brightgreen.svg "Concepticon: 100%")
![Source: 100%](https://img.shields.io/badge/Source-100%25-brightgreen.svg "Source: 100%")
![BIPA: 65%](https://img.shields.io/badge/BIPA-65%25-orange.svg "BIPA: 65%")
![CLTS SoundClass: 100%](https://img.shields.io/badge/CLTS%20SoundClass-100%25-brightgreen.svg "CLTS SoundClass: 100%")

- **Varieties:** 21
- **Concepts:** 501
- **Lexemes:** 10,239
- **Sources:** 14
- **Synonymy:** 1.18
- **Cognacy:** 10,239 cognates in 6,152 cognate sets (4,695 singletons)
- **Cognate Diversity:** 0.58
- **Invalid lexemes:** 0
- **Tokens:** 56,128
- **Segments:** 243 (84 BIPA errors, 1 CLTS sound class errors, 160 CLTS modified)
- **Inventory size (avg):** 40.67

# Contributors

Name | GitHub user | Description | Role |
--- | --- | --- | --- |
Frederic Blum | @Tarotis | Data collection, CLDF conversion and annotation | Author
Carlos M. B. Ugarte | @MuffinLinwist | CLDF conversion and annotation | Author
Roberto Zariquiey | | Data collector | Author
Johann-Mattis List | @LinguList| CLDF conversion | Author




## CLDF Datasets

The following CLDF datasets are available in [cldf](cldf):

- CLDF [Wordlist](https://github.com/cldf/cldf/tree/master/modules/Wordlist) at [cldf/cldf-metadata.json](cldf/cldf-metadata.json)