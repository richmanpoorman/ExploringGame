from __future__ import annotations

from typing import Protocol, Optional, Tuple

from .View import View

from pygame.event import Event

'''
    Represents the different states of the game
'''
class GameState(Protocol):

    def onEnterState(self) -> None: ... 

    def update(self) -> None: ... 

    def onExitState(self) -> None: ... 

    def view(self, screenSize : Optional[Tuple[int, int]] = None) -> View: ...

    def onEvent(self, event : Event) -> None: ...