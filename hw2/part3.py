# HW2 Part 3 – Counting with a dictionary
#
# In `part3.py`:
#
# 1. Build a dictionary counting works per artist, and print it: `{'Vincent van Gogh': 1, ...}`. A
#    work with no artist counts under `'Unknown'`.
# 2. Print the artist with the most works: `Most works: Claude Monet (2)`
#
# (This is the letter-counting pattern from Class 3, applied to art.)

from artworks import artworks

artist_counts = {}

for artwork in artworks: 
    artist = artwork.get("artist", "Unknown")

    if artist in artist_counts:
        artist_counts[artist] = artist_counts[artist] + 1
    else:
        artist_counts[artist] = 1

print(artist_counts)

most_works_artist = ""
most_works_count = 0

for artist in artist_counts:
    if artist_counts[artist] > most_works_count:
        most_works_artist = artist
        most_works_count = artist_counts[artist]

print(f"Most works: {most_works_artist} ({most_works_count})")