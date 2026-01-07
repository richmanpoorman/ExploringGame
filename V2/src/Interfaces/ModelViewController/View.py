from __future__ import annotations

from typing import Protocol, Literal, Tuple, Optional

from pygame import Surface

from ..HasFeature.Broadcaster import Broadcaster
from ..HasFeature.Listening import Listening
from ..HasFeature.Displayable import Displayable
from ..HasFeature.Interactable import Interactable
from ...Types.Types import SignalID

class View(Broadcaster, Listening, Displayable, Interactable, Protocol):

    def listen(self, signalID: str, *args, **kwargs) -> None: ...

    def broadcast(self, signalID: SignalID, *args, **kwargs) -> None: ...

    def connect(self, listener : Listening) -> None: ...

    def disconnect(self, listener : Listening) -> None: ...

    def surface(self, size: Optional[Tuple[int, int]] = None) -> Surface: ...

    def updateSurface(self, *args, **kwargs) -> None: ...