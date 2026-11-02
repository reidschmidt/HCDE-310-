
# This function connects to the Art Institute of Chicago API.

import requests

# Choose which artwork fields we want returned by the API.
FIELDS = "id,title,artist_title,date_display,medium_display"

# Minimum relevance score for an artwork to be included.
SCORE_THRESHOLD = 0.001

# AI Written part
def search_artworks(search_term):
    # API address for searching artworks
    url = "https://api.artic.edu/api/v1/artworks/search"

    # Information sent to the API
    params = {
        "q": search_term,
        "fields": FIELDS,
        "limit": 10
    }

    # Identify our application when making the request
    headers = {
        "AIC-USER-Agent": "HCDE310 student project"
    }

    # Send the request to the API
    response = requests.get(
        url,
        params=params,
        headers=headers,
        timeout=10
    )

    # Check whether the request was successful
    response.raise_for_status()

    # Convert the response into Python data
    data = response.json()

    # Get the artwork results from the API
    artworks = data.get("data", [])

    # Keep only artworks with a meaningful relevance score
    relevant_artworks = []

    for artwork in artworks:
        score = artwork.get("_score", 0)

        if score > SCORE_THRESHOLD:
            relevant_artworks.append(artwork)

    # Return only relevant artwork results
    return relevant_artworks
