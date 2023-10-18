import random


class Karakter:
    """Generell klasse for karakter som alle skal arve fra"""
    def __init__(self, navn, hp, pos):
        self.navn = navn
        self.hp=hp
        self.inventory = []
        self.pos = pos
        self.sleep = False

    # Funksjonene nedenfor printer informasjon til konsollen
    def print_meg(self):
        print(f"{self.navn} har hp: {self.hp}")
    
    def print_inventory(self):
        print(f"{self.navn} sitt inventory: ", end="")
        for item in self.inventory:
            print(item.mitt_navn(), end=" | ")
        print("")

class Fiende(Karakter):
    def __init__(self, hp, pos):
        super().__init__(random.choice(navneliste), hp, pos)

# Liste for monsternavn
navneliste=["Mutantelg", "Mutantgrevling", "Mutantrådyr", "Mutantrev"]

