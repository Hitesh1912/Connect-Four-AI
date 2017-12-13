import random
import time
from Negamax import Negamax

# The column number ranging from 0-6 is taken from the user. If it is valid,the move is played on the grid.
# Otherwise the user is prompted again to enter the valid column number.
def userMove(arrayRep,validRowValue):

    column = raw_input("Please enter a column between 0-6: ")
    if column.isalpha():
        return userMove(arrayRep, validRowValue)
    #Enter being pressed with the column number condition is handled here.
    if column=="" or column=="EOF" or int(column) not in range(0,7):
        return userMove(arrayRep, validRowValue)
    column=int(column)
    if validRowValue[column] < 6:
       return column
    else:
       return userMove(arrayRep,validRowValue)

# The agent move is computed here
def agentMove(arrayRep,validRowValue):
    start_time = time.time()
    #The max depth is set here
    agentObj=Negamax(arrayRep, validRowValue, 8)
    finalColumnNumber=agentObj.getMove(arrayRep,validRowValue,1,2)
    print("--- %s seconds ---" % (time.time() - start_time))
    return finalColumnNumber

# Random Agent is created to test the agent's performance by comparing the various metrics.
def randomAgent(arrayRep,validRowValue):
    randomcol = random.randint(0, 4)
    if validRowValue[randomcol] < 6:
        return randomcol
    else:
        return randomAgent(arrayRep,validRowValue)
