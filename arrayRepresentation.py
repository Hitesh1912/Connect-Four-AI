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

def victory(arrayRep,x):
    for i in range(len(arrayRep)):
        for j in range(len(arrayRep[i])):
            if arrayRep[i][j]==x:
                if j<=3:
                    if (arrayRep[i+1][j]==x and arrayRep[i+2][j]==x and arrayRep[i+3][j]==x):
                        print "x wins",x
                        return 1
                elif (arrayRep[i-1][j]== x and arrayRep[i-2][j]== x and arrayRep[i-3][j]== x):
                    print "x wins",x
                    return 1
    return 0

def randomAgent(validRowValue):
        column = int(input("Please enter a column between 0-6: "))
        if 0 <= column <= 6:
            if validRowValue[column] < 6:
                return column
            else:
                return randomAgent(validRowValue)
        else:
            return randomAgent(validRowValue)


def agentMove(validRowValue,arrayRep):
    #move = 0
    for i in range(len(arrayRep)):
        for j in range(len(arrayRep[i])):
            if arrayRep[i][j]==1 and arrayRep[i][j+1]==1:
                print "Checking here::"
                if j<6:
                    return j+2
                else:
                    return j-1
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
randomAgentMove = 0
agentColumnNumber = 0
agentRow = 0
randomRow = 0
while flag == 0:
    randomAgentMove = randomAgent(validRowValue)
    randomRow = validRowValue[randomAgentMove]
    arrayRep[randomRow][randomAgentMove] = 2
    validRowValue[randomAgentMove] += 1
    ConnectFourGrid.printing_on_screen(randomRow,randomAgentMove,2)
    flag=victory(arrayRep,2)
    if flag==1:
        break
    agentColumnNumber = agentMove(validRowValue,arrayRep)
    agentRow = validRowValue[agentColumnNumber]
    arrayRep[agentRow][agentColumnNumber] = 1
    validRowValue[agentColumnNumber] += 1
    ConnectFourGrid.printing_on_screen(agentRow, agentColumnNumber,1)
    flag=victory(arrayRep, 1)
    if flag==1:
        break
    for x in validRowValue:#Checking for Tie/Draw
        if x==6:
            break;


