from __future__ import annotations

from typing import Protocol, Optional, Tuple, TYPE_CHECKING

from .View import View
from .Logic import Logic


if TYPE_CHECKING:
    from .Context import Context

from pygame.event import Event
from pygame.surface import Surface


'''
    Represents the different states of the game
'''
class GameState(Protocol):

    def setContext(self, context : Context) -> None: ...

    def onEnterState(self) -> None: ... 

    def update(self) -> None: ... 

    def onExitState(self) -> None: ... 

    def onEvent(self, event : Event) -> None: ... # Sends the event to the view

    def onCommand(self, command : str) -> None: ... # Parses command from view and sends it to the controller
    
    def surface(self, size : Tuple[int, int] = (512, 512)) -> Surface: ...

    @property 
    def view(self) -> View: ...
    
    @property 
    def context(self) -> Context: ...
    
    @property 
    def logic(self) -> Logic: ...