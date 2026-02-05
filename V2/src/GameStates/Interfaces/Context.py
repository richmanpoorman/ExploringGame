from __future__ import annotations

from typing import Protocol, TYPE_CHECKING
from ...Data.Data import Data

if TYPE_CHECKING:
    from .GameState import GameState

class Context(Protocol):

    def enterState(self, state : GameState) -> None: ...

    def exitState(self) -> None: ... 

    @property
    def state(self) -> GameState: ...

    @property 
    def data(self) -> Data: ... 