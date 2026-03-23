import pygame
import random
import math

class Resource:
  def __init__(self, typE, level):
      self.typE = typE
      self.level = level
      self.sevIndex = random.randint(6,10)  # Add severity index like Disease
      self.area = []  # Add area list like Disease
      self.levelOfResource()



  def typeOfResource(self):
      if self.typE == "M":
          return "Mine"
      elif self.typE == "F":
          return "Farm"
      elif self.typE == "A":
          return "Animal"
     
  
  def levelOfResource(self):
      if self.level == 1:
          self.numBlocks = 10
          return "resource level one"
      elif self.level == 2:
          self.numBlocks = 15
          return "resource level two"
      elif self.level == 3:
          self.numBlocks = 20
          return "resource level three"
  def resourceDisplay(self, surface, x, y):
      if self.typE == "M":
        color = (120, 120, 120)
      elif self.typE == "F":
        color = (0, 200, 0)
      elif self.typE == "A":
        color = (200, 150, 0)
      else:
        color = (255, 255, 255)
      
      cols = 10
      for i in range(self.numBlocks):
          rect_x = x + (i % cols) * 50
          rect_y = y + (i // cols) * 50
          pygame.draw.rect(surface, color, (rect_x, rect_y, 40, 40))

  def spread(self,valid,n):
       x = self.area[len(self.area)-1][0]
       y = self.area[len(self.area)-1][1]
       resource=[]
       c=0
       while len(resource) < math.ceil(n/2):
            if random.choice([True,False]):
                try:
                    y = y + 11 * random.choice([1,-1])
                    if valid[x][y]not in resource:
                        resource.append(valid[x][y])
                except:
                    c += 1
            else:
                try:
                    x = x+11*random.choice([1,-1])
                    if valid[x][y] not in resource:
                        resource.append(valid[x][y])
                except:
                    c += 1
            if c > 11:
                print("restart")
                return(self.randGen(valid))
       if len(resource)!= math.ceil(n/2):
                return(self.randGen(valid))
       return resource
  def randGen(self,valid):
       x=random.choice(list(valid.keys()))
       y=random.choice(list(valid[x].keys()))
       self.area.append(valid[x][y])
       return self.spread(valid,self.sevIndex)
       

   
  def update(self,valid):
       append=(self.spread(valid,int(self.sevIndex)+4-int(self.cure())))
       for i in range(len(append)):
           self.area.append(append[i])
       if self.sevIndex==0:
           return True
       else: 
           return self.area

