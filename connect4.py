import ConnectFourGrid
import game
import agent
import time

#Alternate moves between agent,opponent and their representation on the turtle screen is handled in this method
def gameMoves():
    #used to represent the game state internally. 1 represents agent's piece, 2 for opponent's piece and 0 for empty space
    arrayRep = [[0 for x in range(7)] for y in range(6)]
    #Has the valid row value of the next move for all the columns.
    validRowValue = [0 for x in range(7)]
    #The agent plays in the centre column by default.Hence the values are updated in the arrays.
    arrayRep[0][3]=1
    validRowValue[3]+=1
    ConnectFourGrid.printing_on_screen(0,3,1)
    while True:
        colInputFromUser=agent.userMove(arrayRep,validRowValue)
        rowNumber=validRowValue[colInputFromUser]
        # The pieces are displayed on the turtle screen.
        ConnectFourGrid.printing_on_screen(rowNumber, colInputFromUser, 2)
        arrayRep[rowNumber][colInputFromUser] = 2
        validRowValue[colInputFromUser] += 1
        #Victory condition is checked after the agent plays to see if it has resulted in victory.
        if game.victory(arrayRep,2)==1:
            print"Red won"
            #sleep is added to freeze the turtle screen when the game ends.
            time.sleep(5)
            break
        #Tie happens when the whole grid is filled and there are no connect 4's for agent or opponent.
        if game.tie(arrayRep):
            print "Match tied"
            time.sleep(5)
            break
        colInputFromAgent = agent.agentMove(arrayRep,validRowValue)
        rowNumberAgent = validRowValue[colInputFromAgent]
        ConnectFourGrid.printing_on_screen(rowNumberAgent, colInputFromAgent, 1)
        arrayRep[rowNumberAgent][colInputFromAgent] = 1
        validRowValue[colInputFromAgent] += 1
        if game.victory(arrayRep, 1) == 1:
            print "Blue won"
            time.sleep(5)
            break
        if game.tie(arrayRep):
            print "Match tied"
            time.sleep(5)
            break

#Execution begins from here.
#How to start the game:
## Please enter the valid column number from 0-6 in the command prompt and press enter key to play the move

if __name__ == "__main__":
    gameMoves()
