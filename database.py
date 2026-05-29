import sqlite3

conn = sqlite3.connect("baltic_esports.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS teams (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    country TEXT,
    game TEXT,
    founding_date TEXT,
    owner TEXT,
    sponsors TEXT,
    logo_url TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS players (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nickname TEXT,
    real_name TEXT,
    country TEXT,
    game TEXT,
    active_team_id INTEGER,
    total_earnings REAL,
    previous_teams TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS tournaments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    season TEXT,
    game TEXT,
    prize_pool INTEGER,
    organizer TEXT,
    status TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS tournament_placements (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tournament_id INTEGER,
    team_id INTEGER,
    place_achieved TEXT,
    prize_won INTEGER
)
""")

conn.commit()
conn.close()

print("Database created successfully")