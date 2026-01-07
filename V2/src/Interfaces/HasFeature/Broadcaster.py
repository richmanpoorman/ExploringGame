from __future__ import annotations

from typing import Protocol

from .Listening import Listening
from ...Types.Types import SignalID
class Broadcaster(Protocol): 

    def connect(self, listener : Listening, *args, **kwargs) -> None: 
        pass 
    
    def disconnect(self, listener : Listening, *args, **kwargs) -> None: 
        pass 

    def broadcast(self, signalID : SignalID, *args, **kwargs) -> None:
        pass 
