# 10/31/25 edition: 128 lines (w/comments). Functions, if/elifs, matrix
# x coords a/b/c L-->R y coords 1/2/3 top/bot
# TODO: SILLY EDITION: pick the charset for each player, ai type/difficulty picker
# TODO: PRETTIFY: make lines between cells? + add 1/2/3 labels for rows, highlight/color the winning/losing ones
# TODO: BASIC FUNCTIONALITY: actual ai that isnt random, clean up w/win/loss functions

import random

#inits
grid = ["-","-","-"],["-","-","-"],["-","-","-"]
x_move = 0
y_move = 0


# converts a/b/c to 0/1/2
def x_conversion(x):
    global x_move
    global y_move
    global x_move
    if x == "a":
        x_move = 0
    elif x == "b":
        x_move = 1
    elif x == "c":
        x_move = 2
    else:
        print("This is not a valid move")
        main()

# converts 1/2/3 to 0/1/2
def y_conversion(y):
    global y_move
    y = int(y)
    if y <= 3 and y >= 0:
        y_move = y-1
    else:
        print("This is not a valid move")
        main()

# updates grid w/players move
def register_move(x,y):
    if grid[x][y] == "-":
        grid[x][y] = "X"
        print("A\tB\tC\n-----------------")
        for row in grid:
            print(*row, sep="\t")
    else:
        print("This seat is taken! pick another")
        main()

def main():
# human input/first move
    prompt = input("Enter move\n").lower()
    global x_move
    global y_move
    x_move = prompt[0]
    y_move = prompt[1]
#    print("raw coords: x",x_move,"y",y_move)
    x_conversion(x_move)
    y_conversion(y_move)
#    print("converted coords: x", x_move,"y",y_move)
    register_move(y_move,x_move) #look idk why its backwards it just works this way
    win_checker()
    random_ai_move()
    win_checker()
    main()

def random_ai_move():
    ai_x_move = random.randint(0,2)
    ai_y_move = random.randint(0,2)
    if grid[ai_x_move][ai_y_move] == "-":
        grid[ai_x_move][ai_y_move] = "O"
        print("AI's move\nA\tB\tC\n-----------------")
        for row in grid:
            print(*row, sep="\t")
    else:
        random_ai_move()

def win_checker():
    for i in range(2):
        #row checker
        if grid[i][0] == grid[i][1] == grid[i][2]:
            if grid[i][0] == "X":
                print("You win!")
                replay_check()
            elif grid[i][0] == "O":
                print("you lose lol")
                replay_check()
#            else:
#                print("")
        #grid checker
        elif grid[0][i] == grid[1][i] == grid[2][i]:
            if grid[0][i] == "X":
                print("You win")
                replay_check()
            elif grid[0][i] == "O":
                print("you lose lol")
                replay_check()
#           else:
#                print("")
    if grid[0][0] == grid[1][1] == grid[2][2]:
        if grid[0][0] == "X":
            print("You win")
            replay_check()
        elif grid[0][0] == "O":
            print("you lose lol")
            replay_check()
    elif grid[2][0] == grid[1][1] == grid[0][2]:
        if grid[2][0] == "X":
            print("You win")
            replay_check()
        elif grid[2][0] == "O":
            print("you lose lol")
            replay_check()

def replay_check():
    resp = input("Play again?\n")
    if resp[0] == "y":
        global grid
        grid = ["-","-","-"],["-","-","-"],["-","-","-"]
        main()
    else:
        print("Thanks for playing!")
        exit()

# Intro
print("it's tic tac toe! but very inefficently coded!\nenter your choice in x/y cords, with a-c for columns and 1-3 for rows")
main()