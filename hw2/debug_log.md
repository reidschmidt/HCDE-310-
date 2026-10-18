# HW2 Part 5 – Debug log (`debug_log.md`)

Record **at least 2 errors** you hit. No errors? Break something on purpose and log it. For each error, write:

---

## Entry 1

### 1. Error message

AttributeError: 'dict' object has no attribute 'append'

### 2. What I thought it meant

I thought it meant that I messed up my dictionary variable. 

### 3. What it actually meant

I used {} instead of [] on  titles = {}

### 4. The fix

titles = []

## Entry 2

### 1. Error message

AttributeError: 'list' object has no attribute 'get'

### 2. What I thought it meant

I knew it was an issue with the words by the .get part. I thought I was accessing variables wrong.

### 3. What it actually meant

I needed to put artwork instead of artworks. 

### 4. The fix

    Wrong
    title = artworks.get("title", "Unknown")
    artist = artworks.get("artist", "Unknown")
    year = artworks.get("year", "Unknown") 

    Right
    title = artwork.get("title", "Unknown")
    artist = artwork.get("artist", "Unknown")
    year = artwork.get("year", "Unknown")