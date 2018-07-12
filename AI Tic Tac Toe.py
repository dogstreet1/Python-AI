import random
import time
turn = 1
Game_Run = True

grid = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

print("Welcome to Tic Tac Toe! You will be playing against an AI. Here is the board.")

print("\n \n -  -  - \n|0||1||2| \n -  -  - \n|3||4||5| \n -  -  - \n|6||7||8| \n -  -  -")


def Board():
    print("\n \n -  -  - \n|" + str(grid[0]) + "||" + str(grid[1]) + "||" + str(grid[2]) + "| \n -  -  - \n|" + str(grid[3]) + "||" + str(grid[4]) + "||" + str(grid[5]) + "| \n -  -  - \n|" + str(grid[6]) + "||" + str(grid[7]) + "||" + str(grid[8]) + "| \n -  -  -")

def WinCheck(myList,A,B,C):
    if myList[A] == myList[B] == myList[C]:
        if myList[A] == "X":
            print("Player 1 wins! Game over.")
            return True

        if myList[A] == "O":
            print("AI wins! Game over.")
            return True
        
    else:
        return False


    

while Game_Run:
    if turn % 2 == 1:
        
        temp = input("\nPlayer 1, please enter a space, 0 through 8: ")
        P1_Move = int(temp)
        while not grid[P1_Move] == " ":
            temp = input("Please enter an unoccupied space, that space is filled 0 through 8: ")
            P1_Move = int(temp)
        P1_Move = int(temp)
        grid[P1_Move] = "X"
        Board()
        if WinCheck(grid,0,1,2):
            Game_Run = False
        if WinCheck(grid,3,4,5):
            Game_Run = False
        if WinCheck(grid,6,7,8):
            Game_Run = False
        if WinCheck(grid,0,3,6):
            Game_Run = False
        if WinCheck(grid,1,4,7):
            Game_Run = False
        if WinCheck(grid,2,5,8):
            Game_Run = False
        if WinCheck(grid,0,4,8):
            Game_Run = False
        if WinCheck(grid,2,4,6):
            Game_Run = False
        
    else:
        print("\nNow it's the AI's turn!")
        time.sleep(3)
        AI_Move = random.randint(0, 9)
        while not grid[AI_Move] == " ":
            AI_Move = random.randint(0,9)
        grid[AI_Move] = "O"
        Board()
        if WinCheck(grid,0,1,2):
            Game_Run = False
        if WinCheck(grid,3,4,5):
            Game_Run = False
        if WinCheck(grid,6,7,8):
            Game_Run = False
        if WinCheck(grid,0,3,6):
            Game_Run = False
        if WinCheck(grid,1,4,7):
            Game_Run = False
        if WinCheck(grid,2,5,8):
            Game_Run = False
        if WinCheck(grid,0,4,8):
            Game_Run = False
        if WinCheck(grid,2,4,6):
            Game_Run = False
        time.sleep(2)

    turn += 1
    if turn == 10:
        Game_Run = False
        print("It's a tie! Game over!")
        
