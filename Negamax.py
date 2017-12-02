
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
                                return 10000

                            elif validRowValue[j - 1] == i:
                                print "return j -1"
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
                    #diagonal attack- 4
                    if arrayRep[i][j] == agent_number:

                        if i <= 2 and j <= 3:
                            if arrayRep[i + 1][j + 1] == agent_number and arrayRep[i + 2][j + 2] == agent_number:
                                if validRowValue[j + 3] == i + 3:
                                    return 10000
                                if j != 0 and i != 0:
                                    if validRowValue[j - 1] == i - 1:
                                        return 10000
                            if arrayRep[i + 3][j + 3] == agent_number:
                                if arrayRep[i + 2][j + 2] == agent_number and arrayRep[i + 1][j + 1] == 0 and  validRowValue[j + 1] == i + 1:
                                    return 10000
                                if arrayRep[i + 2][j + 2] == 0 and arrayRep[i + 1][j + 1] == agent_number and validRowValue[j + 2] == i + 1:
                                    return 10000

                        if i <= 2 and j >= 3:

                            if arrayRep[i + 1][j - 1] == agent_number and arrayRep[i + 2][j - 2] == agent_number:
                                if validRowValue[j - 3] == i + 3:
                                    return 10000
                                if j < 6 and i != 0:
                                    if validRowValue[j + 1] == i - 1:
                                        return 10000
                            if arrayRep[i + 3][j - 3] == agent_number:
                                if arrayRep[i + 2][j - 2] == agent_number and arrayRep[i + 1][j - 1] == 0 and \
                                        validRowValue[j - 1] == i + 1:
                                    return 10000
                                if arrayRep[i + 2][j - 2] == 0 and arrayRep[i + 1][j - 1] == agent_number and \
                                        validRowValue[j - 2] == i + 2:
                                    return 10000

                        if i >= 3 and j >= 3:

                            if arrayRep[i - 1][j - 1] == agent_number and arrayRep[i - 2][j - 2] == agent_number:
                                if validRowValue[j - 3] == i - 3:
                                    return 10000
                                if j < 6 and i < 6:
                                    if validRowValue[j + 1] == i + 1:
                                        return 10000
                            if arrayRep[i - 3][j - 3] == agent_number:
                                if arrayRep[i - 2][j - 2] == agent_number and arrayRep[i - 1][j - 1] == 0 and \
                                        validRowValue[j - 1] == i - 1:
                                    return 10000
                                if arrayRep[i - 2][j - 2] == 0 and arrayRep[i - 1][j - 1] == agent_number and \
                                        validRowValue[j - 2] == i - 2:
                                    return 10000

                        if i >= 3 and j <= 3:
                            if arrayRep[i - 1][j + 1] == agent_number and arrayRep[i - 2][j + 2] == agent_number:
                                if validRowValue[j + 3] == i - 3:
                                    return 10000
                                if j != 0 and i < 6:
                                    if validRowValue[j - 1] == i + 1:
                                        return 10000
                            if arrayRep[i - 3][j + 3] == agent_number:
                                if arrayRep[i - 2][j + 2] == agent_number and arrayRep[i - 1][j + 1] == 0 and \
                                        validRowValue[j + 1] == i - 1:
                                    return 10000
                                if arrayRep[i - 2][j + 2] == 0 and arrayRep[i - 1][j + 1] == agent_number and \
                                        validRowValue[j + 2] == i - 2:
                                    return 10000

            for i in range(len(arrayRep)):

                for j in range(len(arrayRep[i])):

                    # Checking for opponent vertical connect-4

                    if arrayRep[i - 1][j] == opponent_number and arrayRep[i - 2][j] == opponent_number and arrayRep[i - 3][j] == opponent_number:

                        #print "Checking here Vertical::"

                        if validRowValue[j] == i:
                            return 9999
                            # return j

                    # Checking for opponent horizontal connect-4

                    if j < 4:

                        if arrayRep[i][j] == opponent_number and arrayRep[i][j + 1] == opponent_number and arrayRep[i][j + 2] == opponent_number:

                            #print "Checking here::"

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
                    if arrayRep[i][j] == opponent_number:

                        if i <= 2 and j <= 3:
                            if arrayRep[i + 1][j + 1] == opponent_number and arrayRep[i + 2][j + 2] == opponent_number:
                                if validRowValue[j+3] == i+3:
                                    return 9999
                                if j!=0 and i!=0:
                                    if validRowValue[j-1] == i-1:
                                        return 9999
                            if arrayRep[i+3][j+3]==opponent_number:
                                if arrayRep[i+2][j+2]==opponent_number and arrayRep[i+1][j+1]==0 and validRowValue[j+1]==i+1:
                                    return 9999
                                if arrayRep[i+2][j+2]==0 and arrayRep[i+1][j+1]==opponent_number and validRowValue[j+2]==i+1:
                                    return 9999



                        if i <= 2 and j >= 3:

                            if arrayRep[i + 1][j - 1] == opponent_number and arrayRep[i + 2][j - 2] == opponent_number:
                                if validRowValue[j-3] == i+3:
                                    return 9999
                                if j<6 and i!=0:
                                    if validRowValue[j+1] == i-1:
                                        return 9999
                            if arrayRep[i+3][j-3]==opponent_number:
                                if arrayRep[i+2][j-2]==opponent_number and arrayRep[i+1][j-1]==0 and validRowValue[j-1]==i+1:
                                    return 9999
                                if arrayRep[i+2][j-2]==0 and arrayRep[i+1][j-1]==opponent_number and validRowValue[j-2]==i+2:
                                    return 9999

                        if i >= 3 and j >= 3:

                            if arrayRep[i - 1][j - 1] == opponent_number and arrayRep[i - 2][j - 2] == opponent_number :
                                if validRowValue[j-3] == i-3:
                                    return 9999
                                if j<6 and i<6:
                                    if validRowValue[j+1] == i+1:
                                        return 9999
                            if arrayRep[i-3][j-3]==opponent_number:
                                if arrayRep[i-2][j-2]==opponent_number and arrayRep[i-1][j-1]==0 and validRowValue[j-1]==i-1:
                                    return 9999
                                if arrayRep[i-2][j-2]==0 and arrayRep[i-1][j-1]==opponent_number and validRowValue[j-2]==i-2:
                                    return 9999

                        if i >= 3 and j <= 3:
                            if arrayRep[i - 1][j + 1] == opponent_number and arrayRep[i - 2][j + 2] == opponent_number:
                                if validRowValue[j+3] == i-3:
                                    return 9999
                                if j!=0 and i<6:
                                    if validRowValue[j-1] == i+1:
                                        return 9999
                            if arrayRep[i-3][j+3]==opponent_number:
                                if arrayRep[i-2][j+2]==opponent_number and arrayRep[i-1][j+1]==0 and validRowValue[j+1]==i-1:
                                    return 9999
                                if arrayRep[i-2][j+2]==0 and arrayRep[i-1][j+1]==opponent_number and validRowValue[j+2]==i-2:
                                    return 9999






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
                                return 3002
                            if validRowValue[j-1] == i:
                                return 3003
                    elif arrayRep[i][4] == 0 and validRowValue[4] == i:
                        if arrayRep[i][5] == agent_number and arrayRep[i][6] == agent_number:
                            return 3005

                    #horizontal disjoint attck-3
                    if j<=4:
                        if arrayRep[i][j] == agent_number and arrayRep[i][j+2] == agent_number and validRowValue[j+1]==i:
                                return 3099

                    #horizontal disjoint 3 defence
                        if arrayRep[i][j] == opponent_number and arrayRep[i][j+2] == opponent_number and validRowValue[j+1]==i:
                            #print"Entering diag disjoint def 3"
                            return 3090
                        # random
            if validRowValue[3] < 5:
                newRow = validRowValue[3]
                arrayRep[newRow + 1][3] = opponent_number
                print "New row", newRow
                if game.victory(arrayRep, opponent_number) != 1:
                                arrayRep[newRow + 1][3] = 0
                                return 4000
                arrayRep[newRow + 1][3] = 0
            if validRowValue[4] < 5:
                            newRow = validRowValue[4]
                            arrayRep[newRow + 1][4] = opponent_number
                            if game.victory(arrayRep, opponent_number) != 1:
                                arrayRep[newRow + 1][4] = 0
                                return 3000
                            arrayRep[newRow + 1][4] = 0
            if validRowValue[2] < 5:
                            newRow = validRowValue[2]
                            arrayRep[newRow + 1][2] = opponent_number
                            if game.victory(arrayRep, opponent_number) != 1:
                                arrayRep[newRow + 1][2] = 0
                                return 2000
                            arrayRep[newRow + 1][2] = 0
            if validRowValue[5] < 5:
                            newRow = validRowValue[5]
                            arrayRep[newRow + 1][5] = opponent_number
                            if game.victory(arrayRep, opponent_number) != 1:
                                arrayRep[newRow + 1][5] = 0
                                return 1000
                            arrayRep[newRow + 1][5] = 0
            if validRowValue[1] < 5:
                            newRow = validRowValue[1]
                            arrayRep[newRow + 1][1] = opponent_number
                            if game.victory(arrayRep, opponent_number) != 1:
                                arrayRep[newRow + 1][1] = 0
                                return 500
                            arrayRep[newRow + 1][1] = 0
            if validRowValue[6] < 5:
                            newRow = validRowValue[6]
                            arrayRep[newRow + 1][6] = opponent_number
                            if game.victory(arrayRep, opponent_number) != 1:
                                arrayRep[newRow + 1][6] = 0
                                return 250
                            arrayRep[newRow + 1][6] = 0
            if validRowValue[0] < 5:
                            newRow = validRowValue[0]
                            arrayRep[newRow + 1][0] = opponent_number
                            if game.victory(arrayRep, opponent_number) != 1:
                                arrayRep[newRow + 1][0] = 0
                                return 200
                            arrayRep[newRow + 1][0] = 0
            # import random
            #
            # randomScore = random.randint(0, 6)
            # print "Checking here", randomScore
            # return randomScore
            #


            import random

            randomScore = random.randint(1, 5)
            print "Checking here", randomScore
            return randomScore
