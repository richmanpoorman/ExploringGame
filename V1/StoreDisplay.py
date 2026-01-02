import pygame as py

from Store import Store
from Button import Button
from Inventory import Inventory
from GameState import GameState

class StoreDisplay:
    DIMENSIONS  = (150, 15)
    INBETWEEN_X = 10
    INBETWEEN_Y = 5
    CAPTION_HEIGHT = 3
    DESC_HEIGHT = 50
    Y_POS = 20
    ARMOR_X_POS = 10
    EQUIPMENT_X_POS = ARMOR_X_POS + (DIMENSIONS[0] + INBETWEEN_X) 
    CONSUMABLE_X_POS = EQUIPMENT_X_POS + (DIMENSIONS[0] + INBETWEEN_X) 
    PLAYER_INVENTORY : Inventory = None
    def leaveStore() -> None:
        GameState.setState(GameState.EXPLORE_STATE)
    LEAVE_BUTTON = Button((200, 400), (100, 50), leaveStore, "Leave")


    def setup(store : Store):
        StoreDisplay.store             = store
        StoreDisplay.armorButtons      = [Button((StoreDisplay.ARMOR_X_POS, StoreDisplay.buttonYPosition(i)), \
                                         StoreDisplay.DIMENSIONS, StoreDisplay.armorButtonMaker(i), store.armorStock[i].name)      for i in range(5)] 
        StoreDisplay.equipmentButtons  = [Button((StoreDisplay.EQUIPMENT_X_POS, StoreDisplay.buttonYPosition(i)), \
                                         StoreDisplay.DIMENSIONS, StoreDisplay.equipmentButtonMaker(i), store.equipmentStock[i].name)  for i in range(5)]
        StoreDisplay.consumableButtons = [Button((StoreDisplay.CONSUMABLE_X_POS, StoreDisplay.buttonYPosition(i)), \
                                         StoreDisplay.DIMENSIONS, StoreDisplay.consumableButtonMaker(i), store.consumableStock[i].name) for i in range(5)]

    

    def buttonDisplay(screen : py.Surface, font : py.font, bgColor : tuple = (255, 255, 255)):
        StoreDisplay.LEAVE_BUTTON.drawButton(screen, font, bgColor)

        moneyText = font.render("Money: " + str(StoreDisplay.PLAYER_INVENTORY.money), True, (0, 0, 0))
        moneyBox  = py.Surface((150, 15), py.SRCALPHA)
        moneyBox.blit(moneyText, (1, 1))
        py.draw.rect(screen, bgColor, py.Rect(10, 400, 150, 15))
        screen.blit(moneyBox, (10, 400))

        armorText = font.render("ARMOR", True, (0, 0, 0))
        armorBox  = py.Surface((StoreDisplay.DIMENSIONS[0], StoreDisplay.DIMENSIONS[1]), py.SRCALPHA)
        armorBox.blit(armorText, (1, 1))
        py.draw.rect(screen, bgColor, py.Rect(StoreDisplay.ARMOR_X_POS, StoreDisplay.Y_POS - StoreDisplay.DIMENSIONS[1] - StoreDisplay.CAPTION_HEIGHT, StoreDisplay.DIMENSIONS[0], StoreDisplay.DIMENSIONS[1]))
        screen.blit(armorBox, (StoreDisplay.ARMOR_X_POS, StoreDisplay.Y_POS - StoreDisplay.DIMENSIONS[1] - StoreDisplay.CAPTION_HEIGHT))

        for button, item, cost in zip(StoreDisplay.armorButtons, StoreDisplay.store.armorStock, StoreDisplay.store.armorCosts):
            button.drawButton(screen, font, bgColor)
            if (item == None):
                continue
            hpText   = font.render("HP RES: " + str(item.resistance[0]), True, (100, 100, 100))
            mpText   = font.render("MP RES: " + str(item.resistance[1]), True, (100, 100, 100))
            costText = font.render("COST: " + str(cost), True, (100, 100, 100))
            textBox  = py.Surface((button.dimensions[0], StoreDisplay.DESC_HEIGHT), py.SRCALPHA)
            textBox.blit(hpText, (1, 1))
            textBox.blit(mpText, (1, 16))
            textBox.blit(costText, (1, 32))
            py.draw.rect(screen, bgColor, py.Rect(button.position[0], button.position[1] + button.dimensions[1] + StoreDisplay.CAPTION_HEIGHT, button.dimensions[0], StoreDisplay.DESC_HEIGHT))
            screen.blit(textBox, (button.position[0], button.position[1] + button.dimensions[1] + StoreDisplay.CAPTION_HEIGHT))
            
        equipmentText = font.render("EQUIPMENT", True, (0, 0, 0))
        equipmentBox  = py.Surface((StoreDisplay.DIMENSIONS[0], StoreDisplay.DIMENSIONS[1]), py.SRCALPHA)
        equipmentBox.blit(equipmentText, (1, 1))
        py.draw.rect(screen, bgColor, py.Rect(StoreDisplay.EQUIPMENT_X_POS, StoreDisplay.Y_POS - StoreDisplay.DIMENSIONS[1] - StoreDisplay.CAPTION_HEIGHT, StoreDisplay.DIMENSIONS[0], StoreDisplay.DIMENSIONS[1]))
        screen.blit(equipmentBox, (StoreDisplay.EQUIPMENT_X_POS, StoreDisplay.Y_POS - StoreDisplay.DIMENSIONS[1] - StoreDisplay.CAPTION_HEIGHT))
        
        for button, item, cost in zip(StoreDisplay.equipmentButtons, StoreDisplay.store.equipmentStock, StoreDisplay.store.equipmentCosts):
            button.drawButton(screen, font, bgColor)
            if (item == None):
                continue
            hpText   = font.render("HP DMG: " + str(item.dmg[0]), True, (100, 100, 100))
            mpText   = font.render("MP DMG: " + str(item.dmg[1]), True, (100, 100, 100))
            costText = font.render("COST: " + str(cost), True, (100, 100, 100))
            textBox  = py.Surface((button.dimensions[0], StoreDisplay.DESC_HEIGHT), py.SRCALPHA)
            textBox.blit(hpText, (1, 1))
            textBox.blit(mpText, (1, 16))
            textBox.blit(costText, (1, 32))
            py.draw.rect(screen, bgColor, py.Rect(button.position[0], button.position[1] + button.dimensions[1] + StoreDisplay.CAPTION_HEIGHT, button.dimensions[0], StoreDisplay.DESC_HEIGHT))
            screen.blit(textBox, (button.position[0], button.position[1] + button.dimensions[1] + StoreDisplay.CAPTION_HEIGHT))
            
        consumableText = font.render("CONSUMABLE", True, (0, 0, 0))
        consumableBox  = py.Surface((StoreDisplay.DIMENSIONS[0], StoreDisplay.DIMENSIONS[1]), py.SRCALPHA)
        consumableBox.blit(consumableText, (1, 1))
        py.draw.rect(screen, bgColor, py.Rect(StoreDisplay.CONSUMABLE_X_POS, StoreDisplay.Y_POS - StoreDisplay.DIMENSIONS[1] - StoreDisplay.CAPTION_HEIGHT, StoreDisplay.DIMENSIONS[0], StoreDisplay.DIMENSIONS[1]))
        screen.blit(consumableBox, (StoreDisplay.CONSUMABLE_X_POS, StoreDisplay.Y_POS - StoreDisplay.DIMENSIONS[1] - StoreDisplay.CAPTION_HEIGHT))
        
        for button, item, cost in zip(StoreDisplay.consumableButtons, StoreDisplay.store.consumableStock, StoreDisplay.store.consumableCosts):
            button.drawButton(screen, font, bgColor)
            if (item == None):
                continue
            hpText   = font.render("HP RCV: " + str(item.recover[0]), True, (100, 100, 100))
            mpText   = font.render("MP RCV: " + str(item.recover[1]), True, (100, 100, 100))
            costText = font.render("COST: " + str(cost), True, (100, 100, 100))
            textBox  = py.Surface((button.dimensions[0], StoreDisplay.DESC_HEIGHT), py.SRCALPHA)
            textBox.blit(hpText, (1, 1))
            textBox.blit(mpText, (1, 16))
            textBox.blit(costText, (1, 32))
            py.draw.rect(screen, bgColor, py.Rect(button.position[0], button.position[1] + button.dimensions[1] + StoreDisplay.CAPTION_HEIGHT, button.dimensions[0], StoreDisplay.DESC_HEIGHT))
            screen.blit(textBox, (button.position[0], button.position[1] + button.dimensions[1] + StoreDisplay.CAPTION_HEIGHT))
            

    def buttonCheck(mousePosition : tuple):
        StoreDisplay.LEAVE_BUTTON.press(mousePosition)
        for button in StoreDisplay.armorButtons:
            button.press(mousePosition)
        for button in StoreDisplay.equipmentButtons:
            button.press(mousePosition)
        for button in StoreDisplay.consumableButtons:
            button.press(mousePosition)

    def buttonYPosition(index : int) -> int:
        return StoreDisplay.Y_POS + (StoreDisplay.DIMENSIONS[1] + StoreDisplay.INBETWEEN_Y + StoreDisplay.DESC_HEIGHT + StoreDisplay.CAPTION_HEIGHT) * index

    def empty() -> None:
        print("NONE")

    def armorButtonMaker(index : int):
        def button():
            if (StoreDisplay.store.armorStock[index] != None):
                didBuy = StoreDisplay.store.buyArmor(index, StoreDisplay.PLAYER_INVENTORY)
                if (didBuy):
                    StoreDisplay.armorButtons[index].action = StoreDisplay.empty
                    StoreDisplay.armorButtons[index].name   = "NONE"
        return button
    
    def equipmentButtonMaker(index : int):
        def button():
            if (StoreDisplay.store.equipmentStock[index] != None):
                didBuy = StoreDisplay.store.buyEquipment(index, StoreDisplay.PLAYER_INVENTORY)
                if (didBuy):
                    StoreDisplay.equipmentButtons[index].action = StoreDisplay.empty
                    StoreDisplay.equipmentButtons[index].name   = "NONE"
        return button
    
    def consumableButtonMaker(index : int):
        def button():
            if (StoreDisplay.store.consumableStock[index] != None):
                didBuy = StoreDisplay.store.buyConsumable(index, StoreDisplay.PLAYER_INVENTORY)
                if (didBuy):
                    StoreDisplay.consumableButtons[index].action = StoreDisplay.empty
                    StoreDisplay.consumableButtons[index].name   = "NONE"
        return button