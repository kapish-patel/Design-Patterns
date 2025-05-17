from abc import ABC, abstractmethod


class AbsBaseCharacter(ABC):
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
