import sqlite3

# Temporary sample data until API integration works
teams = [
    ("NAVI Junior", "EE", "CS2"),
    ("Baltic Wolves", "LV", "CS2"),
    ("Vilnius Esports", "LT", "Valorant")
]

conn = sqlite3.connect("baltic_esports.db")
cursor = conn.cursor()

for team in teams:
    cursor.execute("""
        INSERT INTO teams (name, country, game)
        VALUES (?, ?, ?)
    """, team)

conn.commit()
conn.close()

print("Teams imported successfully.")