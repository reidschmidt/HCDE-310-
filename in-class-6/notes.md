# In-class 6 notes

## What happens with a wrong key? What status code?

When I used the wrong key, NASA's API returned a status code of 403. This means that the request was forbidden because the key was wrong.

## Where does your key live, and why isn't it in earth.py?

My key is stored in a .env file. It's not directly in earth.py because that file will be given to GitHub. Keeping the key in .env which Git ignores will help keep it private.

## Stuck? Where?

I had a couple minor spelling and spacing errors in my code that I was able to fix pretty quickly. It also took me a while to set up the correct .venv stuff. 