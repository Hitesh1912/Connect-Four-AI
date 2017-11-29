
def __init__(self,arrRep,validRowValue,max_depth=4):

    self.max_depth=max_depth

    self.arrRep=[]

    self.arrRep=arrRep

    self.valueRowValue=validRowValue

def negaMaxEval(self,arrRep,agent_number,opponent_number,depth=0):

    if depth == self.max_depth:

        score=self.evaluateFunc(self.arrRep)

        return score

    best_score=-999999

    best_action=None

    for x in range(0,6,1):

        current_column=x

        isAllowed,legalRowNumber= arrayRepresentation.check_move(x,arrRep,self.validRowValue,agent_number)

        if not isAllowed:

            continue

        winner,game_over = arrayRepresentation.game_over(arrRep, agent_number,opponent_number, current_column, legalRowNumber)

        if game_over:

            if winner == agent_number:

                best_currscore = 9999999999

            elif winner == opponent_number:

                best_currscore = -9999999999

            else:

                best_currscore = 0

        else:

            best_submove, best_currscore = self.__negamax(arrRep,

                                                          opponent_number,

                                                          agent_number,

                                                          depth + 1)

            best_currscore *= -1

        rowNumber =legalRowNumber[x]

        arrRep[rowNumber][x]=0

        legalRowNumber[x]-=1

        if best_currscore > best_score:

            best_score = best_currscore

            best_move = x

    return best_move, best_score

