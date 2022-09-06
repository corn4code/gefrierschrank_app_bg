import sqlite3
from datetime import datetime
# enter pic by adding url for pic
connection = sqlite3.connect("gefrierschrank.db")
cursor = connection.cursor()

def initial_creation():
    try:
        sql = '''CREATE TABLE inhalt(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            gegenstand TEXT,
            kategorie TEXT,
            offen_geschlossen BOOLEAN,
            bild TEXT,
            hinzugefügt_am DATE
        );'''
        cursor.execute(sql)
        connection.commit()
    except:
        connection.close()

def add_item(item, kat_item, o_g, bild=None):
    try:
        current_date = str(datetime.now().date())
        cursor.execute("""INSERT INTO inhalt (gegenstand, hinzugefügt_am, kategorie, offen_geschlossen, bild) VALUES (?, ?, ?, ?, ?)""",(item, current_date, kat_item, o_g, bild))
        connection.commit()
    except:
        connection.close()

item = input("Item: " ).strip()
kat_item = input("kategory? ").strip()
o_g = 1 if input("open? (y/n)").lower().strip() == "y" else 0

add_item(item, kat_item, o_g)

connection.close()

