from absBaseCharacter import AbsBaseCharacter

class BaseCharacter(AbsBaseCharacter):
    def __init__(self, description: str = 'Hero with basic abilities', attack: int = 10, defence: int = 0, 
                 speed: int = 0):
        self._description = description
        self._attack = attack
        self._defence = defence
        self._speed = speed

    def get_Description(self) -> str:
        return self._description

    def get_Attack(self) -> str:
        return f"Player Attack damage: {self._attack}"
    
    def get_Defence(self) -> str:
        return f"Player Defence: {self._defence}"
    
    def get_Speed(self) -> str:
        return f"Player Speed: {self._speed}"