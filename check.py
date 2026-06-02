import sqlite3

conn = sqlite3.connect("baltic_esports.db")
cursor = conn.cursor()

print("\nTEAMS")
cursor.execute("SELECT * FROM teams")
for row in cursor.fetchall():
    print(row)

print("\nPLAYERS")
cursor.execute("SELECT * FROM players")
for row in cursor.fetchall():
    print(row)

conn.close()