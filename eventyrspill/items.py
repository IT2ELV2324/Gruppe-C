import random

konsoll_UT = True

def konsoll(tekst: str, end:str="\n"):
    if konsoll_UT:
        print(tekst, end=end)

class Vaapen:
    """
    En generell klasse som alle våpen skal arve fra
    """
    def __init__(self):
        pass

    def innenfor_rekkevidde(self, angriper, motstander):
        # Sjekker om motstanderen er innenfor rekkevidden til våpenet
        if abs(motstander.pos - angriper.pos) <= self.range:
            return True
        else:
            return False

    #En metode for angrepssytemet
    def angrip(self, angriper, motstander):
        skade = 0
        if self.innenfor_rekkevidde(angriper, motstander):
            # Skaden gjort er gitt ved en verdi mellom den minste og den største skaden mulig 
            skade = random.randint(self.min_skade, self.maks_skade)

            if self.dytt > 0:
                #Hvis angriperen er til venstre for motstanderen skal den dytte den mot høyre
                #Hvis angriperen er til høyre for motstanderen skal den dytte den mot venstre
                if angriper.pos < motstander.pos:
                    motstander.pos += self.dytt
                else:
                    motstander.pos -= self.dytt
                konsoll(f"{angriper.navn} dyttet {motstander.navn} med {self.dytt} steg")
        else:
            konsoll(f"{angriper.navn} klarte ikke å nå {motstander.navn}")
        if skade > 0:
            motstander.hp = motstander.hp - skade
            konsoll(f"{angriper.navn} gjorde {skade} skade mot {motstander.navn} med {self.navn}")

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
        self.dytt = 0
        self.navn = "Dolk"

class Smørkniv(Vaapen):
    def __init__(self):
        super().__init__()
        self.range = 2
        self.min_skade = 10
        self.maks_skade = 20
        self.dytt = 0
        self.navn = "Smørkniv"

class Paraply(Vaapen):
    def __init__(self):
        super().__init__()
        self.range = 3
        self.min_skade = 0
        self.maks_skade = 0
        self.dytt = 5
        self.navn = "Paraply"

        

#slett denne senere
class Juks(Vaapen):
    def __init__(self):
        self.range = 999
        self.min_skade = 100
        self.maks_skade = 999
        self.dytt = 0
        self.navn = "Juks"

class Pil_og_bue(Vaapen):
    def __init__(self, piler: int):
        super().__init__()
        self.range = 15
        self.min_skade = 10
        self.maks_skade = 15
        self.dytt = 0
        self.piler = piler
        self.navn = "Pil og bue"

    def angrip(self, angriper, motstander):
        #Overskriver den originale Vaapen.angrip-funksjonen
        
        #Sjekker om man har nok piler for å begrense mulighetene for spam
        if self.piler > 0:
            self.piler -= 1
            super().angrip(angriper, motstander)
            konsoll(f"{angriper.navn} har {self.piler} piler igjen")
        else:
            konsoll(f"{angriper.navn} er tom for piler!")

class Heal(Vaapen):
    def __init__(self, hp: int):
        super().__init__()
        self.healPotion = hp
        self.navn = "Healpotion"
        self.range = 10

    def angrip(self, angriper, motstander):
        healed = random.choice([motstander, angriper])
        healed.hp += self.healPotion
        if healed.hp > 100:
            healed.hp = 100

class Sleep(Vaapen):
    def __init__(self):
        super().__init__()
        self.navn = "Sleep"
        self.range = 1000

    def angrip(self,angriper,motstander):
        sleeping = random.choice([motstander, angriper])
        sleeping.sleep = True
        print(f"{sleeping.navn} ble truffet av en sleeping potion og sovna")


