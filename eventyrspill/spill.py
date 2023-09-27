"""Hovedfilen"""
import items
import karakterer
import random

heltenavn = str(input("Hva vil du hete? ")).capitalize()

def load_dialog():
    dialog_file = open("./eventyrspill/dialog.txt", encoding="utf-8")

    all_dialog = ['HER LIGGER ALL DIALOG']
    for line in dialog_file:
        if "helte_navn" in line:
            line = line.replace("helte_navn", heltenavn)
        all_dialog.append(line.strip("\n"))
    
    return all_dialog

dialog = load_dialog()
print(dialog[1])
#hent dialog ved å bruke dialog[i], der i er linjen i dialog.txt hvor teksten ligger.

hovedperson = karakterer.Karakter(heltenavn, hp=100, xp=0, pos=0)
hovedperson.inventory = [items.Kniv(), items.Pil_og_bue(piler=15)]

fiende = karakterer.Karakter("Fiende", hp=100, xp=0, pos=2)
fiende.inventory.append(items.Kniv())


### Hovedpersonen angriper
print("Ditt inventory: ", end="")
for item in hovedperson.inventory:
    print(item.navn, end=" | ")


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