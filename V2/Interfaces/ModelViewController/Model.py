from abc import ABC as Interface, abstractmethod
from typing import override

from Interfaces.HasFeature.Runnable import Runnable
from Interfaces.HasFeature.Broadcaster import Broadcaster
from Interfaces.HasFeature.Listening import Listening

class Model(Runnable, Broadcaster, Listening, Interface):
    @override 
    @abstractmethod
    def init(self) -> None: 
        pass 

    @override
    @abstractmethod
    def broadcast(self, signalID : SignalID, to : ControllerLocations) -> 
