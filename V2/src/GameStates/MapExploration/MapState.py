from __future__ import annotations

from typing import Optional, Tuple, TYPE_CHECKING

from ..Interfaces.View import View

if TYPE_CHECKING:
    from ...Runners.StateStackMachine import StateStackMachine

from pygame.event import Event

from .MapView import MapView
from .MapLogic import MapLogic

class MapState:

    def __init__(self):
        pass 

    def init(self, stateMachine : StateStackMachine):
        self.__stateMachine : StateStackMachine = stateMachine 
        self.__logic        : MapLogic          = MapLogic(self.__stateMachine.data)
        self.__view         : MapView           = MapView(self.__logic)

    def onStateEntrance(self) -> None: 
        self.view.start()

    def update(self) -> None: 
        self.view.update()

    def onExitState(self) -> None: 
        self.view.exit()

    @property 
    def view(self) -> View: 
        return self.__view

    def onEvent(self, event : Event) -> None: 
        pass 