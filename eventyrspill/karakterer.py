#HOVEDPERSON = {"hp": 100, "xp":0, "slag": 3, "dodge": 2}
#FIENDE = {"hp": 90, "xp":0, "slag": 3, "dodge": 4}

class Karakter:
    """Generell klasse for karakter som alle skal arve fra"""
    #_hp = 100
    #_xp = 0
    #_slag = 0
    #_dodge = 0
    def __init__(self, navn, hp, xp, pos):
        self.navn = navn
        self.hp=hp
        self.xp=xp
        self.inventory = []
        self.pos = pos

    def print_meg(self):
        print(f"{self.navn} har hp: {self.hp} og xp: {self.xp}")
    
    def print_inventory(self):
        print(f"{self.navn} sitt inventory: ", end="")
        for item in self.inventory:
            print(item.mitt_navn(), end=" | ")
        print("")


navneliste=["Mutantleopard", "Mutantape", "Mutantpapegøye"]

