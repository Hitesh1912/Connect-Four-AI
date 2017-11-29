import arrayRepresentation

def check_move(x,arrRep,validRowValue,playerNumber):

    allowed=True

    if validRowValue[x]>=6:

        allowed=False

    rowNumber=validRowValue[x]

    if allowed:

        arrRep[validRowValue[x]][x]=playerNumber

        validRowValue[x]+=1

    return allowed,rowNumber

def game_over(arrRep, agent_number,opponent_number, current_column, legalRowNumber):

    isWinningMove=arrayRepresentation.victory(arrRep,agent_number)

    if isWinningMove==1:

        return agent_number,isWinningMove

    else:

        isWinningMove = arrayRepresentation.victory(arrRep, opponent_number)

    if isWinningMove==1:

        return opponent_number, isWinningMove