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
            anzahl INT,
            offen_geschlossen BOOLEAN,
            bild TEXT,
            hinzugefügt_am DATE
        );'''
        cursor.execute(sql)
        connection.commit()
    except:
        connection.close()

def add_item(item, kat_item, o_g, anzahl=1, bild=None):
    try:
        current_date = str(datetime.now().date())
        cursor.execute("""INSERT INTO inhalt (gegenstand, hinzugefügt_am, kategorie, offen_geschlossen, anzahl, bild) VALUES (?, ?, ?, ?, ?, ?)""",(item, current_date, kat_item, o_g, anzahl, bild))
        connection.commit()
    except:
        connection.close()

def delete_item(item):
    try:
        cursor.execute("""DELETE FROM inhalt WHERE gegenstand=?""", (item, ))
        connection.commit()
    except:
        connection.close()

# def chg_open_status(item):
# #try:
#     cursor.execute("""UPDATE inhalte SET (SELECT offen_geschlossen FROM inhalt WHERE gegenstand=:was) CASE WHEN (SELECT offen_geschlossen FROM inhalt WHERE gegenstand=:was) = 1 THEN 0
#                     ELSE 0 END;""", {"was":item})        
#     connection.commit()

#     # except:
#     #     connection.close()
# def chg_open doesnt work

def chg_anzahl(item,plusminus):
    try:
        cursor.execute("UPDATE inhalt SET anzahl = anzahl + ? WHERE gegenstand = ?",(plusminus, item,))
        connection.commit()
    except:
        connection.close()

# item = input("Item: " ).strip()
# kat_item = input("kategory? ").strip()
# o_g = 1 if input("open? (y/n)").lower().strip() == "y" else 0
# anzahl = 3
# add_item(item, kat_item, o_g)
chg_anzahl("weißbrot",3)

# initial_creation()
# add_item(item, kat_item,o_g,anzahl)

# chg_anzahl('weißbrot',-1)

connection.commit()
connection.close()

