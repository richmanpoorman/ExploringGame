# Consumable Items
class Consumable:
    def __init__(self, name : str = "NONE", hp : int = 0, mp : int = 0):
        self.name = name
        self.recover = (hp, mp)

    def __str__(self):
        return self.name + ": (HP: " + str(self.recover[0]) + ", MP: " + str(self.recover[1]) + ")"
    
    def __repr__(self):
        return self.__str__()