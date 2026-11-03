# MusicBrainz API Guide - Reid Schmidt

## What is MusicBrainz?

MusicBrainz is an open music database that provides information about artists, albums, recordings, and other music-related metadata. Its API allows developers to search for music information and retrieve structured data using Python or other programming languages. Designers might find this API useful when creating music discovery platforms, artist profiles, playlists, or applications that organize music information. It provides access to music metadata without requiring a paid API key.

## Setup

MusicBrainz does not require an API key for basic API requests.

To use the API with Python:

1. Make sure Python is installed.
2. Install the `requests` library:

```bash
pip install requests
```

3. Import the library in your Python file:

```python
import requests
```

4. Send a GET request to the MusicBrainz API using the endpoint:

```text
https://musicbrainz.org/ws/2/artist/
```

5. Include a search query, request JSON formatting, and identify your application with a User-Agent header.

MusicBrainz requires a descriptive User-Agent for API requests. Its API also has a rate limit of approximately one request per second.

## Working Example: Search for an Artist

This example searches MusicBrainz for Kendrick Lamar and retrieves his artist ID, name, country, and artist type.

### Python Code

```python
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
```

### Output

```text
Status code: 200
{'id': '381086ea-f511-4aba-bdf9-71c753dc5077', 'name': 'Kendrick Lamar', 'country': 'US', 'type': 'Person'}
```

### How It Works

1. **Import requests:** Allows Python to send HTTP requests to the MusicBrainz API.
2. **Set the URL:** Points to the MusicBrainz artist search endpoint.
3. **Set parameters:** Searches for Kendrick Lamar, requests JSON formatting, and limits the results to one artist.
4. **Set headers:** Identifies the application with a User-Agent.
5. **Send the request:** Uses `requests.get()` to contact MusicBrainz. The timeout prevents the program from waiting indefinitely.
6. **Check the response:** Prints the HTTP status code. A 200 means the request was successful.
7. **Read the JSON:** Converts the response into Python data.
8. **Extract information:** Gets the first artist result and prints selected fields. The `.get()` method safely handles optional fields like country and type.

## Gotchas and Limitations

- **Rate limits:** MusicBrainz limits requests to approximately one request per second. Sending requests too quickly can result in errors or temporary blocking.
- **User-Agent requirement:** Requests should include a descriptive User-Agent identifying the application. Missing or generic headers can cause problems.
- **Missing data:** Not every artist has a country or type listed. Using `.get()` instead of directly accessing optional fields helps prevent errors when information is missing.
- **Search results:** A search may return multiple artists with similar names. Limiting results to one does not guarantee the first result is always the correct artist.
- **JSON structure:** Artist information is stored inside the `artists` list, so the code accesses `data["artists"][0]`. If there are no results, this will cause an error.

## Design Applications

**Project Idea: Music Discovery Platform**

A designer could use the MusicBrainz API to build a music discovery platform that lets users search for artists and explore their information. The application could display artist profiles, countries, and links between artists, albums, and recordings. This could help users discover new music and learn more about the artists behind it.

**Ethical and UX Consideration: Data Accuracy**

MusicBrainz is a community-maintained database, so some artist information may be incomplete or outdated. A designer should avoid presenting missing information as fact and should make it clear when information is unavailable. The interface should also distinguish between verified information and missing metadata so users aren't misled.

