from __future__ import annotations
import warnings

warnings.warn("This file has been phased out due to architectural changes", DeprecationWarning)


from typing import Callable, Dict, List, TypeVar
type SignalID = str

class SignalBus:
    T = TypeVar('T', bound=Callable[..., None])
    _listeners : Dict[str, List[SignalBus.T]]

    def __init__(self) -> None:
        self._listeners = {}

    def addListener(self, signalID : SignalID, function : SignalBus.T) -> None:
        if signalID not in self._listeners: self._listeners[signalID] = []
        if function in self._listeners[signalID]: return 
        self._listeners[signalID].append(function)

    def removeListener(self, signalID : SignalID, function : SignalBus.T) -> None: 
        if signalID not in self._listeners or function not in self._listeners[signalID]: return 
        self._listeners[signalID].remove(function)

    def signal(self, signalID : SignalID, *args, **kwargs) -> None: 
        if signalID not in self._listeners: return 
        for listener in self._listeners[signalID]:
            listener(*args, **kwargs)

# A default, global signal bus to send the signals to 
GLOBAL_SIGNAL_BUS = SignalBus() 

# A decorator which adds the listeners to the signal bus (global bus by default)
# Can choose to make their own signal bus for the sake of managing scope
def listener(signalID : SignalID, signalBus : SignalBus = GLOBAL_SIGNAL_BUS):
    def listener_instance(function: SignalBus.T) -> SignalBus.T:
        signalBus.addListener(signalID, function)
        return function
    return listener_instance

# Function to send the signal out to all of the listeners
def signal(signalID : SignalID, *args, signalBus : SignalBus = GLOBAL_SIGNAL_BUS, **kwargs) -> None: 
    signalBus.signal(signalID, *args, **kwargs)