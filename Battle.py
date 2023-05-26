from Character import Character
from random import randint
from Basics import Stats
from GameState import GameState
from Armor import Armor
from typing import Tuple
from ItemButtons import ItemButtons

class Enemy:    
    def __init__(self, hp : int, mp : int, physical : int, magical : int, lvl : int = 1, exp : int = randint(10, 100), money : int = randint(5, 10), armor : Armor = Armor(), name : str = None):
        self.stats = Stats(hp = hp, mp = mp, physicalDmg = physical, magicDmg = magical, lvl = lvl, exp = exp)
        self.armor = armor
        self.money = money
        self.name = name

    def getStats(self):
        return self.stats

    def takeDamage(self, damage : Tuple[int, int]) -> int:
        armor = self.armor 
        # If statements to deal with armor that makes resistances worse (a negative resistance)
        physicalDmg = max(0, damage[0] - armor.resistance[0]) if damage[0] != 0 else 0
        magicalDmg  = max(0, damage[1] - armor.resistance[1]) if damage[1] != 0 else 0
        totalDmg = physicalDmg + magicalDmg

        self.stats.changeHp(-totalDmg)
        return totalDmg

    def attack(self, player : Character) -> None:
        player.takeDamage(self.stats.dmg)
        print("ENEMY ATTACK")

    def AI(self, player : Character) -> None:
        self.attack(player)
    
    def defeat(self) -> Tuple[int, int]: # (EXP, MONEY) 
        return (self.stats.lvl * self.stats.exp, self.money)


class Battle:
    PHYSICAL_ATTACK = 0
    MAGIC_ATTACK    = 1
    BAG             = 2
    RUN             = 3
    currentEnemy : Enemy = None
    playerTurn : bool = True 

    def setEnemy(enemy : Enemy) -> None:
        Battle.currentEnemy = enemy

    def getEnemy() -> Enemy:
        return Battle.currentEnemy

    def playerAttack(damage : Tuple[int, int]) -> None:
        Battle.currentEnemy.takeDamage(damage)


    def playerChoice(input : int, player : Character, enemy : Enemy) -> bool: # If a choice has been made
        playerStats = player.getStats()
        if (input == Battle.PHYSICAL_ATTACK):
            print("Physical Damage")
            dmg = (playerStats.dmg[0] + player.inventory.equipment.dmg[0], 0)
            enemy.takeDamage(dmg)

        elif (input == Battle.MAGIC_ATTACK):
            manaCost = player.inventory.equipment.mpCost
            if (playerStats.mp < manaCost):
                print("TODO:: Not enough Mana")
                return False
            print("Magical Damage")
            playerStats.changeMp(-manaCost)
            dmg = (0, playerStats.dmg[1] + player.inventory.equipment.dmg[1])
            enemy.takeDamage(dmg)

        elif (input == Battle.BAG):
            # TODO:: The bag stuff 
            if (not player.inventory.bag):
                print("Empty Bag")
                return False 
            print("Bag")
            ItemButtons.makeConsumableButton(player)
            GameState.setState(GameState.CONSUMABLE_STATE)
            

        elif (input == Battle.RUN):
            runChance = 50 * (playerStats.lvl / Battle.getEnemy().getStats().lvl)
            rng = randint(0, 100)
            print(runChance, rng)
            if  rng <= runChance:
                Battle.currentEnemy = None
        else:
            return False 
        return True

    def hasWon(player : Character, enemy : Enemy) -> bool:
        if (player.getStats().hp <= 0):
            GameState.setState(GameState.GAMEOVER_STATE)
            return False
        return enemy == None or enemy.getStats().hp <= 0

    
    def battle(player : Character, input : int) -> None:
        enemy = Battle.currentEnemy
        # If the player has beaten the enemy
        if (Battle.hasWon(player, Battle.currentEnemy)):
            GameState.setState(GameState.EXPLORE_STATE)
            if (enemy == None):
                return
            enemyLvl   = enemy.getStats().lvl
            playerLvl  = player.getStats().lvl
            enemyExp   = enemy.getStats().exp 
            enemyMoney = enemy.money
            gainedExp  = max(1, enemyLvl - playerLvl + 1) * (1 + enemyExp)
            player.gainRewards(gainedExp, enemyMoney)
            Battle.currentEnemy = None
            return 
        
        # If the player made a selection
        if (Battle.playerTurn):
            if (Battle.playerChoice(input, player, enemy)):
                Battle.playerTurn = False
        else:
            enemy.AI(player) # Enemy Does Things
            Battle.playerTurn = True
        
        





