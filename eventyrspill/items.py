class Vaapen:
    """
    En generell klasse som alle våpen skal arve fra
    """
    def __init__(self):
        pass
    def angrip(self, angriper, motstander):
        pass

class Kniv(Vaapen):
    def __init__(self):
        super().__init__()

    def angrip(self, angriper, motstander):
        if abs(motstander.pos - angriper.pos) < 3:
            motstander.hp = motstander.hp - 10



