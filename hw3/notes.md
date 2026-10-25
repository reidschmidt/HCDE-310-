# HW3 Part 1 – Read the response first

AI Use: Stage 2 (Tutor)

Open `sample_response.json` (a saved Art Institute of Chicago search). In `notes.md`:

---

## 1. The total number of results is at `data["pagination"]["total"]`. What's the path to the first artwork's title?

data["data"][0]["title"]

## 2. Find 3 more fields you'd want to show a user, and their paths

Artist: data["data"][0]["artist_title"]
Date: data["data"][0]["date_display"]
Medium: data["data"][0]["medium_display"]

## 3. Which fields are `null` for some works?

artist_title is null for "Baraque Pearl Mounted as a Cat Holding a Mouse." The top level preference field is also null.

## 4. Predict
*open `fetch.py` and read it, but don't change anything yet. What do you think will happen when you run it?*

I think the purpose of the code is to allows users to search for things, but seeing that the code isn't yet complete it will probably encounter an error.

## 5. Run it
*run `python3 fetch.py`. When it asks for a search term, type a word (like `cat`) and press Enter. What actually happened? Read the traceback bottom line first: what went wrong, and which line of your file caused it?*

We recieved an error from line 514. The error is request.exceptions.MissingSchema: Invalid URL '': No scheme supplied. So it seems like it failed because we are missing a URL.
