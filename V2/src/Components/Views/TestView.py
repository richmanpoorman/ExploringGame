from typing import Tuple
from pygame import Surface
from pygame.event import Event
from src.Interfaces.HasFeature.Listening import Listening
from src.Types.Types import SignalID
from ...Interfaces.ModelViewController.View import View

class TestView(View):
    def __init__(self) -> None:
        super().__init__()

    def connect(self, listener: Listening, *args, **kwargs) -> None:
        return super().connect(listener, *args, **kwargs)
    
    def disconnect(self, listener: Listening, *args, **kwargs) -> None:
        return super().disconnect(listener, *args, **kwargs)
    
    def broadcast(self, signalID: str, *args, **kwargs) -> None:
        return super().broadcast(signalID, *args, **kwargs)
    
    def listen(self, signalID: SignalID, *args, **kwargs) -> None:
        return super().listen(signalID, *args, **kwargs)
    
    def surface(self, size: Tuple[int, int] | None = None) -> Surface:
        return super().surface(size)
    
    def updateSurface(self, *args, **kwargs) -> None:
        return super().updateSurface(*args, **kwargs)
    
    def onEvent(self, event: Event) -> None:
        return super().onEvent(event)
    