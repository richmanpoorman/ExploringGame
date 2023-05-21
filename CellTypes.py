from Basics import Cell
from Terrain import TERRAIN_COLOR 
from random import randint
from Basics import GameState
from Battle import Battle
from Battle import Enemy
from Store import Store

def fight(percentChance : int):
    if (randint(0, 100) > percentChance):
        return
    print("Fight")
    GameState.setState(GameState.BATTLE_STATE)
    Battle.setEnemy(Enemy(hp = 100, mp = 0, dmg = 1, lvl = 1, exp = 0, money = 0))

# Classes with different behavior
class PlainCell(Cell):
    ENEMY_CHANCE = 20

    def __init__(self, position : tuple):
        super().__init__(position, ".", TERRAIN_COLOR["."])

    def action(self) -> None:
        print("Plain")
        fight(self.ENEMY_CHANCE)

class MountainCell(Cell):
    ENEMY_CHANCE = 70

    def __init__(self, position : tuple):
        super().__init__(position, "^", TERRAIN_COLOR["^"])

    def action(self) -> None:
        print("Mountain")
        fight(self.ENEMY_CHANCE)

class ValleyCell(Cell):
    ENEMY_CHANCE = 50

    def __init__(self, position : tuple):
        super().__init__(position, "w", TERRAIN_COLOR["w"])

    def action(self) -> None:
        print("Valley")
        fight(self.ENEMY_CHANCE)

class ForestCell(Cell):
    ENEMY_CHANCE = 90

    def __init__(self, position : tuple):
        super().__init__(position, "T", TERRAIN_COLOR["T"])

    def action(self) -> None:
        print("Forest")
        fight(self.ENEMY_CHANCE)

class ShopCell(Cell):
    def __init__(self, position : tuple):
        super().__init__(position, "S", TERRAIN_COLOR["S"])
        self.store = Store()

    def action(self) -> None:
        print("SHOPPING")

class WallCell(Cell):
    def __init__(self, position : tuple):
        super().__init__(position, "\"", TERRAIN_COLOR["\""])
        self.isBlocked = True

class SettlementCell(Cell):
    def __init__(self, position : tuple):
        super().__init__(position, "!", TERRAIN_COLOR["!"])

    def action(self) -> None:
        print("Explore : Settlement")

class TowerCell(Cell):
    def __init__(self, position : tuple):
        super().__init__(position, "|", TERRAIN_COLOR["|"])

    def action(self) -> None:
        print("Explore : Tower")

class HutCell(Cell):
    def __init__(self, position : tuple):
        super().__init__(position, "+", TERRAIN_COLOR["+"])

    def action(self) -> None:
        print("Explore : Hut")

class CityCell(Cell):
    def __init__(self, position : tuple):
        super().__init__(position, "#", TERRAIN_COLOR["#"])

    def action(self) -> None:
        print("Explore : City")

class WinCell(Cell):
    def __init__(self, position : tuple):
        super().__init__(position, "X", TERRAIN_COLOR["X"])

    def action(self) -> None:
        print("You Win!")

class BorderCell(Cell):
    def __init__(self, position : tuple):
        super().__init__(position, "%", TERRAIN_COLOR["%"])

    def action(self) -> None:
        print("Border")

class CliffCell(Cell):

    def __init__(self, position : tuple):
        super().__init__(position, "~", TERRAIN_COLOR["~"])

    def action(self) -> None:
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