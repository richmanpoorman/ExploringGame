from __future__ import annotations
from typing import Set
from Interfaces.HasFeature.Listening import Listening
from Interfaces.HasFeature.Broadcaster import Broadcaster

from Types.Types import SignalID

class LocalBroadcaster(Broadcaster): 

    __listeners : Set[Listening]

    def __init__(self) -> None:
        self.__listeners = set()

    def connect(self, listener : Listening) -> None: 
        self.__listeners.add(listener)
    
    def disconnect(self, listener : Listening) -> None: 
        self.__listeners.remove(listener)

    def broadcast(self, signalID : SignalID, *args, **kwargs) -> None:
        for listener in self.__listeners: 
            listener.listen(signalID, *args, **kwargs)

    def close(self) -> None:
        self.__listeners.clear()