import sqlite3
def create(name):
    conn = sqlite3.connect(name)
    conn.close()
def get_all(tabelle):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM " + tabelle)
    rows = cursor.fetchall()
    conn.close()
    return rows
def get_arg(tabelle,arg):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT " + arg + " FROM " + tabelle)
    rows = cursor.fetchall()
    conn.close()
    return rows
conn = sqlite3.connect('database.db')
cursor = conn.cursor()
user = "eike"
passwort = "test"
conn.execute("CREATE TABLE displaydata (text TEXT)")
#c
#conn.commit()
#create("database.db")
conn.close()