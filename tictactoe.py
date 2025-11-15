# 10/31/25 edition: 128 lines (w/comments). Functions, if/elif, matrix
# 11/9/25 edition: 165 lines (w/comments). Prep work for different sized grids (using vars for functions instead of hardcoded values), user-chosen symbols, create/reset grid progrmatically, general clean up
# TODO: SILLY EDITION: ai type/difficulty picker, make different sizes of grids (this will need to update the layout, as well as AI + x move dict + intro info)
# TODO: PRETTIFY: make lines between cells? + highlight/color the winning/losing ones, prolly get rid of all the globals
# TODO: BASIC FUNCTIONALITY: actual ai that isn't random, clean up w/win/loss functions, probably not have a main func, find check for all of row being same for win condition, write formula for diagnol, replace dicts with ord/chr for ascii, change .lower to .upper (for ascii), change win checker to only be for things that include the newest one.

import random

#inits
whitespace_mark = ""
grid_size = 3
grid = []
x_move = 0
x_move_dict = {
    "a": 0,
    "b": 1,
    "c": 2
}
ai_y_move_dict = {
    0 : "A",
    1 : "B",
    2 : "C"
}
y_move = 0
turn_count = 0

# makes grid programmatically
def grid_init():
    global grid
    grid = [[whitespace_mark for col in range(grid_size)] for row in range(grid_size)]

# converts letters to ints
def x_conversion(x):
    global x_move
    if x in x_move_dict:
        x_move = x_move_dict[x_move]
    else:
        print("This is not a valid move.")
        main()

# converts natural counting to comp counting
def y_conversion(y):
    global y_move
    y = int(y)
    if y <= grid_size and y >= 0:
        y_move = y-1
    else:
        print("This is not a valid move.")
        main()

# prints the grid
def print_grid():
    print("\tA\tB\tC\n-------------------------")
    i = 1
    for row in grid:
        print(i,*row, sep="\t")
        i += 1
    print("")

# updates grid w/players move
def register_move(x,y):
    if grid[x][y] == whitespace_mark:
        grid[x][y] = player_mark
        print_grid()
    else:
        print("This seat is taken! pick another")
        main()

# core loop
def main():
# human input + convert to matrix index
    prompt = input("Enter your move\n").lower()
    global x_move
    global y_move
    global turn_count
    x_move = prompt[0]
    y_move = prompt[1]
    x_conversion(x_move)
    y_conversion(y_move)
    # player move resolution
    register_move(y_move,x_move) #"backwards" cause of how 2d matrix indexes work
    turn_count += 1
    win_checker()
    # ai turn
    random_ai_move()
    turn_count += 1
    win_checker()
    # repeat
    main()

# "AI" that just picks a random spot
def random_ai_move():
    ai_x_move = random.randint(0,grid_size-1)
    ai_y_move = random.randint(0,grid_size-1)
    if grid[ai_x_move][ai_y_move] == whitespace_mark:
        grid[ai_x_move][ai_y_move] = ai_mark
        if ai_y_move in ai_y_move_dict:
            ai_y_move = ai_y_move_dict[ai_y_move]
        print(f"The AI chose: \n{ai_y_move}{ai_x_move+1}")
        print_grid()
    else:
        random_ai_move()

# player-agnostic win/loss checker
def win_checker():
    if turn_count == (grid_size**2):
        print("Drat, a draw!")
        replay_check()
    for i in range(grid_size-1):
        #row checker
        if grid[i][0] == grid[i][1] == grid[i][2]: #this will need to be updated for grid sizes
            if grid[i][0] == player_mark:
                print("You win!")
                replay_check()
            elif grid[i][0] == ai_mark:
                print("you lose lol")
                replay_check()
        #column checker
        elif grid[0][i] == grid[1][i] == grid[2][i]:
            if grid[0][i] == player_mark:
                print("You win")
                replay_check()
            elif grid[0][i] == ai_mark:
                print("you lose lol")
                replay_check()
    # the silly hard coded diagonal checkers
    if grid[0][0] == grid[1][1] == grid[2][2]:
        if grid[0][0] == player_mark:
            print("You win")
            replay_check()
        elif grid[0][0] == ai_mark:
            print("you lose lol")
            replay_check()
    elif grid[2][0] == grid[1][1] == grid[0][2]:
        if grid[2][0] == player_mark:
            print("You win")
            replay_check()
        elif grid[2][0] == ai_mark:
            print("you lose lol")
            replay_check()

# resets board or exits program
def replay_check():
    resp = input("Play again?\n").lower()
    if resp[0] == "y":
        global grid
        global turn_count
        grid_init()
        turn_count = 0
        main()
    else:
        print("Thanks for playing!")
        exit()

# Intro
print(f"It's tic tac toe!\n\nEnter your choice in x/y cords, with A-C for columns and 1-{grid_size} for rows\n")
player_mark=input("But first! Enter the character/symbol you'd like to use.\n")
player_mark=player_mark[0]
ai_mark=input("Now enter the character/symbol for the computer to use.\n")
ai_mark=ai_mark[0]
whitespace_mark=input("And, finally, enter what you'd like the placeholder symbol for a cell to be. Default is -, but it can be anything!\n")
whitespace_mark=whitespace_mark[0]
grid_init()
print_grid()
main()