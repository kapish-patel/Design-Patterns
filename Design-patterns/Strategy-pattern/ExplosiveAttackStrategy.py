# this is a concrete implementation of the Explosive attack steategy

from attackStrategy import AttackStrategy
from player import Player

class ExplosiveAttackStrategy(AttackStrategy):

    def attack(self, target: Player) -> None:
        damage = 40
        print(f"Attacking {target.name} with an explosive attack damage deal {damage}!")
        target.set_health(target.get_health() - damage)
        print(target.newPlayerHealthStr())
