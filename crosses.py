# __________________________________ norts and crosses
def crosses():
  import random
  import sys
  import time
  playingGrid =[[0, 0, 0], 
              [0, 0, 0], 
              [0, 0, 0]]
  print("Defining Functions")
  def numToText(num):
    if (num == 0): return ' ' # If the variable = 0, then it will print out a blank(Empty?)
    if (num == 1): return 'O' # if the array is labeled(correct term?) as 1, then it will print out a naught
    if (num == 2): return 'X' # if the array is labeled 2 then it shall print out a crross


  def printGrid():
    print('┌ ─ ┬ ─ ┬ ─ ┐')
    print('│ ' + numToText(playingGrid[0][0]) + ' │ ' + numToText(playingGrid[1][0]) + ' │ ' + numToText(playingGrid[2][0]) + ' │')
    print('├ ─ ┼ ─ ┼ ─ ┤')
    print('│ ' + numToText(playingGrid[0][1]) + ' │ ' + numToText(playingGrid[1][1]) + ' │ ' + numToText(playingGrid[2][1]) + ' │')
    print('├ ─ ┼ ─ ┼ ─ ┤')
    print('│ ' + numToText(playingGrid[0][2]) + ' │ ' + numToText(playingGrid[1][2]) + ' │ ' + numToText(playingGrid[2][2]) + ' │')
    print('└ ─ ┴ ─ ┴ ─ ┘')

    
  def checkVictory(): 

    for i in range(0, 3):    # looks at each box in the grid andd checks 3 boxes in each specified vector
        for j in range(0, 3):

            if (playingGrid[i][j] == 0):
                continue

            for vector in [[1, 0], [1, 1], [0, 1], [-1, 1]]: #The four ways that the program will check for the 8 possibilities of winning.

                try:
                    boxToCheck = [i, j]
                    charToCheckFor = playingGrid[i][j]
                    for x in range(1, 3):

                        boxToCheck[0] += vector[0] #+= is the same as the operative.iadd operative. (have to remember this one, was useful)
                        boxToCheck[1] += vector[1]

                        
                        if (playingGrid[boxToCheck[0]][boxToCheck[1]] != charToCheckFor): # checks for the same symbols in the vectors that form a complete line (so that if a line is complete, the endgame will run)
                            break

                       # if last box in loop and still have not broken, then three in a row has been formed. print character
                        if (x == 2):
                            return numToText(playingGrid[i][j])

                except:
                    continue
    return ' '

  def chooseComputerMove():

    emptyBoxes = [] # box with nothing in it.
    for i in range(0, 3):
        for j in range(0, 3):
            if (playingGrid[i][j] == 0):
                emptyBoxes += [[i, j]] #Creates a list of possibilities, picks at random from them. Saves time on coding each and every single possibility
    return emptyBoxes[random.randint(1, len(emptyBoxes) - 1)]

  print("functions have been defined, initializing the program.")

  time.sleep(2)

  input("Welcome to naughts and crosses, press enter to being!.\n Co-ordinates are in the form 1 1 = the top left box.")
  #players move.
  while(1):


    while(1): #Repeat process until a valid input is detected and processed.

        move = input(" " "Your turn. Make your move:" " ")


        if (len(move) == 3):
            if (1 <= int(move[0]) <= 3 and 1 <= int(move[2]) <= 3): #Check for correct input
                if (playingGrid[int(move[0]) - 1][int(move[2]) - 1] == 0): #Check that box is empty.
                    playingGrid[int(move[0]) - 1][int(move[2]) - 1] = 2 #Put a cross in box.
                    printGrid()
                    break

            print("Invalid input. Try again with proper coords")

    victoryResult = checkVictory()
    if (victoryResult == 'X'):
        print ('You win!')
        break # checks if the player has won.

    computerMove = chooseComputerMove()
    playingGrid[computerMove[0]][computerMove[1]] = 1
    print(" " "Computer will now take it's turn")
    printGrid() # makes the computer move

        
    victoryResult = checkVictory()
    if (victoryResult == 'O'):
        print ('Computer wins!')
        break # check for computer win
  time.sleep(5)
  sys.exit
#___________________________________norts and crosses