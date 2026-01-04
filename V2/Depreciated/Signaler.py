import warnings

warnings.warn("This file has been phased out due to architectural changes", DeprecationWarning)
from V2.Depreciated.SignalBus import SignalBus, GLOBAL_SIGNAL_BUS, listener, signal, SignalID
from typing import Dict 


type BusID = str 

class Signaler:
    _buses : Dict[BusID, SignalBus]
    
    def resetBuses(self) -> None: 
        _buses = {"default" : GLOBAL_SIGNAL_BUS}

    def addBus(self, busID : BusID, signalBus : SignalBus) -> None:
        self._buses[busID] = signalBus

    def setDefaultBus(self, signalBus : SignalBus = GLOBAL_SIGNAL_BUS) -> None: 
        self._buses["default"] = signalBus
    
    def bus(self, busID : BusID = "default") -> SignalBus: 
        if busID not in self._buses: raise RuntimeError('Bus [{busID}] was not found')
        return self._buses[busID]
    
    # Decorator wrapper to use the default bus or specific bus when given
    def listener(self, signalID : SignalID, busID : BusID = "default"):
        def listener_instance(function):
            @listener(signalID, self.bus(busID)) 
            def func(*args, **kwargs): 
                function(*args, **kwargs)
            return func 
        return listener_instance 
    
    def signal(self, signalID : SignalID, *args, busID : BusID = "default", **kwargs): 
        signal(signalID, *args, signalBus=self.bus(busID), **kwargs)
