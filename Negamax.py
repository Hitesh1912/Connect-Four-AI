
import game
import random
class Negamax:
    def __init__(self,arrRep,validRowValue,max_depth):
        self.max_depth = max_depth
        self.arrRep=arrRep
        self.valueRowValue=validRowValue
        self.stateScore={}

    def getMove(self,arrRep,validRowValue,agent_number,opponent_number):
        move, score = self.negaMaxEval(arrRep, agent_number,opponent_number,0,validRowValue,-99999,10000)
        # if move == None:
        #     number = random.randint(0, 6)
        #     print "before while", number
        #     while validRowValue[number] > 6:
        #         number = random.randint(0, 6)
        #         print "Inside while", number
        #     print "Entering number",number
        #     return number
        # print "Final:",score
        return move

    def negaMaxEval(self,arrRep,agent_number,opponent_number,depth,validRowValue,alpha,beta):
        import hashlib
        #hashValue=hash(frozenset[arrRep])
        hashValue = hashlib.sha256(str(arrRep).encode('utf-8', 'ignore')).hexdigest()
        count=0
        if hashValue in self.stateScore:
            return None,self.stateScore[hashValue]

        if depth == self.max_depth:
            score=self.evaluation_func(arrRep,validRowValue,agent_number,opponent_number)
            self.stateScore[hashValue]=score
            return None,score

        best_score=-99999999
        best_action=None
        for col in range(0,7,1):
            current_column=col
            isAllowed,validRowValue= game.check_move(current_column,arrRep,validRowValue,agent_number)
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
                best_submove, best_currscore = self.negaMaxEval(arrRep,opponent_number,agent_number,depth + 1,validRowValue,-beta,-alpha)
                best_currscore *= -1
            #Previous Arrayrep is restored.
            rowNumber =validRowValue[current_column]
            arrRep[rowNumber-1][current_column]=0
            validRowValue[current_column]-= 1
            if best_currscore > best_score:
                best_score = best_currscore
                best_action = col
            if alpha < best_score:
                alpha = best_score
            if alpha >= beta:
                break
        if best_action is None:
            print "I was here"
            best_score=self.evaluation_func(arrRep,validRowValue,agent_number,opponent_number)
        self.stateScore[hashValue]=best_score
        return best_action, best_score

    def evaluation_func(self,arrayRep,validRowValue,agent_number,opponent_number):
            for i in range(len(arrayRep)):

                for j in range(len(arrayRep[i])):

                    # Vertical connect 4 Attack

                    if arrayRep[i - 1][j] == agent_number and arrayRep[i - 2][j] == agent_number and arrayRep[i - 3][j] == agent_number:

                        #print "Checking here Vertical::"

                        if validRowValue[j] == i:
                            return 10000
                            #return j


                    # Horizontal connect 4 Attack

                    if j < 4:

                        if arrayRep[i][j] == agent_number and arrayRep[i][j + 1] == agent_number and arrayRep[i][j + 2] == agent_number:

                            print "Checking here::"

                            if validRowValue[j + 3] == i:

                                print "return j + 3"
                                return 9999

                            elif validRowValue[j - 1] == i:
                                print "return j -1"
                                return 9998

                                # return j - 1

                    # Disjoint horizontal connect 4 -Attack

                    if j < 4:

                        if arrayRep[i][j] == agent_number and arrayRep[i][j + 3] == agent_number:

                            if arrayRep[i][j + 1] == agent_number and arrayRep[i][j + 2] == 0:

                                if validRowValue[j + 2] == i:
                                    return 9997
                                    # return j + 2

                            elif arrayRep[i][j + 1] == 0 and arrayRep[i][j + 2] == agent_number:

                                if validRowValue[j + 1] == i:
                                    return 9996
                                    # return j + 1
                    #diagonal attack- 4
                    if arrayRep[i][j] == agent_number:

                        if i <= 2 and j <= 3:
                            if arrayRep[i + 1][j + 1] == agent_number and arrayRep[i + 2][j + 2] == agent_number:
                                if validRowValue[j + 3] == i + 3:
                                    return 9982
                                if j != 0 and i != 0:
                                    if validRowValue[j - 1] == i - 1:
                                        return 9981
                            if arrayRep[i + 3][j + 3] == agent_number:
                                if arrayRep[i + 2][j + 2] == agent_number and arrayRep[i + 1][j + 1] == 0 and  validRowValue[j + 1] == i + 1:
                                    return 9970
                                if arrayRep[i + 2][j + 2] == 0 and arrayRep[i + 1][j + 1] == agent_number and validRowValue[j + 2] == i + 1:
                                    return 9970

                        if i <= 2 and j >= 3:

                            if arrayRep[i + 1][j - 1] == agent_number and arrayRep[i + 2][j - 2] == agent_number:
                                if validRowValue[j - 3] == i + 3:
                                    return 9980
                                if j < 6 and i != 0:
                                    if validRowValue[j + 1] == i - 1:
                                        return 9979
                            if arrayRep[i + 3][j - 3] == agent_number:
                                if arrayRep[i + 2][j - 2] == agent_number and arrayRep[i + 1][j - 1] == 0 and \
                                        validRowValue[j - 1] == i + 1:
                                    return 9965
                                if arrayRep[i + 2][j - 2] == 0 and arrayRep[i + 1][j - 1] == agent_number and \
                                        validRowValue[j - 2] == i + 2:
                                    return 9965

                        if i >= 3 and j >= 3:

                            if arrayRep[i - 1][j - 1] == agent_number and arrayRep[i - 2][j - 2] == agent_number:
                                if validRowValue[j - 3] == i - 3:
                                    return 9978
                                if j < 6 and i < 6:
                                    if validRowValue[j + 1] == i + 1:
                                        return 9977
                            if arrayRep[i - 3][j - 3] == agent_number:
                                if arrayRep[i - 2][j - 2] == agent_number and arrayRep[i - 1][j - 1] == 0 and \
                                        validRowValue[j - 1] == i - 1:
                                    return 9960
                                if arrayRep[i - 2][j - 2] == 0 and arrayRep[i - 1][j - 1] == agent_number and \
                                        validRowValue[j - 2] == i - 2:
                                    return 9960

                        if i >= 3 and j <= 3:
                            if arrayRep[i - 1][j + 1] == agent_number and arrayRep[i - 2][j + 2] == agent_number:
                                if validRowValue[j + 3] == i - 3:
                                    return 9976
                                if j != 0 and i < 6:
                                    if validRowValue[j - 1] == i + 1:
                                        return 9975
                            if arrayRep[i - 3][j + 3] == agent_number:
                                if arrayRep[i - 2][j + 2] == agent_number and arrayRep[i - 1][j + 1] == 0 and \
                                        validRowValue[j + 1] == i - 1:
                                    return 9955
                                if arrayRep[i - 2][j + 2] == 0 and arrayRep[i - 1][j + 1] == agent_number and \
                                        validRowValue[j + 2] == i - 2:
                                    return 9955

            for i in range(len(arrayRep)):

                for j in range(len(arrayRep[i])):

                    # Checking for opponent vertical connect-4

                    if arrayRep[i - 1][j] == opponent_number and arrayRep[i - 2][j] == opponent_number and arrayRep[i - 3][j] == opponent_number:

                        #print "Checking here Vertical::"

                        if validRowValue[j] == i:
                            return 9987
                            # return j

                    # Checking for opponent horizontal connect-4

                    if j < 4:

                        if arrayRep[i][j] == opponent_number and arrayRep[i][j + 1] == opponent_number and arrayRep[i][j + 2] == opponent_number:

                            #print "Checking here::"

                            if validRowValue[j + 3] == i:
                                return 9986

                                # return j + 3

                            elif validRowValue[j - 1] == i:
                                return 9985

                                # return j - 1

                    # Checking the disjoint horizontal connect-4

                    if j < 4:

                        if arrayRep[i][j] == opponent_number and arrayRep[i][j + 3] == opponent_number:

                            if arrayRep[i][j + 1] == opponent_number and arrayRep[i][j + 2] == 0:

                                if validRowValue[j + 2] == i:
                                    return 9984
                                    # return j + 2

                            elif arrayRep[i][j + 1] == 0 and arrayRep[i][j + 2] == opponent_number:

                                if validRowValue[j + 1] == i:
                                    return 9983
                                    # return j + 1
                    if arrayRep[i][j] == opponent_number:

                        if i <= 2 and j <= 3:
                            if arrayRep[i + 1][j + 1] == opponent_number and arrayRep[i + 2][j + 2] == opponent_number:
                                if validRowValue[j+3] == i+3:
                                    return 9982
                                if j!=0 and i!=0:
                                    if validRowValue[j-1] == i-1:
                                        return 9981
                            if arrayRep[i+3][j+3]==opponent_number:
                                if arrayRep[i+2][j+2]==opponent_number and arrayRep[i+1][j+1]==0 and validRowValue[j+1]==i+1:
                                    return 9970
                                if arrayRep[i+2][j+2]==0 and arrayRep[i+1][j+1]==opponent_number and validRowValue[j+2]==i+1:
                                    return 9970



                        if i <= 2 and j >= 3:

                            if arrayRep[i + 1][j - 1] == opponent_number and arrayRep[i + 2][j - 2] == opponent_number:
                                if validRowValue[j-3] == i+3:
                                    return 9980
                                if j<6 and i!=0:
                                    if validRowValue[j+1] == i-1:
                                        return 9979
                            if arrayRep[i+3][j-3]==opponent_number:
                                if arrayRep[i+2][j-2]==opponent_number and arrayRep[i+1][j-1]==0 and validRowValue[j-1]==i+1:
                                    return 9965
                                if arrayRep[i+2][j-2]==0 and arrayRep[i+1][j-1]==opponent_number and validRowValue[j-2]==i+2:
                                    return 9965

                        if i >= 3 and j >= 3:

                            if arrayRep[i - 1][j - 1] == opponent_number and arrayRep[i - 2][j - 2] == opponent_number :
                                if validRowValue[j-3] == i-3:
                                    return 9978
                                if j<6 and i<6:
                                    if validRowValue[j+1] == i+1:
                                        return 9977
                            if arrayRep[i-3][j-3]==opponent_number:
                                if arrayRep[i-2][j-2]==opponent_number and arrayRep[i-1][j-1]==0 and validRowValue[j-1]==i-1:
                                    return 9960
                                if arrayRep[i-2][j-2]==0 and arrayRep[i-1][j-1]==opponent_number and validRowValue[j-2]==i-2:
                                    return 9960

                        if i >= 3 and j <= 3:
                            if arrayRep[i - 1][j + 1] == opponent_number and arrayRep[i - 2][j + 2] == opponent_number:
                                if validRowValue[j+3] == i-3:
                                    return 9976
                                if j!=0 and i<6:
                                    if validRowValue[j-1] == i+1:
                                        return 9975
                            if arrayRep[i-3][j+3]==opponent_number:
                                if arrayRep[i-2][j+2]==opponent_number and arrayRep[i-1][j+1]==0 and validRowValue[j+1]==i-1:
                                    return 9955
                                if arrayRep[i-2][j+2]==0 and arrayRep[i-1][j+1]==opponent_number and validRowValue[j+2]==i-2:
                                    return 9955


                        #attack connect 3
            for i in range(len(arrayRep)):

                for j in range(len(arrayRep[i])):

                    # Vertical connect 3 Attack
                    if i<3:
                        if arrayRep[i][j] == agent_number and arrayRep[i+1][j] == agent_number:
                            if validRowValue[j] == i+2:
                                return 3000

                    # Horizontal connect 3 Attack

                    if j<4:
                        if arrayRep[i][j] == agent_number and arrayRep[i][j+1] == agent_number:
                            if validRowValue[j+2] == i:
                                return 3000
                            if validRowValue[j-1] == i:
                                return 3000

                    elif arrayRep[i][4] == 0 and validRowValue[4] == i:
                        if arrayRep[i][5] == agent_number and arrayRep[i][6] == agent_number:
                            return 3000

            import random

            randomScore = random.randint(0, 2000)
            print "Checking here", randomScore
            return randomScore