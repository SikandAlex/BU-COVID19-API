import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            return conn

def addData(conn, data):
    sql = ''' INSERT INTO testing(date,negative,positive,invalid,total,isolated,noncontagious,recovered,processing_time)
                  VALUES(?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
    return cur.lastrowid

conn = create_connection('bu_covid_data.db')

with conn:

    data = ('8-22-20', 1925, 6, 9, 1940, 21, 1, 3, 18.4)
    print(addData(conn, data))
