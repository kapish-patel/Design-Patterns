# speed enchantment adds attack and walking speed of character
from absEnchantmentDecorator import AbsEnchantmentDecorator
class SpeedEnchantment(AbsEnchantmentDecorator):
    def __init__(self, character):
        super().__init__(character)
        self.description = "Speed Enchantment"
        self.attack = 3
        self.speed = 2

    def get_Description(self) -> str:
        return f"{self.character.get_Description()} + {self.description}"

    def get_Attack(self) -> str:
        return f"{self.character.get_Attack()} + {self.attack}"
    
    def get_Speed(self) -> str:
        return f"{self.character.get_Speed()} + {self.speed}"
    
    def get_Defence(self) -> str:
        return self.character.get_Defence()
    