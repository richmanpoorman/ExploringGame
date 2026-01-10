from __future__ import annotations

from typing import Protocol

class Runnable(Protocol):

    def init(self, *args, **kwargs) -> None: ...

    def update(self) -> None: ...

    def close(self) -> None: ...