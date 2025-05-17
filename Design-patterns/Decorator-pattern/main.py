#  main file whhich will handle operations
from BaseCharacter import BaseCharacter
from fireEnchantment import FireEnchantment
from shieldEnchantment import ShieldEnchantment
from speedEnchantment import SpeedEnchantment

def main():
    hero = BaseCharacter()
    print(hero.get_Description(), hero.get_Attack())

    fire_enchanted_hero = FireEnchantment(hero)
    print(fire_enchanted_hero.get_Description(), fire_enchanted_hero.get_Attack())

    # Adding shield enchantment
    shield_enchanted_hero = ShieldEnchantment(fire_enchanted_hero)
    print(shield_enchanted_hero.get_Description(), shield_enchanted_hero.get_Defence())

    # Adding speed enchantment
    speed_enchanted_hero = SpeedEnchantment(shield_enchanted_hero)
    print(speed_enchanted_hero.get_Description(), speed_enchanted_hero.get_Speed())

    # Adding fire enchantment
    fire_enchanted_hero = FireEnchantment(speed_enchanted_hero)
    print(fire_enchanted_hero.get_Description(), fire_enchanted_hero.get_Attack())

if __name__ == '__main__':
    main()
