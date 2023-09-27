import random

class Vaapen:
    """
    En generell klasse som alle våpen skal arve fra
    """
    def __init__(self):
        pass

    #En metode for angrepssytemet
    def angrip(self, angriper, motstander):

        # Skaden gjort er gitt ved en verdi mellom den minste og den største skaden mulig 
        skade = random.randint(self.min_skade, self.maks_skade)
        
        # Sjekker om motstanderen er innenfor rekkevidden til våpenet
        if abs(motstander.pos - angriper.pos) < self.range:
            motstander.hp = motstander.hp - skade
        print(f"{angriper.navn} gjorde {skade} skade mot {motstander.navn} med {self.navn}")


# Våpnene er fordelt i ulike klasser, og de arver den generelle angrepsmetoden
# Det er definert egne verdier for skade, rekkevidde o.l. i hver klasse
# Vi har valgt å gjøre det slik for at det skal enklere med våpenspesifikke metoder 
class Kniv(Vaapen):
    def __init__(self):
        super().__init__()
        self.range = 2
        self.min_skade = 20
        self.maks_skade = 30
        self.navn = "Kniv"

class Pil_og_bue(Vaapen):
    def __init__(self, piler):
        super().__init__()
        self.range = 15
        self.min_skade = 10
        self.maks_skade = 15
        self.piler = piler
        self.navn = "Pil og bue"
    
    def angrip(self, angriper, motstander):
        if self.piler > 0:
            self.piler -= 1
            super().angrip(angriper, motstander)
            print(f"{angriper.navn} har {self.piler} piler igjen")
        else:
            print(f"{angriper.navn} er tom for piler!")