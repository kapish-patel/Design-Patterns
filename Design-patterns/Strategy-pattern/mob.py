# this is a base class for all mobs
from attackStrategy import AttackStrategy
from player import Player

class Mob():
    
    def __init__(self, name: str, strategy: AttackStrategy):
        self.attackStrategy = strategy
        self.name = name

    def attack(self, player: Player):
        self.attackStrategy.attack(player)
    
    def set_strategy(self, strategy: AttackStrategy):
        self.attackStrategy = strategy
        print(f"{self.name} has changed its attack strategy to {self.attackStrategy.__class__.__name__}")