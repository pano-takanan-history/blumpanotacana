In order to convert the data to the TSV format compatible with EDICTOR (and easy to browse in Excel), you can use pyedictor:

$ pip install pyedictor
$ edictor wordlist --name=blumpanotacana --addon="partial_cognacy:cogids"

This will output the data to the file blumpanotacana.tsv. We allow users to access the file via EDICTOR directly, using the following link:

https://lingulist.de/edev/?file=blumpanotacana.tsv&preview=500&basics=DOCULECT|CONCEPT|TOKENS|COGIDS&publish=true

With this link, you can browse the data in the EDICTOR tool online (without being able to manipulate the data).

## Attach data from Grambank

In order to get the data of the languages that are both in this dataset and in Grambank, you can use the following code in `sqlite3`:

```SQL
attach 'blumpanotacana.sqlite' as db1;
attach '../grambank/grambank.sqlite' as db2;

SELECT * FROM
  db1.LanguageTable a
INNER JOIN
  db2.ValueTable b 
ON 
  a.cldf_glottocode = b.cldf_languageReference;
```
