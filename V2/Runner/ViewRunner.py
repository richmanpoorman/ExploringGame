

from typing import override

from Interfaces.ModelViewController.View import View
from Interfaces.HasFeature.Runnable import Runnable

from Types.Types import SignalID, ModelViewControllerData

from Interfaces.HasFeature.Listening import Listening
from Interfaces.HasFeature.Broadcaster import Broadcaster

from System.LocalBroadcaster import LocalBroadcaster
from System.LocalListener import LocalListener

class ViewRunner(Listening, Broadcaster, Runnable):

    __view : View 

    __toViewBroadcaster       : Broadcaster
    __toControllerBroadcaster : Broadcaster 

    __fromViewListener       : Listening 
    __fromControllerListener : Listening


    def __init__(self) -> None:
        pass
    
    def init(self, initialView : View, controllerBroadcaster: Broadcaster) -> None: 
        self.__view = initialView

        self.__toViewBroadcaster       = LocalBroadcaster() 
        self.__toControllerBroadcaster = LocalBroadcaster()

        self.__fromControllerListener = LocalListener() 
        self.__fromViewListener       = LocalListener() 

        controllerBroadcaster.connect(self.__fromControllerListener)
        self.__view.connect(self.__fromViewListener)


    def update(self) -> None: 
        pass 

    def close(self) -> None: 
        pass 

    def listen(self, signalID : SignalID, *args, **kwargs) -> None: 
        match (signalID, kwargs):
            case ("change_view", {"modelViewController" : mvc, **rest}):
                modelViewController : ModelViewControllerData = mvc 
                self.setView(modelViewController.view)
            case (_, {"to" : "controller", **rest}):
                self.broadcast(signalID, to="controller", *args, **rest)
            case (_, {"to" : "view", **rest}):
                self.__fromViewListener.listen(signalID, to="view", *args, **rest)
            case _:
                raise NotImplementedError("Expected either a 'change_view' signal ID with a modelViewController assigned a ModelViewControllerData or to have 'to' argument be assigned to 'controller' or 'view'")

    @override
    def broadcast(self, signalID: SignalID, *args, **kwargs) -> None:
        match kwargs: 
            case {"to" : "view", **rest}:
                self.__toViewBroadcaster.broadcast(signalID, *args, **rest)
            case {"to" : "controller", **rest}:
                self.__toControllerBroadcaster.broadcast(signalID, *args, **rest)
            case _:
                raise NotImplementedError("The broadcast doesn't have a destination to be sent to: set 'to' field to 'view' or 'controller'")

    @override
    def connect(self, listener: Listening) -> None:
        self.__toControllerBroadcaster.connect(listener)

    @override
    def disconnect(self, listener: Listening, *args, **kwargs) -> None:
        self.__toControllerBroadcaster.disconnect(listener) 

    def setView(self, view : View) -> None: 
        self.__view.disconnect(self.__fromViewListener) 
        self.__toViewBroadcaster.disconnect(self.__view)
        self.__view = view 
        self.__view.connect(self.__fromViewListener) 
        self.__toViewBroadcaster.connect(self.__view)

    @property 
    def view(self) -> View: 
        return self.__view