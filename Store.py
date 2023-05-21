from Armor import Armor
from Equipment import Equipment
from Consumable import Consumable
from ItemNameGenerator import ItemNameGenerator
from random import randint
from typing import Tuple
from Inventory import Inventory
class Store:
    
    def __init__(self):
        self.armorStock      = [None for i in range(5)]
        self.armorCosts      = [0    for i in range(5)]
        self.equipmentStock  = [None for i in range(5)]
        self.equipmentCosts  = [0    for i in range(5)]
        self.consumableStock = [None for i in range(5)]
        self.consumableCosts = [0    for i in range(5)]
        # self.restock(lvl)

    # How the values of the 
    def getStatSplit(valueLevel : int, lvl : int = 1) -> Tuple[int, int, int]:
        TOTAL_RANGE = 10

        startValue = TOTAL_RANGE * (lvl - 1 + valueLevel)
        netValue = startValue + randint(0, TOTAL_RANGE * (valueLevel + 1))

        split = randint(-netValue, 2 * netValue)
        otherSide = netValue - split

        cost  = (valueLevel + 1) * netValue

        return (split, otherSide, cost)

    def restock(self, lvl : int = 1) -> None:
        
        armorNames      = ItemNameGenerator(itemListFilePath = 'ArmorTypes.txt')
        equipmentNames  = ItemNameGenerator(itemListFilePath = 'WeaponTypes.txt')
        consumableNames = ItemNameGenerator(itemListFilePath = 'ConsumableTypes.txt')

        for i in range(5):
            
            if self.armorStock[i] == None:
                physical, magical, cost = Store.getStatSplit(i, lvl)
                self.armorStock[i] = Armor(name = armorNames.generateName(), physicalResistance = physical, mpResistance = magical)
                self.armorCosts[i] = cost

            if self.equipmentStock[i] == None: 
                physical, magical, cost = Store.getStatSplit(i, lvl)
                mpCost = max(0, magical // (i + 1 + randint(0, lvl)))
                self.equipmentStock[i] = Equipment(name = equipmentNames.generateName(), physical = physical, magic = magical, mpCost = mpCost)
                self.equipmentCosts[i] = cost

            if self.consumableStock[i] == None:
                physical, magical, cost = Store.getStatSplit(i, lvl)
                self.consumableStock[i] = Consumable(name = consumableNames.generateName(), hp = physical, mp = magical)
                self.consumableCosts[i] = cost

    def buyArmor(self, index : int, inventory : Inventory):
        if not inventory.useMoney(self.armorCosts[index]):
            print("No Money")
            return 
        inventory.addArmor(self.armorStock[index])
        self.armorStock[index] = None 
        self.armorCosts[index] = 0
    
    def buyEquipment(self, index : int, inventory : Inventory):
        if not inventory.useMoney(self.equipmentCosts[index]):
            print("No Money")
            return 
        inventory.addEquipment(self.equipmentStock[index])
        self.equipmentStock[index] = None 
        self.equipmentCosts[index] = 0

    def buyConsumable(self, index : int, inventory : Inventory):
        if not inventory.useMoney(self.consumableCosts[index]):
            print("No Money")
            return 
        inventory.addConsumable(self.consumableStock[index])
        self.consumableStock[index] = None 
        self.consumableStock[index] = 0
# TEST

# testStore = Store() 
# testStore.restock()

# print("ARMOR:")
# for armor in zip(testStore.armorStock, testStore.armorCosts):
#     print(armor)

# print("EQUIPMENT:")
# for equipment in zip(testStore.equipmentStock, testStore.equipmentCosts):
#     print(equipment)

# print("CONSUMABLE:")
# for consumable in zip(testStore.consumableStock, testStore.consumableCosts):
#     print(consumable)

# testInventory = Inventory()
# testInventory.addMoney(1)
# testStore.buyArmor(1, testInventory)
# for armor in zip(testStore.armorStock, testStore.armorCosts):
#     print(armor)
# print()
# testInventory.addMoney(10000000000)
# testStore.buyArmor(1, testInventory)
# for armor in zip(testStore.armorStock, testStore.armorCosts):
#     print(armor)