import pygame as py
from pygame.locals import *
from Button import Button 
from RenderingFunctions import font, SCREEN_SIZE
from Character import Character
from Board import Board
from Battle import Battle
from StoreDisplay import StoreDisplay

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

def playerMove(key : py.key, player : Character, board : Board) -> None:
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

def refresh() -> None:
    global inputVal
    inputVal = -1
