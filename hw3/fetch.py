# HW3 Part 2 + Part 3 + Part 4
#
# Instructions: README.md in this folder (same as the assignment on Canvas).

import requests

FIELDS = "id,title,artist_title,artist_display,date_display,medium_display"

# Functions go here (above the code that runs)

def count_by_artist(artworks):
    counts = {}

    for artwork in artworks:
        artist = artwork.get("artist_title") or "Unknown"

        if artist in counts:
            counts[artist] = counts[artist] + 1
        else:
            counts[artist] = 1

    return counts

def save_results(artworks, filename):
    with open(filename, "w", encoding="utf-8") as file:
        for artwork in artworks:
            title = artwork.get("title") or "Unknown title"
            artist = artwork.get("artist_title") or "Unknown artist"
            date = artwork.get("date_display") or "Unknown date"

            file.write(f"{date}, {artist}, {title}\n")
            

term = input("Search the Art Institute for: ")

url = "https://api.artic.edu/api/v1/artworks/search"    
params = {"q": term, "fields": FIELDS}   

try:
    headers = {"AIC-USER-Agent": "HCDE310 student project"}
    response = requests.get(url, params=params, headers=headers)

    if response.status_code != 200:
        print(f"Request failed: {response.status_code} {response.reason}")

    else:
        data = response.json()
        artworks = data["data"]

        if len(artworks) == 0:
            print("No artworks found. Try another search term.")
            save_results(artworks, "search_results.txt")
            print("Results saved to search_results.txt")

        else:
            for artwork in artworks:
                title = artwork.get("title") or "Unknown title"
                artist = artwork.get("artist_title") or "Unknown artist"
                date = artwork.get("date_display") or "Unknown date"
                medium = artwork.get("medium_display") or "Unknown medium"

                print()
                print("Title:", title)
                print("Artist:", artist)
                print("Date:", date)
                print("Medium:", medium)

            print()
            print("Artworks by artist:")
            counts = count_by_artist(artworks)

            for artist in counts:
                print(artist + ":", counts[artist])

            save_results(artworks, "search_results.txt")
            print("\nResults saved to search_results.txt")

except Exception as error:
    print("Unable to complete the request:", error)
