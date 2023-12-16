import sqlite3
from datetime import datetime


def openDB():
    conn = sqlite3.connect('blog2.db')
    curs = conn.cursor()
    return conn, curs


def closeDB(conn):
    conn.commit()
    conn.close()


def create_table():
    conn, curs = openDB()
    curs.execute('''DROP TABLE IF EXISTS articles''')
    curs.execute('''CREATE TABLE IF NOT EXISTS articles (
                 id INTEGER PRIMARY KEY,
                 title TEXT,
                 price INT
    )''')
    closeDB(conn)


def show_table():
    conn, curs = openDB()
    curs.execute('''SELECT * FROM articles''')
    data = curs.fetchall()
    closeDB(conn)
    return data


def select_index(id): 
    conn, curs = openDB()
    curs.execute('''SELECT * FROM articles WHERE id=(?)''', [id])
    data = curs.fetchall()
    closeDB(conn)
    return data


def create_index(title, price):
    conn, curs = openDB()
    date = datetime.utcnow()
    curs.execute('''INSERT INTO articles (title,price)
                 VALUES (?,?)''', [title,price])
    closeDB(conn)


def update_index(title, price):
    conn, curs = openDB()
    date = datetime.utcnow()
    curs.execute('''UPDATE articles SET title=(?), price = (?)
                 WHERE id=(?)''', [title, price])
    closeDB(conn)


def delete_index(id):
    conn, curs = openDB()
    curs.execute('''DELETE FROM articles WHERE id=(?)''', [id])
    closeDB(conn)
def price_d():
    conn, curs = openDB()
    curs.execute('''SELECT sum(price) FROM articles''')
    price = curs.fetchall()
    closeDB(conn)
    return price[0]
