import pygame 
from Button import Button
from Disease import Disease
pygame.init()

# Mo Spiegel

def display(screen, font):
    for i in buttons:
        i.hover()
        i.display(screen, font)
    pygame.display.flip() #Updates the pygame screen based on what you've set in memory (the fill color)

#2/27/26|Ethan Tang 
screen = pygame.display.set_mode((1840-184, 1040-104))
clock = pygame.time.Clock()
font1 = pygame.font.SysFont('freesanbold.ttf', 50)
backI = pygame.transform.smoothscale(pygame.image.load('DaoistPharacueticalBackground1.png').convert(),(1840-184,1040-104)) 

buttonData = [ #Stores dictionary for each button's data
    {"label":"Play", "x":410, "y":210, "w":100, "h":100, "c1":(66,173,245), "c2":(56,150,214), "c3":(43,119,171)}
]
    
buttons = []


for data in buttonData:
   buttons.append(Button(**data)) #**data unpacks all the terms in the dictionary, puts them in the argument of Button


running=True
while running:
   screen.blit(backI,(0,0))
   # poll for events
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running=False
       if event.type == pygame.MOUSEBUTTONDOWN:
           mouseClicked = True
           display(screen, font1, mouseClicked)
       if event.type == pygame.MOUSEBUTTONUP:
           mouseClicked = False
   display(screen, font1, mouseClicked)
   pygame.display.flip()
   clock.tick(10)
pygame.quit()



