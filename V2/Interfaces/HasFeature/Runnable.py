from abc import ABC as Interface, abstractmethod

class Runnable(Interface):

    @abstractmethod
    def init(self, *args, **kwargs) -> None: 
        pass 

    @abstractmethod 
    def update(self) -> None: 
        pass 

    @abstractmethod
    def close(self) -> None: 
        pass 