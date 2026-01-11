from typing import Literal

from ovld import OvldBase as Overloadable 

from ...Runners.Data import Data

class MapLogic(Overloadable):

    def __init__(self, data : Data):
        self.data = data

    def handle(command : Literal["move"], direction : Literal["up", "down", "left", "right"]) -> None: 
        pass 

    def handle(command : str, *args, **kwargs) -> None: 
        raise RuntimeError(f"Handle Command '{command}' not found, with args: {args} and kwargs: {kwargs}")
    
    def get(command : str, *args, **kwargs) -> None: 
        raise RuntimeError(f"Get Command '{command}' not found, with args: {args} and kwargs: {kwargs}")