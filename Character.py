from Basics import Location
from Basics import CellDisplay
from Basics import Stats
from Inventory import Inventory
from typing import Tuple

class Character:
    def __init__(self, hp : int = 100, dmg : int = 10, mp : int = 100):
        self.location = Location()
        self.display = CellDisplay("@", (0, 255, 0))
        self.stats = Stats(hp = hp, mp = mp, physicalDmg = dmg, magicDmg = 2 * dmg, lvl = 1, exp = 0, money = 0)
        self.inventory = Inventory()

    def move(self, deltaX : int, deltaY : int) -> None:
        x, y = self.location.getPosition()
        x += deltaX 
        y += deltaY 
        self.location.updatePosition((x, y))

    def getPosition(self) -> Tuple[int, int]:
        return self.location.getPosition()
    
    def getStats(self) -> Stats:
        return self.stats
    
    def takeDamage(self, damage : Tuple[int, int]) -> int:
        armor = self.inventory.armor 
        physicalDmg = max(0, damage[0] - armor.resistance[0]) if damage[0] != 0 else 0
        magicalDmg  = max(0, damage[1] - armor.resistance[1]) if damage[1] != 0 else 0
        totalDmg = physicalDmg + magicalDmg

        self.stats.changeHp(-totalDmg)
        return totalDmg
