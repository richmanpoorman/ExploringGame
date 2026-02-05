from __future__ import annotations

from typing import Protocol, Tuple 

from ..Cells.Cell import Cell

from pygame.surface import Surface
from pygame.font import Font, SysFont

from config.Config import FONTS

from .MapObject import MapObject
class MapPlayer:

    FONT        : str = FONTS['cell_font']
    FONT_COLOR  : Tuple[int, int, int] = (255, 255, 0)
    MAP_SYMBOL  : str = '@'

    def onEnterCell(self, cell : Cell) -> None: ... 

    def onExitCell(self, cell : Cell) -> None: ... 

    def update(self) -> None: 
        pass 
    
    def surface(self, size : Tuple[int, int] = (32, 32)) -> Surface: 
        display : Surface = Surface(size) 
        font    : Font    = SysFont(self.FONT, sum(size) // 2 - 1)
        text    : Surface = font.render(self.MAP_SYMBOL, True, self.FONT_COLOR)
        display.blit(text, (0, 0))
        return display

    def canMoveTo(self, cell : Cell) -> bool: 
        return True
    
    def onInteractWithObject(self, other : MapObject) -> None:
        pass 