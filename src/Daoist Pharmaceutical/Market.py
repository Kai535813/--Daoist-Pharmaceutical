
# Kai Yun Chao
# Market Class
import random
import pygame
import os


class Market:
    # None of the rarity is actually decided yet.
    TCM1Names = ["金銀花(Honeysuckle)", "枸杞(Goji Berry)",
                 "菊花(Chrysanthemum)", "砷(Arsenic)"]
    TCM1Rarity = [1, 1, 5, 10]
    TCM2Names = ["竹蜂(Carpenter Bee)", "人參(Ginseng)",
                 "燕窩(Swallow Nest)", "水銀(Mercury)"]
    TCM2Rarity = [3, 1, 2, 5]
    TCM3Names = ["牛黃(Cattle Gallstone)", "鹿茸(Velvet Deer Antler)",
                 "龜板(Turtle Shell)", "虎骨(Tiger Bone)", "犀角(Rhinoceros Horn)"]
    TCM3Rarity = [6, 3, 2, 1, 1]

    WestLowNames = ["Ibuprofen", "Paracetamol", "Amoxicillin"]
    WestLowRarity = [1, 1, 1]
    WestHighNames = ["Valacyclovir", "Rifampin", "Morphine"]
    WestHighRarity = [1, 1, 1]
    WestUltraNames = ["Fentanyl", "Tigecycline"]
    WestUltraRarity = [1, 1]

    TCM1Cost = (10, 20)
    TCM2Cost = (50, 150)
    TCM3Cost = (500, 10000)

    # Western medicine prices are not decided yet.
    WestLowCost = (1, 3)
    WestHighCost = (1, 3)
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

    def display_market(self, screen):

        try:
            background = pygame.image.load("Market.png")
            background = pygame.transform.scale(background, (960, 420))
            background = background.convert()
        except pygame.error as e:
            print("ERROR loading image:", e)
            background = None

        if background:
            screen.blit(background, (0, 0))
        else:
            screen.fill((118, 78, 71))

        positions = [(20, 20), (330, 20), (660, 20),
                     (20, 200), (330, 200), (660, 200)]


        pygame.display.flip()
