import pygame

# Singleton which stores the static variables for game state (THERE IS NO INSTANCE)
class GameState:
    # Actual State
    state = 0

    EXPLORE_STATE = 0
    BATTLE_STATE  = 1

    def setState(state : int) -> None:
        GameState.state = state

    def getState() -> int:
        return GameState.state

class Stats:
    def __init__(self, hp : int, mp : int, dmg : int, lvl : int, exp : int = 0, money : int = 0):
        self.hp = hp
        self.maxHp = hp
        self.mp = mp 
        self.maxMp = mp
        self.dmg = dmg 
        self.lvl = lvl 
        self.exp = exp
        self.money = money 
    
    def changeHp(self, deltaHp : int = 0) -> None:
        self.hp += deltaHp 
    
    def changeMp(self, deltaMp : int = 0) -> None:
        self.mp += deltaMp 
    
    def getHpPercentage(self) -> float:
        return self.hp / self.maxHp 
    
    def getMpPercentage(self) -> float:
        return self.mp / self.maxMp


# Classes representing different things
    # BASIC CLASSES (Testing out composition) IN ORDER TO BE ABLE TO BE EXTENDED LATER
class Location:
    def __init__(self, position : tuple = (0, 0)):
        self.position = position
    
    def getPosition(self) -> tuple:
        return self.position

    def updatePosition(self, newPosition : tuple) -> None:
        self.position = newPosition

#
# Cell Class : Each individual spot of the board
#

class Cell:
    def __init__(self, position : tuple, display : str = "X", color : tuple = (255, 255, 255)):
        self.location = Location(position)
        self.display = CellDisplay(display, color)
        self.isBlocked = False
        self.found = False
        self.color = color
    
    def getLocation(self) -> tuple:
        return self.location.getPosition()
    
    
    def getSurface(self, font : pygame.font) -> pygame.surface:
        return self.display.getSurface(font)

    def getDisplay(self) -> str:
        
        return self.display.getDisplay()
    
    def find(self) -> None:
        self.found = True 
    
    def isFound(self) -> bool:
        return self.found

    def isBlocked(self) -> bool:
        return self.isBlocked
    
    def action(self) -> None:
        print("No Override")
        pass


class CellDisplay:

    CELL_FONT_SIZE  = 20
    

    def __init__(self, display : str = "@", color : tuple = (255, 255, 255)):
        self.display = display
        self.color = color

    def setDisplay(self, display : str = "@") -> None:
        self.display = display

    def getSurface(self, font : pygame.font) -> pygame.surface:
        return font.render(self.display, True, self.color, None)

    def getDisplay(self) -> str:
        return self.display
