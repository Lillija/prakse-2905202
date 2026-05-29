import requests

URL = "https://liquipedia.net/api.php"

params = {
    "action": "query",
    "format": "json",
    "list": "categorymembers",
    "cmtitle": "Category:Teams",
    "cmlimit": 10
}

response = requests.get(URL, params=params)
data = response.json()

teams = data["query"]["categorymembers"]

for team in teams:
    print(team["title"])