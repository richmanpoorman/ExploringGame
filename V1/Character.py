from Basics import Location
from Basics import CellDisplay
from Basics import Stats
from Inventory import Inventory
from typing import Tuple
from random import randint 

class Character:
    LVL_EXP = 50
    LVL_REWARD = 10
    def __init__(self, hp : int = 100, dmg : int = 10, mp : int = 100):
        self.location = Location()
        self.display = CellDisplay("@", (0, 255, 0))
        self.stats = Stats(hp = hp, mp = mp, physicalDmg = dmg, magicDmg = 2 * dmg, lvl = 1, exp = 0)
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

    def levelUp(self):
        while (self.stats.exp >= self.stats.lvl * Character.LVL_EXP):
            self.stats.exp -= self.stats.lvl * Character.LVL_EXP
            self.stats.maxHp += randint(1, Character.LVL_REWARD)
            self.stats.maxMp += randint(1, Character.LVL_REWARD)
            self.stats.hp = self.stats.maxHp 
            self.stats.mp = self.stats.maxMp
            self.stats.dmg = (self.stats.dmg[0] + randint(1, Character.LVL_REWARD), self.stats.dmg[1] + randint(1, Character.LVL_REWARD))
            self.stats.lvl += 1

    def gainRewards(self, exp : int, money : int):
        self.stats.exp += exp 
        self.levelUp()
        self.inventory.money += money 
