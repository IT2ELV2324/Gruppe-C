import random

class Vaapen:
    """
    En generell klasse som alle våpen skal arve fra
    """
    def __init__(self):
        pass
    
    def angrip(self, angriper, motstander):
        if abs(motstander.pos - angriper.pos) < self.range:
            motstander.hp = motstander.hp - random.randint(self.min_skade, self.maks_skade)
        

class Kniv(Vaapen):
    def __init__(self):
        super().__init__()
        self.range = 2
        self.min_skade = 20
        self.maks_skade = 30

