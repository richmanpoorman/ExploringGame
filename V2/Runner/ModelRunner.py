

from typing import Literal, override

from Interfaces.ModelViewController.Model import Model
from Interfaces.HasFeature.Runnable import Runnable


from Interfaces.HasFeature.Listening import Listening
from Interfaces.HasFeature.Broadcaster import Broadcaster
from System.LocalBroadcaster import LocalBroadcaster
from System.LocalListener import LocalListener

from Types.Types import SignalID, ModelViewControllerData

class ModelRunner(Listening, Broadcaster, Runnable):

    __model : Model

    __toModelBroadcaster      : Broadcaster
    __toControllerBroadcaster : Broadcaster 

    __fromModelListener      : Listening 
    __fromControllerListener : Listening

    def __init__(self) -> None:
        pass

    def init(self, initialModel : Model, controllerBroadcaster : Broadcaster) -> None:
        self.__model = initialModel

        self.__fromModelListener      = LocalListener() 
        self.__fromControllerListener = LocalListener() 

        self.__toModelBroadcaster      = LocalBroadcaster()
        self.__toControllerBroadcaster = LocalBroadcaster()

        controllerBroadcaster.connect(self.__fromControllerListener)
        self.__model.connect(self.__fromModelListener) 

    def update(self) -> None: 
        pass 

    def close(self) -> None: 
        pass

    @override
    def listen(self, signalID : SignalID, *args, **kwargs) -> None:
        match (signalID, kwargs):
            case ("change_model", {"modelViewController" : mvc, **rest}):
                modelViewController : ModelViewControllerData = mvc
                self.setModel(modelViewController.model)
                self.broadcast("change_controller", to="controller", modelViewController=modelViewController, *args, **rest)
            case (_, {"to" : "controller", **rest}):
                self.broadcast(signalID, to="controller", *args, **rest)
            case (_, {"to" : "model", **rest}):
                self.broadcast(signalID, to="model", *args, **rest) 
            case _: 
                raise NotImplementedError("Expected either a 'change_view' signal ID with a modelViewController assigned a ModelViewControllerData or to have 'to' argument be assigned to 'controller' or 'model'")

    @override
    def broadcast(self, signalID : SignalID, *args, **kwargs) -> None: 
        match kwargs: 
            case {"to" : "model", **rest}:
                self.__toModelBroadcaster.broadcast(signalID, *args, **rest)
            case {"to" : "controller", **rest}:
                self.__toControllerBroadcaster.broadcast(signalID, *args, **rest)
            case _:
                raise NotImplementedError("The broadcast doesn't have a destination to be sent to: set 'to' field to 'model' or 'controller'")
            
    @override
    def connect(self, listener : Listening) -> None: 
        self.__toControllerBroadcaster.connect(listener)
    
    @override
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