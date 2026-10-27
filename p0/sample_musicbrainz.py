
import requests

url = "https://musicbrainz.org/ws/2/artist/"

params = {
    "query": "artist:Kendrick Lamar",
    "fmt": "json",
    "limit": 1
}

headers = {
    "User-Agent": "HCDE310P0 (reids23@uw.edu)"
}

response = requests.get(
    url,
    params=params,
    headers=headers,
    timeout=10
)

print("Status code:", response.status_code)

data = response.json()

sample = data["artists"][0]

print({
    "id": sample["id"],
    "name": sample["name"],
    "country": sample.get("country"),
    "type": sample.get("type")
})
