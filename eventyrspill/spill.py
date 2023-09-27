"""Hovedfilen"""
import items
import karakterer

dialog = ['HER LIGGER ALL DIALOG']

def load_dialog():
    dialog_file = open("./eventyrspill/dialog.txt", encoding="utf-8")

    for line in dialog_file:  
        dialog.append(line.strip("\n"))

load_dialog()
print(dialog[1])
#hent dialog ved å bruke dialog[i], der i er linjen i dialog.txt hvor teksten ligger.