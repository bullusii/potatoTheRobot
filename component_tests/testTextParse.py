#!/usr/bin/python


##WHAT IT LOOKS LIKE
#output this - many times - so have to limit 1 per 20seconds or so
#b'https://wendelswienerfest.org?redir=food'


clue1 = "https://www.christmas.com/clue1"
clue2 = "https://www.christmas.com/clue2"
clue3 = "https://www.christmas.com/clue3"
clue4 = "https://www.christmas.com/clue4"
clue5 = "https://www.christmase.com"

## CAn I put the actual text into the clue? To send to api or run locally if cached?

if "clue" in clue5:
    print "Found Clue"
    theclue = clue5.split("clue")
    print theclue[1]
