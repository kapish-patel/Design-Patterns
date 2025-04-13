#a static factory class that returns the appropriate attack strategy based on the type of attack

from attackStrategy import AttackStrategy
from MeleeAttackStrategy import MeleeAttackStrategy
from RangedAttackStrategy import RangedAttackStrategy
from ExplosiveAttackStrategy import ExplosiveAttackStrategy


class AttackStrategyFactory:

    def __init__(self):
        self.attackStrategys = {
            'zombie': MeleeAttackStrategy(),
            'skeleton': RangedAttackStrategy(),
            'creeper': ExplosiveAttackStrategy()
        }

    def get_attack_strategy(self, attack_type: str)-> AttackStrategy:
        return self.attackStrategys.get(attack_type.lower(), None)