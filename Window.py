# import the pygame module
import pygame
 
# import pygame.locals for easier
# access to key coordinates
from pygame.locals import *

from random import randint

from Board import Board 
from Basics import Cell
from Character import Character

from Basics import GameState

from Battle import Battle



# Initialize the pygame stuff
pygame.init()

# Static variables
SCREEN_SIZE = [500, 500]

WHITE = [255, 255, 255]
BLACK = [0  , 0  , 0  ]
RED   = [255, 0  , 0  ]
BLUE  = [0  , 0  , 255]
PLAYER_SIZE = 10

BOARD_SIZE = (21, 21)
CELL_SIZE  = 20

OFFSET  = 40
SPACING = 1

SEE_DISTANCE = 5
FAR_OPACITY  = 75
# Initialization variables
screen = pygame.display.set_mode(SCREEN_SIZE)

screenOpen = True
clock = pygame.time.Clock()

board = Board()
player = Character()

font = pygame.font.SysFont(None, CELL_SIZE)


def statDisplay(player : Character) -> None:
    BAR_BACK_COLOR = (100, 100, 100)
    BAR_WIDTH  = 200
    BAR_HEIGHT = 15
    HP_POS_X, HP_POS_Y = 20, 20
    MP_POS_X, MP_POS_Y = 20, 40

    pygame.draw.rect(screen, BAR_BACK_COLOR, pygame.Rect(HP_POS_X, HP_POS_Y, BAR_WIDTH, BAR_HEIGHT))
    pygame.draw.rect(screen, RED           , pygame.Rect(HP_POS_X, (int)(HP_POS_Y * player.getStats().getHpPercentage()), BAR_WIDTH, BAR_HEIGHT))


    pygame.draw.rect(screen, BAR_BACK_COLOR, pygame.Rect(MP_POS_X, MP_POS_Y, BAR_WIDTH, BAR_HEIGHT))
    pygame.draw.rect(screen, BLUE          , pygame.Rect(MP_POS_X, (int)(MP_POS_Y * player.getStats().getMpPercentage()), BAR_WIDTH, BAR_HEIGHT))

def renderCell(deltaX : int, deltaY : int, halfBoardSize : tuple) -> None:
    dispX = OFFSET + (deltaX + halfBoardSize[0]) * (CELL_SIZE + SPACING)
    dispY = OFFSET + (deltaY + halfBoardSize[1]) * (CELL_SIZE + SPACING)
    
    if deltaX == 0 and deltaY == 0:
        screen.blit(player.display.getSurface(font), (dispX, dispY))
        return
    
    x, y = player.getPosition()
    x += deltaX
    y += deltaY
    position = (x, y)
    if not board.hasCell(position):
        board.generateTerrain(position)
    
    # See Cells
    squaredDistance = deltaX * deltaX + deltaY * deltaY
    squaredSight = SEE_DISTANCE * SEE_DISTANCE

    if (squaredDistance <= squaredSight):
        board.getCell(position).find()
    
    if (board.getCell(position).isFound()):
        cellSurface = board.getCell(position).getSurface(font)
        if (squaredDistance > squaredSight // 2):
            cellSurface.set_alpha(FAR_OPACITY)
        screen.blit(cellSurface, (dispX, dispY))


def renderBoard() -> None:
    halfBoardSize = (BOARD_SIZE[0] // 2, BOARD_SIZE[1] // 2)
    for deltaX in range(-halfBoardSize[0] + 1, halfBoardSize[1]):
        for deltaY in range(-halfBoardSize[1] + 1, halfBoardSize[1]):
            renderCell(deltaX, deltaY, halfBoardSize)


class Button:
    def __init__(self, position : tuple, dimensions : tuple, action, name : str= ""):
        self.position = position
        self.dimensions = dimensions 
        self.action = action
        self.name = name
    
    def press(self, position : tuple) -> None:
        x, y = position

        left   = self.position[0] 
        right  = self.position[0] + self.dimensions[0]
        top    = self.position[1]
        bottom = self.position[1] + self.dimensions[1]

        if (x < left or x > right or y < top or y > bottom):
            return 
        print("Here we go")
        self.action()
        

inputVal = -1
def battleInputButton(changeInputTo : int):
    def inputFunc() -> None:
        global inputVal
        inputVal = changeInputTo 
    return inputFunc
battleButtons = [
    Button((100, 100), (100, 100), battleInputButton(0))
]

def renderBattle() -> None: 
    for button in battleButtons:
        x, y = button.position 
        w, h = button.dimensions
        pygame.draw.rect(screen, WHITE, pygame.Rect(x, y, w, h))

def checkButtons(mousePosition : tuple) -> None:
    for button in battleButtons:
        button.press(mousePosition)

def playerMove(key : pygame.key, player : Character) -> None:
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
    board.activateCell(player.getPosition())


while screenOpen:
    # Reset the press down values and update state
    currState = GameState.getState()
    key = None 
    inputVal = -1
    mousePosition = (-1, -1)

    # for loop through the event queue
    
    for event in pygame.event.get():
        
        # Check for KEYDOWN event
        if event.type == KEYDOWN: 
            key = event.key
        
        elif event.type == MOUSEBUTTONDOWN:
            mousePosition = pygame.mouse.get_pos()
            
        # Check for QUIT event
        elif event.type == QUIT:
            screenOpen = False
    
    # TODO:: ADD PLAYER INTERACTION
    if (currState == GameState.EXPLORE_STATE):
        playerMove(key, player)
    elif (currState == GameState.BATTLE_STATE):
        checkButtons(mousePosition)
        Battle.battle(player, inputVal)

    # Draw new stuff

    screen.fill(BLACK)
    
    if (currState == GameState.EXPLORE_STATE):
        renderBoard()
        statDisplay(player)
    elif (currState == GameState.BATTLE_STATE):
        renderBattle()
    # Update the screen
    pygame.display.flip()
    clock.tick(20)
pygame.quit()