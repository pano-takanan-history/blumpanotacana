-- Retrieve data from Grambank
CREATE VIEW IF NOT EXISTS retrieve_grambank AS
SELECT * FROM
  db1.ValueTable a
INNER JOIN db2.LanguageTable b 
ON b.cldf_glottocode = a.cldf_languageReference;
