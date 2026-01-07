from __future__ import annotations
from pathlib import Path
from typing import Any, Optional

from ..Interfaces.ModelViewController.Database import Query, Database

class GlobalDatabase(Database):
    '''
        A database where every instance of the database actually acceses the 
        same database ( aka the database is a singleton )
    '''

    __instance : Optional[GlobalDatabase] = None 

    def __new__(cls):
        if cls.__instance is None: 
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self): 
        pass 

    def get(self, query : Query, *args, **kwargs) -> Any: 
        raise ValueError('The get query {query} either doesn\'t exist or doesn\'t work with args: {args} and kwargs: {kwargs}')

    def set(self, query : Query, *args, **kwargs) -> Any: 
        raise ValueError('The set query {query} either doesn\'t exist or doesn\'t work with args: {args} and kwargs: {kwargs}')
    
    def importData(self, filepath: Path) -> None:
        pass
    
    def exportData(self, filepath: Path) -> None:
        pass