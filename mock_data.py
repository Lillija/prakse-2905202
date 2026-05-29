import sqlite3

conn = sqlite3.connect("baltic_esports.db")
cursor = conn.cursor()

teams = [
    ("Riga Wolves", "LV", "CS2", "2020", "Owner A", "RedBull", ""),
    ("Tallinn Titans", "EE", "Valorant", "2019", "Owner B", "Intel", "")
]

cursor.executemany("""
INSERT INTO teams (name, country, game, founding_date, owner, sponsors, logo_url)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", teams)

conn.commit()
conn.close()

print("Mock data inserted")