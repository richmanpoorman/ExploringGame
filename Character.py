from Basics import Location
from Basics import CellDisplay
from Basics import Stats
class Character:
    def __init__(self, hp : int = 100, dmg : int = 10, mp : int = 10):
        self.location = Location()
        self.display = CellDisplay("@", (0, 255, 0))
        self.stats = Stats(hp, mp, dmg, 1, 0, 0)

    def move(self, deltaX : int, deltaY : int) -> None:
        x, y = self.location.getPosition()
        x += deltaX 
        y += deltaY 
        self.location.updatePosition((x, y))

    def getPosition(self) -> tuple:
        return self.location.getPosition()
    
    def getStats(self) -> Stats:
        return self.stats
