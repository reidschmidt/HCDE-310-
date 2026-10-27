
import requests
import json

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 47.6062,
    "longitude": -122.3321,
    "current": "temperature_2m,relative_humidity_2m,precipitation,wind_speed_10m",
    "daily": "temperature_2m_max,temperature_2m_min,precipitation_probability_max",
    "timezone": "America/Los_Angeles"
}

response = requests.get(url, params=params, timeout=10)

print("Status code:", response.status_code)
print("URL:", response.url)

data = response.json()

sample = {
    "latitude": data["latitude"],
    "longitude": data["longitude"],
    "current": data["current"],
    "daily": {
        "time": data["daily"]["time"][:2],
        "temperature_2m_max": data["daily"]["temperature_2m_max"][:2],
        "temperature_2m_min": data["daily"]["temperature_2m_min"][:2],
        "precipitation_probability_max": data["daily"]["precipitation_probability_max"][:2]
    }
}

print(json.dumps(sample, indent=2))
