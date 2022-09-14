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

def delete_item(item):
    try:
        cursor.execute("""DELETE FROM inhalt WHERE gegenstand=?""", (item, ))
        connection.commit()
    except:
        connection.close()

def chg_open_status(item):
    try:
        zustand = cursor.execute("""SELECT offen_geschlossen FROM inhalt WHERE gegenstand=?""", (item, ))
        if str(zustand) == "0":
            cursor.execute("""UPDATE inhalt SET offen_geschlossen = 1""")
        else:
            cursor.execute("""UPDATE inhalt SET offen_geschlossen = 0""")
            
        connection.commit()

    except:
        connection.close()
    pass

def chg_anzahl(item):
    pass

# item = input("Item: " ).strip()
# kat_item = input("kategory? ").strip()
# o_g = 1 if input("open? (y/n)").lower().strip() == "y" else 0

# add_item(item, kat_item, o_g)
# chg_open_status("test")
delete_item("test")

connection.close()

