from __future__ import annotations


from typing import Any, Protocol

from pathlib import Path

type Query = str 

class Database(Protocol):
    
    def get(self, query : Query, *args, **kwargs) -> Any: ...

    def set(self, query : Query, *args, **kwargs) -> Any: ...

    def exportData(self, filepath : Path) -> None: ...

    def importData(self, filepath : Path) -> None: ...