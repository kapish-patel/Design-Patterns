# shield adds defence enchantment to character
from absEnchantmentDecorator import AbsEnchantmentDecorator

class ShieldEnchantment(AbsEnchantmentDecorator):
    def __init__(self, character):
        super().__init__(character)
        self.description = "Shield Enchantment"
        self.defence = 5

    def get_Description(self) -> str:
        return f"{self.character.get_Description()} + {self.description}"

    def get_Defence(self) -> str:
        return f"{self.character.get_Defence()} + {self.defence}"
    
    def get_Attack(self) -> str:
        return self.character.get_Attack()
    
    def get_Speed(self) -> str:
        return self.character.get_Speed()