from typing import Protocol, Any

from ...Runners.Data import Data

class Logic(Protocol): 
    def handle(command : str, data : Data, *args, **kwargs) -> None: ...

    def get(command : str, data : Data, *args, **kwargs) -> Any: ...