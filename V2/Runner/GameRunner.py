

from Interfaces.HasFeature.Runnable import Runnable

class GameRunner(Runnable):

    def __init__(self):
        self.init()
        self.run() 
        self.close()

    def run(self) -> None: 
        pass 

    # Initialization 
    def init(self) -> None: 
        pass
    
    
    # Running 
    def update(self) -> None: 
        pass 

    # Clean up
    def close(self) -> None: 
        pass 