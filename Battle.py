from Character import Character
from random import randint
from Basics import Stats
from Basics import GameState

import pygame

class Enemy:    
    def __init__(self, hp : int, mp : int, dmg : int, lvl : int = 1, exp : int = randint(10, 100), money : int = randint(5, 10)):
        self.stats = Stats(hp, mp, dmg, lvl, exp, money)

    def turn(self, player : Character) -> None:
        enemyMove = self.AI()
        enemyMove(player)

    def getStats(self):
        return self.stats

    def attack(self, player : Character) -> None:
        playerStats = player.getStats()
        dmg = self.getStats().dmg
        playerStats.changeHp(-dmg)
        print("ENEMY ATTACK")

    def AI(self):
        # TODO:: ADD COMPLEXITY
        return self.attack
    
    def defeat(self) -> tuple: # (EXP, MONEY) 
        return (self.stats.lvl * self.stats.exp, self.stats.money)


class Battle:
    currentEnemy : Enemy = None
    playerTurn : bool = True 

    def setEnemy(enemy : Enemy) -> None:
        Battle.currentEnemy = enemy

    def getEnemy() -> Enemy:
        return Battle.currentEnemy

    def playerAttack(player : Character, enemy : Enemy) -> None:
        playerDmg = player.getStats().dmg
        enemyStats = enemy.getStats()
        enemyStats.changeHp(-playerDmg)
        print("Did", player.getStats().dmg, "Damage")

    def playerChoice(input : int):
        if (input == -1):
            return None
        print("Attack")
        return Battle.playerAttack

    def hasWon(player : Character, enemy : Enemy) -> bool:
        return enemy == None or player.getStats().hp <= 0 or enemy.getStats().hp <= 0

    def battleTurn(input : int, player : Character, enemy : Enemy, playerTurn : bool = True) -> bool: # Whether the turn is over
        
        if (playerTurn):
            move = Battle.playerChoice(input) 
            if (move == None):
                return False
            move(player, enemy)
            return True
        
        enemy.turn(player)
        return True
    
    def battle(player : Character, input : int) -> None:
        enemy = Battle.currentEnemy
        # If the player has beaten the enemy
        if (Battle.hasWon(player, Battle.currentEnemy)):
            GameState.setState(GameState.EXPLORE_STATE)
            Battle.currentEnemy = None
            return 
        
        # If the player made a selection
        if (Battle.battleTurn(input, player, enemy, Battle.playerTurn)):
            Battle.playerTurn = False
            # Enemy Turn
            enemy.AI()(player)
            Battle.playerTurn = True
        
        





