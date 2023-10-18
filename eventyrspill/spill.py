"""Hovedfilen"""
import items
import karakterer
import random
import os
import textwrap

heltenavn = ""

if __name__ == "__main__":    
    while len(heltenavn) < 2:
        heltenavn = str(input("Hva vil du hete? ")).capitalize()

def load_dialog():
    dialog_file = open(os.path.dirname(__file__) + "/dialog.txt", encoding="utf-8")

    all_dialog = ['HER LIGGER ALL DIALOG']
    for line in dialog_file:
        if "helte_navn" in line:
            line = line.replace("helte_navn", heltenavn)
        
        wrapper = textwrap.TextWrapper(width=100)  
        wrapped_line = wrapper.fill(text=line)
        
        all_dialog.append(wrapped_line)
    
    return all_dialog




#hent dialog ved å bruke dialog[i], der i er linjen i dialog.txt hvor teksten ligger.

def trykk_enter():
    input("... Trykk enter for å fortsette ...\n")


def fight():
    våkneFiende = 50
    våkneHelt = 50

    while hovedperson.hp > 0 and fiende.hp > 0:
        if fiende.pos > hovedperson.pos:
            fiende.pos -= 1
        elif fiende.pos < hovedperson.pos:
            fiende.pos += 1
        print("")
        hovedperson.print_meg()
        fiende.print_meg()
        print(f"Avstand: {abs(fiende.pos - hovedperson.pos)}")

        
        ### Hovedpersonen angriper
        hovedperson.print_inventory()

        funnet_vaapen = False
        while not funnet_vaapen:
            vaapen_valg = input("Ditt valg: ").capitalize().strip()
            for item in hovedperson.inventory:
                if item.navn[:len(vaapen_valg)] == vaapen_valg:
                    vaapen = item
                    funnet_vaapen = True
                    break

        if not hovedperson.sleep:
            vaapen.angrip(angriper=hovedperson, motstander=fiende)
        
        else:
            
            if random.randint(1,100) < våkneHelt:
                hovedperson.sleep = False
                våkneHelt = 50
                print(heltenavn, "våkna!")
            else:
                print("Zzz..")
                våkneHelt += 10


        ### Fienden angriper
        if not fiende.sleep:
            if fiende.hp > 0: #Siden hovedperson angriper først uansett, tenkte jeg at det var greit å sjekke om fienden lever før den angriper
                vaapen = random.choice(fiende.inventory)
                vaapen.angrip(angriper=fiende, motstander=hovedperson)

        else:
            
            if random.randint(1,100) < våkneFiende:
                fiende.sleep = False
                våkneFiende = 50
                print(fiende, "våkna!")
            else:
                print(f"{fiende.navn} kan ikke angripe. Den sover!")
                våkneFiende += 10
     
        trykk_enter()
    #print(f"\n Hovedperson har {hovedperson.hp} hp igjen. Fienden har {fiende.hp} igjen. \n")
    if hovedperson.hp > 0:
        print(f"{fiende.navn} døde")
    else:
        print("Du døde")


### Klargjør til første fight
hovedperson = karakterer.Karakter(heltenavn, hp=100, pos=0)
hovedperson.inventory = [items.Dolk(), items.Pil_og_bue(piler=10), items.Heal(hp=50), items.Sleep()]

fiende = karakterer.Fiende(hp=100,pos=5)
fiende.inventory = [items.Smørkniv()]

if __name__ == "__main__":
    juksemodus = input("Oensker du et juksevaapen? (ja/nei): ").capitalize().strip()

    dialog = load_dialog()
    print(dialog[1])
    print(dialog[2])

    ### Første fight (garantert seier)
    print(dialog[3])
    
    if juksemodus == "Ja":
        hovedperson.inventory.append(items.Juks())
    
    fight()


    ### Andre fight
    print(dialog[4])
    print("Du fikk en paraply!")
    trykk_enter()
    print(dialog[5])
    trykk_enter()
    #hovedperson.hp = 100 #endret det slik at hovedperson starter med 100hp
    hovedperson.inventory.append(items.Paraply())
    fiende = karakterer.Fiende(hp=100, pos=1)
    fiende.inventory = [items.Dolk()]
    fight()

    ### Tredje fight
    # hovedperson.inventory.append(items.)
    print(dialog[6])
    fiende = karakterer.Fiende(hp=100, pos=5)
    fiende.inventory = [items.Pil_og_bue(piler=4), items.Smørkniv()]
    fight()

    if hovedperson.hp > 0:
        print(dialog[7])
    else:
        print(dialog[8])

