import sqlite3
import requests

WEBFLOW_API_TOKEN = "ecb5a6e8262ac99a4690ad57bd89c58ede5ac804893c0fb9c57d1e8c50241b94"
COLLECTION_ID = "6a1934fd39df80166a9a8bc5"

url = f"https://api.webflow.com/v2/collections/{COLLECTION_ID}/items"

headers = {
    "Authorization": f"Bearer {WEBFLOW_API_TOKEN}",
    "Content-Type": "application/json"
}

conn = sqlite3.connect("baltic_esports.db")
cursor = conn.cursor()

cursor.execute("SELECT name, country, game FROM teams")
teams = cursor.fetchall()

print(f"Found {len(teams)} teams in database")

for t in teams:
    payload = {
        "isDraft": False,
        "isArchived": False,
        "fieldData": {
            "name": t[0],
            "slug": t[0].lower().replace(" ", "-"),
            "country": t[1],
            "game": t[2]
        }
    }

    response = requests.post(url, headers=headers, json=payload)

    print(response.status_code, response.text)

conn.close()