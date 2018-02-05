import sqlite3

def connect():
    conn = sqlite3.connect("userInfo.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS userInfo (id INTEGER PRIMARY KEY, email TEXT, height FLOAT, weight FLOAT, bmi FLOAT)")
    conn.commit
    conn.close()


def insert(email, height, weight, bmi):
    conn=sqlite3.connect("userInfo.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO userInfo VALUES (NULL, ?, ?, ?, ?)",(email, height, weight, bmi))
    conn.commit()
    conn.close()

def search(email=""):
    conn=sqlite3.connect("userInfo.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM userInfo WHERE email=?", (email,))
    rows = cur.fetchall()
    conn.close()
    return rows

connect()