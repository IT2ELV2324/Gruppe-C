#HOVEDPERSON = {"hp": 100, "xp":0, "slag": 3, "dodge": 2}
#FIENDE = {"hp": 90, "xp":0, "slag": 3, "dodge": 4}

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
