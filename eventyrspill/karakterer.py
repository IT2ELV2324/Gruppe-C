#HOVEDPERSON = {"hp": 100, "xp":0, "slag": 3, "dodge": 2}
#FIENDE = {"hp": 90, "xp":0, "slag": 3, "dodge": 4}
'''
 if char_type == "fighter":
    type_dict = FIGHTER
elif char_type == "thief":
    type_dict = THIEF
elif char_type == "mage":
    type_dict = MAGE
else:
    raise Exception("This character type doesn't exist!")
    '''

class Karakter:
    """Generell klasse for karakter som alle skal arve fra"""
    #_hp = 100
    #_xp = 0
    #_slag = 0
    #_dodge = 0
    def __init__(self, navn, hp, xp):
        self._navn=navn
        self._hp=hp
        self._xp=xp
        self._assign_attributes()

    def __init__(self, char_type):
        self._char_type = char_type
        self._assign_attributes()

    def _assign_attributes(self):
        type_dict=TYPE[self._char_type]
        self._hp = type_dict["health"]
        self._slag = type_dict["slag"]
        self._dodge = type_dict["dodge"]

    pass

def main():
    fighter_character = Character("fighter")
    print(fighter_character._char_type)


if __name__ == "__main__":
    main()

