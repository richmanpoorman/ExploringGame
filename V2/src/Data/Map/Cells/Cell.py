from __future__ import annotations

from typing import Protocol, Tuple, TYPE_CHECKING

if TYPE_CHECKING:
    from ..MapObjects.MapObject import MapObject

from pygame import Surface

class Cell(Protocol):
    
    def onObjectEnterCell(self, object : MapObject) -> None: ... 

    def onObjectExitCell(self, object : MapObject) -> None: ... 

    def update(self) -> None: ...
    
    def surface(self, size : Tuple[int, int] = (32, 32)) -> Surface: ...

    def canMoveTo(self, object : MapObject) -> bool: ...