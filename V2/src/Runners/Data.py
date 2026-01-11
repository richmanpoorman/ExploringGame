from dataclasses import dataclass

from typing import TYPE_CHECKING

if TYPE_CHECKING: 
    from ..GameStates.MapExploration.Map.MapData import MapData

@dataclass
class Data: 
    mapData : MapData 
