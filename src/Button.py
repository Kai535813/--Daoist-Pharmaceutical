#Button Class: Mo Spiegel, Period 3B

class Button:
    def __init__(self, x, y, w, h, c1, c2, c3, label):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.label = label
        self.over = False #True if user is hovering over button
        
    def display(self):
        #Draws button to screen
        pass
    
    def hover(self):
        #Detects if user is hovering over button, updates over boolean
        pass