import ConnectFourGrid










arrayRep = [[0 for x in range(7)] for y in range(6)]



flag = 0

#arrayRep[0][3] = 1

#print arrayRep

validRowValue = [0 for x in range(7)]

#validRowValue[3] += 1

#ConnectFourGrid.printing_on_screen(0, 3,1)

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

    flag=victory(arrayRep, 2)

    print flag

    if flag ==1:

        break

    agentColumnNumber = agentMove(validRowValue, arrayRep)

    agentRow = validRowValue[agentColumnNumber]

    arrayRep[agentRow][agentColumnNumber] = 1

    validRowValue[agentColumnNumber] += 1

    ConnectFourGrid.printing_on_screen(agentRow, agentColumnNumber,1)

    flag=victory(arrayRep, 1)

    print "agent",flag

    if flag ==1:

        print "WINNING MOVE",agentColumnNumber

        break

    for x in validRowValue:#Checking for Tie/Draw

        if x==6:

            break




