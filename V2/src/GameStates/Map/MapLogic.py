from typing import Literal, Tuple


from ...Data.Data import Data
from ...Data.Map.MapObjects.MapPlayer import MapPlayer

from ..Interfaces.Context import Context
class MapLogic:

    def __init__(self, context : Context, renderDistance : Tuple[int, int] = (50, 50)):
        self.__context = context
        self.__mapData = context.data.mapData
        self.__player  = self.__mapData.getObjects(MapPlayer)[0]
        
        self.renderDistance = renderDistance # Load the initial chunks
        
        self.__checkAndGenerateCells(self.__mapData.objectLocation(self.__player), self.renderDistance)

    def setContext(self, context : Context) -> None: 
        self.__context = context
        self.__mapData = context.data.mapData
        self.__player  = self.__mapData.getObjects(MapPlayer)[0]

    def handle(self, command : str, *args, **kwargs) -> None: 
        match (command, args, kwargs):
            case ("move", [direction], _) | ("move", [], {"direction" : direction}): self.__move(direction)
            case _: raise RuntimeError(f"MapLogic Handle Command '{command}' not found, with args: {args} and kwargs: {kwargs}")
    
    def get(self, command : str, *args, **kwargs) -> None: 
        raise RuntimeError(f"MapLogic Get Command '{command}' not found, with args: {args} and kwargs: {kwargs}")
    
    def __move(self, direction : Literal["up", "down", "left", "right"]) -> None: 
        (row, column) = self.__mapData.objectLocation(self.__player)
        newPosition : Tuple[int, int] = (row, column)
        match direction:
            case "down" : newPosition = (row + 1, column)
            case "up"   : newPosition = (row - 1, column)
            case "left" : newPosition = (row, column - 1)
            case "right": newPosition = (row, column + 1)
        
        self.__mapData.moveObject(self.__player, newPosition)
        self.__checkAndGenerateCells(newPosition, self.renderDistance)

        # print(self.__mapData.objectLocation(self.__player))

    def __checkAndGenerateCells(self, fromPosition : Tuple[int, int], renderDistance : Tuple[int, int]) -> None: 
        renderWidth, renderHeight = renderDistance
        initialRow, initialColumn = fromPosition

        # TODO: Naive row by row; should be doing in distance based rather than just a linear scan, or generate by chunks
        for row in range(initialRow - renderHeight, initialRow + renderHeight + 1):
            for column in range(initialColumn - renderWidth, initialColumn + renderWidth + 1): 
                if self.__mapData.cellAt((row, column)) is None: 
                    self.__mapData.generateAndAddNewCell((row, column))
                    print(f'Generated {type(self.__mapData.cellAt((row, column)))}')