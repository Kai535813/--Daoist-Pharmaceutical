# Disease Class: Mo Spiegel, Period 3B
import math
import random
import pygame


class Disease:
   # Class Attributes: Lists of all possible symptoms, progressing in severity
   symptomsTier1 = [
       "上火(Shànghuǒ)",
       "气虚(Qì Xū)",
       "肝气郁结(Gān Qì Yù Jié)",
       "风寒(Fēng Hán)",
   ]
   symptomsTier2 = ["痰湿(Tán Shī)", "湿热(Shī Rè)", "风热(Fēng Rè)"]
   symptomsTier3 = ["阳虚(Yáng Xū)", "阴虚(Yīn Xū)", "血瘀(Xuè Yū)"]




   def __init__(self, year):
       self.year = year  # Takes year count from main file
       self.sevIndex = 0  # Modified by 'getSeverityIndex' method
       self.symptoms = []  # Modified by 'getSymptoms' method
       self.area = []  # List of coordinates where the disease exists
       self.cured = False
       self.medicineI = {
           "Ars": {
               "上火(Shànghuǒ)": 0.5,
               "气虚(Qì Xū)": 0.5,
               "肝气郁结(Gān Qì Yù Jié)": 0.5,
               "风寒(Fēng Hán)": 0.5,
           }
       }
       self.sevMod = 3
       self.meds = ["Ars", random.randint(6,12)]
       self.cureI = 0
       self.delete=[]




   # Ethan Tang|3B
   def getSymptoms(self):
       if self.year <= 80:
           x = random.randint(
               1, 2
           )  # Denotes how many symptoms will be present in an instance of a disease (bounds increase with time)
           while x > 0:
               symp = Disease.symptomsTier1[
                   random.randint(0, len(Disease.symptomsTier1) - 1)
               ]
               if symp not in self.symptoms:
                   self.symptoms.append(symp)
                   x -= 1




       elif self.year <= 200:
           x = random.randint(1, 3)
           while x > 0:
               symp = Disease.symptomsTier1[
                   random.randint(0, len(Disease.symptomsTier1) - 1)
               ]
               if symp not in self.symptoms:
                   self.symptoms.append(symp)
                   x -= 1
               symp = Disease.symptomsTier2[
                   random.randint(0, len(Disease.symptomsTier2) - 1)
               ]
               if symp not in self.symptoms:
                   self.symptoms.append(symp)
                   x -= 1
       elif self.year <= 500:
           x = random.randint(1, 3)
           while x > 0:
               symp = Disease.symptomsTier1[
                   random.randint(0, len(Disease.symptomsTier1) - 1)
               ]
               if symp not in self.symptoms:
                   self.symptoms.append(symp)
                   x -= 1
               symp = Disease.symptomsTier2[
                   random.randint(0, len(Disease.symptomsTier2) - 1)
               ]
               if symp not in self.symptoms:
                   self.symptoms.append(symp)
                   x -= 1
               symp = Disease.symptomsTier3[
                   random.randint(0, len(Disease.symptomsTier3) - 1)
               ]
               if symp not in self.symptoms:
                   self.symptoms.append(symp)
                   x -= 1




   # Mo Spiegel, Period 3B
   def getSeverityIndex(self):
       for i in self.symptoms:
           # Assigns each symptom of the disease a severity index based on its tier
           # The sum of each symptoms' severity index is the disease severity
           if i == "上火(Shànghuǒ)":
               self.symptoms.append(random.randint(7, 15))
               self.sevIndex = self.sevIndex + self.symptoms[len(self.symptoms) - 1]

           elif i == "气虚(Qì Xū)":
               self.symptoms.append(random.randint(7, 15))
               self.sevIndex = self.sevIndex + self.symptoms[len(self.symptoms) - 1]

           elif i == "肝气郁结(Gān Qì Yù Jié)":
               self.symptoms.append(random.randint(7, 15))
               self.sevIndex = self.sevIndex + self.symptoms[len(self.symptoms) - 1]

           elif i == "风寒(Fēng Hán)":
               self.symptoms.append(random.randint(7, 15))
               self.sevIndex = self.sevIndex + self.symptoms[len(self.symptoms) - 1]

           elif i == "痰湿(Tán Shī)":
               self.symptoms.append(random.randint(5, 8))
               self.sevIndex = self.sevIndex + self.symptoms[len(self.symptoms) - 1]

           elif i == "湿热(Shī Rè)":
               self.symptoms.append(random.randint(5, 8))
               self.sevIndex = self.sevIndex + self.symptoms[len(self.symptoms) - 1]

           elif i == "风热(Fēng Rè)":
               self.symptoms.append(random.randint(5, 8))
               self.sevIndex = self.sevIndex + self.symptoms[len(self.symptoms) - 1]

           elif i == "阳虚(Yáng Xū)":
               self.symptoms.append(random.randint(5, 11))
               self.sevIndex = self.sevIndex + self.symptoms[len(self.symptoms) - 1]

           elif i == "阴虚(Yīn Xū)":
               self.symptoms.append(random.randint(5, 11))
               self.sevIndex = self.sevIndex + self.symptoms[len(self.symptoms) - 1]

           elif i == "血瘀(Xuè Yū)":
               self.symptoms.append(random.randint(5, 11))
               self.sevIndex = self.sevIndex + self.symptoms[len(self.symptoms) - 1]




   # Ethan Tang|3B
   def spread(self, valid, n):
       x = self.area[random.randint(0, len(self.area) - 1)][0]
       y = self.area[random.randint(0, len(self.area) - 1)][1]
       disease = []
       c = 0
       while len(disease) < math.ceil(n / 2):
           if random.choice([True, False]):
               try:
                   y = y + 11 * random.choice([1, -1])
                   if valid[x][y] not in self.area:
                       disease.append(valid[x][y])
               except:
                   c += 1
           else:
               try:
                   x = x + 11 * random.choice([1, -1])
                   if valid[x][y] not in self.area:
                       disease.append(valid[x][y])
               except:
                   c += 1
           if c > 30:
               print("restart")
               return self.spread(valid, n)
       if len(disease) != math.ceil(n / 2):
           return self.spread(valid)
       for i in disease:
           self.area.append(i)
       return disease




   def cure(self):
       # The presence of a pharmacy will call the cure method and pass in the list of medicines the pharmacy has, which will decrease the severity of symptoms
       for i in range(0, int(len(self.symptoms) / 2)):
           for i2 in range(0, int(len(self.meds) / 2)):
               self.cureI = int(self.cureI+ (float (self.medicineI[self.meds[i2]] [self.symptoms[i]])* float(self.meds[i2 + len(self.meds) // 2])))


   def randGen(self, valid):
       self.getSymptoms()
       self.getSeverityIndex()
       print(self.symptoms)
       print(self.sevIndex)
       x = random.choice(list(valid.keys()))
       y = random.choice(list(valid[x].keys()))
       self.area.append(valid[x][y])
       return self.spread(valid, self.sevIndex)




   def update(self, valid):
       self.cure()
       if self.sevIndex-self.cureI <= 0:
           self.cured = True
       if self.sevMod - self.cureI < 0:
           self.delete = []
           print()
           for i in range(abs(self.sevMod - self.cureI)):
               if len(self.area)-1- i<0:
                   print(self.delete)
                   return self.delete
               else:
                   self.delete.append(self.area[len(self.area) - 1 - i])
                   del self.area[len(self.area) - 1 - i]
           self.cureI = 0
           print(self.delete)
           return self.delete
       append = self.spread(valid, self.sevMod - self.cureI)
       for i in range(len(append)):
           self.area.append(append[i])
       self.cureI = 0
       return self.area
