from Basics import Cell
from Terrain import TERRAIN_COLOR 
from random import randint
from GameState import GameState
from Battle import Battle
from Battle import Enemy
from Store import Store
from StoreDisplay import StoreDisplay

def fight(percentChance : int, lvl : int = 1):
    if (randint(0, 100) > percentChance):
        return
    print("Fight")
    GameState.setState(GameState.BATTLE_STATE)
    # TODO:: Change to more varied enemies
    lvl      += randint(-5, 5)
    lvl      = max(1, lvl)

    hp       = 10 * lvl + randint(0, 10)
    mp       = 10 * lvl + randint(0, 10)
    netScore = randint(lvl, 2 * lvl)
    physical = netScore // 3 + 1
    magical  = 2 * netScore // 3 + 1
    exp      = randint(netScore, netScore + hp + mp)
    money    = randint(netScore, netScore + hp + mp)
    Battle.setEnemy(Enemy(hp = hp, mp = mp, physical = physical, magical = magical, lvl = lvl, exp = exp, money = money))

# Classes with different behavior
class PlainCell(Cell):
    ENEMY_CHANCE = 20

    def __init__(self, position : tuple):
        super().__init__(position, ".", TERRAIN_COLOR["."])

    def action(self, lvl : int = 1) -> None:
        print("Plain")
        fight(self.ENEMY_CHANCE, lvl)

class MountainCell(Cell):
    ENEMY_CHANCE = 70

    def __init__(self, position : tuple):
        super().__init__(position, "^", TERRAIN_COLOR["^"])

    def action(self, lvl : int = 1) -> None:
        print("Mountain")
        fight(self.ENEMY_CHANCE, lvl)

class ValleyCell(Cell):
    ENEMY_CHANCE = 50

    def __init__(self, position : tuple):
        super().__init__(position, "w", TERRAIN_COLOR["w"])

    def action(self, lvl : int = 1) -> None:
        print("Valley")
        fight(self.ENEMY_CHANCE, lvl)

class ForestCell(Cell):
    ENEMY_CHANCE = 90

    def __init__(self, position : tuple):
        super().__init__(position, "T", TERRAIN_COLOR["T"])

    def action(self, lvl : int = 1) -> None:
        print("Forest")
        fight(self.ENEMY_CHANCE, lvl)

class ShopCell(Cell):
    def __init__(self, position : tuple):
        super().__init__(position, "S", TERRAIN_COLOR["S"])
        self.store = Store()

    def action(self, lvl : int = 1) -> None:
        GameState.setState(GameState.SHOP_STATE)
        self.store.restock(lvl)
        StoreDisplay.setup(self.store)

        print("SHOPPING")

class WallCell(Cell):
    def __init__(self, position : tuple):
        super().__init__(position, "\"", TERRAIN_COLOR["\""])
        self.isBlocked = True

class SettlementCell(Cell):
    def __init__(self, position : tuple):
        super().__init__(position, "!", TERRAIN_COLOR["!"])

    def action(self, lvl : int = 1) -> None:
        print("Explore : Settlement")

class TowerCell(Cell):
    def __init__(self, position : tuple):
        super().__init__(position, "|", TERRAIN_COLOR["|"])

    def action(self, lvl : int = 1) -> None:
        print("Explore : Tower")

class HutCell(Cell):
    def __init__(self, position : tuple):
        super().__init__(position, "+", TERRAIN_COLOR["+"])

    def action(self, lvl : int = 1) -> None:
        print("Explore : Hut")

class CityCell(Cell):
    def __init__(self, position : tuple):
        super().__init__(position, "#", TERRAIN_COLOR["#"])

    def action(self, lvl : int = 1) -> None:
        print("Explore : City")

class WinCell(Cell):
    def __init__(self, position : tuple):
        super().__init__(position, "X", TERRAIN_COLOR["X"])

    def action(self, lvl : int = 1) -> None:
        print("You Win!")

class BorderCell(Cell):
    def __init__(self, position : tuple):
        super().__init__(position, "%", TERRAIN_COLOR["%"])

    def action(self, lvl : int = 1) -> None:
        print("Border")

class CliffCell(Cell):

    def __init__(self, position : tuple):
        super().__init__(position, "~", TERRAIN_COLOR["~"])

    def action(self, lvl : int = 1) -> None:
        print("Cliff")

# Map of classes to the symbol
TERRAIN_CLASS = {
    "." : PlainCell,
    "T" : MountainCell,
    "^" : ValleyCell,
    "w" : ForestCell,
    
    # Special places; \"alls and shops
    "S"  : ShopCell,
    "\"" : WallCell,
    
    # Special Terrain Ewents
    "!" : SettlementCell,
    "|" : TowerCell,
    "+" : HutCell,
    "#" : CityCell,
    
    # Special \"all ewent
    "X" : WinCell,

    # Border Ewents
    "%" : BorderCell,
    "~" : CliffCell,
    
    # Extra
    "?" : None
}