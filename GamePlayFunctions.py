import pygame as py
from pygame.locals import *
from Button import Button 
from RenderingFunctions import font, SCREEN_SIZE
from Character import Character
from Board import Board
from Battle import Battle
from StoreDisplay import StoreDisplay
from Inventory import Inventory
from GameState import GameState
from Basics import Stats

inputVal = -1
# Create the buttons which change the input value
def battleInputButton(changeInputTo : int):
    def inputFunc() -> None:
        global inputVal
        inputVal = changeInputTo 
    return inputFunc

    # Creates the buttons, with the names above
buttonNames = [ "Physical Attack", "Magic Attack", "Bag", "Run"]
battleButtons = [ Button((110 * (i) + 20, SCREEN_SIZE[1] - 150), (100, 50), battleInputButton(i), buttonNames[i]) for i in range(len(buttonNames)) ]

def checkBattleButtons(mousePosition : tuple) -> None:
    for button in battleButtons:
        button.press(mousePosition)

class ItemButtons:
    armorButtonList = []
    equipmentButtonList = []
    consumableButtonList = []

    def makeItemButtons(player : Character):
        inventory = player.inventory 
        stats = player.getStats()

        DIMENSIONS  = (170, 12)
        INBETWEEN_X = 10
        INBETWEEN_Y = 1
        CAPTION_HEIGHT = 3
        DESC_HEIGHT = 50
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
            Button((ARMOR_X_POS, Y_POS + buttonYPosition(idx)), DIMENSIONS, armorFunction(idx), inventory.armorList[idx].name)
            for idx in reversed(range(len(inventory.armorList)))
        ]
        ItemButtons.equipmentButtonList = [
            Button((EQUIPMENT_X_POS, Y_POS + buttonYPosition(idx)), DIMENSIONS, weaponFunction(idx), inventory.equipmentList[idx].name)
            for idx in reversed(range(len(inventory.equipmentList)))
        ]
        ItemButtons.consumableButtonList = [
            Button((CONSUMABLE_X_POS, Y_POS + buttonYPosition(idx)), DIMENSIONS, consumableFunction(idx, stats), inventory.bag[idx].name)
            for idx in reversed(range(len(inventory.bag)))
        ]
        
    def itemButtonCheck(mousePosition : tuple, inventory : Inventory) -> None:
        for button in ItemButtons.armorButtonList:
            button.press(mousePosition)
        for button in ItemButtons.equipmentButtonList:
            button.press(mousePosition)
        for button in ItemButtons.consumableButtonList:
            if (button.press(mousePosition)):
                ItemButtons.makeItemButtons(inventory)
    
itemButton     = Button((20, 430), (50, 15), lambda : GameState.setState(GameState.ITEM_STATE), "Equipment Menu")
exitItemButton = Button((20, 430), (50, 15), lambda : GameState.setState(GameState.EXPLORE_STATE), "Exit Menu")



def playerMove(player : Character, board : Board, key : py.key) -> None:
    moveTo = (0, 0)
    if key == K_w:
        moveTo = (0 , -1)
    elif key == K_s:
        moveTo = (0 , 1 )
    elif key == K_a:
        moveTo = (-1, 0 )
    elif key == K_d:
        moveTo = (1 , 0 )
    else:
        return
    playerPos = player.getPosition()
    newPos = (playerPos[0] + moveTo[0], playerPos[1] + moveTo[1])
    if (board.getCell(newPos).isBlocked):
        return
    
    player.move(moveTo[0], moveTo[1])
    board.activateCell(player.getPosition(), player.getStats().lvl)

def runBattle(player : Character, mousePosition : tuple) -> None:
    checkBattleButtons(mousePosition)
    Battle.battle(player, inputVal)

def runStore(mousePosition : tuple) -> None:
    StoreDisplay.buttonCheck(mousePosition)

def runBoard(player : Character, board : Board, key : py.key, mousePosition : tuple) -> None:
    playerMove(player, board, key)
    if (itemButton.press(mousePosition)):
        ItemButtons.makeItemButtons(player)

def runItem(player : Character, mousePosition : tuple):
    exitItemButton.press(mousePosition)
    ItemButtons.itemButtonCheck(mousePosition, player)


def gameOverButtonFunction():
    def buttonFunc():
        GameState.setState(GameState.EXPLORE_STATE)
        print(GameState.getState())
    return buttonFunc 

gameOverButton = Button((0, 0), (500, 500), gameOverButtonFunction(), "GAME OVER (PRESS TO RESTART)")
def runGameOver(mousePosition : tuple):
    gameOverButton.press(mousePosition)

def refresh() -> None:
    global inputVal
    inputVal = -1
