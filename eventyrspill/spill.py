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
        
        wrapper = textwrap.TextWrapper(width=100)  
        wrapped_line = wrapper.fill(text=line)
        
        all_dialog.append(wrapped_line)
    
    return all_dialog

dialog = load_dialog()
print(dialog[1])
print(dialog[2])


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
        if fiende.hp > 0: #Siden hovedperson angriper først uansett, tenkte jeg at det var greit å sjekke om fienden lever før den angriper
            vaapen = random.choice(fiende.inventory)
            vaapen.angrip(angriper=fiende, motstander=hovedperson)
    print(f"\n Hovedperson har {hovedperson.hp} hp igjen. Fienden har {fiende.hp} igjen. \n")

juksemodus = input("Oensker du et juksevaapen? (ja/nei): ").capitalize().strip()


### Første fight (garantert seier)
print(dialog[3])
hovedperson = karakterer.Karakter(heltenavn, hp=100, pos=0)
hovedperson.inventory = [items.Dolk(), items.Pil_og_bue(piler=10)]
if juksemodus == "Ja":
    hovedperson.inventory.append(items.Juks())
fiende = karakterer.Fiende(hp=100,pos=0)
fiende.inventory = [items.Smørkniv()]
fight()


### Andre fight
print("Du fikk en paraply!")
print(dialog[4])
print(dialog[5])
hovedperson.hp = 100 #endret det slik at hovedperson starter med 100hp
hovedperson.inventory.append(items.Paraply())
fiende = karakterer.Fiende(hp=100, pos=1)
fiende.inventory = [items.Dolk()]
fight()

### Tredje fight
# hovedperson.inventory.append(items.)
fiende = karakterer.Fiende(hp=100, pos=5)
fight()


#funksjon for å sjekke sannsynlighet for seier (kjører programmet 1000 ganger og ser på seiersraten)

        
            
   
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

