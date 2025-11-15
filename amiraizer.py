#cli script converting given file into Amira's shorthand, appending it to file
#probably will update later for whole words (like 'in' and 'possibly') but just a char by char encoding for now

import sys
args = sys.argv
file_name = args[1]

encoder = {
    "a": "┤" ,
    "b": "╡" ,
    "c": "╖" ,
    "d": "─" ,
    "e": "§" ,
    "f": "╞" ,
    "g": "°" ,
    "h": "π" ,
    "i": "┐" ,
    "j": "╤" ,
    "k": "ƒ" ,
    "l": "⌐" ,
    "m": "╬" ,
    "n": "∩" ,
    "o": "╒" ,
    "p": "├" ,
    "q": "┴" ,
    "r": "╔" ,
    "s": "│" ,
    "t": "╚" ,
    "u": "═" ,
    "v": "╛" ,
    "w": "╓" ,
    "x": "ε" ,
    "y": "┌" ,
    "z": "╭" ,
    "-": "¬" ,
    "possible": "±" ,
    "in": "ˋ" ,
    "1": "β" ,
    "2": "δ" ,
    "3": "ζ" ,
    "4": "η" ,
    "5": "θ" ,
    "6": "λ" ,
    "7": "ξ" ,
    "8": "ρ" ,
    "9": "Φ" ,
    "0": "α"
}

file = open(file_name,"r")
contents = file.read()
print(f"Input: {contents}")

contents = contents.lower()
array = list(contents)

i = 0
while i < len(array):
    if array[i] in encoder.keys():
        array[i] = encoder.get(array[i])
        i+=1
    else:
        i+=1


output = "".join(array)
print(f"Output is: {output}")

with open(file_name,"a") as out_file:
    out_file.write(output)