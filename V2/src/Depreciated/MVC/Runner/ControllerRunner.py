from __future__ import annotations

from typing import Literal

from ovld import ovld as overload

from ..Interfaces.ModelViewController.Controller import Controller
from ..Interfaces.ModelViewController.ControllerManager import ControllerManager


from ..Interfaces.HasFeature.Listening import Listening
from ..Interfaces.HasFeature.Broadcaster import Broadcaster
from ..Interfaces.ModelViewController.ViewManager import ViewManager
from ..Interfaces.ModelViewController.ModelManager import ModelManager

from ..Types.Types import ModelViewControllerData, SignalID

from ..System.LocalBroadcaster import LocalBroadcaster
from ..System.LocalListener import LocalListener


class ControllerRunner:
    
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
    
    def init(self, initialController : Controller, modelManager : ModelManager, viewManager : ViewManager) -> None:
        self.__controller  = initialController

        self.__controllerBroadcaster = LocalBroadcaster()
        self.__modelBroadcaster      = LocalBroadcaster()
        self.__viewBroadcaster       = LocalBroadcaster()

        self.__controllerListener    = LocalListener()
        self.__controller.connect(self.__controllerListener)

        self.__modelListener         = LocalListener()
        modelManager.connect(self.__modelListener)

        self.__viewListener          = LocalListener()
        viewManager.connect(self.__viewListener)
    
    def update(self) -> None: 
        pass 

    def close(self) -> None: 
        pass

    @overload 
    def listen(self, signalID : Literal["change_controller"], modelViewController : ModelViewControllerData) -> None: 
        self.setController(modelViewController.controller)
        self.broadcast("change_view", to="view", modelViewController=modelViewController)

    @overload 
    def listen(self, signalID : SignalID, to : Literal["view"], *args, **kwargs) -> None: 
        self.broadcast(signalID, to="view", *args, **kwargs)

    @overload 
    def listen(self, signalID : SignalID, to : Literal["model"], *args, **kwargs) -> None: 
        self.broadcast(signalID, to="model", *args, **kwargs)

    @overload 
    def listen(self, signalID : SignalID , to : Literal["controller"], *args, **kwargs) -> None: 
        self.broadcast(signalID, to="controller", *args, **kwargs)

    def listen(self, signalID : SignalID, *args, **kwargs) -> None: 
        raise ValueError("Expected either a 'change_view' signal ID with a modelViewController assigned a ModelViewControllerData or to have 'to' argument be assigned to 'controller', 'view', or 'model'")

    @overload
    def broadcast(self, signalID : SignalID, to : Literal["view"], *args, **kwargs) -> None: 
        self.__viewBroadcaster.broadcast(signalID, *args, **kwargs)

    @overload 
    def broadcast(self, signalID : SignalID, to : Literal["controller"], *args, **kwargs) -> None: 
        self.__controllerBroadcaster.broadcast(signalID, *args, **kwargs)

    @overload 
    def broadcast(self, signalID : SignalID, to : Literal["model"], *args, **kwargs) -> None: 
        self.__modelBroadcaster.broadcast(signalID, *args, **kwargs)

    def broadcast(self, signalID : SignalID, *args, **kwargs) -> None:
        raise ValueError("The broadcast doesn't have a destination to be sent to: set 'to' field to 'model', 'controller', or 'view'")

    @overload
    def connect(self, listener : Listening, origin : Literal["view"]) -> None: 
        self.__viewBroadcaster.connect(listener)

    @overload 
    def connect(self, listener : Listening, origin : Literal["model"]) -> None: 
        self.__modelBroadcaster.connect(listener)

    def connect(self, listener : Listening, *args, **kwargs) -> None: 
        raise ValueError("Expected to connect with only the 'origin' parameter being 'view' or 'model'")
                    
    @overload 
    def disconnect(self, listener : Listening, origin : Literal["view"]) -> None: 
        self.__viewBroadcaster.disconnect(listener)

    @overload 
    def disconnect(self, listener : Listening, origin : Literal["model"]) -> None: 
        self.__modelBroadcaster.disconnect(listener)

    def disconnect(self, listener : Listening, *args, **kwargs) -> None: 
        raise ValueError("Expected to disconnect with only the 'origin' parameter being 'view' or 'model'")
    
    
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