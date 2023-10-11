"""Hovedfilen"""
import items
import karakterer
import random
import os
import textwrap

heltenavn = ""

while len(heltenavn) < 2:
    heltenavn = str(input("Hva vil du hete? ")).capitalize()

def load_dialog():
    dialog_file = open(os.path.dirname(__file__) + "/dialog.txt", encoding="utf-8")

    all_dialog = ['HER LIGGER ALL DIALOG']
    for line in dialog_file:
        if "helte_navn" in line:
            line = line.replace("helte_navn", heltenavn)
        #TEXTWRAPPER
        all_dialog.append(line.strip("\n")) #TA BORT .STRIP NÅR TEXTWRAPPER FUNGERER
    
    return all_dialog


dialog = load_dialog()
print(dialog[1])


#hent dialog ved å bruke dialog[i], der i er linjen i dialog.txt hvor teksten ligger.



def fight():
    while hovedperson.hp > 0 and fiende.hp > 0:
        if fiende.pos > hovedperson.pos:
            fiende.pos -= 1
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
                if item.navn == vaapen_valg:
                    vaapen = item
                    funnet_vaapen = True
                    break

        vaapen.angrip(angriper=hovedperson, motstander=fiende)


        ### Fienden angriper
        vaapen = random.choice(fiende.inventory)
        vaapen.angrip(angriper=fiende, motstander=hovedperson)
    print(f"\n Hovedperson har {hovedperson.hp} hp igjen. Fienden har {fiende.hp} igjen. \n")

### Første fight (garantert seier)
hovedperson = karakterer.Karakter(heltenavn, hp=100, pos=0)
hovedperson.inventory = [items.Dolk(), items.Pil_og_bue(piler=10)]

fiende = karakterer.Fiende(fiende.inventory = [items.Smørkniv()]

fight()

### Andre fight
print("Du fikk en paraply!")
hovedperson.inventory.append(items.Paraply())
fiende = karakterer.Fiende(hp=100, pos=1)
fiende.inventory = [items.Dolk()]
fight()

### Tredje fight
# hovedperson.inventory.append(items.)
fiende = karakterer.Fiende(hp=100, pos=5)


if hovedperson.hp <= 0 and fiende.hp <=0:
    print("Både du og fienden døde! Det er uavgjort")
elif hovedperson.hp > 0 and fiende.hp <= 0:
    print("Du vant!")
else:
    print("Du tapte :( ")
    