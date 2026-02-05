from .Map.MapData import MapData
from .Stats.PlayerStats import PlayerStats
class Data: 

    def __init__(self):
        self.mapData = MapData()
        self.playerStats = PlayerStats() 