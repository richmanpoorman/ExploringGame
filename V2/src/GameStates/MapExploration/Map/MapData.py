from .Cells.Cell import Cell 

from typing import Dict, Tuple, Optional

from .Cells.BaseCell import BaseCell
from .Cells.ForestCell import ForestCell
from .Cells.MountainCell import MountainCell
from .Cells.PlainsCell import PlainsCell

from random import choice

from .MapObjects.MapObject import MapObject
from .MapObjects.MapPlayer import MapPlayer
class MapData: 
    
    def __init__(self):
        self.cellMap : Dict[Tuple[int, int], Cell] = dict()
        self.objectMap : Dict[MapObject, Tuple[int, int]] = dict() 
        
        self.objectAt[(0, 0)] = MapPlayer()
        self.cellMap[(0, 0)] = BaseCell() 

    def at(self, location : Tuple[int, int]) -> Cell | MapObject: 
        mapObject : Optional[MapObject] = self.objectAt(location)
        if mapObject is not None: 
            return mapObject 
        return self.cellAt(location)

    def objectAt(self, location : Tuple[int, int]) -> Optional[MapObject]:
        for (mapObject, objectLocation) in self.objectMap.items():
            if location == objectLocation: 
                return mapObject 
        return None
    
    def cellAt(self, location : Tuple[int, int]) -> Cell: 
        if location not in self.cellMap: 
            self.generateCell(location) 
        return self.cellMap[location]

    def generateCell(self, location : Tuple[int, int]) -> None: 
        options = [ForestCell, MountainCell, PlainsCell]
        cell : Cell = choice(options)()

        self.cellMap[location] = cell