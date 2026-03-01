import pygame
from Button import Button
from Disease import Disease

#Initialize pygame
pygame.init()

#SETUP

running = True

#Setup screen window
screen = pygame.display.set_mode((920,520))

#Choose fonts
font1 = pygame.font.SysFont('freesanbold.ttf', 50)

buttonData = [ #Stores dictionary for each button's data
    {"label":"Play", "x":410, "y":210, "w":100, "h":100, "c1":(66,173,245), "c2":(56,150,214), "c3":(43,119,171)}
]
    
buttons = []
    
for data in buttonData:
    buttons.append(Button(**data)) #**data unpacks all the terms in the dictionary, puts them in the argument of Button


#DRAW
def display(screen, font):
    screen.fill((83, 136, 148))
    for i in buttons:
        i.display(screen, font)
    pygame.display.flip() #Updates the pygame screen based on what you've set in memory (the fill color)
        
#Perpetual while loop: Keeps the program running until the user quits, screen remains up
while running:
    display(screen, font1)
    for event in pygame.event.get(): #Checks for all user input events: For loop loops through all events that have occurred since the last frame
        if event.type == pygame.QUIT: #Checks to see if the user input was clicking the exit button
            running = False #Ends the program once exit is clicked