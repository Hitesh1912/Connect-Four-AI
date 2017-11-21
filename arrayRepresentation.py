import random

def randomAgent(validRowValue):

    randomcol= random.randint(0,6)
    if validRowValue[randomcol]<5:
        return randomcol
    else:
        randomcol(validRowValue)

def agentMove(validRowValue):
    move = random.randint(0, 6)
    if validRowValue[move] < 5:
        return move
    else:
        agentMove(validRowValue)

arrayRep = [[0 for x in range(7)] for y in range(6)]
flag=0
arrayRep[0][3]=1
print arrayRep
validRowValue=[0 for x in range(7)]
validRowValue[3]+=1
print validRowValue

while flag==0:
    agentColumnNumber=agentMove(validRowValue)
    validRowValue[agentColumnNumber]+=1
    arrayRep[validRowValue[agentColumnNumber]][agentColumnNumber]=1
    print arrayRep
    randomAgentMove=randomAgent(validRowValue)
    validRowValue[agentColumnNumber] += 1
    arrayRep[validRowValue[agentColumnNumber]][randomAgentMove]=2
    print arrayRep
    break


