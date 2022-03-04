import sqlite3 as sq
from db_info import name as db_name_and_extension
from db_info import no_extension_name as db_name

def create_db():
    con = sq.connect(db_name_and_extension)
    cur = con.cursor()

    cur.execute(f'''CREATE TABLE IF NOT EXISTS {db_name}(
                id INTEGER NOT NULL PRIMARY KEY, 
                value REAL NOT NULL, 
                timeStamp TEXT NOT NULL)
                ''')

    con.commit()
    con.close()