from __future__ import annotations

from typing import Tuple

from pygame import Surface

from pygame.font import Font, SysFont

from .....Config import FONTS

from ..MapObjects.MapObject import MapObject

class BaseCell:
    FONT        : str = FONTS['cell_font']
    FONT_COLOR  : Tuple[int, int, int] = (255, 255, 255)
    MAP_SYMBOL  : str = 'B'

    def __init__(self):
        pass 

    def onObjectEnterCell(self, object : MapObject) -> None: 
        pass 

    def onObjectExitCell(self, object : MapObject) -> None: 
        pass 

    def update(self) -> None: 
        pass 

    
    def surface(self, size : Tuple[int, int] = (32, 32)) -> Surface: 
        display : Surface = Surface(size) 
        font    : Font    = SysFont(self.FONT, sum(size) / 2)
        text    : Surface = font.render(self.MAP_SYMBOL, True, self.FONT_COLOR)
        display.blit(text, (0, 0))

    def canMoveTo(self, object : MapObject) -> bool: 
        return True