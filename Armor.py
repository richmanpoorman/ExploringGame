class Armor:
    def __init__(self, name : str = "NONE", mpResistance : int = 0, physicalResistance : int = 0):
        self.name = name
        self.resistance = (physicalResistance, mpResistance)