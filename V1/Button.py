import pygame as py

class Button:
    def __init__(self, position : tuple, dimensions : tuple, action, name : str = ""):
        self.update(position, dimensions, action, name)
    
    def press(self, position : tuple) -> bool:
        x, y = position

        left   = self.position[0] 
        right  = self.position[0] + self.dimensions[0]
        top    = self.position[1]
        bottom = self.position[1] + self.dimensions[1]

        if (x < left or x > right or y < top or y > bottom):
            return False
        print("Here we go")
        self.action()
        return True
    
    # If the button changes for some reason
    def update(self, position : tuple = None, dimensions : tuple = None, action = None, name : str = None):
        if position != None:
            self.position = position 
        if dimensions != None:
            self.dimensions = dimensions 
        if name != None:
            self.name = name 
        if action != None:
            self.action = action
        
        

    def drawButton(self, screen : py.Surface, font : py.font, bgColor : tuple = (255, 255, 255)) -> None:
        x, y = self.position
        w, h = self.dimensions
        text = font.render(self.name, True, (0, 0, 0))
        self.textBox = py.Surface(self.dimensions, py.SRCALPHA)
        surfaceLocation = (w // 2 - font.size(self.name)[0] // 2, h // 2 - font.size(self.name)[1] // 2)
        self.textBox.blit(text, surfaceLocation)
        py.draw.rect(screen, bgColor, py.Rect(x, y, w, h))
        screen.blit(self.textBox, self.position)