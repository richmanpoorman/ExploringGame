from __future__ import annotations

from ...Types.Types import SignalID

from typing import Protocol

class Listening(Protocol):

    def listen(self, signalID : SignalID, *args, **kwargs) -> None: ... 
