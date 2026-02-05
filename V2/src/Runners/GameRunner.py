from __future__ import annotations

from pygame.time import Clock
import pygame 

from typing import Tuple 

from .StateStackMachine import StateStackMachine
from ..GameStates.Map.MapState import MapState


class GameRunner:

    FPS         : int             = 60 
    SCREEN_SIZE : Tuple[int, int] = (800, 600)
    SCREEN_NAME : str             = "Exploration Game"

    def __init__(self):
        
        pygame.init() 
        self.screen = pygame.display.set_mode(GameRunner.SCREEN_SIZE)

        self.init()
        self.run() 
        self.close()

    # Initialization 
    def init(self) -> None: 
        
        
        self.stateMachine = StateStackMachine()

        self.stateMachine.init()



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
                    self.stateMachine.onEvent(event)

            # Update game logic 
            self.update() 

            # Draw to screen 
            self.screen.blit(self.stateMachine.surface(self.screen.get_size()), (0, 0))

            pygame.display.flip()

            clock.tick(GameRunner.FPS)

    


    # Running 
    def update(self) -> None: 
        pass 

    # Clean up
    def close(self) -> None: 
        pass 

        pygame.quit() 