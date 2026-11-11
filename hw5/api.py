
import requests

URL = "https://api.artic.edu/api/v1/artworks/search"
FIELDS = "id,title,artist_title,date_display,image_id,_score"
SCORE_THRESHOLD = 0.001


def get_artworks(artist):
    params = {"q": artist, "fields": FIELDS, "limit": 10}
    headers = {"User-Agent": "hcde310-artist-search/1.0"}
    response = requests.get(URL, params=params, headers=headers, timeout=10)
    response.raise_for_status()

    artworks = response.json().get("data", [])
    relevant_artworks = []

    for artwork in artworks:
        score = artwork.get("_score", 0)
        if score > SCORE_THRESHOLD:
            relevant_artworks.append(artwork)

    return relevant_artworks[:10]
