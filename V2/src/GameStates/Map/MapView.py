from __future__ import annotations

from typing import Optional, Tuple, Dict, Any

from pygame import Surface 
from pygame.event import Event 
from pygame import KEYDOWN

from .MapLogic import MapLogic

from ..Interfaces.Context import Context

from ...Data.Map.MapData import MapData

from ...Data.Map.MapObjects.MapPlayer import MapPlayer

from ...Data.Map.Cells.Cell import Cell
from ...Data.Map.MapObjects.MapObject import MapObject


from ...Data.Settings import KEY_BINDINGS

class MapView: 
    CELL_SIZE : Tuple[int, int] = (16, 16)
    MAP_SIZE  : Tuple[int, int] = (19, 19)

    def __init__(self, context : Context, logic : MapLogic):
        self.setContext(context)
        self.logic : MapLogic = logic
        self.__bindings : Dict[int, str] = KEY_BINDINGS["exploration"]

    def setContext(self, context : Context) -> None: 
        self.context = context

    '''Things to do when entering the view'''
    def start(self) -> None: 
        pass 

    '''Things to do every time the frame is updated'''
    def update(self) -> None: 
        pass 

    '''Things to do when exiting the view'''
    def exit(self) -> None: 
        pass 

    def surface(self, screenSize : Tuple[int, int] = (512, 512)) -> Surface: 
        surface : Surface = Surface(screenSize)
        width, height = screenSize
        cellWidth, cellHeight = self.CELL_SIZE
        mapWidth, mapHeight   = self.MAP_SIZE
        
        mapData : MapData = self.context.data.mapData

        (playerRow, playerCol) = mapData.getObjectsLocations(MapPlayer)[0]
        
        for row in range(-(mapWidth // 2), mapWidth // 2 + 1):
            for column in range(-(mapHeight // 2), mapHeight // 2 + 1): 
                cellOrObject : Cell | MapObject = mapData.at((playerRow + row, playerCol + column))
                cellSurface : Surface = cellOrObject.surface((cellWidth, cellHeight))
                surface.blit(cellSurface, (width // 2 + row * cellWidth, height // 2 + column * cellHeight))
                
        return surface

    def onEvent(self, event : Event) -> Optional[Tuple[str, ...]]: 
        
        if event.type != KEYDOWN or event.key not in self.__bindings:
            return None
        return (self.__bindings[event.key], )
                
    def handle(command : str, *args, **kwargs) -> None: 
        raise RuntimeError(f"MapView Handle Command {command} not found, with args: {args} and kwargs: {kwargs}")

    def get(command : str, *args, **kwargs) -> Any: 
        raise RuntimeError(f"MapView Get Command {command} not found, with args: {args} and kwargs: {kwargs}")