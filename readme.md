## Purpose

These are fun little (non-IF) based things I'm making just to see if I can (and to practice coding). It's probably nothing you haven't seen before! But feel free to download/modify/use/etc.

### tictactoe.py

Tic-tac-toe in the terminal. The goal is to update it after each week of my Intro to Scripting class to reflect the things I've learned (or, the things that I feel confident enough in teaching/figuring out myself). EDIT: probably finished with this, because it's already over-engineered to all hell.

### amiraizer.py

Python script to take a text file and convert it into the reality-resistant shorthand of one of my characters (so I don't have to do it myself!). In/out is printed in the terminal, but output is also appended to the file. The only non-alphanumeric char that's converted is "-" while others (including whitespace) are left as is (intentional).

### higher_lower_game.py

I was only supposed to make pseudocode for this for my IT 140 homework...but I wanted to make sure it was correct....so I just programmed the whole thing. oops


### self_printer.py and self_printer_2

My friend sent me an old article about how code you find online could have trojans in it. But it started with discussing a competition to write a program that produces itself as the output. So I just *had* to run into my room and do it myself.

self_printer.py uses curl to access a copy of itself on github. self_printer_2.py is much more sensible and cats its own file to stdout.

I could def strip out comments/use a url shortener to use less characters. Or learn more about the subprocess module to find how to use the absolute minimum words/characters.

But they work!

### moksha_checker.py

Moksha is a writing submission tracking/management system for literary journals. Each submission is given a URL with unique sub/user id that allows the writer to check the status of a specific submission (namely, what number in "line" you are and if they've rejected you yet). To save writers time from having to open/refresh a bunch of URLs (and taking advantage that all of these URLs are public), I wrote a script to batch-check a series of URLs and return the queue position (since it's less sus for a single user to make multiple requests sometimes than a central website making hundreds/thousands of requests per day. And also these links should be considered secrets/not handed to 3rd parties, since they can be used by anyone to withdraw a submission)(they should fix that). Prints the market's name + queue position (and how much you've moved up in line, if applicable) OR submission status.

Needs to be updated so that it'll work if this is your first time running it/don't have any history and to have the full/correct names of markets. And how to handle the edge case of 2 subs to the same market.