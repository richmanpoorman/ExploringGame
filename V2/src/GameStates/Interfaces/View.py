from __future__ import annotations

from typing import Protocol, Optional, Tuple, Any

from pygame import Surface 
from pygame.event import Event 

from ...Data.Data import Data

from .Context import Context

class View(Protocol): 

    def setContext(self, context : Context) -> None: ...

    '''Things to do when entering the view'''
    def start(self) -> None: ...

    '''Things to do every time the frame is updated'''
    def update(self) -> None: ... 

    '''Things to do when exiting the view'''
    def exit(self) -> None: ...

    def surface(self, screenSize : Tuple[int, int] = (512, 512)) -> Surface: ... 

    def onEvent(self, event : Event) -> Optional[Tuple[str, ...]]: ... # Returns the command of the input

    def handle(command : str, *args, **kwargs) -> None: ...

    def get(command : str, *args, **kwargs) -> Any: ...