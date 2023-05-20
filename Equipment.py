class Equipment:
    def __init__(self, name : str = "NONE", physical : int = 0, magic : int = 0, mpCost : int = 10):
        self.name = name
        self.dmg = (physical, magic)
        self.mpCost = mpCost