from Basics  import Location 
from Basics  import CellDisplay
from Basics  import Cell
from Terrain import TERRAIN
from Terrain import TERRAIN_COLOR
from CellTypes import TERRAIN_CLASS
from random  import shuffle
from random  import choices
# The stored board is a map with
# (x, y) tuple as the key, and a Cell as the value

#
# Board Class : The total grid
#
class Board:
    def __init__(self):
        self.board = {}
    
    def getLocation(self, location : Location) -> tuple:
        return self.getCell(location.position())

    def generateTerrain(self, position : tuple) -> None:
        if (self.hasCell(position)):
            return
        
        discoverOrder = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        shuffle(discoverOrder)
        for delta in discoverOrder:
            adj = (delta[0] + position[0], delta[1] + position[1])
            
            if not self.hasCell(adj):
                continue
            adjacentLetter = self.getCell(adj).getDisplay()
            
            options, weights = TERRAIN[adjacentLetter]
            letter = options[0]
            if (len(options) > 1):
                letter = (choices(options, weights = weights, k = 1))[0]
            
            self.addSpecialCell(position, letter)
            # color = TERRAIN_COLOR[letter]
            # self.addCell(Cell(position, letter, color))
            return
        
        letter = (choices([".", "T", "w", "^"], k = 1))[0]
        self.addSpecialCell(position, letter)
        # color = TERRAIN_COLOR[letter]
        # self.addCell(Cell(position, letter, color))

    
    def activateCell(self, position : tuple, lvl : int = 1) -> None:
        self.getCell(position).action(lvl)

    def addSpecialCell(self, position : tuple, display : str):
        self.addCell(TERRAIN_CLASS[display](position))

    
    def addCell(self, newCell : Cell) -> bool:
        pos = newCell.getLocation()
        if pos in self.board:
            return False
        self.board[pos] = newCell
        return True

    def hasCell(self, position : tuple) -> bool:
        return position in self.board

    def getCell(self, position : tuple) -> Cell:
        if position not in self.board:
            raise Exception("Position Does Not Exist in the Board")
        return self.board[position] 