from abc import ABC, abstractmethod
from absBaseCharacter import AbsBaseCharacter

class AbsEnchantmentDecorator(AbsBaseCharacter):
    def __init__(self, character):
        self.character = character

    @abstractmethod
    def get_Description(self) -> str:
        pass

    @abstractmethod
    def get_Attack(self) -> str:
        pass

    @abstractmethod
    def get_Defence(self) -> str:
        pass

    @abstractmethod
    def get_Speed(self) -> str:
        pass