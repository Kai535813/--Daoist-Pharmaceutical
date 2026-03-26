#Ethan Tang|3B
# This file isn't actually run during the game, this is just what I used to locate every pixel drawn on the scree
Import pygame
with open("pixels.txt","a+") as pixel:
   pixels=pygame.PixelArray(backI)
   for x in range(0,1472,11):
       pixel.write(f"{x}: {{")
       for y in range(0,832,11):
           r,g,b,a = backI.unmap_rgb(pixels[x][y])
           if g > 50 and g > r + 20 and g > b + 15:
               pixel.write(f"{y}: {x,y,r,g,b}, ")
       pixel.write("},")
del pixels
