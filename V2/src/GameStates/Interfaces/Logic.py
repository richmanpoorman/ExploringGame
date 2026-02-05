from typing import Protocol, Any

from ...Data.Data import Data

from .Context import Context

class Logic(Protocol): 
    
    def setContext(self, context : Context) -> None: ... 
    
    def handle(command : str, *args, **kwargs) -> None: ...

    def get(command : str, *args, **kwargs) -> Any: ...