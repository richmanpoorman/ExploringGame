# import the py module
import pygame as py
 
# import py.locals for easier
# access to key coordinates
from pygame.locals import *

from RenderingFunctions import *
from GamePlayFunctions import *

from Board import Board 
from Character import Character
from GameState import GameState
from StoreDisplay import StoreDisplay
# Initialize the py stuff


# Static variables


clock = py.time.Clock()

board = Board()
player = Character()
StoreDisplay.PLAYER_INVENTORY = player.inventory


while screenOpen:
    # Reset the press down values and update state
    currState = GameState.getState()
    key = None 
    mousePosition = (-1, -1)
    refresh()

    # for loop through the event queue
    
    for event in py.event.get():
        
        # Check for KEYDOWN event
        if event.type == KEYDOWN: 
            key = event.key
        
        elif event.type == MOUSEBUTTONDOWN:
            mousePosition = py.mouse.get_pos()
            
        # Check for QUIT event
        elif event.type == QUIT:
            screenOpen = False
    
    # TODO:: ADD PLAYER INTERACTION
    if (currState == GameState.EXPLORE_STATE):
        playerMove(key, player, board)
    elif (currState == GameState.BATTLE_STATE):
        runBattle(player, mousePosition)
    elif (currState == GameState.SHOP_STATE):
        runStore(mousePosition)

    # Draw new stuff
    screen.fill(BLACK)
    
    if (currState == GameState.EXPLORE_STATE):
        renderBoard(player, board)
    elif (currState == GameState.BATTLE_STATE):
        renderBattle(player.getStats(), battleButtons)
    elif (currState == GameState.SHOP_STATE):
        renderStore()


    # Update the screen
    py.display.flip()
    clock.tick(20)
py.quit()