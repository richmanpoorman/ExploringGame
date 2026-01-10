from __future__ import annotations

from ..HasFeature.Runnable import Runnable

from typing import Protocol

class GameManager(Runnable, Protocol):
    
    def init(self, *args, **kwargs) -> None: ...

    def update(self) -> None: ... 

    def close(self) -> None: ...