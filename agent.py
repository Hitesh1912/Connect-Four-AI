import random
import time

from Negamax import Negamax
def userInput(arrayRep,validRowValue):

    column = raw_input("Please enter a column between 0-6: ")
    if column.isalpha():
        return userInput(arrayRep, validRowValue)
    if column=="" or column=="EOF" or int(column) not in range(0,6):
         return userInput(arrayRep, validRowValue)
    column=int(column)
    if validRowValue[column] < 6:
       return column
    else:
       return userInput(arrayRep,validRowValue)


def agentMove(arrayRep,validRowValue):
    start_time = time.time()
    agentObj=Negamax(arrayRep,validRowValue,6)
    finalColumnNumber=agentObj.getMove(arrayRep,validRowValue,1,2)
    print("--- %s seconds ---" % (time.time() - start_time))
    return finalColumnNumber
    #return hardCodedAI(arrayRep,validRowValue)


def randomAgent(arrayRep,validRowValue):
    randomcol = random.randint(0, 4)
    if validRowValue[randomcol] < 6:
        return randomcol
    else:
        return randomAgent(arrayRep,validRowValue)

def hardCodedAI(arrayRep,validRowValue):
    for i in range(len(arrayRep)):

        for j in range(len(arrayRep[i])):

            # Vertical connect 4 Attack

            if arrayRep[i - 1][j] == 1 and arrayRep[i - 2][j] == 1 and arrayRep[i - 3][j] == 1:

                print "Checking here Vertical::"

                if validRowValue[j] == i:
                    return j

            # Horizontal connect 4 Attack

            if j < 4:

                if arrayRep[i][j] == 1 and arrayRep[i][j + 1] == 1 and arrayRep[i][j + 2] == 1:

                    print "Checking here::"

                    if validRowValue[j + 3] == i:

                        return j + 3

                    elif validRowValue[j - 1] == i:

                        return j - 1

            # Disjoint horizontal connect 4 -Attack

            if j < 4:

                if arrayRep[i][j] == 1 and arrayRep[i][j + 3] == 1:

                    if arrayRep[i][j + 1] == 1 and arrayRep[i][j + 2] == 0:

                        if validRowValue[j + 2] == i:
                            return j + 2

                    elif arrayRep[i][j + 1] == 0 and arrayRep[i][j + 2] == 1:

                        if validRowValue[j + 1] == i:
                            return j + 1

    for i in range(len(arrayRep)):

        for j in range(len(arrayRep[i])):

            # Checking for opponent vertical connect-4

            if arrayRep[i - 1][j] == 2 and arrayRep[i - 2][j] == 2 and arrayRep[i - 3][j] == 2:

                print "Checking here Vertical::"

                if validRowValue[j] == i:
                    return j

            # Checking for opponent horizontal connect-4

            if j < 4:

                if arrayRep[i][j] == 2 and arrayRep[i][j + 1] == 2 and arrayRep[i][j + 2] == 2:

                    print "Checking here::"

                    if validRowValue[j + 3] == i:

                        return j + 3

                    elif validRowValue[j - 1] == i:

                        return j - 1

            # Checking the disjoint horizontal connect-4

            if j < 4:

                if arrayRep[i][j] == 2 and arrayRep[i][j + 3] == 2:

                    if arrayRep[i][j + 1] == 2 and arrayRep[i][j + 2] == 0:

                        if validRowValue[j + 2] == i:
                            return j + 2

                    elif arrayRep[i][j + 1] == 0 and arrayRep[i][j + 2] == 2:

                        if validRowValue[j + 1] == i:
                            return j + 1
    return randomAgent(arrayRep,validRowValue)