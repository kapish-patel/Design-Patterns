#  fire enchantment decorator

from absEnchantmentDecorator import AbsEnchantmentDecorator

class FireEnchantment(AbsEnchantmentDecorator):
    def __init__(self, character):
        super().__init__(character)
        self.description = "Fire Enchantment"
        self.attack = 5

    def get_Description(self) -> str:
        return f"{self.character.get_Description()} + {self.description}"

    def get_Attack(self) -> str:
        return f"{self.character.get_Attack()} + {self.attack}"
    
    def get_Defence(self) -> str:
        return self.character.get_Defence()
    
    def get_Speed(self) -> str:
        return self.character.get_Speed()