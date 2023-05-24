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
    barUsed = int(width * percentage)
    py.draw.rect(screen, backColor, py.Rect(pos[0], pos[1], width, height))
    py.draw.rect(screen, color    , py.Rect(pos[0], pos[1], barUsed, height))

def numberDisplay(name : str, position : tuple,  value : int, maxValue : int = None, dimensions : tuple = None, textColor : tuple = (0, 0, 0), bgColor : tuple = (255, 255, 255)):
    textValue = name + ": " + str(value) + ("" if maxValue == None else " / " + str(maxValue))
    textDisplay(textValue, position, dimensions, textColor, bgColor)
    

def textDisplay(textValue : str, position : tuple, dimensions : tuple = None, textColor : tuple = (0, 0, 0), bgColor : tuple = (255, 255, 255)):
    x, y = position
    dim = dimensions if dimensions != None else (font.size(textValue)[0] + 2, font.size(textValue)[1] + 2)
    w, h = dim
    text = font.render(textValue, True, textColor)
    textBox = py.Surface(dim, py.SRCALPHA)
    
    
    # surfaceLocation = (w // 2 - font.size(textValue)[0] // 2, h // 2 - font.size(textValue)[1] // 2)
    surfaceLocation = (1, h // 2 - font.size(textValue)[1] // 2)
    textBox.blit(text, surfaceLocation)
    py.draw.rect(screen, bgColor, py.Rect(x, y, w, h))
    screen.blit(textBox, position)

def infoDisplay(player : Character):
    defaultHeight = font.size("X")[1] + 2
    stats = player.getStats()
    inventory = player.inventory

    numberDisplay("HP", (20, 20), stats.hp, stats.maxHp)
    numberDisplay("MP", (20, 20 + defaultHeight), stats.mp, stats.maxMp)

    numberDisplay("LVL", (20, 20 + 2 * defaultHeight + 1), stats.lvl)
    numberDisplay("EXP", (20, 20 + 3 * defaultHeight + 1), stats.exp, stats.lvl * Character.LVL_EXP)
    
    numberDisplay("$", (20, 20 + 4 * defaultHeight + 1), inventory.money)

    textDisplay("ARMOR: " + inventory.armor.name, (20, 450))
    numberDisplay("STR RES" , (20, 450 + defaultHeight), inventory.armor.resistance[0])
    numberDisplay("MAG RES" , (20, 450 + 2 * defaultHeight), inventory.armor.resistance[1])

    textDisplay("EQUIPMENT: " + inventory.equipment.name, (220, 450))
    numberDisplay("STR" , (220, 450 + defaultHeight), inventory.equipment.dmg[0])
    numberDisplay("MAG" , (220, 450 + 2 * defaultHeight), inventory.equipment.dmg[1])

    numberDisplay("STR", (420, 450), stats.dmg[0])
    numberDisplay("MAG", (420, 450 + defaultHeight), stats.dmg[1])

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
    # statDisplay(percentage = player.getStats().getHpPercentage(), pos = (20, 20), width = 200, height = 15, color = RED, backColor = (100, 100, 100))
    # statDisplay(percentage = player.getStats().getMpPercentage(), pos = (20, 40), width = 200, height = 15, color = BLUE, backColor = (100, 100, 100))
    infoDisplay(player)
    
    halfBoardSize = (BOARD_SIZE[0] // 2, BOARD_SIZE[1] // 2)
    for deltaX in range(-halfBoardSize[0] + 1, halfBoardSize[1]):
        for deltaY in range(-halfBoardSize[1] + 1, halfBoardSize[1]):
            renderCell(player, board, deltaX, deltaY, halfBoardSize)


def renderBattle(player: Character, battleButtons : list) -> None: 
    # statDisplay(percentage = stats.getHpPercentage(), pos = (20, 20), width = 200, height = 15, color = RED, backColor = (100, 100, 100))
    # statDisplay(percentage = stats.getMpPercentage(), pos = (20, 40), width = 200, height = 15, color = BLUE, backColor = (100, 100, 100))
    infoDisplay(player)
    for button in battleButtons:
        button.drawButton(screen, font = font)

def renderStore():
    StoreDisplay.buttonDisplay(screen, font)