from __future__ import annotations

from typing import Protocol, Optional, Tuple

from pygame import Surface 
from pygame.event import Event 

from ...Data.Data import Data

class View(Protocol): 

    '''Things to do when entering the view'''
    def start(self, data : Data) -> None: ...

    '''Things to do every time the frame is updated'''
    def update(self, data : Data) -> None: ... 

    '''Things to do when exiting the view'''
    def exit(self, data : Data) -> None: ...

    def surface(self, data : Data, screenSize : Optional[Tuple[int, int]] = None) -> Surface: ... 

    def onEvent(self, data : Data, event : Event) -> None: ...