from .Cells.Cell import Cell 

from typing import Dict, Tuple, Optional, List, Type

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
        self.__objectMap : Dict[MapObject, Tuple[int, int]] = dict() 
        
        self.addObject(MapPlayer(), (0, 0))
        self.cellMap[(0, 0)] = BaseCell() 

    def addObject(self, mapObject : MapObject, location : Tuple[int, int]) -> None: 
        self.__objectMap[mapObject] = location 

    def removeObject(self, mapObject : MapObject) -> None: 
        del self.__objectMap[mapObject]

    def addCell(self, cell : Cell, location : Tuple[int, int]) -> Optional[Cell]: 
        previousCell : Optional[Cell] = self.cellAt(cell)
        self.cellMap[(location)] = cell 
        return previousCell

    def at(self, location : Tuple[int, int]) -> Cell | MapObject: 
        mapObject : Optional[MapObject] = self.primaryObjectAt(location)
        if mapObject is not None: 
            return mapObject 
        cell : Optional[Cell] = self.cellAt(location)
        if cell is None: 
            raise RuntimeError(f"Tried to get cell at {location} but there was nothing there!")
        return cell 

    def primaryObjectAt(self, location : Tuple[int, int]) -> Optional[MapObject]:
        objects : List[MapObject] = self.objectsAt(location) 
        if len(objects) == 0: 
            return None
        return objects[0]

    def objectsAt(self, location : Tuple[int, int]) -> List[MapObject]:
        return [mapObject for (mapObject, objectLocation) in self.__objectMap.items() if objectLocation == location]
    
    def objectLocation(self, mapObject : MapObject) -> Tuple[int, int]: 
        return self.__objectMap[mapObject]

    def cellAt(self, location : Tuple[int, int]) -> Optional[Cell]: 
        if location not in self.cellMap: 
            return None 
        return self.cellMap[location]

    def cellAtDefinitely(self, location : Tuple[int, int]) -> Cell: 
        cell : Optional[Cell] = self.cellAt(location)
        if self.cellAt(location) is None: 
            cell = self.generateCell(location) 
            self.addCell(cell, location)
        return cell

    def generateCell(self, location : Tuple[int, int]) -> Cell: # TODO :: Add better terrain generation rules
        options = [ForestCell, MountainCell, PlainsCell]
        cell : Cell = choice(options)()
        return cell
    
    def generateAndAddNewCell(self, location : Tuple[int, int]) -> Cell: 
        if self.cellAt(location) is not None: 
            raise RuntimeError(f'Tried to generate a new cell, but {self.cellAt(location)} was already there')
        cell : Cell = self.generateCell(location)
        self.addCell(cell, location)
        
    def moveObjects(self, origin : Tuple[int, int], destination : Tuple[int, int]) -> List[MapObject]: 
        movedObjects : List[MapObject] = self.objectsAt(origin)
        if len(movedObjects) == 0: 
            return []

        if origin == destination:
            return movedObjects 
        
        objectsAtDestination : List[MapObject] = self.objectsAt(destination)

        for mapObject in movedObjects: 
            for destinationObject in objectsAtDestination: 
                mapObject.onInteractWithObject(destinationObject)
                destinationObject.onInteractWithObject(mapObject)

        for mapObject in movedObjects:
            self.__objectMap[mapObject] = destination
        
        return movedObjects + objectsAtDestination
    
    def moveObject(self, mapObject : MapObject, destination : Tuple[int, int]) -> List[MapObject]: 
        if mapObject not in self.__objectMap:
            return [] 
        
        objectsAtDestination : List[MapObject] = self.objectsAt(destination)
        for destinationObject in objectsAtDestination:
            mapObject.onInteractWithObject(destinationObject)
            destinationObject.onInteractWithObject(mapObject)

        self.__objectMap[mapObject] = destination

        return [mapObject] + objectsAtDestination
    
    def getObjects(self, objectType : Type[MapObject]) -> List[MapObject]:
        return [mapObject for mapObject in self.__objectMap.keys() if isinstance(mapObject, objectType)]
    
    def getObjectsLocations(self, objectType : Type[MapObject]) -> List[Tuple[int, int]]:
        return [location for mapObject, location in self.__objectMap.items() if isinstance(mapObject, objectType)]