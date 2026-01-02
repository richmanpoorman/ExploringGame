class Equipment:
    def __init__(self, name : str = "NONE", physical : int = 0, magic : int = 0, mpCost : int = 10):
        self.name = name
        self.dmg = (physical, magic)
        self.mpCost = mpCost
    
    def __str__(self):
        return self.name + ": (Physical Strength: " + str(self.dmg[0]) + ", Magical Strength: " + str(self.dmg[1]) + ", MP Cost: " + str(self.mpCost) + ")"
    
    def __repr__(self):
        return self.__str__()