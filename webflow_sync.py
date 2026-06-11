import sqlite3
import requests

WEBFLOW_API_TOKEN = "ef557b89efebf902d0244b1389bec87b5dda22e3679f64c9b3fb7a775b9f0b85"
COLLECTION_ID = "6a1934fd39df80166a9a8bc5"

url = f"https://api.webflow.com/v2/collections/{COLLECTION_ID}/items"

headers = {
    "Authorization": f"Bearer {WEBFLOW_API_TOKEN}",
    "Content-Type": "application/json"
}

conn = sqlite3.connect("baltic_esports.db")
cursor = conn.cursor()

cursor.execute("""
    SELECT name, country, game
    FROM teams
""")

teams = cursor.fetchall()

print(f"Found {len(teams)} teams in database")

for team in teams:

    payload = {
        "isDraft": False,
        "isArchived": False,
        "fieldData": {
            "name": team[0],
            "slug": team[0].lower().replace(" ", "-"),
            "country": team[1],
            "game": team[2]
        }
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            json=payload
        )

        if response.status_code in [200, 201, 202]:
            print(f"SUCCESS: {team[0]}")
        else:
            print(f"FAILED: {team[0]}")
            print(f"Status Code: {response.status_code}")
            print(response.text)

    except Exception as e:
        print(f"ERROR while sending {team[0]}")
        print(e)

conn.close()

print("Synchronization complete.")