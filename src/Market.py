# Kai Yun Chao
import random
Amoxicillin = random.randint(10,21)
Insulin = random.randint(50, 71)
Metoprolol = random.randint(200, 231)
med = 100
Med = 200
MED = 300
TCMName = ["med", "Med", "MED"]
TCMCost = [med, Med, MED]
WestName = ["Amox" , "Ins" , " Meto"]
WestCost = [Amoxicillin, Insulin, Metoprolol]

wc = random.randint(0,2)
wn = random.randint(0, 2)
tn = random.randint(0,2)
tc = random.randint(0,2)
Med1 = (WestName[wn], WestCost[wc]) 
Med2 = (TCMName[tn],TCMCost[tc])

print(Med1)