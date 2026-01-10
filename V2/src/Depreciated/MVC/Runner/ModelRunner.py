from __future__ import annotations

from typing import Literal

from ovld import ovld as overload

from ..Interfaces.ModelViewController.Model import Model
from ..Interfaces.ModelViewController.ModelManager import ModelManager
from ..Interfaces.ModelViewController.ControllerManager import ControllerManager

from ..Interfaces.HasFeature.Listening import Listening
from ..Interfaces.HasFeature.Broadcaster import Broadcaster
from ..System.LocalBroadcaster import LocalBroadcaster
from ..System.LocalListener import LocalListener

from ..Types.Types import SignalID, ModelViewControllerData

class ModelRunner(ModelManager):

    __model : Model

    __toModelBroadcaster      : Broadcaster
    __toControllerBroadcaster : Broadcaster 

    __fromModelListener      : Listening 
    __fromControllerListener : Listening

    def __init__(self) -> None:
        pass

    def init(self, initialModel : Model, controllerBroadcaster : ControllerManager) -> None:
        self.__model = initialModel

        self.__fromModelListener      = LocalListener() 
        self.__fromControllerListener = LocalListener() 

        self.__toModelBroadcaster      = LocalBroadcaster()
        self.__toControllerBroadcaster = LocalBroadcaster()

        controllerBroadcaster.connect(self.__fromControllerListener, origin="model")
        self.__model.connect(self.__fromModelListener) 
    

    def update(self) -> None: 
        pass 

    def close(self) -> None: 
        pass

    # Receivers

    @overload
    def listen(self, signalID : Literal["change_model"], modelViewController : ModelViewControllerData) -> None: 
        self.setModel(modelViewController.model)
        self.broadcast("change_controller", to="controller", modelViewController=modelViewController)

    @overload
    def listen(self, signalID : SignalID, to : Literal["model"], *args, **kwargs) -> None: 
        self.broadcast(signalID, to="model", *args, **kwargs)

    @overload
    def listen(self, signalID : SignalID, to : Literal["controller"], *args, **kwargs) -> None: 
        self.broadcast(signalID, to="controller", *args, **kwargs)

    
    def listen(self, signalID : SignalID, *args, **kwargs) -> None: 
        raise ValueError("Expected a 'change_model' signal with a ModelViewControllerData, or the 'to' field to be set to 'model' or 'controller'")

    # Broadcasts
    @overload
    def broadcast(self, signalID : SignalID, to : Literal["model"], *args, **kwargs) -> None: 
        self.__toModelBroadcaster.broadcast(signalID, *args, **kwargs)

    @overload
    def broadcast(self, signalID : SignalID, to : Literal["controller"], *args, **kwargs) -> None: 
        self.__toControllerBroadcaster.broadcast(signalID, *args, **kwargs)


    def broadcast(self, signalID : SignalID, *args, **kwargs) -> None: 
        raise ValueError("The broadcast doesn't have a destination to be sent to: set 'to' field to 'model' or 'controller'")
    
    def connect(self, listener : Listening) -> None: 
        self.__toControllerBroadcaster.connect(listener) 

    def disconnect(self, listener : Listening) -> None: 
        self.__toControllerBroadcaster.disconnect(listener)

    # Set the Model value
    def setModel(self, model : Model) -> None: 
        self.__model.disconnect(self.__fromModelListener) 
        self.__toModelBroadcaster.disconnect(self.__model)
        self.__model = model 
        self.__model.connect(self.__fromModelListener) 
        self.__toModelBroadcaster.connect(self.__model)

    @property
    def model(self) -> Model: 
        return self.__model