# a concret implementation of melee attack strategy

from attackStrategy import AttackStrategy
from player import Player

class MeleeAttackStrategy(AttackStrategy):

    def attack(self, target: Player) -> None:
        damage = 10
        print(f"Attacking {target.name} with a melee attack damage deal {damage}!")
        target.set_health(target.get_health() - damage)
        print(target.newPlayerHealthStr())
