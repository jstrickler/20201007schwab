import sqlite3

RESTORE_DATA = [
    ('no party', 1),
    ('Democratic - Republican', 5),
    ('Republican', 19),
    ('Democratic', 22),
    ('Democratic', 36)
]

PARTY_UPDATE = '''
update presidents 
set party = ?
where termnum = ?
'''  # ? is SQLite3 placeholder; other DBMSs may use other placeholders

PARTY_QUERY = """
select termnum, firstname, lastname, party
from presidents
where termnum = ?
"""

with sqlite3.connect("../DATA/presidents.db") as s3conn:
    s3cursor = s3conn.cursor()

    for data in RESTORE_DATA:
        s3cursor.execute(PARTY_UPDATE, data)  # second argument to execute() is iterable of values to fill in placeholders from left to right
    s3conn.commit()

    for termnum, _ in RESTORE_DATA:
        s3cursor.execute(PARTY_QUERY, [termnum])
        print(s3cursor.fetchone())
