from typing import Literal

from ovld import OvldBase as Overloadable 

from ...Data.Data import Data

class MapLogic(Overloadable):

    def __init__(self):
        pass

    def handle(command : Literal["move"], data : Data, direction : Literal["up", "down", "left", "right"]) -> None: 
        pass 

    def handle(command : str, data : Data, *args, **kwargs) -> None: 
        raise RuntimeError(f"Handle Command '{command}' not found, with args: {args} and kwargs: {kwargs}")
    
    def get(command : str, data : Data, *args, **kwargs) -> None: 
        raise RuntimeError(f"Get Command '{command}' not found, with args: {args} and kwargs: {kwargs}")