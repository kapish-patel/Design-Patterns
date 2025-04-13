# this is a base class for all mobs
from attackStrategy import AttackStrategy
from player import Player

class Mob():
    
    def __init__(self, name: str, strategy: AttackStrategy):
        self.health = 30
        self.attackStrategy = strategy
        self.name = name

    def attack(self, player: Player):
        self.attackStrategy.attack(player)