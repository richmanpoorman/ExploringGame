from __future__ import annotations

from typing import Protocol, Tuple 

from ..Cells.Cell import Cell

from pygame.surface import Surface

class MapObject(Protocol):

    def onEnterCell(self, cell : Cell) -> None: ... 

    def onExitCell(self, cell : Cell) -> None: ... 

    def update(self) -> None: ...
    
    def surface(self, size : Tuple[int, int] = (32, 32)) -> Surface: ...

    def canMoveTo(self, cell : Cell) -> bool: ...