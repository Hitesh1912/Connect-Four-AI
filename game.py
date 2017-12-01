def check_move(x, arrRep, validRowValue, playerNumber):
    allowed = True
    if validRowValue[x] >= 6:
        allowed = False
    #rowNumber = validRowValue[x]

    if allowed:
        arrRep[validRowValue[x]][x] = playerNumber
        validRowValue[x] += 1
    return allowed, validRowValue


def game_over(arrRep, agent_number, opponent_number, current_column, validRowValue):
    isWinningMove = victory(arrRep, agent_number)
    if isWinningMove == 1:
        return agent_number, True
    else:
        isWinningMove = victory(arrRep, opponent_number)
    if isWinningMove == 1:
        return opponent_number, True
    count=0
    for i in range(len(validRowValue)):
        if validRowValue[i] == 6:
            count += 1
    if count == 7:
        return None,True
    return None,False #No one has won


def victory(arrayRep, x):
    for i in range(len(arrayRep)):

        for j in range(len(arrayRep[i])):

            if arrayRep[i][j] == x:

                if j == 3:

                    if (arrayRep[i][j + 1] == x and arrayRep[i][j + 2] == x and arrayRep[i][j + 3] == x) or (
                                        arrayRep[i][j - 1] == x and arrayRep[i][j - 2] == x and arrayRep[i][
                                    j - 3] == x):


                        return 1

                elif j < 3:

                    if (arrayRep[i][j + 1] == x and arrayRep[i][j + 2] == x and arrayRep[i][j + 3] == x):


                        return 1

                elif (arrayRep[i][j - 1] == x and arrayRep[i][j - 2] == x and arrayRep[i][j - 3] == x):



                    return 1

    for i in range(len(arrayRep)):

        for j in range(len(arrayRep[i])):

            if arrayRep[i][j] == x:

                if i <= 2:

                    if (arrayRep[i + 1][j] == x and arrayRep[i + 2][j] == x and arrayRep[i + 3][j] == x):

                        return 1

                elif (arrayRep[i - 1][j] == x and arrayRep[i - 2][j] == x and arrayRep[i - 3][j] == x):
                    return 1

    for i in range(len(arrayRep)):

        for j in range(len(arrayRep[i])):

            if arrayRep[i][j] == x:

                if i <= 2 and j <= 3:
                    if (arrayRep[i + 1][j + 1] == x and arrayRep[i + 2][j + 2] == x and arrayRep[i + 3][j + 3] == x):

                        return 1

                if i <= 2 and j >= 3:

                    if (arrayRep[i + 1][j - 1] == x and arrayRep[i + 2][j - 2] == x and arrayRep[i + 3][j - 3] == x):


                        return 1

                if i >= 3 and j >= 3:

                    if (arrayRep[i - 1][j - 1] == x and arrayRep[i - 2][j - 2] == x and arrayRep[i - 3][j - 3] == x):


                        return 1

                if i >= 3 and j <= 3:
                    if (arrayRep[i - 1][j + 1] == x and arrayRep[i - 2][j + 2] == x and arrayRep[i - 3][j + 3] == x):


                        return 1

    return 0

def tie(arrayRep):
    for i in range(len(arrayRep)):

        for j in range(len(arrayRep[i])):
            if arrayRep[i][j]==0:
                return False
    return True