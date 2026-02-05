from __future__ import annotations

from dataclasses import dataclass
from typing import List, Callable, Protocol


@dataclass 
class Level:
    lvl : int 
    exp : int
    expToLevelUp : int 
    _onLevelUp : Callable[[Level], Level] = lambda x : x

    def gainEXP(self, expAmount : int) -> None: 
        self.exp += expAmount 
        while self.exp >= self.expToLevelUp:
            self.exp -= self.expToLevelUp
            self.lvl += 1 
            self._onLevelUp(self)

    def modifyLevelUp(self, onLevelUp : Callable[[Level], Level]) -> None: 
        self._onLevelUp = lambda level : onLevelUp(self._onLevelUp(level))

@dataclass 
class HealthPoints:
    maxHP : int
    hp    : int 
    onDeath : Callable[[HealthPoints], None]

    def damage(self, damage : Damage) -> None:
        self.hp -= damage.damage 
        if self.hp <= 0: 
            self.onDeath(self)

    def heal(self, heal : Heal) -> None:
        self.hp = min(self.hp + heal.heal, self.maxHP)

@dataclass 
class Mana:
    maxMana : int
    mana    : int 

    def use(self, amount : int, onUse : Callable[[], None]) -> bool: 
        if amount > self.mana: 
            return False 
        self.mana -= amount 
        onUse() 
    
    def recover(self, amount : int) -> None: 
        self.mana = min(self.mana + amount, self.maxMana)

@dataclass 
class Damage:
    damage : int 
    _onDamage : Callable[[Damage], Damage] = lambda x : x

    def modifyDamage(self, onDamage : Callable[[Damage], Damage]) -> None: 
        self._onDamage = lambda damage : onDamage(self._onDamage(damage))

    def calculateDamage(self, healthPoints : HealthPoints) -> None: 
        damage = self._onDamage(self)
        healthPoints.damage(damage)
    
@dataclass 
class Heal: 
    heal : int 
    _onHeal : Callable[[Heal], Heal] = lambda x : x 

    def modifyHeal(self, onHeal : Callable[[Heal], Heal]) -> None: 
        self._onHeal = lambda heal : onHeal(self._onHeal(heal))

    def calculateHeal(self, healthPoints : HealthPoints) -> None: 
        heal = self._onHeal(self)
        healthPoints.heal(heal)
    