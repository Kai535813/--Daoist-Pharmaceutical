import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
font = pygame.font.SysFont(None, 100)


class Resource:
  def __init__(self, typE, level):
      self.typE = typE
      self.level = level
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


# Create some resources for demonstration
resources = [
    Resource("M", 2),  # Mine with level 2 -> 2 gray rectangles
    Resource("F", 3),  # Farm with level 3 -> 3 green rectangles
    Resource("A", 1),  # Animal with level 1 -> 1 brown rectangle
]

running = True
while running:
    screen.fill((0, 0, 0))  # Clear the screen

    # Draw resources
    y_offset = 50
    for resource in resources:
        resource.resourceDisplay(screen, 50, y_offset)
        # Calculate rows for this resource and add spacing
        rows = (resource.numBlocks - 1) // 10  # Number of rows (0-based)
        y_offset += (rows + 1) * 50 + 20  # Height per row + buffer

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    


pygame.quit()
