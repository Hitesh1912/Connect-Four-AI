import ConnectFourGrid
import game
import agent

def gameMoves():
    arrayRep = [[0 for x in range(7)] for y in range(6)]
    validRowValue = [0 for x in range(7)]
    arrayRep[0][3]=1
    validRowValue[3]+=1
    ConnectFourGrid.printing_on_screen(0,3,1)
    while True:
        colInputFromUser=agent.userInput(arrayRep,validRowValue)
        rowNumber=validRowValue[colInputFromUser]
        ConnectFourGrid.printing_on_screen(rowNumber, colInputFromUser, 2)
        arrayRep[rowNumber][colInputFromUser] = 2
        validRowValue[colInputFromUser] += 1
        if game.victory(arrayRep,2)==1:
            break
        colInputFromAgent = agent.agentMove(arrayRep,validRowValue)
        rowNumberAgent = validRowValue[colInputFromAgent]
        ConnectFourGrid.printing_on_screen(rowNumberAgent, colInputFromAgent, 1)
        arrayRep[rowNumberAgent][colInputFromAgent] = 1
        validRowValue[colInputFromAgent] += 1
        if game.victory(arrayRep, 1) == 1:
            break


if __name__== "__main__":
    gameMoves()