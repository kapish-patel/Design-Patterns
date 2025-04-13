# this is a base class for all attack strategies
from abc import ABC, abstractmethod
from player import Player

class AttackStrategy(ABC):

    @abstractmethod
    def attack(self, target: Player) -> None:
        pass