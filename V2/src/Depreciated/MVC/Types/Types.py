from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING: 
    from ..Interfaces.ModelViewController.Controller import Controller 
    from ..Interfaces.ModelViewController.Model import Model 
    from ..Interfaces.ModelViewController.View import View

type SignalID = str

@dataclass
class ModelViewControllerData: 
    '''
        Represents the package of the model, view, and controller 
        that work together, and are run together 
    '''
    model      : Model
    view       : View 
    controller : Controller 
