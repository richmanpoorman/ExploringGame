from __future__ import annotations

from abc import ABC as Interface, abstractmethod

from Interfaces.HasFeature.Listening import Listening
from Types.Types import SignalID
class Broadcaster(Interface): 

    @abstractmethod
    def connect(self, listener : Listening, *args, **kwargs) -> None: 
        pass 
    
    @abstractmethod
    def disconnect(self, listener : Listening, *args, **kwargs) -> None: 
        pass 

    @abstractmethod
    def broadcast(self, signalID : SignalID, *args, **kwargs) -> None:
        pass 
