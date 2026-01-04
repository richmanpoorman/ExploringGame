from abc import ABC as Interface, abstractmethod
from pygame import Surface 

class Displayable(Interface):
    @property
    @abstractmethod
    def surface(self) -> 