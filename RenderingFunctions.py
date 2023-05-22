import pygame as py
from Character import Character
from Basics import Stats 
from Board import Board
from StoreDisplay import StoreDisplay

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
py.init()
screen = py.display.set_mode(SCREEN_SIZE)

screenOpen = True
font = py.font.SysFont(None, CELL_SIZE)

def statDisplay(percentage : float, pos : tuple, width : int, height : int, color : tuple, backColor : tuple ) -> None:
    hpBarUsed = int(width * percentage)
    py.draw.rect(screen, backColor, py.Rect(pos[0], pos[1], width, height))
    py.draw.rect(screen, color    , py.Rect(pos[0], pos[1], hpBarUsed, height))
    
def renderCell(player : Character, board : Board, deltaX : int, deltaY : int, halfBoardSize : tuple) -> None:
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

def renderBoard(player : Character, board : Board) -> None:
    statDisplay(percentage = player.getStats().getHpPercentage(), pos = (20, 20), width = 200, height = 15, color = RED, backColor = (100, 100, 100))
    statDisplay(percentage = player.getStats().getMpPercentage(), pos = (20, 40), width = 200, height = 15, color = BLUE, backColor = (100, 100, 100))
    
    halfBoardSize = (BOARD_SIZE[0] // 2, BOARD_SIZE[1] // 2)
    for deltaX in range(-halfBoardSize[0] + 1, halfBoardSize[1]):
        for deltaY in range(-halfBoardSize[1] + 1, halfBoardSize[1]):
            renderCell(player, board, deltaX, deltaY, halfBoardSize)


def renderBattle(stats : Stats, battleButtons : list) -> None: 
    statDisplay(percentage = stats.getHpPercentage(), pos = (20, 20), width = 200, height = 15, color = RED, backColor = (100, 100, 100))
    statDisplay(percentage = stats.getMpPercentage(), pos = (20, 40), width = 200, height = 15, color = BLUE, backColor = (100, 100, 100))
    for button in battleButtons:
        button.drawButton(screen, font = font)

def renderStore():
    StoreDisplay.buttonDisplay(screen, font)