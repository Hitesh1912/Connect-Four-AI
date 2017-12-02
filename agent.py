import random
import time

from Negamax import Negamax
def userInput(arrayRep,validRowValue):

    column = raw_input("Please enter a column between 0-6: ")
    if column.isalpha():
        return userInput(arrayRep, validRowValue)
    if column=="" or column=="EOF" or int(column) not in range(0,7):
        return userInput(arrayRep, validRowValue)
    column=int(column)
    if validRowValue[column] < 6:
       return column
    else:
       return userInput(arrayRep,validRowValue)


def agentMove(arrayRep,validRowValue):
    start_time = time.time()
    agentObj=Negamax(arrayRep,validRowValue,8)
    finalColumnNumber=agentObj.getMove(arrayRep,validRowValue,1,2)
    print("--- %s seconds ---" % (time.time() - start_time))
    return finalColumnNumber
    #return hardCodedAI(arrayRep,validRowValue)
# def userInput(arrayRep,validRowValue):
#     start_time = time.time()
#     agentObj=Negamax(arrayRep,validRowValue,2)
#     finalColumnNumber=agentObj.getMove(arrayRep,validRowValue,1,2)
#     print("--- %s seconds ---" % (time.time() - start_time))
#     return finalColumnNumber

def randomAgent(arrayRep,validRowValue):
    randomcol = random.randint(0, 4)
    if validRowValue[randomcol] < 6:
        return randomcol
    else:
        return randomAgent(arrayRep,validRowValue)