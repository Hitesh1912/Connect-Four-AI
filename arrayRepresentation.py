import random
import ConnectFourGrid


# def randomAgent(validRowValue):
#     #randomcol = 0
#     randomcol = random.randint(0, 6)
#     print "randomcol", randomcol
#     if validRowValue[randomcol] < 6:
#         return randomcol
#     else:
#         return randomAgent(validRowValue)

def randomAgent(validRowValue):
        column = int(input("Please enter a column between 0-6: "))
        if 0 <= column <= 6:
            if validRowValue[column] < 6:
                return column
            else:
                return randomAgent(validRowValue)
        else:
            return randomAgent(validRowValue)


def agentMove(validRowValue):
    #move = 0
    move = random.randint(0, 6)
    print "move", move
    if validRowValue[move] < 6:
        return move
    else:
        return agentMove(validRowValue)

arrayRep = [[0 for x in range(7)] for y in range(6)]
flag = 0
arrayRep[0][3] = 1
#print arrayRep
validRowValue = [0 for x in range(7)]
validRowValue[3] += 1
ConnectFourGrid.printing_on_screen(0, 3,1)
#print validRowValue
count = 1
randomAgentMove = 0
agentColumnNumber = 0
agentRow = 0
randomRow = 0
while flag == 0:
    count += 2
    randomAgentMove = randomAgent(validRowValue)
    #print "debugging", randomAgentMove
    randomRow = validRowValue[randomAgentMove]
    arrayRep[randomRow][randomAgentMove] = 2
    validRowValue[randomAgentMove] += 1
    ConnectFourGrid.printing_on_screen(randomRow,randomAgentMove,2)
    # print arrayRep
    #print "before vali", validRowValue
    agentColumnNumber = agentMove(validRowValue)

    #print "debugging22", agentColumnNumber
    #print "arr", arrayRep
    #print "vali", validRowValue
    agentRow = validRowValue[agentColumnNumber]
    arrayRep[agentRow][agentColumnNumber] = 1
    validRowValue[agentColumnNumber] += 1
    ConnectFourGrid.printing_on_screen(agentRow, agentColumnNumber,1)
    # print arrayRep
    #print "count",count
    if count == 35:
        break
#print arrayRep
#print "validRowValue:", validRowValue


