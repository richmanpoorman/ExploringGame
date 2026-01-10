from __future__ import annotations

from typing import Protocol, Literal

from ..HasFeature.Listening import Listening
from ..HasFeature.Broadcaster import Broadcaster
from ..HasFeature.Runnable import Runnable

from ..ModelViewController.Model import Model

from ...Types.Types import SignalID

class ModelManager(Listening, Broadcaster, Runnable, Protocol):

    def init(self, *args, **kwargs) -> None: ... 

    def update(self) -> None: ...

    def close(self) -> None: ...

    def listen(self, signalID: str, *args, **kwargs) -> None: ...

    def broadcast(self, signalID: SignalID, *args, **kwargs) -> None: ...

    def connect(self, listener : Listening) -> None: ...

    def disconnect(self, listener : Listening) -> None: ...

    def setModel(self, model : Model) -> None: ...

    def model(self) -> Model: ...