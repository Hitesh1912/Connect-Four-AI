import random

def randomAgent(validRowValue):
    #randomcol = 0
    randomcol = random.randint(0, 6)
    print "randomcol", randomcol
    if validRowValue[randomcol] < 6:
        return randomcol
    else:
        randomAgent(validRowValue)

def agentMove(validRowValue):
    #move = 0
    move = random.randint(0, 6)
    print "move", move
    if validRowValue[move] < 6:
        return move
    else:
        agentMove(validRowValue)

arrayRep = [[0 for x in range(7)] for y in range(6)]
flag = 0
arrayRep[0][3] = 1
#print arrayRep
validRowValue = [0 for x in range(7)]
validRowValue[3] += 1
#print validRowValue
count = 1
randomAgentMove = 0
agentColumnNumber = 0
agentRow = 0
randomRow = 0
while flag == 0:
    count += 2
    randomAgentMove = randomAgent(validRowValue)
    print "debugging", randomAgentMove
    randomRow = validRowValue[randomAgentMove]
    arrayRep[randomRow][randomAgentMove] = 2
    validRowValue[randomAgentMove] += 1
    # print arrayRep
    print "before vali", validRowValue
    agentColumnNumber = agentMove(validRowValue)

    print "debugging22", agentColumnNumber
    print "arr", arrayRep
    print "vali", validRowValue
    agentRow = validRowValue[agentColumnNumber]
    arrayRep[agentRow][agentColumnNumber] = 1
    validRowValue[agentColumnNumber] += 1
    # print arrayRep
    print "count",count
    if count == 28:
        break
print arrayRep
print "validRowValue:", validRowValue


