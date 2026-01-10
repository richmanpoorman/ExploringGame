from __future__ import annotations

from typing import Protocol, Literal

from src.Types.Types import SignalID

from ..HasFeature.Listening import Listening
from ..HasFeature.Broadcaster import Broadcaster
from ..HasFeature.Runnable import Runnable

from .Controller import Controller



class ControllerManager(Listening, Broadcaster, Runnable, Protocol):
    
    def init(self, *args, **kwargs) -> None: ... 

    def update(self) -> None: ...

    def close(self) -> None: ...

    def listen(self, signalID: SignalID, *args, **kwargs) -> None: ...

    def broadcast(self, signalID: SignalID, *args, **kwargs) -> None: ...

    def connect(self, listener : Listening, origin : Literal["view", "model"]) -> None: ...

    def disconnect(self, listener : Listening, origin : Literal["view", "model"]) -> None: ...

    def setController(self, controller : Controller) -> None: ...

    def controller(self) -> Controller: ...