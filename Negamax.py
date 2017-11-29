import game
import copy
class Negamax:
    def __init__(self,arrRep,validRowValue,max_depth):
        self.max_depth = max_depth
        self.arrRep=arrRep
        self.valueRowValue=validRowValue
        self.stateScore={}

    def getMove(self,arrRep,validRowValue,agent_number,opponent_number):
        move, score = self.negaMaxEval(arrRep, agent_number,opponent_number,0,validRowValue)
        print score
        return move

    def negaMaxEval(self,arrRep,agent_number,opponent_number,depth,validRowValue):
        import hashlib
        #hashValue=hash(frozenset[arrRep])
        hashValue = hashlib.sha256(str(arrRep).encode('utf-8', 'ignore')).hexdigest()
        count=0
        print "curr",agent_number
        print "opp",opponent_number
        if hashValue in self.stateScore:
            return None,self.stateScore[hashValue]

        if depth == self.max_depth:
            score=self.evaluation_func(arrRep,validRowValue,agent_number,opponent_number)
            self.stateScore[hashValue]=score
            return None,score

        best_score=-999
        best_action=None
        for col in range(0,6,1):
            current_column=col
            isAllowed,legalRowNumber= game.check_move(current_column,arrRep,validRowValue,agent_number)
            if not isAllowed:
                continue
            winner,game_over = game.game_over(arrRep, agent_number,opponent_number, current_column, validRowValue)
            if game_over:
                if winner == agent_number:
                    best_currscore = 9999
                elif winner == opponent_number:
                    best_currscore = -9999
                else:
                    best_currscore = 0
            else:
                best_submove, best_currscore = self.negaMaxEval(arrRep,opponent_number,agent_number,depth + 1,validRowValue)
                best_currscore *= -1

            #Previous Arrayrep is restored.
            rowNumber =validRowValue[current_column]
            print "Fail-1",rowNumber
            print "Fail-2",current_column
            arrRep[rowNumber][current_column]=0
            validRowValue[current_column]-= 1

            print "Seeing if changes restored", arrRep
            if best_currscore > best_score:
                best_score = best_currscore
                best_action = col

        if best_action is None:
            best_score=self.evaluation_func(arrRep,validRowValue,agent_number,opponent_number)
        self.stateScore[hashValue]=best_score
        return best_action, best_score

    def evaluation_func(self,arrayRep,validRowValue,agent_number,opponent_number):
            for i in range(len(arrayRep)):

                for j in range(len(arrayRep[i])):

                    # Vertical connect 4 Attack

                    if arrayRep[i - 1][j] == agent_number and arrayRep[i - 2][j] == agent_number and arrayRep[i - 3][j] == agent_number:

                        print "Checking here Vertical::"

                        if validRowValue[j] == i:
                            return 10000
                            #return j


                    # Horizontal connect 4 Attack

                    if j < 4:

                        if arrayRep[i][j] == agent_number and arrayRep[i][j + 1] == agent_number and arrayRep[i][j + 2] == agent_number:

                            print "Checking here::"

                            if validRowValue[j + 3] == i:

                                #return j + 3
                                return 10000

                            elif validRowValue[j - 1] == i:
                                return 10000

                                # return j - 1

                    # Disjoint horizontal connect 4 -Attack

                    if j < 4:

                        if arrayRep[i][j] == agent_number and arrayRep[i][j + 3] == agent_number:

                            if arrayRep[i][j + 1] == agent_number and arrayRep[i][j + 2] == 0:

                                if validRowValue[j + 2] == i:
                                    return 10000
                                    # return j + 2

                            elif arrayRep[i][j + 1] == 0 and arrayRep[i][j + 2] == agent_number:

                                if validRowValue[j + 1] == i:
                                    return 10000
                                    # return j + 1

            for i in range(len(arrayRep)):

                for j in range(len(arrayRep[i])):

                    # Checking for opponent vertical connect-4

                    if arrayRep[i - 1][j] == opponent_number and arrayRep[i - 2][j] == opponent_number and arrayRep[i - 3][j] == opponent_number:

                        print "Checking here Vertical::"

                        if validRowValue[j] == i:
                            return 9999
                            # return j

                    # Checking for opponent horizontal connect-4

                    if j < 4:

                        if arrayRep[i][j] == opponent_number and arrayRep[i][j + 1] == opponent_number and arrayRep[i][j + 2] == opponent_number:

                            print "Checking here::"

                            if validRowValue[j + 3] == i:
                                return 9999

                                # return j + 3

                            elif validRowValue[j - 1] == i:
                                return 9999

                                # return j - 1

                    # Checking the disjoint horizontal connect-4

                    if j < 4:

                        if arrayRep[i][j] == opponent_number and arrayRep[i][j + 3] == opponent_number:

                            if arrayRep[i][j + 1] == opponent_number and arrayRep[i][j + 2] == 0:

                                if validRowValue[j + 2] == i:
                                    return 9999
                                    # return j + 2

                            elif arrayRep[i][j + 1] == 0 and arrayRep[i][j + 2] == opponent_number:

                                if validRowValue[j + 1] == i:
                                    return 9999
                                    # return j + 1
            import random
            print "Checking here",arrayRep
            randomcol = random.randint(0, 80)
            return randomcol

