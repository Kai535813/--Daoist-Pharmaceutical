# Kai Yun Chao
# Market Class
import random

class Market:
    TCM1Names = ["金銀花(Honeysuckle)", "枸杞(Goji Berry)", "菊花(Chrysanthemum)", "砷(Arsenic)"]
    TCM2Names = ["竹蜂(Carpenter Bee)", "人參(Ginseng)", "燕窩(Swallow Nest)", "水銀(Mercury)"]
    TCM3Names = ["牛黃(Cattle Gallstone)", "鹿茸(Velvet Deer Antler)", "龜板(Turtle Shell)", "虎骨(Tiger Bone)", "犀角(Rhinoceros Horn)"]

    WestLowNames  = ["Ibuprofen", "Paracetamol", "Amoxicillin"]
    WestHighNames = ["Valacyclovir", "Rifampin", "Morphine"]
    WestUltraNames = ["Fentanyl", "Tigecycline"]

    TCM1Cost  = (10, 20)
    TCM2Cost  = (50, 150)  
    TCM3Cost  = (500, 10000)
    
    # Western medicine prices are not decided yet.
    WestLowCost   = (1, 3)
    WestHighCost  = (1, 3)
    WestUltraCost = (1, 3)

    def __init__(self):
        self.options = {}
        self.stock()

    def _pick(self, names, cost_range):
        name = random.choice(names)
        cost = random.randint(*cost_range)
        return (name, cost)

    def stock(self):
        self.inventory = {
            "TCM1":       self._pick(self.TCM1Names,       self.TCM1Cost),
            "TCM2":       self._pick(self.TCM2Names,       self.TCM2Cost),
            "TCM3":       self._pick(self.TCM3Names,       self.TCM3Cost),
            "WestLow":   self._pick(self.WestLowNames,   self.WestLowCost),
            "WestHigh":  self._pick(self.WestHighNames,  self.WestHighCost),
            "WestUltra": self._pick(self.WestUltraNames, self.WestUltraCost),
        }






