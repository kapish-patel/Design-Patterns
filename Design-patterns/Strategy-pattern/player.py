# player class which allows to set the player,name, health. 

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
    
    def set_health(self, health):
        self.health = health
    
    def get_health(self):
        return self.health
    
    def get_name(self):
        return self.name
    
    def newPlayerHealthStr(self):
        return f"{self.name} has {self.health} health left."