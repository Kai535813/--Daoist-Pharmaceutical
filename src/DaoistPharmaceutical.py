import pygame # type: ignore
# Mo Spiegel 
from Button import Button
from Disease import Disease
def display(screen, font):
    for i in buttons:
        i.display(screen, font)
    pygame.display.flip() #Updates the pygame screen based on what you've set in memory (the fill color)

#2/27/26|Ethan Tang 
pygame.init()
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

for data in buttonData:
    buttons.append(Button(**data)) #**data unpacks all the terms in the dictionary, puts them in the argument of Button

running=True
while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    screen.blit(backI,(0,0))
    display(screen, font1)
    pygame.display.flip()

    clock.tick(10)

pygame.quit()

