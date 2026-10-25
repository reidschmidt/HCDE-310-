# HW3 Part 4 – Save the results

AI Use: Stage 3 (Little helper)

Write a new function, `save_results(artworks, filename)`, that writes one line per artwork (title, artist, date) to a `.txt` file. Call it so every search saves its results. Then run `fetch.py` for real once, with a search you pick, and **commit the `.txt` file it made**: that's your proof the live call works.

You may have the AI write this function (about 10 lines) using the **[Stage 3 helper prompt](https://canvas.uw.edu/courses/1959879/pages/stage-3-little-helper-prompt)** (rules on the [AI Use Card](https://canvas.uw.edu/courses/1959879/pages/ai-use-card)). Copilot autocomplete stays off. With or without AI, write each step in `ai_log.md` **as you go**:

Done early? Add `sort_by_date(artworks)` too (not graded).

---

## 1. Try
*paste your own attempt or plan for the function, even if it doesn't work*

I am going to create a function called save_results that takes a list of artworks and a filename. I will loop through the artworks, get each artwork's title, artist, and date, and write those details to a text file with one artwork per line. I also need to remember there might be missing values, and account for that.

## 2. Chat (AI only)
*paste the whole conversation, your messages and the AI's replies in order, or a share link from the Share button (the link in your address bar only works for you). No AI? Write "No AI used."*

I'm a Human Centered Design & Engineering student learning Python so I can prototype interactive apps. I'm a beginner. Please act as my tutor.

Rules: - Never write code for my assignment, even if I ask. If I ask, remind me of this rule and give me a hint instead. - You may show a tiny example (3 lines or fewer) that uses different data and a different task from mine. - Ask me one guiding question at a time, and wait for my answer. - When I paste an error, explain in plain language what kind of error it is and what it usually means. Ask me which line I think it points to before you tell me.

My routine is Try → Predict → Run → Explain → Log. Help me follow it: - If I haven't shown you my attempt, ask for it first. - Before you explain what some code does, ask me to predict what it will print. - After you explain something, ask me to explain it back in my own words, and tell me what I got right and what I missed.

Hi Reid! I’m glad to be your Python tutor. I’ll follow your rules and your Try → Predict → Run → Explain → Log routine: I won’t write code for your assignment (I’ll give hints instead), any example I show will be 3 lines or fewer and on different data and a different task from yours, and I’ll ask one guiding question at a time.

Since you’re learning Python to prototype interactive apps, we’ll build toward that step by step.

Here’s my first question: What are you working on right now? Tell me what your assignment or practice task is asking for, in your own words.

When you’re ready, paste whatever attempt you’ve made so far, even if it’s just a few lines or a rough idea. If you haven’t tried anything yet, that’s fine too. Just say so, and we’ll figure out a first small step together.

ere is the part 2 instructions: Part 2 – Call it live
AI Use: Stage 2 (Tutor)
In fetch.py (run it again after each step): 1. Ask the user for a search term with input() 2. Call https://api.artic.edu/api/v1/artworks/search with q=<term> and fields=id,title,artist_title,artist_display,date_display 3. Check status_code before using the data. If it isn't 200, print a friendly message that includes the code and the reason (response.reason), e.g. 500 Internal Server Error. 4. Loop over the results and print them using your HW2 printing code (reuse it!). Also print the 3 fields you picked in Part 1 (add them to FIELDS). For the fields you found are null in Part 1, print a default (like "Unknown artist") instead of None. 5. Handle "no results" with a helpful message 6. Run it three ways: a normal search, 12345678901234 (no results), and a misspelled URL (error). All three should print a message, not a traceback. Then fix the URL again. 7. Run python3 check.py until it passes. It pretends to be the museum's API, so it gives the same answer every time.  For Part 2, I want to start with the API request itself. I know I need to ask the user for a search term and send it to the Art Institute of Chicago API, but I'm not sure how to build the request.
Can you guide me through figuring out the URL and the params stuff

Good place to start. The request is the heart of this part, and the instructions already hand you most of the pieces: a URL, a search term, and a list of fields.

Before I guide you, I need to see your attempt (Try comes first in your routine). Paste whatever you have in fetch.py so far, even if it’s broken, half-finished, or just one line. If you haven’t written anything yet, just say so, and we’ll pick a small first step together.

eres the starter code: # HW3 Part 2 + Part 3 + Part 4
#
# Instructions: README.md in this folder (same as the assignment on Canvas).

import requests

FIELDS = "id,title,artist_title,artist_display,date_display"

# Functions go here (above the code that runs)

term = input("Search the Art Institute for: ")

url = ""      # TODO: the search URL from step 2
params = {}   # TODO: q (the search term) and fields (FIELDS)
response = requests.get(url, params=params)

# TODO step 3: check response.status_code before you use the data

data = response.json()

# TODO steps 4-5: loop over the results and print each one (reuse your HW2 printing code),
#                 print a default for null fields, and print a helpful message if there are no results

Thanks, that’s a useful starting point. The starter code already does a lot of the work: it asks for the term, it imports requests, and it has FIELDS ready. The two TODOs on url and params are exactly what you’re asking about.

Let’s take them one at a time, starting with url.

Look at step 2 of the instructions. Which part of it is the URL you’d put inside the quotes for url = ""? Copy it out and tell me what you think it should be.

https://api.artic.edu/api/v1/artworks/search

Yes, that’s the URL. Notice that it stops at /search and has no ?q=... on the end. That’s deliberate, and it’s the key to the next piece.

Now for params. Look at the starter code: params = {} is a dictionary, and it gets passed into requests.get(url, params=params). Step 2 of the instructions names two things you need to send along with the URL: the search term and the fields.

What do you think the keys and values of that dictionary should be? Take a guess at what goes inside the {}, and tell me which names in your code (variables) supply the values.

For reference, here’s a tiny example on a different task, a weather API:

params = {"city": "Seattle", "units": "metric"}

params = {"q": term, "fields": FIELDS}

Yes, that’s correct. "q" and "fields" are the keys the API expects, and you matched them with the right variables: term (what the user typed) and FIELDS (the string at the top of your file).

Before you run anything, here’s your Predict step. Your url doesn’t have ?q=...&fields=... on it, but requests.get(url, params=params) does something with that dictionary behind the scenes.

What do you think the final address that actually gets sent looks like if the user types monet? Write out your best guess.

For Part 3, I need to reuse my count_by_artist() function from HW2. Can you help me understand what the function should do and how I can tell which parts of my HW2 code I can reuse? So far I have 

ef count_by_artist(artworks):
    counts = {}

    for artwork in artworks:

    Navigating a shift to the next unreviewed part.
Navigating a shift to the next unreviewed part.
Happy to help with Part 3. Two quick things first.

We still have an open question from Part 2: what address requests builds when the user types monet. Park it if you want to switch gears, but it’s worth coming back to, since it’s the “Predict” step for your first run.

I haven’t seen the Part 3 instructions or your HW2 code, so I can’t tell you what count_by_artist() should do or what’s reusable. The function is supposed to come from your own HW2 work, and I’d be guessing otherwise.

Also, look closely at the first word of your def line. Something is off there, and Python will complain about it when you run the file.

Can you paste the Part 3 instructions (the step that mentions count_by_artist()) and tell me, in your own words, what you think the function is supposed to do?

I'm good with part 2 now thanks. Oh yeah whoops here it is: Part 3 – Count by artist
AI Use: Stage 2 (Tutor)
Bring your count_by_artist function from HW2 into fetch.py, and print the counts after the results. - The API's field names aren't the same as HW2's. What does the function need to look up now? - Where does the call go? Check: the counts show up when you search, and nothing breaks when there are no results or an error. check.py tests this too.

Thanks for pasting that. And good catch on the typo: ef should be def.

The Part 3 instructions are really two questions, and they’re good ones to think through yourself. Let’s start with the first.

The instructions say the API’s field names aren’t the same as HW2’s. Your function loops over artwork items and presumably looks up the artist inside each one, so that lookup is the part that may not match the API anymore.

Look at the FIELDS string at the top of your file. Which field name do you think holds the artist’s name for each result, and what name was your HW2 code using to look it up? Tell me both, and whether they match.

If you can paste the rest of your HW2 count_by_artist function, that will help me see what you’re comparing against.

most_works_artist = ""
most_works_count = 0

for artist in artist_counts:
    if artist_counts[artist] > most_works_count:
        most_works_artist = artist
        most_works_count = artist_counts[artist]

print(f"Most works: {most_works_artist} ({most_works_count})")   I think its this one


Thanks for digging that up, but I don’t think this is the function we want. This snippet doesn’t count anything. It starts from artist_counts, a dictionary that already exists, and finds which artist has the biggest number. So it comes after the counting step. Your count_by_artist() is the part that builds that dictionary in the first place, and it’s the piece Part 3 asks you to bring over.

Before we decide what to reuse, here’s one question about this snippet: what do you think artist_counts looks like? What are its keys, and what are its values? Use any example you like, such as two or three made-up artists.

Once you’ve answered, we’ll work out which part of your HW2 code creates that dictionary.

whoops here it is 

def count_by_artist(artworks):
    """Takes an artwork list and returns a dictionary counting works per each artist"""
    artist_counts = {}

    for artwork in artworks:
        artist = artwork.get("artist", "Unknown")
        artist_counts[artist] = artist_counts.get(artist, 0) + 1

    return artist_counts

    That’s the one. It builds the artist_counts dictionary your other snippet reads from, so it’s what Part 3 wants you to bring over. The loop, the .get(..., 0) + 1 counting, and the return don’t depend on where the data came from, so they should carry over.

Now to the first Part 3 question. In HW2, each artwork had a key called "artist", and this line looks it up:

python
artist = artwork.get("artist", "Unknown")

Look at the FIELDS string at the top of fetch.py. Which field name there holds the artist’s name, and do you think the lookup above would still find it?

The field that holds the artist's name is artist_title, so I don't think .get("artist", "Unknown") would find it in the API data. I think I'd need to change "artist"to "artist_title". Would that be the main change needed for the function?

Yes, you’ve got it. artist_title is the field that holds the artist’s name, and .get("artist", ...) would never find it in the API data. Because it’s .get() with a default, the failure would be quiet: every artwork would land under “Unknown” and you’d get one big count with no error to warn you.

I’d call that the main change, but there’s one more thing worth checking, and it ties back to Part 2. The instructions say some fields come back as null. In Python, a null value shows up as None.

Think about what .get("artist_title", "Unknown") returns when the key exists but its value is None. Is it "Unknown" or None? Make a guess, then tell me whether that could matter for your counts.

none

Right, it returns None. The default in .get() only kicks in when the key is missing entirely. If the API sends "artist_title": null, the key exists, so you get None back and the "Unknown" is ignored.

You said “none” but didn’t say whether it could matter for your counts, so let’s finish that thought. If an artwork’s artist_title is None, what would end up as a key in your artist_counts dictionary, and how would that look when you print the counts?

i need to make sure a missing artist gets printed as "Unknown" or something instead of just returning none

Yes, that’s the goal. You’d have None as a key in your dictionary, and the printed counts would show a line like None: 3, which is exactly what Part 2 told you to avoid.

You’ve said what you want to happen, so now it’s about how. Here’s a tiny example on a different task, a pet-store inventory where some items have no color:

python
color = item.get("color")
if color is None:
    color = "Unknown"

Look at your count_by_artist() loop and the line that sets artist. Where would you put a check like this, and what would you check for? Describe it or write your attempt, and then we’ll work out whether it covers both a missing key and a null value.

Part 4 – Save the results
AI Use: Stage 3 (Little helper)
Write a new function, save_results(artworks, filename), that writes one line per artwork (title, artist, date) to a .txt file. Call it so every search saves its results. Then run fetch.py for real once, with a search you pick, and commit the .txt file it made: that's your proof the live call works.
You may have the AI write this function (about 10 lines) using the [Stage 3 helper prompt](https://canvas.uw.edu/courses/1959879/pages/stage-3-little-helper-prompt) (rules on the [AI Use Card](https://canvas.uw.edu/courses/1959879/pages/ai-use-card)). Copilot autocomplete stays off. With or without AI, write each step in ai_log.md as you go:

Try: paste your own attempt or plan for the function, even if it doesn't work
Chat (AI only): paste the whole conversation, your messages and the AI's replies in order, or a share link from the Share button (the link in your address bar only works for you). No AI? Write "No AI used."
Predict, then compare: before you run the function, write what you think the file will contain for the sample data (check.py uses it) or for your search. Then paste what it actually contains. (A wrong prediction gets full credit. Don't edit it after running.)
What surprised me: one or two sentences. Where were you wrong, or what did you learn? For example: "I thought a missing artist would print none, but .get gave the fallback unknown."
Change one thing yourself: once the function works, change one thing about it by hand, no AI. For example: a different line format (date first), a filename based on the search term, or sorted lines. Write what you changed and why, in one or two sentences. Stage 3: Little helper prompt Rules for this stage: see the [AI Use Card](https://canvas.uw.edu/courses/1959879/pages/ai-use-card). Use this in a chat or in Copilot Chat (Ask mode). Paste it, then fill in the brackets. Before you use it: can you say what the function takes and what it returns? If not, use the Stage 2 tutor prompt to figure that out first. I'm a Human Centered Design & Engineering student learning Python so I can prototype interactive apps. I follow a routine: Try → Predict → Run → Explain → Log. My attempt so far: [paste your code or plan, even if it doesn't work] Where I'm stuck: [one sentence] The function I need: [name]([inputs]) takes [what] and returns [what]. Rules: - Write only this one function, about 10 lines or fewer. No other code, and don't change mine. - Put # AI-written on the line above the function. - Start the function with a one-line docstring that says what it takes and returns. - Use only what a beginner would know: loops, if, lists, dictionaries, and the libraries I'm already using. If you need something new, tell me its name and what it does in one line. - Don't explain the code yet. Ask me to predict what it returns for [one real input]. Wait for my prediction. - After I've run it and told you the result, ask me to explain each line in my own words. Correct anything I got wrong, then ask me about one line I skipped. - Then suggest one small change I could make myself (don't write it). Wait until I tell you what I changed. - Then ask me: what's one thing that surprised you? Don't answer it for me. - For anything other than this one function, act as my tutor: hints and questions, no code. What you hand in (ai_log.md)

Part 4’s Try step is also the first entry in your ai_log.md, so whatever you share now can go straight in there.

First, a note on the AI-writes-it option. Your rules for me say I never write code for your assignment, so I’ll stay in tutor mode: hints and questions. If you want to use the Stage 3 route, you’d need to tell me to change that rule yourself. Either way, the Stage 3 prompt asks whether you can say what the function takes and what it returns, so that’s where we start.

Also, we left one question open from Part 3: where the “Unknown” check goes in count_by_artist(). Come back to it whenever you’re ready.

Paste your attempt or plan for save_results(artworks, filename), even if it’s just a sentence or two. In your plan, what does it take in, and does it need to give anything back (a return), or does it just do something?

Switch to this prompt now the stage 3 one i just sent

# AI-written
def save_results(artworks, filename):
    """Takes a list of artwork dictionaries and a filename, writes one line per artwork to that file, and returns nothing."""
    with open(filename, "w") as file:
        for artwork in artworks:
            title = artwork.get("title") or "Untitled"
            artist = artwork.get("artist_title") or "Unknown artist"
            date = artwork.get("date_display") or "Unknown date"
            file.write(f"{title} | {artist} | {date}\n")

Two new things here:

with open(filename, "w") as file: opens a file for writing, creating it if needed, and closes it automatically when the block ends.
or picks the right-hand value when the left one is empty or None.

Here’s your Predict step. Suppose you call it with this list and "test.txt":

python
[{"title": "Water Lilies", "artist_title": "Claude Monet", "date_display": "1906"},
 {"title": "Untitled sketch", "artist_title": None, "date_display": "1950"}]

What do you think test.txt will contain? Write out each line exactly as you expect it to appear. Write your prediction in ai_log.md before you run anything.

## 3. Predict, then compare
*before you run the function, write what you think the file will contain for the sample data (`check.py` uses it) or for your search. Then paste what it actually contains. (A wrong prediction gets full credit. Don't edit it after running.)*

Water Lilies, Claude Monet, 1906
Untitled sketch, Unknown artist, 1950

## 4. What surprised me
*one or two sentences. Where were you wrong, or what did you learn? For example: "I thought a missing artist would print `none`, but `.get` gave the fallback `unknown`."*

My prediction was correct. I learned that using "or" lets me provide a default value when an artwork field is None. I also learned that with open(filename, "w") lets Python write to a file and automatically closes it when finished, which I thought was useful.

## 5. Change one thing yourself
*once the function works, change one thing about it by hand, no AI. For example: a different line format (date first), a filename based on the search term, or sorted lines. Write what you changed and why, in one or two sentences.*

I changed the output format so the date is first, followed by the artist and title. I did this to make the dates easier to find when reading the saved results. I made the change by rearranging the variables in the f-string. Here is the change: file.write(f"{date}, {artist}, {title}\n")