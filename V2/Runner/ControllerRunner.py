from __future__ import annotations

from typing import Literal, override

from Interfaces.ModelViewController.Controller import Controller

from Interfaces.HasFeature.Listening import Listening
from Interfaces.HasFeature.Broadcaster import Broadcaster
from Interfaces.HasFeature.Runnable import Runnable

from Types.Types import ModelViewControllerData, SignalID

from System.LocalBroadcaster import LocalBroadcaster
from System.LocalListener import LocalListener



class ControllerRunner(Listening, Broadcaster, Runnable):
    
    '''
    The controller sits between the model and the view, taking input and 
    translating to the model
    '''
    # What 'translation' to use to transfer information from the view to the model
    __controller : Controller  

    __controllerBroadcaster : Broadcaster
    __modelBroadcaster      : Broadcaster 
    __viewBroadcaster       : Broadcaster

    __controllerListener    : Listening
    __modelListener         : Listening
    __viewListener          : Listening

    def __init__(self) -> None:
        pass
    
    @override
    def init(self, initialController : Controller, modelBroadcaster : Broadcaster, viewBroadcaster : Broadcaster) -> None:
        self.__controller  = initialController

        self.__controllerBroadcaster = LocalBroadcaster()
        self.__modelBroadcaster      = LocalBroadcaster()
        self.__viewBroadcaster       = LocalBroadcaster()

        self.__controllerListener    = LocalListener()
        self.__controller.connect(self.__controllerListener)

        self.__modelListener         = LocalListener()
        modelBroadcaster.connect(self.__modelListener)

        self.__viewListener          = LocalListener()
        viewBroadcaster.connect(self.__viewListener)
    
    def update(self) -> None: 
        pass 

    def close(self) -> None: 
        pass

    @override
    def listen(self, signalID : SignalID, *args, **kwargs) -> None: 
        match (signalID, kwargs):
            case ("change_controller", {"modelViewController" : mvc, **rest}):
                modelViewController : ModelViewControllerData = mvc
                self.setController(modelViewController.controller)
                self.broadcast("change_view", to="view", modelViewController=modelViewController, *args, **rest)
            case (_, {"to" : "view", **rest}):
                self.broadcast(signalID, to="view", *args, **rest)
            case (_, {"to" : "model", **rest}):
                self.broadcast(signalID, to="model", *args, **rest)
            case (_, {"to" : "controller", **rest}):
                self.broadcast(signalID, to="controller", *args, **rest)
            case _: 
                raise NotImplementedError("Expected either a 'change_view' signal ID with a modelViewController assigned a ModelViewControllerData or to have 'to' argument be assigned to 'controller', 'view', or 'model'")

    @override
    def broadcast(self, signalID : SignalID, *args, **kwargs) -> None:
        match kwargs: 
            case {"to" : "view", **rest}:
                self.__viewBroadcaster.broadcast(signalID, *args, **rest)
            case {"to" : "controller", **rest}:
                self.__controllerBroadcaster.broadcast(signalID, *args, **rest)
            case {"to" : "model", **rest}:
                self.__modelBroadcaster.broadcast(signalID, *args, **rest)
            case _:
                raise NotImplementedError("The broadcast doesn't have a destination to be sent to: set 'to' field to 'model', 'controller', or 'view'")

    @override
    def connect(self, listener : Listening, origin : Literal["view", "model"]) -> None: 
        match origin: 
            case "view":
                self.__viewBroadcaster.connect(listener)
            case "model":
                self.__modelBroadcaster.connect(listener)
    
    @override
    def disconnect(self, listener : Listening, origin : Literal["view", "model"]) -> None: 
        match origin: 
            case "view":
                self.__viewBroadcaster.disconnect(listener)
            case "model":
                self.__modelBroadcaster.disconnect(listener)
    
    # Set the controller value
    def setController(self, controller : Controller) -> None: 
        self.__controller.disconnect(self.__controllerListener)
        self.__controllerBroadcaster.disconnect(self.__controller)
        self._controller = controller 
        self.__controller.connect(self.__controllerListener)
        self.__controllerBroadcaster.connect(self.__controller)
        
    @property
    def controller(self) -> Controller: 
        return self._controller