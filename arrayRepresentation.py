arrayRep = [[0 for x in range(7)] for y in range(6)]
flag=0
arrayRep[0][3]=1
print arrayRep
rowValueWhenPlayedNext=[0 for x in range(7)]
rowValueWhenPlayedNext[3]+=1
print rowValueWhenPlayedNext

while flag==0:
 randomAgentmove=randomAgent()
 agentColumnNumber=agentmove()
 break
