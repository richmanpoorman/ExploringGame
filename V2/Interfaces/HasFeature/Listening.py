from __future__ import annotations

from abc import ABC as Interface, abstractmethod
from typing import Callable

from Types.Types import SignalID


class Listening(Interface):

    @abstractmethod 
    def listen(self, signalID : SignalID, *args, **kwargs) -> None:
        pass
