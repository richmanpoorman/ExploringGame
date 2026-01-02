from Consumable import Consumable 
from Basics import Stats
from Equipment import Equipment
from Armor import Armor

class Inventory:
    
    def __init__(self):
        self.money = 0

        self.equipmentList = [Equipment(name = "Basic", physical = 1, magic = 1)]
        self.equipment = self.equipmentList[0]

        self.armorList = [Armor(mpResistance = 0, physicalResistance = 0)]
        self.armor = self.armorList[0]
        
        self.bag = list() 
        
        # CONSUMABLES
    # Uses and removes consumable in the bag
    def useConsumable(self, index : int, playerStats : Stats) -> None:
        item = self.bag.pop(index)
        playerStats.changeHp(item.recover[0])
        playerStats.changeMp(item.recover[1])

    # Adds the item to the bag
    def addConsumable(self, item : Consumable) -> None:
        self.bag.append(item)    

        # EQUIPMENT
    def useWeapon(self, index : int) -> None:
        self.equipment = self.equipmentList[index]
    
    def addEquipment(self, item : Equipment) -> None:
        self.equipmentList.append(item)

    def useArmor(self, index : int) -> None:
        self.armor = self.armorList[index]
    
    def addArmor(self, item : Equipment) -> None:
        self.armorList.append(item)
    
    def useMoney(self, amount : int) -> bool:
        if (amount > self.money):
            return False 
        self.money -= amount
        return True
    
    def addMoney(self, amount : int) -> None:
        self.money += amount