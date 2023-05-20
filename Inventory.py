from Item import Item 
from Basics import Stats
from Equipment import Equipment
from Armor import Armor

class Inventory:
    
    def __init__(self):
        self.equipmentList = [Equipment(name = "Basic", physical = 1, magic = 1)]
        self.equipment = self.equipmentList[0]

        self.armorList = [Armor(mpResistance = 0, physicalResistance = 0)]
        self.armor = self.armorList[0]
        
        self.bag = list() 
        
        # CONSUMABLES
    # Uses and removes consumable in the bag
    def useItem(self, index : int, playerStats : Stats) -> None:
        item = self.bag.pop(index)
        playerStats.changeHp(item.hp)
        playerStats.changeMp(item.mp)

    # Adds the item to the bag
    def addItem(self, item : Item) -> None:
        self.bag.append(item)    

        # EQUIPMENT
    def equip(self, index : int) -> None:
        self.equipment = self.equipmentList[index]
    
    def addEquipment(self, item : Equipment) -> None:
        self.equipmentList.append(item)