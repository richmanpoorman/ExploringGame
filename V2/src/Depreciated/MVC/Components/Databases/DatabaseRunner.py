from __future__ import annotations
from pathlib import Path

from ..Interfaces.HasFeature.Runnable import Runnable
from ..Interfaces.ModelViewController.Database import Query, Database

from typing import Any

class DatabaseRunner(Database, Runnable):

    def __init__(self):
        pass 

    # Initialization 
    def init(self) -> None: 
        pass
    
    
    # Running 
    def update(self) -> None: 
        pass 

    # Clean up
    def close(self) -> None: 
        pass 

    def get(self, query : Query, *args, **kwargs) -> Any: 
        raise ValueError('The get query {query} either doesn\'t exist or doesn\'t work with args: {args} and kwargs: {kwargs}')

    def set(self, query : Query, *args, **kwargs) -> Any: 
        raise ValueError('The set query {query} either doesn\'t exist or doesn\'t work with args: {args} and kwargs: {kwargs}')
    
    def importData(self, filepath: Path) -> None:
        pass
    
    def exportData(self, filepath: Path) -> None:
        pass