from __future__ import annotations

from ..Interfaces.ModelViewController.GameManager import GameManager

from .ControllerRunner import ControllerRunner 
from .ModelRunner import ModelRunner
from .ViewRunner import ViewRunner
from ..Interfaces.ModelViewController.Model import Model 
from ..Interfaces.ModelViewController.View import View 
from ..Interfaces.ModelViewController.Controller import Controller

from ..Components.Models.TestModel import TestModel
from ..Components.Views.TestView import TestView
from ..Components.Controller.TestController import TestController

from pygame.time import Clock
import pygame 

from typing import Tuple 

class GameRunner(GameManager):

    FPS         : int             = 60 
    SCREEN_SIZE : Tuple[int, int] = (800, 600)
    SCREEN_NAME : str             = "Exploration Game"

    INITIAL_MODEL      : Model      = TestModel() 
    INITIAL_CONTROLLER : Controller = TestController() 
    INITIAL_VIEW       : View       = TestView()

    def __init__(self):
        
        pygame.init() 
        self.screen = pygame.display.set_mode(GameRunner.SCREEN_SIZE)

        self.init()
        self.run() 
        self.close()

    # Initialization 
    def init(self) -> None: 
        self.__model      = ModelRunner() 
        self.__controller = ControllerRunner() 
        self.__view       = ViewRunner() 

        self.__model.init(GameRunner.INITIAL_MODEL, self.__controller)
        self.__controller.init(GameRunner.INITIAL_CONTROLLER, self.__model, self.__view)
        self.__view.init(GameRunner.INITIAL_VIEW, self.__controller)
        

    def run(self) -> None: 
        clock : Clock = Clock() 
        self.running = True 

        # Game Loop
        while (self.running):

            # Handle input
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    self.running = False 
                else: 
                    self.__view.onEvent(event)

            # Update game logic 
            self.update() 

            # Draw to screen 
            self.screen.blit(self.__view.surface(self.screen.get_size()), (0, 0))

            pygame.display.flip()

            clock.tick(GameRunner.FPS)

    


    # Running 
    def update(self) -> None: 
        self.__model.update() 
        self.__controller.update() 
        self.__view.update() 

    # Clean up
    def close(self) -> None: 
        self.__model.close() 
        self.__controller.close() 
        self.__view.close() 

        pygame.quit() 