# Kai Yun Chao
# Market Class
import random
#Assigning the random cost for each medicine, and the name of the medicine in both TCM and Western Medicine.
金銀花 = random.randint(10, 20)
枸杞 = random.randint(10, 20)
菊花 = random.randint(1, 5)
砷 = random.randint(10, 20)
竹蜂 = random.randint(50, 100)
人參 = random.randint(200, 400)
燕窩 = random.randint(70, 150)
水銀 = random.randint(50, 70)
牛黃 = random.randint(500, 700)
鹿茸 = random.randint(1000, 1200)
龜板 = random.randint(2000, 3000)
虎骨 = random.randint(4000, 7000)
犀角 = random.randint(8000, 10000)
# Cost for the western medicine is still undicided.
Ibuprofen = random.randint(1, 3)
Paracetamol = random.randint(1, 3)
Amoxicillin = random.randint(1, 3)
Valacyclovir = random.randint(1, 3)
Rifampin = random.randint(1, 3)
Morphine = random.randint(1, 3)
Fentanyl = random.randint(1, 3)
Tigecycline = random.randint(1, 3)
# The name and cost of the medicine are stored in a list, and the random number is used to select a medicine from the list.
TCM1Name = ["金銀花(Honeysuckle)", "枸杞(Goji Beery)", "菊花(Chrysanthemum)",  "砷(Arsenic)"]
TCM2Name = ["竹蜂(Carpenter Bee)","人參(Ginseng)", "燕窩(Swallow Nest)", "水銀(Mercury)"]
TCM3Name = ["牛黃(Cattle Gallstone)", "鹿茸(Velvet Deer Antler)", "龜板(Turtle Shell)", "虎骨(Tiger Bone)", "犀角(Rhinoceros Horn)"]
TCM1Cost = [金銀花, 枸杞, 菊花, 砷]
TCM2Cost = [竹蜂, 人參, 燕窩, 水銀]
TCM3Cost = [牛黃, 鹿茸, 龜板, 虎骨, 犀角]

WestLowName = ["Ibuprofen", "Paracetamol", "Amoxicillin"]
WestHighName = ["Valacyclovir", "Rifampin", "Morphine"]
WestUltraName = ["Fentanyl", "Tigecycline"]
WestLowCost = [Ibuprofen, Paracetamol, Amoxicillin]
WestHighCost = [Valacyclovir, Rifampin, Morphine]
WestUltraCost = [Fentanyl, Tigecycline]

# The random number is used to select a medicine from the list, and the name and cost of the medicine are stored in a tuple.
T1N = random.randint(0,3)
T2N = random.randint(0, 3)
T3N = random.randint(0,4)
T1C = random.randint(0,3)
T2C = random.randint(0,3)
T3C = random.randint(0,4)

WLN = random.randint(0,2)
WLC = random.randint(0,2)
WHN = random.randint(0,2)
WHC = random.randint(0,2)
WUN = random.randint(0,1)
WUC = random.randint(0,1)
Med1 = (TCM1Name[T1N], TCM1Cost[T1C])
Med2 = (TCM2Name[T2N], TCM2Cost[T2C])
Med3 = (TCM3Name[T3N], TCM3Cost[T3C])
Med4 = (WestLowName[WLN], WestLowCost[WLC])
Med5 = (WestHighName[WHN], WestHighCost[WHC])
Med6 = (WestUltraName[WUN], WestUltraCost[WUC])

print(Med1, Med2, Med3)
print(Med4, Med5, Med6)