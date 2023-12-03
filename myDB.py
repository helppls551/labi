import sqlite3
from datetime import datetime

def openDB():
    conn = sqlite3.connect*('blog.db')
    curs = conn.cursor()
    return conn,curs

def closeDB(conn):
    conn.commit()
    conn.close()

def create_table():
    conn,curs = openDB()
    curs.execute('''DROP TABLE IF EXISTS articles''')
    curs.execute('''CREATE TABLE IF NOT EXISTS articles (
                 id INTEGER PRIMARY KEY
                 title VARCHAR(60)
                 intro VARCHAR(300)
                 text TEXT,
                 date VARCHAR(40)
    )''')
    closeDB(conn)

def show_table():
    conn,curs = openDB()
    curs.execute =('''SELECT * FROM articles''')
    data = curs.fetchall()
    closeDB(conn)
    return

def select_index():
    pass

def create_index(title,intro,text):
    conn,curs = openDB()
    date = datetime.utcnow()
    curs.execute('''INSERT INTO articles(title,intro,text,date)
                 VALUES(?,?,?,?)''',[title,intro,text,date])
    closeDB(conn)

def update_index():
    pass

def delete_index():
    passs