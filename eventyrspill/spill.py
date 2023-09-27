"""Hovedfilen"""
import items
import karakterer
import random
import os

heltenavn = ""

while len(heltenavn) < 2:
    heltenavn = str(input("Hva vil du hete? ")).capitalize()

def load_dialog():
    dialog_file = open(os.path.dirname(__file__) + "/dialog.txt", encoding="utf-8")

    all_dialog = ['HER LIGGER ALL DIALOG']
    for line in dialog_file:
        if "helte_navn" in line:
            line = line.replace("helte_navn", heltenavn)
        all_dialog.append(line.strip("\n"))
    
    return all_dialog

dialog = load_dialog()
print(dialog[1])
print(dialog[2], dialog[3], dialog[4], dialog[5])
#hent dialog ved å bruke dialog[i], der i er linjen i dialog.txt hvor teksten ligger.


### Første fight
hovedperson = karakterer.Karakter(heltenavn, hp=100, xp=0, pos=0)
hovedperson.inventory = [items.Dolk(), items.Pil_og_bue(piler=10)]

fiende = karakterer.Karakter("Fiende", hp=100, xp=0, pos=5)
fiende.inventory.append(items.Smørkniv())

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


if hovedperson.hp <= 0 and fiende.hp <=0:
    print("Både du og fienden døde! Det er uavgjort")
elif hovedperson.hp > 0 and fiende.hp <= 0:
    print("Du vant!")
else:
    print("Du tapte :( ")
    