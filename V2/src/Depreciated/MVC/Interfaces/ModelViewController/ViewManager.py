from __future__ import annotations

from abc import ABC as Interfac
from ..HasFeature.Listening import Listening
from ..HasFeature.Broadcaster import Broadcaster
from ..HasFeature.Runnable import Runnable
from ..HasFeature.Displayable import Displayable
from ..HasFeature.Interactable import Interactable

from ..ModelViewController.View import View

from ...Types.Types import SignalID

from pygame import Surface

from typing import Optional, Tuple, Protocol

class ViewManager(Listening, Broadcaster, Runnable, Displayable, Interactable, Protocol):
    def init(self, *args, **kwargs) -> None: ... 

    def update(self) -> None: ...

    def close(self) -> None: ...

    def listen(self, signalID: str, *args, **kwargs) -> None: ...

    def broadcast(self, signalID: SignalID, *args, **kwargs) -> None: ...

    def connect(self, listener : Listening) -> None: ...

    def disconnect(self, listener : Listening) -> None: ...

    def surface(self, size: Optional[Tuple[int, int]] = None) -> Surface: ...

    def updateSurface(self, *args, **kwargs) -> None: ...

    def setView(self, view : View) -> None: ...

    def view(self) -> View: ...