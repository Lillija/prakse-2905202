import requests

URL = "https://liquipedia.net/api.php"

params = {
    "action": "query",
    "format": "json",
    "list": "categorymembers",
    "cmtitle": "Category:Teams",
    "cmlimit": 10
}

headers = {
    "User-Agent": "BalticEsportsMarket/1.0"
}

response = requests.get(
    URL,
    params=params,
    headers=headers
)

print("Final URL:")
print(response.url)

print("\nStatus:")
print(response.status_code)

print("\nContent-Type:")
print(response.headers.get("Content-Type"))

print("\nFirst 300 chars:")
print(response.text[:300])