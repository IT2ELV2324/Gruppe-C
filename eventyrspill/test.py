"Funksjon for å sjekke sannsynlighet for seier. Dette skjer ved å kjøre programmet 1000 ganger og ser på seiersraten"

import random
from spill import *
items.konsoll_UT = False

def test(ganger):

    hovedperson_seier = 0
    fiende_seier = 0
    forhold = 0
    hovedperson.inventory = [items.Dolk()]
    fiende.inventory = [items.Dolk()]
    
    for i in range(ganger):
        hovedperson.hp = 100 
        fiende.hp = 100
        
        while hovedperson.hp > 0 and fiende.hp > 0:
            if fiende.pos > hovedperson.pos:
                fiende.pos -= 1
            ### Hovedpersonen angriper

            vaapen = random.choice(hovedperson.inventory)
            vaapen.angrip(angriper=hovedperson, motstander=fiende)

            ### Fienden angriper
            if fiende.hp > 0: 
                vaapen = random.choice(fiende.inventory)
                vaapen.angrip(angriper=fiende, motstander=hovedperson)

        if hovedperson.hp > 0:
            hovedperson_seier += 1
        else:
            fiende_seier += 1
    
    
    forhold = hovedperson_seier / fiende_seier 
    print(f"forholdet mellom seier og tap er: {forhold}")

test(1000)

