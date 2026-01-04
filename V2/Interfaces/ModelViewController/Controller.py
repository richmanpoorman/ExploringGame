from abc import ABC as Interface, abstractmethod
from typing import override, Literal
from Interfaces.HasFeature.Runnable import Runnable
from Interfaces.HasFeature.Broadcaster import Broadcaster
from Interfaces.HasFeature.Listening import Listening
from Types.Types import SignalID

type ControllerLocations = Literal["model", "view"]

class Controller(Runnable, Broadcaster, Listening, Interface):
    @override 
    @abstractmethod
    def init(self) -> None: 
        pass 

    @override
    @abstractmethod
    def broadcast(self, to : ControllerLocations, signalID : SignalID, *args, **kwargs) -> None:
        pass