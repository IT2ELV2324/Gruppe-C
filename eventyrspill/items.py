import random

class Vaapen:
    """
    En generell klasse som alle våpen skal arve fra
    """
    def __init__(self):
        pass

    #En metode for angrepssytemet
    def angrip(self, angriper, motstander):
        skade = 0
        # Sjekker om motstanderen er innenfor rekkevidden til våpenet
        if abs(motstander.pos - angriper.pos) <= self.range:
            # Skaden gjort er gitt ved en verdi mellom den minste og den største skaden mulig 
            skade = random.randint(self.min_skade, self.maks_skade)
        motstander.hp = motstander.hp - skade
        print(f"{angriper.navn} gjorde {skade} skade mot {motstander.navn} med {self.navn}")

    # def dytte(self, angriper, motstander):
    #     motstander.pos = motstander.pos -4
    #     print(f"Du dyttet {angriper.navn} vekk med 4 steg")

    def mitt_navn(self) -> str:
        return f"{self.navn} (range: {self.range})"

# Våpnene er fordelt i ulike klasser, og de arver den generelle angrepsmetoden
# Det er definert egne verdier for skade, rekkevidde o.l. i hver klasse
# Vi har valgt å gjøre det slik for at det skal enklere med våpenspesifikke metoder 
class Dolk(Vaapen):
    def __init__(self):
        super().__init__()
        self.range = 2
        self.min_skade = 20
        self.maks_skade = 30
        self.navn = "Kniv"

class Smørkniv(Vaapen):
    def __init__(self):
        super().__init__()
        self.range = 2
        self.min_skade = 10
        self.maks_skade = 20
        self.navn = "Smørkniv"

class Paraply(Vaapen):
    def __init__(self):
        super().__init__()
        self.range = 4
        self.min_skade = 0
        self.maks_skade = 0
        self.navn = "Paraply"

#slett denne senere
class Juks(Vaapen):
    def __init__(self):
        self.range = 999
        self.min_skade = 100
        self.maks_skade = 999
        self.navn = "Juks"

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

# class healPotion(self):
#     self.hp = hp

#     def __init__(self):
#         pass

#         def bruk(mål):
#             mål.hp += 50
