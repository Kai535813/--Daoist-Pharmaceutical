
class Resource:
   def __init__(self, typE, level):
       self.typE = typE
       self.level = level


   def typeOfResource(self):
       if self.typE == "M":
           return "Mine"
       elif self.typE == "F":
           return "Farm"
       elif self.typE == "A":
           return "Animal"
    
   def levelOfResource(self):
       if self.level == 1:
           return "resource level one"
       elif self.level == 2:
           return "resource level two"
       elif self.level == 3:
           return "resource level three"