# Singleton which stores the static variables for game state (THERE IS NO INSTANCE)
class GameState:
    # Actual State
    state = 0

    EXPLORE_STATE = 0
    BATTLE_STATE  = 1
    SHOP_STATE    = 2
    ITEM_STATE    = 3

    def setState(state : int) -> None:
        GameState.state = state

    def getState() -> int:
        return GameState.state