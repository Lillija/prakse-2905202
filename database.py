import sqlite3

conn = sqlite3.connect("baltic_esports.db")
cursor = conn.cursor()

for team in teams:
    cursor.execute("""
        INSERT INTO teams (name, country, game)
        VALUES (?, ?, ?)
    """, (team["title"], "unknown", "esports"))

conn.commit()
conn.close()