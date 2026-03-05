# Kai Yun Chao
# Market Class
import random
import pygame

class Market:
    # None of the rarity is actually decided yet.
    TCM1Names = ["金銀花(Honeysuckle)", "枸杞(Goji Berry)", "菊花(Chrysanthemum)", "砷(Arsenic)"]
    TCM1Rarity = [1, 2, 3, 4] 
    TCM2Names = ["竹蜂(Carpenter Bee)", "人參(Ginseng)", "燕窩(Swallow Nest)", "水銀(Mercury)"]
    TCM2Rarity = [1, 2, 3, 4]  
    TCM3Names = ["牛黃(Cattle Gallstone)", "鹿茸(Velvet Deer Antler)", "龜板(Turtle Shell)", "虎骨(Tiger Bone)", "犀角(Rhinoceros Horn)"]
    TCM3Rarity = [1, 2, 3, 4, 5] 

    WestLowNames  = ["Ibuprofen", "Paracetamol", "Amoxicillin"]
    WestLowRarity = [1, 2, 3]  
    WestHighNames = ["Valacyclovir", "Rifampin", "Morphine"]
    WestHighRarity = [1, 2, 3]  
    WestUltraNames = ["Fentanyl", "Tigecycline"]
    WestUltraRarity = [1, 2]  

    TCM1Cost  = (10, 20)
    TCM2Cost  = (50, 150)  
    TCM3Cost  = (500, 10000)
    
    # Western medicine prices are not decided yet.
    WestLowCost   = (1, 3)
    WestHighCost  = (1, 3)
    WestUltraCost = (1, 3)

    def __init__(self):
        self.options = {}
        self.stock()

    def _pick(self, names, cost_range, rarity=None):
        name = random.choices(names, weights=rarity, k=1)[0]
        cost = random.randint(*cost_range)
        return (name, cost)

    def stock(self):
        self.inventory = {
            "TCM1":       self._pick(self.TCM1Names, self.TCM1Cost, self.TCM1Rarity),
            "TCM2":       self._pick(self.TCM2Names, self.TCM2Cost, self.TCM2Rarity),
            "TCM3":       self._pick(self.TCM3Names, self.TCM3Cost, self.TCM3Rarity),
            "WestLow":   self._pick(self.WestLowNames, self.WestLowCost, self.WestLowRarity),
            "WestHigh":  self._pick(self.WestHighNames, self.WestHighCost, self.WestHighRarity),
            "WestUltra": self._pick(self.WestUltraNames, self.WestUltraCost, self.WestUltraRarity),
        }



    def display_market(self):
        pygame.init()
        screen_width = 800
        screen_height = 400
        pygame.display.set_caption("Market")
        screen = pygame.display.set_mode((screen_width, screen_height))
        market_image = pygame.image.load('Market.png').convert()
        # Scale the image to fit the screen height while maintaining aspect ratio
        img_width, img_height = market_image.get_size()
        scale_factor = screen_height / img_height
        new_width = int(img_width * scale_factor)
        
        font = pygame.font.SysFont(None, 28)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            color = 200
            screen.fill(color)
            
            # Blit the market image
            screen.blit(market_image, (0, 0))
            
            y = 300
            for category, (name, cost) in self.inventory.items():
                text = font.render(f"{name} - ${cost}", True, (255, 255, 255))
                screen.blit(text, (400, y))
            
                y += 80

            pygame.display.flip()
        pygame.quit()

# Outside the class:
m = Market()
m.display_market()




