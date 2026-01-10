from __future__ import annotations
from ..Types.Types import SignalID
from ..Interfaces.HasFeature.Listening import Listening
from typing import Callable, Dict, List, TypeVar


class LocalListener(Listening):
    T = TypeVar('T', bound=Callable[..., None])
    __listeners : Dict[SignalID, List[LocalListener.T]] = {}

    def __init__(self) -> None:
        self.__listeners = {}

    def listen(self, signalID : SignalID, *args, **kwargs) -> None:
        if signalID not in self.__listeners: return 
        for listener in self.__listeners[signalID]:
            listener(*args, **kwargs)
    
    def registerListener(self, signalID : SignalID, callback : LocalListener.T) -> None:
        if signalID not in self.__listeners:
            self.__listeners[signalID] = []
        self.__listeners[signalID].append(callback)
