"""This script imports the Grmabank data for languages that are
part of the blumpanotacana database.
"""
import sqlite3
import tqdm


ATTACH_BPT = """attach 'blumpanotacana.sqlite3' AS bpt;"""
ATTACH_GB = """attach 'grambank.sqlite3' AS gb;"""

COMBINE = """
SELECT *
FROM bpt.LanguageTable AS a
INNER JOIN gb.ValueTable AS b
ON a.cldf_glottocode = b.cldf_languageReference;
"""

def get_db(path):
    """Loads sqlite3 database."""
    con = sqlite3.connect(path)
    return con.cursor()


output_data = [[
    'Doculect',
    'Concept',
    'Form'
]]

db = get_db('dummy.sqlite3')
db.execute(ATTACH_BPT)
db.execute(ATTACH_GB)
db.execute(COMBINE)

gb_data = []
for row in tqdm.tqdm(db.fetchall()):
    print(row)
    output_data.append(row)
