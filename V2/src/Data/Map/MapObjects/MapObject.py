from __future__ import annotations

from typing import Protocol, Tuple, TYPE_CHECKING, runtime_checkable

if TYPE_CHECKING: 
    from ..Cells.Cell import Cell

from pygame.surface import Surface

@runtime_checkable
class MapObject(Protocol):

    def onEnterCell(self, cell : Cell) -> None: ... 

    def onExitCell(self, cell : Cell) -> None: ... 

    def update(self) -> None: ...
    
    def surface(self, size : Tuple[int, int] = (32, 32)) -> Surface: ...

    def canMoveTo(self, cell : Cell) -> bool: ...

    def onInteractWithObject(self, other : MapObject) -> None: ...