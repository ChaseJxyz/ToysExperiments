## Purpose

These are fun little (non-IF) based things I'm making just to see if I can (and to practice coding). It's probably nothing you haven't seen before! But feel free to download/modify/use/etc.

### tictactoe.py

Tic-tac-toe in the terminal. The goal is to update it after each week of my Intro to Scripting class to reflect the things I've learned (or, the things that I feel confident enough in teaching/figuring out myself).


### amiraizer.py

Command line script to take a text file and convert it into the reality-resistant shorthand of one of my characters (so I don't have to do it myself!). In/out is printed in the terminal, but output is also appened to the file. The only non-alphanumeric char that's converted is "-" while others (including whitespace) are left as is (intentional).

### higher_lower_game.py

I was supposed to make pseudocode for this for my IT 140 homework...but I wanted to make sure it was correct....so I just programmed the whole thing. oops

### moksha_checker.py

Moksha is a submission tracking system for writers. Each submission is given a URL with unique sub id/user id that can be used to check the status of a given submission (namely, what number in "line" you are). To save writers time from having to open/refresh a bunch of URLs, I made a basic script to batch-check a number of URLs and return the queue position (since it's less sus for a single user to make multiple requests sometimes than a central website making hundreds/thousands of requests per day, and also these links should be considered secrets and not handed to 3rd parties since they can be used by anyone to withdraw a submission). Prints the market's name + queue number to terminal.