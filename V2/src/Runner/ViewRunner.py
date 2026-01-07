from __future__ import annotations

from typing import Literal, Optional, Tuple

from ..Interfaces.ModelViewController.View import View
from ..Interfaces.ModelViewController.ViewManager import ViewManager
from ..Interfaces.ModelViewController.ControllerManager import ControllerManager

from ..Interfaces.HasFeature.Broadcaster import Broadcaster
from ..Interfaces.HasFeature.Listening import Listening

from ..Types.Types import SignalID, ModelViewControllerData

from ..System.LocalBroadcaster import LocalBroadcaster
from ..System.LocalListener import LocalListener

from pygame import Surface
from pygame.event import Event

from ovld import ovld as overload

class ViewRunner(ViewManager):

    __view : View 

    __toViewBroadcaster       : Broadcaster
    __toControllerBroadcaster : Broadcaster 

    __fromViewListener       : Listening 
    __fromControllerListener : Listening


    def __init__(self) -> None:
        pass
    
    def init(self, initialView : View, controllerManager: ControllerManager) -> None: 
        self.__view = initialView

        self.__toViewBroadcaster       = LocalBroadcaster() 
        self.__toControllerBroadcaster = LocalBroadcaster()

        self.__fromControllerListener = LocalListener() 
        self.__fromViewListener       = LocalListener() 

        controllerManager.connect(self.__fromControllerListener, origin="view")
        self.__view.connect(self.__fromViewListener)


    def update(self, *args, **kwargs) -> None: 
        self.updateSurface(*args, **kwargs)

    def close(self) -> None: 
        pass 

    @overload 
    def listen(self, signalID : Literal["change_view"], modelViewController : ModelViewControllerData) -> None: 
        self.setView(modelViewController.view)

    @overload 
    def listen(self, signalID : SignalID, to : Literal["controller"], *args, **kwargs) -> None: 
        self.broadcast(signalID, to="controller", *args, **kwargs)

    @overload
    def listen(self, signalID : SignalID, to : Literal["view"], *args, **kwargs) -> None: 
        self.__fromViewListener.listen(signalID, to="view", *args, **kwargs)

    def listen(self, signalID : SignalID, *args, **kwargs) -> None: 
        raise ValueError("Expected either a 'change_view' signal ID with a modelViewController assigned a ModelViewControllerData or to have 'to' argument be assigned to 'controller' or 'view'")

    @overload
    def broadcast(self, signalID : SignalID , to : Literal["view"], *args, **kwargs) -> None: 
        self.__toViewBroadcaster.broadcast(signalID, *args, **kwargs) 

    @overload
    def broadcast(self, signalID : SignalID, to : Literal["controller"], *args, **kwargs) -> None: 
        self.__toControllerBroadcaster.broadcast(signalID, *args, **kwargs) 

    def broadcast(self, signalID: SignalID, *args, **kwargs) -> None:
        raise ValueError("The broadcast doesn't have a destination to be sent to: set 'to' field to 'view' or 'controller'")

    def connect(self, listener: Listening) -> None:
        self.__toControllerBroadcaster.connect(listener)

    def disconnect(self, listener: Listening) -> None:
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
     
    def surface(self, size : Optional[Tuple[int, int]] = None) -> Surface: 
        return self.__view.surface(size)
    
    def updateSurface(self, *args, **kwargs) -> None:
        self.__view.updateSurface(self, *args, **kwargs)

    def onEvent(self, event : Event) -> None: 
        self.__view.onEvent(event)