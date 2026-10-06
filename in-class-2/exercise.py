# Class 2 in-class exercise: strings, lists, loops (AI off)
# Run it:  python3 exercise.py      Check it:  python3 check.py
# Your output must match expected/exercise.txt exactly.

exhibits = [
    "The Art of Everyday Life",
    "Chicago Architecture",
    "Impressionism and the Seasons",
    "Paper Cuts",
    "Faces of the City",
    "Water and Light",
]

# 1. Print each exhibit on its own line, numbered starting at 1:   1. The Art of Everyday Life
for i in exhibits:
    print(i + 1 + ":" + exhibits[i])

# 2. Print a blank line, then each exhibit in ALL CAPS followed by its length:   PAPER CUTS 10
print()
for j in exhibits:  
    print(exhibits[j].upper())
# 3. Print a blank line, then how many exhibit names contain the word "the" (any case):   With "the": 3
print()
count = 0 
for name in exhibits:
    if "the" in name: 
        count +=1
print('With "the": ', count)
# BONUS (optional): Python has a built-in function, enumerate(), that numbers items for you.
# Rewrite your code for #1 so it uses enumerate() instead of adding 1 each time.
# Your output should stay exactly the same, so check.py still passes.
# Look it up: https://docs.python.org/3/library/functions.html#enumerate
# (Hint: it starts counting at 0 unless you tell it otherwise.)
