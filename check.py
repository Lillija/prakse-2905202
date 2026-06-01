import sqlite3

conn = sqlite3.connect("baltic_esports.db")
cursor = conn.cursor()

for table in [
    "teams",
    "players",
    "tournaments",
    "tournament_placements"
]:
    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    count = cursor.fetchone()[0]
    print(table, count)

conn.close()