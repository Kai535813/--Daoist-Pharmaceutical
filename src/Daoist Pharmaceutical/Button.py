# Button Class: Mo Spiegel, Period 3B

import pygame

class Button:
    def __init__(self, label, x, y, w, h, c1, c2, c3, shadowColor, show):
        self.label = label
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.shadowColor = shadowColor
        self.show = show
        self.over = False  # True if user is hovering over button
        self.disT = 1
        self.color=(255,255,255)

    def display(self, screen, font, mouseClicked):
        if self.show == True:
            pygame.draw.rect(screen, self.shadowColor, [self.x-5, self.y-5, self.w, self.h], 0, 30)  # Drop shadow
            if self.over == True and mouseClicked == True:
                pygame.draw.rect(screen, self.c3, [self.x, self.y, self.w, self.h], 0, 30)
            elif self.over == False:
                pygame.draw.rect(screen, self.c1, [self.x, self.y, self.w, self.h], 0, 30)
            elif self.over == True and mouseClicked == False:
                pygame.draw.rect(screen, self.c2, [self.x, self.y, self.w, self.h], 0, 30)

            text = font.render(self.label, True, self.color)
            textRect = text.get_rect()  # Gives you a rectangle object the size of the screen
            textRect.center = (self.x + self.w/2, self.y + self.h/2)
            screen.blit(text, textRect)


    def hover(self):
        mouseX, mouseY = pygame.mouse.get_pos()
        if mouseX <= self.x + self.w and mouseX >= self.x and mouseY >= self.y and mouseY <= self.y + self.h:
            self.over = True
        else:
            self.over = False





