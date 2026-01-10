from src.Interfaces.HasFeature.Listening import Listening
from src.Types.Types import SignalID
from ...Interfaces.ModelViewController.Model import Model

class TestModel(Model):
    
    def __init__(self) -> None:
        super().__init__()

    def connect(self, listener: Listening, *args, **kwargs) -> None:
        return super().connect(listener, *args, **kwargs)
    
    def disconnect(self, listener: Listening, *args, **kwargs) -> None:
        return super().disconnect(listener, *args, **kwargs)
    

    def broadcast(self, signalID: str, *args, **kwargs) -> None:
        return super().broadcast(signalID, *args, **kwargs)
    
    def listen(self, signalID: SignalID, *args, **kwargs) -> None:
        return super().listen(signalID, *args, **kwargs)
    
    