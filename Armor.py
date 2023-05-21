class Armor:
    def __init__(self, name : str = "NONE", physicalResistance : int = 0, mpResistance : int = 0):
        self.name = name
        self.resistance = (physicalResistance, mpResistance)

    def __str__(self):
        return self.name + ": (Physical Resistance: " + str(self.resistance[0]) + ", Magical Resistance: " + str(self.resistance[1]) + ")"
    
    def __repr__(self):
        return self.__str__()