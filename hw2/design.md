# HW2 Part 1 – Model first (in `design.md`, no code)

---

## 1. Why is `artworks` a list of dictionaries and not one big dictionary? What would you lose or gain the other way?

I think that we are using a list of dictionaries and not one big dictionary because it is more organized and will be easier to loop through. More specifically, a list of dictionaries allows us to store serval artworks so we don't end up with weird keys like Artwork_1, Artwork_5, etc. We would lose the ability to organize effectively by different artists, years, etc.

## 2. Which fields are sometimes missing? What should the app show when they are?

The medium, years, and artist field are sometimes missing. I think it would be reasonable to say the app should show "Unkown" or "Not found" when they are missig.