import random

lower_bound = int(input("Enter lowest number\n"))
upper_bound = int(input("Enter highest number\n"))
if upper_bound <= lower_bound:
    print("Upper number must be higher than lower")
    upper_bound = int(input("Enter highest number\n"))

answer = random.randint(lower_bound,upper_bound)

def guess():
    player_guess = int(input(f"Guess a number between {lower_bound} and {upper_bound}\n"))
    while player_guess != answer:
        if player_guess > upper_bound or player_guess < lower_bound:
            print(f"has to be between {lower_bound} and {upper_bound}")
            guess()
        elif player_guess > answer:
            print("too high")
            guess()
        elif player_guess < answer:
            print("too low")
            guess()
    while player_guess == answer:
        print("you win")
        exit()

guess()