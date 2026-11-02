# Things that suprised me

AI was very helpful when I ran into an error when running the tests for my page. I was getting a confusing error, and AI was able to explain it and help me fix it which was suprising. I was also suprised how thourough it made sure I was understanding things in the first part of the assignment (the plan.md work). 

# Things I fixed 

At first AI gave me code for api.py that didn't quite match what should happen when you type in a bunch of random letters (ex. akghkalkgh was still showing real artworks in the results) so I had to go through my code and make sure that didn't happen. With the help of AI, I added a relevance score filter to the artwork search function. I used a minimum relevance score of 0.001 and added a loop that only keeps artworks with a score above that threshold. This helped prevent unrelated results from appearing and made the no results message more useful.

I also was struggling a bit getting used to how to run the page through the terminal so AI helped me struggle through that process. It turns out I was trying to run things when the app wasn't even running, so I was confused on why the terminal wasn't showing anything when I was trying to use the page. 

# AI CHATS

Me: Stage 3: Little helper prompt
Rules for this stage: see the [AI Use Card](https://canvas.uw.edu/courses/1959879/pages/ai-use-card).
Use this in a chat or in Copilot Chat (Ask mode). Paste it, then fill in the brackets.
Before you use it: can you say what the function takes and what it returns? If not, use the Stage 2 tutor prompt to figure that out first.
I'm a Human Centered Design & Engineering student learning Python so I can prototype interactive apps. I follow a routine: Try → Predict → Run → Explain → Log.
My attempt so far: [paste your code or plan, even if it doesn't work] Where I'm stuck: [one sentence] The function I need: `[name]([inputs])` takes [what] and returns [what].
Rules: - Write only this one function, about 10 lines or fewer. No other code, and don't change mine. - Put `# AI-written` on the line above the function. - Start the function with a one-line docstring that says what it takes and returns. - Use only what a beginner would know: loops, if, lists, dictionaries, and the libraries I'm already using. If you need something new, tell me its name and what it does in one line. - Don't explain the code yet. Ask me to predict what it returns for [one real input]. Wait for my prediction. - After I've run it and told you the result, ask me to explain each line in my own words. Correct anything I got wrong, then ask me about one line I skipped. - Then suggest one small change I could make myself (don't write it). Wait until I tell you what I changed. - Then ask me: what's one thing that surprised you? Don't answer it for me. - For anything other than this one function, act as my tutor: hints and questions, no code.
What you hand in (`ai_log.md`)
The headings in your HW's `ai_log.md`: your Try, the chat (or a share link), your prediction vs. what happened, what surprised you, and your change: the one thing you changed in the AI's function yourself, by hand, and why.

AI: The brackets are still blank, so I don’t have your attempt or the function yet. Before anything else, I need to see your Try.

Paste whatever you have so far, even if it’s broken or just a few comment lines sketching a plan. Once I’ve seen it, we’ll pin down the function’s name, what it takes, and what it returns.

Me: Yeah that was just the prompt. here are the assignment instructions: Due: Tue Nov 3, 10am AI: Stage 3 – Little helper (at most one function per prompt) Individual

Build on your HW3 script to make a small web app: a user searches for art and sees useful results. Reuse your HW3 API code, and replace input() and print() with a form and a results page.

This time you plan before you build. The plan is what you'd hand in even without AI, and it's what you give the AI (Stage 3) when you ask it for a piece.

Steps
Sketch the screens. Sketch a search page and a results page, with the bare minimum the page needs. Paper is fine; take a photo.
Write down the data. Which fields from the API response do you actually need on the results page (for example: title, artist, image)? Your HW3 sample response helps.
Spec each piece. For each function or route: what goes in, what comes out, and 2–3 checks: things you'll try in the browser to know it works (for example: search "monet" and see results; submit an empty form and see a message).
Pseudocode. Write the steps as # comments in app.py before you write any code.
Skeleton. Get the whole path working with fake data first: form → /results → a template showing a hard-coded list (see class 9).
One piece at a time. Replace the fake parts with real ones. Commit each time something works.
Steps 1–3 go in plan.md; the pseudocode goes in app.py. Write them before the code they describe.

Where things go (recommended, like the books example in Class 9): - api.py: your HW3 API code, inside a function (for example search_art(term)) that returns the list of artworks - app.py: the routes. Each one reads the input, calls your api.py function, and renders a template - templates/: the HTML pages (home.html, results.html)

Requirements
Two routes: / (a search form) and /results (shows results)
Hand-written: write the / route and home.html template yourself (from Class 9). Code the AI writes gets an # AI-written comment (the helper prompt adds it), so anything without one is yours.
plan.md: your sketch, the data you need, and a spec with 2–3 checks for each piece (steps 1–3 above)
Check and explain. For each piece, AI-written or not: - Run your checks in the browser. Pass or fail? If the AI wrote it: did it add anything you didn't ask for? - Explain: add # comments, in your own words, to the parts that matter most in the code you kept: what each function or route does and why it's needed, and any line that handles user input, errors, or API keys. You don't need one on every line.
Handling empty states: empty input · no results · API error · missing field (for example, no date, or no image if you show images), each with a helpful message
Accessibility basics, such as labels on inputs, alt text, and a page that works with Tab
ai_log.md: your AI chats (paste them), what surprised you, and what you changed
README.md: who it's for (1 sentence), how to run it, a screenshot
Rubric (30 pts)
Row	Pts
App runs; form → API → results	6
Hand-written route + template	4
plan.md: sketch, data, specs + checks, written before the code	6
Checks run (pass/fail noted) + your own comments + ai_log.md	5
All 4 states handled	5
Accessibility + README	4
Here is my fetch.py from hw3 

```python
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

```

AI: Thanks, that gives me what I need. Your HW3 code is your Try for the API half, and the assignment says to plan before building. So no function from me yet, and I won't write code for your assignment anyway. I'll give hints and questions, and we can use a tiny example on different data if you get stuck.

Your fetch.py currently does three jobs at once: asks for input, talks to the API, and prints. Your app will split those jobs across `app.py` and `api.py`, so the piece that moves into `api.py` is the middle one.

Here's my first question: if you wrapped the API part in a function called `search_art(term)`, what would it take in, and what would it return? In particular, what should it return when the API call fails or nothing matches? Answer in your own words, even roughly, and then we'll turn it into the spec for `plan.md`.

Me: The function takes a search term as a string, such as monet, and returns a list of dictionaries containing matching artwork information from the Art Institute of Chicago API. Each dictionary includes the artwork's title, artist, date, and medium.
If there are no matches, it returns an empty list. If the API request fails, it raises a request exception that can be handled by the Flask route in app.py.

AI: That's a clear spec. Here's what you got right and what I'd tighten.

**Right:**
- The input is a string, and the output is a list of dictionaries.
- No matches returns an empty list. That keeps "no results" separate from "something broke."
- Letting the exception pass up to the route is a good design choice, because the route is where you can show the user a message.

**To tighten:**
- Your HW3 code only reads four fields. Your results page might need more, such as an image. The Stage 3 step "Write down the data" asks which fields you actually need on the results page, so your spec should list exactly those fields.
- "Raises a request exception" is a little vague. In your HW3 code, you also treated a non-200 status as a failure. Does `requests` raise an exception for that on its own, or do you have to do something yourself?

Here's my one question: in your HW3 code, what happens when the API responds with a 404 or 500? Does `requests.get` raise an exception, or does your code have to check for that and raise one itself? Tell me what you think, and why, before looking anything up.

Me: In my HW3 code, requests.get does not automatically raise an exception for an HTTP error like a 404 or 500. It returns a response, and my code checks to identify the failure and print an error message.
If I want the error to raise an exception instead, I can use `response.raise_for_status()`. That raises an HTTP error for unsuccessful status codes, which I can catch in a try/except block.
 
AI: Both parts are right. `requests.get` hands back a response for a 404 or 500 instead of raising, and `raise_for_status()` turns a bad status into an exception. That means your `search_art` spec can say "raises on any failure," and the route doesn't need to know which kind it was.

One gap: you described only failures where the server answers with a bad status. Your spec's "API error" check should cover more than that.

My question: can you think of a way the request could fail where the server never sends a response at all? What do you think `requests` does in that case, and does it need `raise_for_status()` for it?

Me: The request could fail if there is no internet connection, the server is down, or the request takes too long and times out. In those situations, `requests` raises a `RequestException` (such as a connection error or timeout) instead of returning a response. It doesn't need `raise_for_status()` because there is no response to check. I can handle both HTTP errors and connection errors with a try/except block in my Flask route.

AI: Right on all of it. No internet, a server that's down, and a timeout all raise a `RequestException` subclass (`ConnectionError`, `Timeout`), and there's no response to check. Your last point is also correct: `HTTPError` is a subclass of `RequestException` too, so one `except` in the route can catch both kinds of failure.

You missed one thing. You listed a timeout as a failure, but `requests` only raises one if you tell it how long to wait. Look back at your HW3 `requests.get(...)` call. Without that, a stalled server could leave your app hanging with no error at all.

Here's my question: what do you think you'd need to add to that `requests.get(...)` call so a slow API ends in an error instead of a hang? Give your best guess, and then we can write the "API error" spec and its checks in `plan.md`.

Me: hhmmm Im not sure to be honest

AI: That's fine. This one is about knowing what the function accepts, and that's something you look up.

Look at your HW3 call: you already pass two named arguments, `params=` and `headers=`. `requests.get` accepts more named arguments than those, and one of them controls how many seconds to wait before giving up.

Here's a tiny example on different data, a different task, with the answer left out:

```python
requests.get("https://example.com/weather", params={"city": "Oslo"}, ???=5)
```

My question: if you were naming that missing argument, what word would you guess for "how long to wait"? If you're not sure, check the `requests` quickstart docs and tell me what you find and which line told you.

Me: would guess the argument is `timeout`

AI: Yes, `timeout` is the right name. It takes a number of seconds. If the server doesn't respond in time, `requests` raises a `Timeout` error, which is a `RequestException`, so the same `except` in your route catches it. Your guess was correct, so you can check it against the quickstart docs to confirm.

Now you have what you need for the `search_art(term)` spec in `plan.md`: what goes in, what comes out, and what raises.

Here's my question: your spec needs 2-3 checks you can run in the browser, and one of them should be for the API error state. The real API is usually up, so how could you make it fail on purpose to see your error message? Throw out any ideas, even silly ones.

Me: could we just like take the api away or make a fake one

AI: Both ideas work, and they're what developers do.

- **"Take the API away":** the simplest way is to break the URL on purpose. A typo in the domain makes the request fail before any response arrives, which is the connection error case. A typo only in the path (after the domain) probably gets a response back with a 404, which is the bad-status case. So you can test both of your branches this way. Turning off your wifi works too, but it only tests the connection branch. Whichever you use, change it back afterward.
- **"Make a fake one":** a fake API that always fails would let you test without touching the real URL. That's more work than you need for this assignment, but it's the same idea as your fake-data skeleton step.

Your plan.md checks should be written as "do X, expect Y", and "expect" should describe what the user sees, not what happens in the code.

Here's my question: pick one of the two ways of breaking the URL and write the check as one sentence: what you do, and what message you expect on the page. What should that message say so it's helpful to someone using the app?

Me: ok i think i got this part. lets work on the api and app.py now

AI: Sounds good. Two reminders first:

- The assignment wants the plan (`plan.md`) and the pseudocode comments in `app.py` written before the code. If your spec and checks aren't written down yet, jot them down quickly now, since they're part of what you hand in.
- I won't write the code for your assignment. I'll give hints and questions, and a tiny example on different data if you get stuck.

Let's start with `api.py`, since it's mostly your HW3 code moved around. Go through your `fetch.py` and sort each part into "moves into `search_art(term)`" or "doesn't move" (stays out or goes to `app.py`). The `input()` line and the `print()` calls are good ones to think about.

My question: what's your attempt at `search_art(term)`? Paste whatever you have, even if it's rough or half-finished. If you haven't started, tell me which parts of `fetch.py` you think move into the function and which don't.

Me: Ok i got the psudocode heres what i got with my code so far what should i do next, 

```python
# AI-written: This function connects to the Art Institute of Chicago API.

import requests

# Choose which artwork fields we want returned by the API.
FIELDS = "id,title,artist_title,date_display,medium_display"

# Minimum relevance score for an artwork to be included.
SCORE_THRESHOLD = 0.001


def search_artworks(search_term):
    # API address for searching artworks
    url = "https://api.artic.edu/api/v1/artworks/search"

    # Information sent to the API
    params = {
        "q": search_term,
        "fields": FIELDS,
        "limit": 10
```

AI: Good progress on the pseudocode. Your paste cuts off in the middle of the `params` dictionary, so I can only see the setup, not the part that makes the request. I'll assume the paste got cut off and that you have the rest.

Before you go further, three things stood out in what I can see:

- **`SCORE_THRESHOLD` and `"limit": 10`** weren't in your HW3 code. The assignment asks you to check whether the AI added anything you didn't ask for, and these are candidates. They also belong in your `ai_log.md`.
- **The `# AI-written` comment** goes on the line directly above the function, not at the top of the file. It should only be there if the AI actually wrote that function, so make sure it matches what happened.
- **The function name** is `search_artworks`, but your spec said `search_art`. Pick one and use the same name in `plan.md`, `api.py`, and `app.py`.

My question: `SCORE_THRESHOLD = 0.001` isn't from your HW3 code. What do you think it does, and where in the function would it get used? Take your best guess from the name and the comment, and tell me whether you asked for it.

Me: I think `SCORE_THRESHOLD` sets a minimum relevance score maybe? for an artwork to be included in the search results. It would be used after the API returns the artworks, when looping through the results and checking each artwork's `_score`. If the score is higher than 0.001, the artwork gets added to the results list.
I didn't originally ask for this in my HW3 code. I added during testing to fix an issue

AI: Your explanation is right. It's a minimum relevance cutoff, it would run after the API responds, and it would loop through the results and keep only artworks whose `_score` is high enough. Tiny nit: "higher than" and "at least" differ only when a score equals the threshold exactly, so just pick one and make your comment match the code.

Two things to take from this:

- **It changes your spec.** With a filter, "no results" can now happen two ways: the API found nothing, or everything scored below the cutoff. Your plan.md check for the empty state should still pass either way, so mention the filter there.
- **Log it.** You added this to fix something, so write down in `ai_log.md` what the problem was and why a cutoff fixed it. If the AI wrote the function around your idea, say so there too. That keeps the `# AI-written` comment honest.

Here's my question: your `FIELDS` string doesn't list `_score`, but your loop would need it. Look at your HW3 sample response. Is `_score` in there, and where? Then tell me what your loop should do if an artwork has no `_score` at all. 

Me: The `_score` field is included in the API search response for each artwork, even though it isn't listed in my `FIELDS` string. I think the loop should use `artwork.get("_score", 0)` so that if an artwork doesn't have a score, it defaults to 0. That way, it won't accidentally pass the relevance filter if its score is missing.

AI: Right on both counts. _score shows up on each item in the search response even when it isn’t in FIELDS. Double-check that against your HW3 sample response, so your plan.md “data” section is based on what you saw rather than on a guess. And .get("_score", 0) is the same pattern you used in HW3 for missing fields. A missing score becomes 0, which falls below the cutoff, so the artwork is left out.

Two things to keep in mind:

A missing score now silently drops an artwork. That’s a reasonable choice, but it’s a decision, so write it in a comment in your own words.
.get("key", 0) only uses the default when the key is missing. Your HW3 code used or instead. What would each one do if the key were present but its value was None? You don’t need to answer this now, but it’s worth testing once the function runs.

Me (different AI): Help me write my function for API.py 

AI: def search_artworks(search_term):
    # API address for searching artworks
    url = "https://api.artic.edu/api/v1/artworks/search"

    # Information sent to the API
    params = {
        "q": search_term,
        "fields": FIELDS,
        "limit": 5
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

Me: # lask.cli.NoAppException

flask.cli.NoAppException: While importing 'art_explorer.app', an ImportError was raised:

Traceback (most recent call last):
&#x20; File "C:\documents\Coding\HCDE-310-\\.venv\Lib\site-packages\flask\cli.py", line 245, in locate_app
&#x20;   \_\_import\_\_(module_name)
&#x20;   \~\~\~\~\~\~\~\~\~\~^^^^^^^^^^^^^
&#x20; File "C:\documents\Coding\HCDE-310-\art_explorer\app.py", line 9, in \<module>
&#x20;   from api import search_artworks
ModuleNotFoundError: No module named 'api'



## Traceback *(most recent call last)*

###

-

#### File "C:\documents\Coding\HCDE-310-\\.venv\Lib\site-packages\flask\cli.py", line *974*, in `app`

raise err from None ^^^^^^^^^^^^^^^^^^^

1.

#### File "C:\documents\Coding\HCDE-310-\\.venv\Lib\site-packages\werkzeug\debug\\\_\_init\_\_.py", line *347*, in `debug_application`

app_iter = self.app(environ, start_response)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1.

#### File "C:\documents\Coding\HCDE-310-\\.venv\Lib\site-packages\flask\cli.py", line *974*, in `app`

raise err from None ^^^^^^^^^^^^^^^^^^^

1.

#### File "C:\documents\Coding\HCDE-310-\\.venv\Lib\site-packages\werkzeug\debug\\\_\_init\_\_.py", line *347*, in `debug_application`

app_iter = self.app(environ, start_response)            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1.

#### File "C:\documents\Coding\HCDE-310-\\.venv\Lib\site-packages\flask\cli.py", line *974*, in `app`

raise err from None ^^^^^^^^^^^^^^^^^^^

1.

#### File "C:\documents\Coding\HCDE-310-\\.venv\Lib\site-packages\flask\cli.py", line *963*, in `run_command`

app: WSGIApplication = info.load_app()  # pyright: ignore                        ^^^^^^^^^^^^^^^

1.

#### File "C:\documents\Coding\HCDE-310-\\.venv\Lib\site-packages\flask\cli.py", line *349*, in `load_app`

app = locate_app(import_name, name)       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1.

#### File "C:\documents\Coding\HCDE-310-\\.venv\Lib\site-packages\flask\cli.py", line *250*, in `locate_app`

raise NoAppException( ^^^^^^^^^^^

> flask.cli.NoAppException: While importing 'art_explorer.app', an ImportError was raised:  Traceback (most recent call last): File "C:\documents\Coding\HCDE-310-\\.venv\Lib\site-packages\flask\cli.py", line 245, in locate_app \_\_import\_\_(module_name) \~\~\~\~\~\~\~\~\~\~^^^^^^^^^^^^^ File "C:\documents\Coding\HCDE-310-\art_explorer\app.py", line 9, in \<module> from api import search_artworks ModuleNotFoundError: No module named 'api' &#x20;

The debugger caught an exception in your WSGI application. You can now look at the traceback which led to the error.

To switch between the interactive traceback and the plaintext one, you can click on the "Traceback" headline. From the text traceback you can also create a paste of it. For code execution mouse-over the frame you want to debug and click on the console icon on the right side.

You can execute arbitrary Python code in the stack frames and there are some extra helpers available for introspection:

- `dump()` shows all variables in the frame
- `dump(obj)` dumps all that's known about the object

AI: he error is coming from this line in app.py:
from api import search_artworks



Python can't find api.py when Flask tries to import it.

Since you're running Flask with:
flask --app art_explorer.app run --debug


the most likely issue is your file location or filename.
1. Check your folder structure
In VS Code Explorer, make sure api.py is directly inside art_explorer, alongside app.py.

It should look exactly like this:
HCDE-310-
│
├── art_explorer/
│   ├── app.py
│   ├── api.py
│   ├── plan.md
│   ├── ai_log.md
│   └── templates/
│       ├── home.html
│       └── results.html
│
└── hw3/


Important: Make sure the file is actually named api.py, not api.py.txt, and that it isn't inside templates.
2. Check the filename
In VS Code:
1. Expand the art_explorer folder.
2. Find api.py.
3. Make sure it appears at the same indentation level as app.py.
3. Try running Flask again
Once you've confirmed the location, run:
flask --app art_explorer.app run --debug


Quick question
Can you tell me whether api.py is currently:
- Directly inside art_explorer, next to app.py
- Inside templates
- Somewhere else
If you want, you can also send me a screenshot of your VS Code Explorer. That will help me pinpoint the problem without changing any of your code.

Me: PS C:\documents\Coding\HCDE-310-> (Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned) ; (& c:\documents\Coding\HCDE-310-\.venv\Scripts\Activate.ps1)
(.venv) PS C:\documents\Coding\HCDE-310-> flask --app art_explorer.app run --debug
Usage: flask run [OPTIONS]
Try 'flask run --help' for help.

Error: While importing 'art_explorer.app', an ImportError was raised:

Traceback (most recent call last):
  File "C:\documents\Coding\HCDE-310-\.venv\Lib\site-packages\flask\cli.py", line 245, in locate_app
    __import__(module_name)
    ~~~~~~~~~~^^^^^^^^^^^^^
  File "C:\documents\Coding\HCDE-310-\art_explorer\app.py", line 9, in <module>
    from api import search_artworks
ModuleNotFoundError: No module named 'api'

(.venv) PS C:\documents\Coding\HCDE-310->

AI: Thanks, this confirms Flask is running from the correct project folder, but Python still cannot locate `api.py`.

Let's troubleshoot this without changing your code yet.

### Step 1: Check whether Python can see `api.py`

In your VS Code terminal, copy and run:

```
dir .\art_explorer\
```

This lists everything inside your `art_explorer` folder.

You should see something like:

```
app.py
api.py
plan.md
ai_log.md
README.md
templates
```

### Step 2: Check the result

There are a few possibilities:

- `api.py` appears: We'll investigate the import path.
- `api.py.txt` appears: Windows saved it as a text file. We'll rename it.
- `api.py` doesn't appear: It may have been saved in another folder.

Send me the output of `dir .\art_explorer\`.

Don't change the import statement or move anything yet. We'll fix the actual cause rather than guessing.

Me: (.venv) PS C:\documents\Coding\HCDE-310-> dir .\art_explorer\


    Directory: C:\documents\Coding\HCDE-310-\art_explorer


Mode                 LastWriteTime         Length Name                                                                                                    
----                 -------------         ------ ----                                                                                                    
d-----         11/1/2026   2:56 PM                templates                                                                                               
d-----         11/1/2026   3:12 PM                __pycache__                                                                                             
-a----         11/1/2026   2:55 PM              0 ai_log.md                                                                                               
-a----         11/1/2026   3:10 PM           1010 api.py                                                                                                  
-a----         11/1/2026   3:12 PM           2191 app.py                                                                                                  
-a----         11/1/2026   2:40 PM           3263 plan.md                                                                                                 
-a----         11/1/2026   2:55 PM              0 README.md                                                                                               
-a----         11/1/2026   2:19 PM        2641161 sketch.jpg                                                                                              


(.venv) PS C:\documents\Coding\HCDE-310->

AI: Good news! We found the issue. Your `api.py` file is in exactly the right location, and its filename is correct.

The problem is the import statement, not your folder structure.

### Step 1: Fix the import in `app.py`

Find this line near the top:

```
from api import search_artworks
```

Replace it with:

```
from .api import search_artworks
```

Why?

You're launching Flask using `art_explorer.app`, so Python treats `art_explorer` as a package. The period in `.api` tells Python to look for `api.py` inside that same package.

### Step 2: Save and rerun Flask

In your terminal, run the same command:

```
flask --app art_explorer.app run --debug
```

### Step 3: Test your website

Try searching for:

- `Monet`
- `Vincent van Gogh`
- `Picasso`

You should now get actual artwork from the Art Institute API instead of the fake Starry Night result.

Don't change anything else yet. Let's see if this fixes the import error first. 

Me: # Search Results

Showing results for: xyzqwerty987654

## Self-Portrait

Artist: Walter Shirlaw

Date: 1878

Medium: Oil on canvas

## Martin Vanden Bogaert Desjardins

Artist: Gérard Edelinck

Date: n.d.

Medium: Engraving and etching on cream wove paper

## Remembrance of Italy

Artist: Jean Baptiste Camille Corot

Date: c. 1866

Medium: Etching on tan laid paper

## Priest and Boy

Artist: Lawrence Carmichael Earle

Date: n.d.

Medium: Watercolor over graphite on cream wove paper

## A Sunday on La Grande Jatte — 1884

Artist: Georges Seurat

Date: 1884–86, border added 1888–89

Medium: Oil on canvas

## Fishing Craft near the Cliffs at Collioure

Artist: Adolphe Appian

Date: 1878

Medium: Etching on China paper colle laid down on white wove paper

## Interior of St. Mark's, Venice

Artist: David Dalhoff Neal

Date: 1869

Medium: Oil on canvas

## Nighthawks

Artist: Edward Hopper

Date: 1942

Medium: Oil on canvas

## Lion (One of a Pair, South Pedestal)

Artist: Edward Kemeys

Date: 1893

Medium: Bronze with green patina

## American Gothic

Artist: Grant Wood

Date: 1930

Medium: Oil on Beaver Board

[Back to search](http://127.0.0.1:5000/)

Interesting! This means the API returned 10 artworks even though you searched for a random string. We shouldn't mark the no-results test as passed yet.

The Art Institute API may be handling that unusual search differently than expected, or something in our API request needs checking.

### Let's check `api.py`

Can you paste your current `api.py` code here?

I want to check these three things:

- Whether the search term is being passed correctly.
- Whether the API is actually filtering by the search term.
- Whether we're correctly interpreting an empty API response.

Don't change anything yet. We'll figure out why this happened before moving to the next test.

Me: # AI-written: This function connects to the Art Institute of Chicago API.

import requests

# Choose which artwork fields we want returned by the API.
FIELDS = "id,title,artist_title,date_display,medium_display"


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

    # Return the artwork results
    return data.get("data", [])

AI: Your `api.py` code looks correct overall. You're using the Art Institute's documented search endpoint, and `"q": search_term` is the correct way to pass the user's search term.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://api.artic.edu\&sz=32)

Art Institute of Chicago API



The surprising part is that the API returned 10 unrelated artworks for `xyzqwerty987654`.

I don't want to change your code unnecessarily. Let's check what the API is actually returning.

### 1. Temporarily update `api.py`

Find this section:

```
# Convert the response into Python datadata = response.json()# Return the artwork resultsreturn data.get("data", [])
```

Change it to:

```
# Convert the response into Python datadata = response.json()# Temporary debugging informationprint("API request URL:", response.url)print("Total matching results:", data.get("pagination", {}).get("total"))# Return the artwork resultsreturn data.get("data", [])
```

### 2. Test again

1. Save `api.py`.
2. Search for `xyzqwerty987654`.
3. Look at your VS Code terminal (not the browser).
4. Find the two lines beginning with `API request URL` and `Total matching results`.

Send me those two lines.

That will tell us whether the search term is reaching the API and how many results the API says it found. Then we can fix the no-results behavior properly.

Don't worry about the temporary print statements; we'll remove them after debugging.

Me: the terminal didnt say anything when i searched

AI: Okay, that tells us something. If the search is reaching your Flask app, we should normally see a `GET /results...` message in the terminal.

Let's narrow it down.

### Step 1: Check the browser URL

After you search for `xyzqwerty987654`, look at the address bar.

It should look something like:

```
http://127.0.0.1:5000/results?search=xyzqwerty987654
```

### Step 2: Check `api.py`

Make sure these two lines are still at the bottom of your `search_artworks()` function:

```
print("API request URL:", response.url)print("Total matching results:", data.get("pagination", {}).get("total"))
```

### Step 3: Tell me two things

1. Does your browser URL contain `/results?search=xyzqwerty987654`?
2. Does your terminal show anything at all after clicking Search?

That will help me determine whether the issue is with the Flask route or the API function. We won't change anything until we know.

