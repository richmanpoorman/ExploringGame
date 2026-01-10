from __future__ import annotations

from typing import Protocol
from pygame.event import Event

class Interactable(Protocol):

    def onEvent(self, event : Event) -> None: ...