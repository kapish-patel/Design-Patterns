# main file which will run the program
from player import Player
from mob import Mob
from attackStrategyFactory import AttackStrategyFactory
def main():
    print(" ** Welcome to Minecraft lets start playing ** ")
    playerName = input("Enter your name: ")
    player = Player(playerName)
    print(f"{player.get_name()} has joined the game with {player.get_health()} health.")
    print("Spawning Mobs........ be ready");

    attackStrategyFactory = AttackStrategyFactory()

    # create mob and assign attack strategy using factory of strategy pattern
    zombie = Mob("Zombie", attackStrategyFactory.get_attack_strategy("zombie"))
    skeleton = Mob("Skeleton", attackStrategyFactory.get_attack_strategy("skeleton"))
    creeper = Mob("Creeper", attackStrategyFactory.get_attack_strategy("creeper"))
    gast = Mob("Gast", attackStrategyFactory.get_attack_strategy("gast"))

    mobs = [zombie, skeleton, creeper]

    # attack the player
    print("Mobs are attacking the player")
    for mob in mobs:
        mob.attack(player)
    
    # zombie changes its attack strategy
    print("Zombie is too near to you its is exploding")
    mobs[0].set_strategy(attackStrategyFactory.get_attack_strategy("creeper"))
    mobs[0].attack(player)



if __name__ == "__main__":
    main()