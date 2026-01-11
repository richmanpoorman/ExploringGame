from __future__ import annotations

from typing import List, Optional, Tuple


from ..GameStates.Interfaces.GameState import GameState

from ..GameStates.Interfaces.View import View

from .Data import Data

from pygame.event import Event 
from pygame import Surface

class StateStackMachine:
    def __init__(self) -> None: 
        pass 

    def init(self, initialState : GameState): 
        self.__data : Data = Data() 
        self.__stateStack : List[GameState] = [initialState] 

    def enterState(self, state : GameState) -> None: 
        exitedState : GameState = self.__stateStack[-1] 
        self.__stateStack.append(state)

        exitedState.onExitState() 
        state.onEnterState()

    def exitState(self) -> None: 
        if len(self.__stateStack) <= 1: 
            raise RuntimeError("Can't exit the base state")
        exitedState  : GameState = self.__stateStack.pop()
        enteredState : GameState = self.__stateStack[-1]

        exitedState.onExitState() 
        enteredState.onEnterState()
        
    @property 
    def state(self) -> GameState: 
        return self.__stateStack[-1]

    @property
    def view(self) -> View: 
        return self.state.view
    
    @property 
    def data(self) -> Data:
        return self.__data

    def surface(self, screenSize : Optional[Tuple[int, int]] = None) -> Surface: 
        return self.view.surface(screenSize)

    def onEvent(self, event : Event) -> None: 
        self.state.onEvent(event)