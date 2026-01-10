from __future__ import annotations

from pygame import Surface 

from typing import Optional, Tuple, Protocol

class Displayable(Protocol):
    
    def surface(self, size : Optional[Tuple[int, int]] = None) -> Surface: ...

    def updateSurface(self, *args, **kwargs) -> None: ...