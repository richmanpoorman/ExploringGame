from __future__ import annotations

from typing import Optional, Tuple, TYPE_CHECKING, Dict, Callable, Literal

from ..Interfaces.View import View

from ..Interfaces.Context import Context
from ..Interfaces.Logic import Logic

from pygame.event import Event
from pygame.surface import Surface

from .MapView import MapView
from .MapLogic import MapLogic

class MapState:

    def __init__(self, context : Context):
        self.__context  : Context = context 
        self.__logic    : MapLogic = MapLogic(self.context)
        self.__view     : MapView = MapView(self.context, self.__logic)
        

    def setContext(self, context : Context) -> None: 
        self.__context : Context = context
        self.view.setContext(context)
        self.logic.setContext(context)


    def onStateEntrance(self) -> None: 
        self.view.start()

    def update(self) -> None: 
        self.view.update()

    def onExitState(self) -> None: 
        self.view.exit()

    def surface(self, size : Tuple[int, int] = (512, 512)) -> Surface: 
        return self.view.surface(size)

    @property 
    def view(self) -> View: 
        return self.__view
    
    @property 
    def context(self) -> Context: 
        return self.__context 
    
    @property 
    def logic(self) -> Logic: 
        return self.__logic

    def onEvent(self, event : Event) -> None: 
        command : Optional[Tuple[str, ...]] = self.view.onEvent(event)
        if command is None: return
        self.onCommand(*command)
        
    def onCommand(self, command : str, *args, **kwargs)  -> None: 
        match command:
            case "move_up": self.__move("up") 
            case "move_down": self.__move("down") 
            case "move_left": self.__move("left")
            case "move_right": self.__move("right")
            case _: raise RuntimeError(f"Command {command} with args: {args} and kwargs: {kwargs} not implemented")

    
        
    def __move(self, direction : Literal["up", "down", "left", "right"]) -> None: 
        self.logic.handle("move", direction)
        # self.view.handle("move", direction)
        print(f'Moved {direction}')