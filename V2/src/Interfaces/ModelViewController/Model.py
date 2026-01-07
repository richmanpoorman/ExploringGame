from __future__ import annotations


from typing import Protocol

from src.Types.Types import SignalID

from ..HasFeature.Broadcaster import Broadcaster
from ..HasFeature.Listening import Listening

class Model(Broadcaster, Listening, Protocol):
    
    def listen(self, signalID: str, *args, **kwargs) -> None: ...

    def broadcast(self, signalID: SignalID, *args, **kwargs) -> None: ...

    def connect(self, listener: Listening, *args, **kwargs) -> None: ...

    def disconnect(self, listener: Listening, *args, **kwargs) -> None: ...
