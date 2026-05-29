import sqlite3

conn = sqlite3.connect("baltic_esports.db")
cursor = conn.cursor()

teams = [
    ("Riga Wolves", "Latvia", "CS2", 1),
    ("Tallinn Titans", "Estonia", "Valorant", 2),
    ("Vilnius Phantoms", "Lithuania", "LoL", 3)
]

cursor.executemany(
    "INSERT INTO teams (name, country, game, ranking) VALUES (?, ?, ?, ?)",
    teams
)

conn.commit()
conn.close()