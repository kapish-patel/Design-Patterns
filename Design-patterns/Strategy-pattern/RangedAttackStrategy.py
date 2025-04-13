#  this is a concret implementation of Ranged attack strategy

from attackStrategy import AttackStrategy
from player import Player

class RangedAttackStrategy(AttackStrategy):

    def attack(self, target: Player) -> None:
        damage = 20
        print(f"Attacking {target.name} with a ranged attack damage deal {damage}!")
        target.set_health(target.get_health() - damage)
        print(target.newPlayerHealthStr())

