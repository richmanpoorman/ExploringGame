from __future__ import annotations

from typing import Optional, Tuple

from pygame import Surface 
from pygame.event import Event 

from .MapLogic import MapLogic

class MapView: 
    def __init__(self, logic : MapLogic):
        self.logic : MapLogic = logic

    '''Things to do when entering the view'''
    def start(self) -> None: 
        pass 

    '''Things to do every time the frame is updated'''
    def update(self) -> None: 
        pass 

    '''Things to do when exiting the view'''
    def exit(self) -> None: 
        pass 

    def surface(self, screenSize : Optional[Tuple[int, int]] = None) -> Surface: 
        return Surface(screenSize)

    def onEvent(self, event : Event) -> None:
        pass 