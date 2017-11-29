import random

import ConnectFourGrid

import Negamax

#using random agent

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

                if j==3:

                    if (arrayRep[i][j+1] == x and arrayRep[i][j+2] == x and arrayRep[i][j+3] == x) or (arrayRep[i][j-1]== x and arrayRep[i][j-2]== x and arrayRep[i][j-3]== x):

                        print "x wins", x

                        return 1

                elif j<3:

                    if (arrayRep[i][j+1] == x and arrayRep[i][j+2] == x and arrayRep[i][j+3] == x):

                        print "x wins",x

                        return 1

                elif (arrayRep[i][j-1]== x and arrayRep[i][j-2]== x and arrayRep[i][j-3]== x):

                    print "x wins",x

                    return 1

    for i in range(len(arrayRep)):

        for j in range(len(arrayRep[i])):

            if arrayRep[i][j] == x:

                if i <=2:

                    if (arrayRep[i + 1][j] == x and arrayRep[i + 2][j] == x and arrayRep[i + 3][j] == x):

                        print "x wins", x

                        return 1

                elif (arrayRep[i - 1][j] == x and arrayRep[i - 2][j] == x and arrayRep[i - 3][j] == x):

                    print "x wins", x

                    return 1

    for i in range(len(arrayRep)):

        for j in range(len(arrayRep[i])):

            if arrayRep[i][j]==x:

                print "x2"

                if i <= 2 and j <= 3:

                    print "A"

                    print i, j

                    if (arrayRep[i + 1][j + 1] == x and arrayRep[i + 2][j + 2] == x and arrayRep[i + 3][j + 3] == x):

                        print "x wins", x

                        return 1

                if i <= 2 and j >= 3:

                    print "B"

                    print i, j

                    if (arrayRep[i + 1][j - 1] == x and arrayRep[i + 2][j - 2] == x and arrayRep[i + 3][j - 3] == x):

                        print "x wins", x

                        return 1

                if i >= 3 and j >= 3:

                    print "C"

                    print i, j

                    if (arrayRep[i - 1][j - 1] == x and arrayRep[i - 2][j - 2] == x and arrayRep[i - 3][j - 3] == x):

                        print "x wins", x

                        return 1

                if i >= 3 and j <= 3:

                    print "D"

                    print i, j

                    if (arrayRep[i - 1][j + 1] == x and arrayRep[i - 2][j + 2] == x and arrayRep[i - 3][j + 3] == x):

                        print "x wins", x

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

            #Vertical connect 4 Attack

            if arrayRep[i-1][j] == 1 and arrayRep[i-2][j] == 1 and arrayRep[i-3][j] == 1:

                print "Checking here Vertical::"

                if validRowValue[j] == i:

                    return j

            #Horizontal connect 4 Attack

            if j<4:

                if arrayRep[i][j]==1 and arrayRep[i][j+1]==1 and arrayRep[i][j+2]==1:

                    print "Checking here::"

                    if validRowValue[j+3] == i:

                        return j+3

                    elif validRowValue[j-1] == i:

                        return j-1

            #Disjoint horizontal connect 4 -Attack

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

            if arrayRep[i-1][j] == 2 and arrayRep[i-2][j] == 2 and arrayRep[i-3][j] == 2:

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

            if j< 4:

                if arrayRep[i][j]==2 and arrayRep[i][j+3]==2:

                    if arrayRep[i][j+1]==2 and arrayRep[i][j+2]==0:

                        if validRowValue[j+2] == i:

                            return j+2

                    elif arrayRep[i][j+1]==0 and arrayRep[i][j+2]==2:

                        if validRowValue[j + 1] == i:

                         return j+1

    # selecting random move

    move = random.randint(0, 6)

    print "move", move

    if validRowValue[move] < 6:

        return move

    else:

        return agentMove(validRowValue,arrayRep)

arrayRep = [[0 for x in range(7)] for y in range(6)]

Negamax.negaMaxEval(arrayRep, 1,2,0)

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

            break;




