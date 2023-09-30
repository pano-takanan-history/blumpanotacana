### Convert the data to SQL to integrate other datasets

To ease the integration with other datasets, we recommend to convert the dataset to SQL. This is easily done by running the following command from pycldf:

`cldf createdb cldf/cldf-metadata.json blumpanotacana.sqlite3`

As an example, you can easily integrate the data from Grambank. As a pre-requisite, please clone Grambank (<https://github.com/grambank/grambank/tree/v1.0.3>) and create the sqlite-database in the same way as presented above. In order to now retrieve the data of the languages that are both in this dataset and in Grambank, you can use the following code in `sqlite3`:

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
