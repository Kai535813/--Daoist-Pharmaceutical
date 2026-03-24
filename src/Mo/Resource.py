

# Resource Class: Simon Sakata, Period 3B
import math
import random
import pygame
from Disease import Disease
from Market import Market
class Resource:
   # Class Attributes: Lists of all possible symptoms, progressing in severity

   def __init__(self, year):
       self.year = year  # Takes year count from main file
       self.nRescource = random.randint(10,14) 
       self.symptoms = []  
       self.area = [] 
       self.cured = False
       self.sevMod = 3
       self.delete=[]
       self.dictArea={}
       self.cureI=1
       self.color=(200,200,0)
       self.accept=False
       self.diseaseClicked = -1
       self.accept=False
       self.info='Type:'
       r = random.randint(0, 10)
       if r == 1:
        r = 2
       elif r < 8:
        r = 1
       else:
        r = 0
       med = (Market.TCM1Names, Market.TCM2Names, Market.TCM3Names,
              Market.TCM1Rarity, Market.TCM2Rarity, Market.TCM3Rarity)
       self.symptoms=(random.choices(med[r],weights=med[r+3],k=1)[0])
       self.meds=self.symptoms
       self.cost=random.randint(self.nRescource*5-self.nRescource*3,self.nRescource*5+self.nRescource*3)

   # Ethan Tang|3B
   def pick(self):
       r=random.randint(0,10)
       if r==1:
        r=2
       elif r<8:
        r=1
       else:
        r=0
       med=(Market.TCM1Names,Market.TCM2Names,Market.TCM3Names,Market.TCM1Rarity,Market.TCM2Rarity,Market.TCM3Rarity)
       return
   
   def spread(self, n):
       x = self.area[random.randint(0, len(self.area) - 1)][0]
       y = self.area[random.randint(0, len(self.area) - 1)][1]
       disease = []
       c = 0
       while len(disease) < math.ceil(n / 2):
           if random.choice([True, False]):
               try:
                   y = y + 11 * random.choice([1, -1])
                   if Disease.valid[x][y] not in self.area and Disease.valid[x][y] not in disease:
                       disease.append(Disease.valid[x][y])
               except:
                   c += 1
           else:
               try:
                   x = x + 11 * random.choice([1, -1])
                   if  Disease.valid[x][y] not in self.area and Disease.valid[x][y] not in disease:
                       disease.append(Disease.valid[x][y])
               except:
                   c += 1
           if c > 30:
               print("restart")
               return self.spread( n)
       if len(disease) != math.ceil(n / 2):
           return self.spread(Disease.valid)
       for i in disease:
           self.area.append(i)
           self.areaRep()
           del Disease.valid[i[0]][i[1]]
       return disease

   def areaRep(self):
       current=len(self.area)-1
       try:
           self.dictArea.setdefault(self.area[current][0],{}).setdefault(self.area[current][1],'a')
       except:
           pass

   def randGen(self):
       x = random.choice(list(Disease.valid.keys()))
       y = random.choice(list(Disease.valid[x].keys()))
       self.area.append(Disease.valid[x][y])
       self.areaRep()
       del Disease.valid[x][y]
       return self.spread(self.nRescource)

   def changeC(self):
       self.color = (230, 230, 100)


   def update(self):
       if self.accept:
            self.nRescource=self.nRescource-self.cureI
            if self.nRescource <= 0:
                self.cured = True
                self.delete=self.area
                self.dictArea={}
                return ((self.delete),0,self.cureI*random.uniform(0.1,0.5))
            self.delete = []
            for i in range(self.cureI):
                    if len(self.area)-1-i<0:
                        return ((self.delete), 0, 0)
                    else:
                        self.delete.append(self.area[len(self.area) - 1 - i])
                        Disease.valid.setdefault(self.area[len(self.area) - 1 - i][0],{}).setdefault(self.area[len(self.area) - 1 - i][1],self.area[len(self.area) - 1 - i])
                        del self.area[len(self.area) - 1 - i]
                        self.areaRep()
                    return ((self.delete), 0, 0)
       return ((),0,0)
