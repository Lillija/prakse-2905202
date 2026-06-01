import sqlite3

conn = sqlite3.connect("baltic_esports.db")
cursor = conn.cursor()

# Teams
teams = [
    ("Riga Wolves", "LV", "CS2", "2020", "Owner A", "RedBull", ""),
    ("Tallinn Titans", "EE", "Valorant", "2019", "Owner B", "Intel", ""),
    ("Vilnius Vikings", "LT", "LoL", "2021", "Owner C", "Logitech", "")
]

cursor.executemany("""
INSERT INTO teams
(name, country, game, founding_date, owner, sponsors, logo_url)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", teams)

# Players
players = [
    ("broky", "Helvijs Saukants", "LV", "CS2", 1, 1200000, "Epsilon"),
    ("YEKINDAR", "Mareks Gaļinskis", "LV", "CS2", 1, 900000, "Virtus.pro"),
    ("ValorGuy", "John Smith", "EE", "Valorant", 2, 50000, "Old Team")
]

cursor.executemany("""
INSERT INTO players
(nickname, real_name, country, game, active_team_id, total_earnings, previous_teams)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", players)

# Tournaments
tournaments = [
    ("Baltic Masters", "2026", "CS2", 10000, "BEA", "Completed"),
    ("Baltic Valorant Cup", "2026", "Valorant", 5000, "BEA", "Upcoming")
]

cursor.executemany("""
INSERT INTO tournaments
(name, season, game, prize_pool, organizer, status)
VALUES (?, ?, ?, ?, ?, ?)
""", tournaments)

# Placements
placements = [
    (1, 1, "1st", 5000),
    (1, 2, "2nd", 3000)
]

cursor.executemany("""
INSERT INTO tournament_placements
(tournament_id, team_id, place_achieved, prize_won)
VALUES (?, ?, ?, ?)
""", placements)

conn.commit()
conn.close()

print("Mock data inserted")