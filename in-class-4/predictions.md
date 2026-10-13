# Class 4: Five broken snippets

Your name: Reid Schmidt
Collaborator: Jayden Low

# Part 1: Predict

**Don't run anything yet.** Read each snippet in `exercise.py` and write your guesses. A wrong guess is fine: the point is to compare.

## Snippet 1
- Which line breaks?
- What error will Python show? (the kind and the message)
- What's the fix?

Line 2 will break. It will show a name error and explain that the variable isn't recognized because of the capitalization. The fix would be making room and Room the same or allowing for lower/uppercase letters.

## Snippet 2
- Which line breaks?
- What error will Python show? (the kind and the message)
- What's the fix?

Line 2 will break. It will show a type error because we are mixing strings and ints. We can add a str to fix.

## Snippet 3
- Which line breaks?
- What error will Python show? (the kind and the message)
- What's the fix?

Line 2 and 3 will break. It will be an index error because it is trying to access things out of range. The fix would be removing the +1's.

## Snippet 4
- Which line breaks?
- What error will Python show? (the kind and the message)
- What's the fix?

The last line will break. It will show a key error because it doesn't recognize visit. We need to change visit to visits.

## Snippet 5
- Which line breaks?
- What error will Python show? (the kind and the message)
- What's the fix?

Line 7 will break. I don't know what kind of error this will return, but it will let us know that it's missing a return statement. We will have to return longest.

# Part 2: Run

Run `python3 exercise.py`. Python stops at the first error, so fix that snippet in `exercise.py`, run again, and see the next one. Fill in what actually happened.

## Snippet 1
- Which line broke?
- What error did Python show?
- What's the fix?

Line 8. KeyError: 'Room' 
The fix is making Room room.

## Snippet 2
- Which line broke?
- What error did Python show?
- What's the fix?

Line 12. TypeError: can only concetenate str(not "int") to str.
The fix is using f"

## Snippet 3
- Which line broke?
- What error did Python show?
- What's the fix?

Line 17. IndexError: list index out of range. Remove first +1

## Snippet 4
- Which line broke?
- What error did Python show?
- What's the fix?

Line 29. NameError: name 'visit' is not defined. Did you mean: 'visits'? The error tells us what to do here. Change to visits.

## Snippet 5
- Which line broke?
- What error did Python show?
- What's the fix?

Line 41. AttributeError: 'NoneType' object has no attribute 'upper' Switch to return longest instead of print longest.

When all five are fixed, run `python3 check.py` until it says ✓.

Bonus: Snippet 5 prints something *before* it crashes. What, and why does it still crash?

# Part 3: Tutor practice (one snippet)

Pick one snippet. Write your guess first, then ask your tutor. Paste the chat (or a share link) below.

- Snippet #5
- Our guess before asking: Change print to return 
- Chat: I'm working on Snippet 5 for my Python class. I think the function is missing a return statement, but I don't quite understand why the program crashes. Can you guide me through it like a tutor? Ask me questions and give me hints instead of immediately giving me the answer. Here is the snippet: # Snippet 5
def longest_title(titles):
    """Return the longest title in a list of titles."""
    longest = ""
    for t in titles:
        if len(t) > len(longest):
            longest = t
    print(longest)
Let's work through it together! I'll give you hints rather than the full answer so you can figure it out yourself.

Look at the last line of your function:

print(longest)

Question 1: What do you think the difference is between print(longest) and return longest?

Here's a hint: imagine another part of your program calls the function like this:

title = longest_title(["Nighthawks", "The Bedroom", "Water Lilies"])
print(title.upper())

The function finds the longest title and prints it. But when the function finishes, what value do you think gets stored in the variable title?

Take a guess! It’s okay if you’re not sure.

Maybe not the longest one
Good guess! Let's trace what the code actually does.

Inside your function, this part:

if len(t) > len(longest):
    longest = t

updates longest whenever it finds a longer title. So by the time the loop finishes, longest really does contain the longest title.

Here's the next hint: Python treats print() and return differently.

print(longest) displays the title on the screen.

return longest sends the title back to wherever the function was called.

Question 2: If a function prints "The Bedroom" but never returns anything, what do you think Python automatically gives back to the code that called the function?

Hint: It's a special Python value that means no value. What do you think it's called?

This might also interest you.



Ad
so we should use return instead
Exactly! You're on the right track. 🙌

Change the last line inside the function from:

print(longest)

to:

return longest


- Did it give you too much? What did you do?

I think the ai did a pretty good job here. Helped me further understand whats going on in my code and I got to the right answer.
