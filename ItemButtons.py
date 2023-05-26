from Character import Character
from Basics import Stats
from Button import Button
from Inventory import Inventory
from GameState import GameState

class ItemButtons:
    armorButtonList = []
    equipmentButtonList = []
    consumableButtonList = []

    inFightConsumableButtonList = []

    def makeItemButtons(player : Character):
        inventory = player.inventory 
        stats = player.getStats()

        DIMENSIONS  = (170, 12)
        INBETWEEN_X = 10
        INBETWEEN_Y = 1
        CAPTION_HEIGHT = 3
        DESC_HEIGHT = 30
        Y_POS = 50
        ARMOR_X_POS = 10
        EQUIPMENT_X_POS = ARMOR_X_POS + (DIMENSIONS[0] + INBETWEEN_X) 
        CONSUMABLE_X_POS = EQUIPMENT_X_POS + (DIMENSIONS[0] + INBETWEEN_X) 

        def buttonYPosition(index : int) -> int:
            return Y_POS + (DIMENSIONS[1] + INBETWEEN_Y + DESC_HEIGHT + CAPTION_HEIGHT) * index
        def armorFunction(idx : int):
            def buttonFunc():
                inventory.useArmor(idx)
            return buttonFunc

        def weaponFunction(idx : int):
            def buttonFunc():
                inventory.useWeapon(idx)
            return buttonFunc

        def consumableFunction(idx : int, stats : Stats):
            def buttonFunc():
                inventory.useConsumable(idx, stats)
            return buttonFunc
        
        ItemButtons.armorButtonList = [
            Button((ARMOR_X_POS, Y_POS + buttonYPosition(len(inventory.armorList) - idx - 1)), DIMENSIONS, armorFunction(idx), inventory.armorList[idx].name)
            for idx in range(len(inventory.armorList))
        ]
        ItemButtons.equipmentButtonList = [
            Button((EQUIPMENT_X_POS, Y_POS + buttonYPosition(len(inventory.equipmentList) - idx - 1)), DIMENSIONS, weaponFunction(idx), inventory.equipmentList[idx].name)
            for idx in range(len(inventory.equipmentList))
        ]
        ItemButtons.consumableButtonList = [
            Button((CONSUMABLE_X_POS, Y_POS + buttonYPosition(len(inventory.bag) - idx - 1)), DIMENSIONS, consumableFunction(idx, stats), inventory.bag[idx].name)
            for idx in range(len(inventory.bag))
        ]
        
    def itemButtonCheck(mousePosition : tuple, inventory : Inventory) -> None:
        for button in ItemButtons.armorButtonList:
            button.press(mousePosition)
        for button in ItemButtons.equipmentButtonList:
            button.press(mousePosition)
        for button in ItemButtons.consumableButtonList:
            if (button.press(mousePosition)):
                ItemButtons.makeItemButtons(inventory)
    
    def makeConsumableButton(player : Character) -> None:
        stats = player.getStats()
        inventory = player.inventory

        DIMENSIONS  = (170, 12)
        INBETWEEN_Y = 1
        CAPTION_HEIGHT = 3
        DESC_HEIGHT = 30
        Y_POS = 50
        X_POS = (500 - 170) // 2
        def consumableFunction(idx : int, stats : Stats):
            def buttonFunc():
                inventory.useConsumable(idx, stats)
                GameState.setState(GameState.BATTLE_STATE)
            return buttonFunc
        
        def buttonYPosition(index : int) -> int:
            return Y_POS + (DIMENSIONS[1] + INBETWEEN_Y + DESC_HEIGHT + CAPTION_HEIGHT) * index
        ItemButtons.inFightConsumableButtonList = [
            Button((X_POS, Y_POS + buttonYPosition(len(inventory.bag) - idx - 1)), DIMENSIONS, consumableFunction(idx, stats), inventory.bag[idx].name)
            for idx in range(len(inventory.bag))
        ]
    