import colorama
from os import system

player = 1

m = [
    ["1","2","3"],
    ["4","5","6"],
    ["7","8","9"]
]

won = 0

while not won:

    #Clears console
    system("cls")
    #Prints map
    for i in m:
        tmp = ""
        for a in i:
            tmp+=a
        print(tmp)
    #Let player play
    play = input(f"Player {player}: ")

    #Top row
    if play == "1":
        x = 0
        y = 0
    elif play == "2":
        x = 1
        y = 0
    elif play == "3":
        x = 2
        y = 0

    #Mid row
    elif play == "4":
        x = 0
        y = 1
    elif play == "5":
        x = 1
        y = 1
    elif play == "6":
        x = 2
        y = 1
    
    #Bottom row
    elif play == "7":
        x = 0
        y = 2
    elif play == "8":
        x = 1
        y = 2
    elif play == "9":
        x = 2
        y = 2
    else:
        continue

    #Check if spot is avaiable
    if m[y][x] != "O" and m[y][x] != "X":
        #Check which player is playing
        if player == 1:
            #Set the play
            m[y][x] = "X"
        else:
            #Set the play
            m[y][x] = "O"
    else:
        print(colorama.Fore.RED + "You cant play here!" + colorama.Style.RESET_ALL)
        continue

    #Checks if player 1 won
    #**Row check**
    if m[0][0] == "X" and m[0][1] == "X" and m[0][2] == "X" or m[1][0] == "X" and m[1][1] == "X" and m[1][2] == "X" or m[2][0] == "X" and m[2][1] == "X" and m[2][2] == "X":
        won = 1
    #**Col check**
    elif m[0][0] == "X" and m[1][0] == "X" and m[2][0] == "X" or m[0][1] == "X" and m[1][1] == "X" and m[2][1] == "X" or m[0][2] == "X" and m[1][2] == "X" and m[2][2] == "X":
        won = 1
    #**Diag check**
    elif m[0][0] == "X" and m[1][1] == "X" and m[2][2] == "X" or m[0][2] == "X" and m[1][1] == "X" and m[2][0] == "X":
        won = 1
    #Checks if player 2 won
    #**Row check**
    if m[0][0] == "O" and m[0][1] == "O" and m[0][2] == "O" or m[1][0] == "O" and m[1][1] == "O" and m[1][2] == "O" or m[2][0] == "O" and m[2][1] == "O" and m[2][2] == "O":
        won = 2
    #**Col check**
    elif m[0][0] == "O" and m[1][0] == "O" and m[2][0] == "O" or m[0][1] == "O" and m[1][1] == "O" and m[2][1] == "O" or m[0][2] == "O" and m[1][2] == "O" and m[2][2] == "O":
        won = 2
    #**Diag check**
    elif m[0][0] == "O" and m[1][1] == "O" and m[2][2] == "O" or m[0][2] == "O" and m[1][1] == "O" and m[2][0] == "O":
        won = 2
    elif m[0][0] != "1" and m[0][1] != "2" and m[0][2] != "3" and m[1][0] != "4" and m[1][1] != "5" and m[1][2] != "6" and m[2][0] != "7" and m[2][1] != "8" and m[2][2] != "9":
        won = 3

    #Changes player
    if player == 1:
        player = 2
    else:
        player = 1

#Clears console
system("cls")
#Prints map
for i in m:
    tmp = ""
    for a in i:
        tmp+=a
    print(tmp)
if won == 1:
    print("Player 1 won !")
elif won == 2:
    print("Player 2 won !")
else:
    print("Nobody won !")

input()