import sqlite3

conn = sqlite3.connect("baltic_esports.db")
cursor = conn.cursor()

cursor.execute("PRAGMA table_info(teams)")
print(cursor.fetchall())

conn.close()