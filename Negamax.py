import game
class Negamax:
    def __init__(self,arrRep,validRowValue,max_depth=4):

            self.max_depth = max_depth

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

                isAllowed,legalRowNumber= game.check_move(x,arrRep,self.validRowValue,agent_number)

                if not isAllowed:

                    continue

                winner,game_over = game.game_over(arrRep, agent_number,opponent_number, current_column, legalRowNumber)

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

    def evaluation_func(self,arrayRep,validRowValue):
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

    def getMove(self,arrRep,validRowValue,agent_number,opponent_number):
        move, score = self.negaMaxEval(arrRep, agent_number,opponent_number)
        print score


        return move
