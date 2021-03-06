from helpers_and_utilities.utils import clear_screen
from helpers_and_utilities.display.map_transform_factory import MapTransformFactory
from helpers_and_utilities.display.constants import SYMBOLIC

resources = 'resources/files'
credits_file = 'credits.txt'
help_file = 'help.txt'
lore_file = 'lore.txt'
keys_file = 'map_keys.txt'
intro_file = 'intro.txt'

class DisplayInfo:
    def __init__(self, hero, display_type=SYMBOLIC):
        self.hero = hero
        self.display_type = display_type

    def display_info(self, info_type):
        dicts = {'character_info': self.display_hero_information,
                 'help': self.display_help,
                 'lore': self.display_lore,
                 'map_keys': self.display_map_keys,
                 'credits': self.display_credits,
                 'exit': exit,
                 }

        dicts[info_type]()

    def display_hero_information(self):
        FORMAT_SPACES = '      '
        print(
            f'{self.hero.name} the {self.hero.title}\n\n'
            f'Current health: {self.hero.health}\n'
            f'Current mana: {self.hero.mana}\n'
            f'Mana regeneration: {self.hero.mana_regeneration_rate}\n\n'
            f'Current Weapon:\n'
            f'{FORMAT_SPACES}Name: {self.hero.weapon.name}\n'
            f'{FORMAT_SPACES}Damage: {self.hero.weapon.damage}\n\n'
            f'Current Spell:\n'
            f'{FORMAT_SPACES}Name: {self.hero.spell.name}\n'
            f'{FORMAT_SPACES}Damage: {self.hero.spell.damage}\n'
            f'{FORMAT_SPACES}Mana Cost: {self.hero.spell.mana_cost}\n'
        )
        input('\nPress Enter to continue... ')
    
    def display_fight_information(self, enemy):
        with open(f'{resources}/battle.txt', "r+") as file:
            print(file.read())
        
        FORMAT_SPACES = '      '
        print(
            f'{FORMAT_SPACES} {self.hero.known_as()} {3*FORMAT_SPACES} versus {self.display_spaces_before_enemy_name(self.hero.known_as())}Enemy: {enemy.name}\n\n'
            f'{FORMAT_SPACES} Current health: {self.hero.health} {5*FORMAT_SPACES}    {self.display_spaces_after_numerical_value(self.hero.health)}Current health: {enemy.health}\n'
            f'{FORMAT_SPACES} Current mana: {self.hero.mana} {5*FORMAT_SPACES}      {self.display_spaces_after_numerical_value(self.hero.mana)}Regular Attack Damage:  {enemy.damage}\n'
            f'{FORMAT_SPACES} Mana regeneration: {self.hero.mana_regeneration_rate} {5*FORMAT_SPACES}   Spell Damage: {enemy.spell.damage} \n\n'
            f'{FORMAT_SPACES} Current Weapon:\n'
            f'{2*FORMAT_SPACES} Name: {self.hero.weapon.name}\n'
            f'{2*FORMAT_SPACES} Damage: {self.hero.weapon.damage}\n\n'
            f'{FORMAT_SPACES} Current Spell:\n'
            f'{2*FORMAT_SPACES} Name: {self.hero.spell.name}\n'
            f'{2*FORMAT_SPACES} Damage: {self.hero.spell.damage}\n'
            f'{2*FORMAT_SPACES} Mana Cost: {self.hero.spell.mana_cost}\n'
        )
        print(f'''Press:
                'z' for regular attack
                'x' to cast spell
                'q' to quit''')
        

    def display_credits(self):
        with open(f'{resources}/{credits_file}', 'r') as fp:
            print(fp.read())
        input('\nPress Enter to continue... ')

    def display_help(self):
        with open(f'{resources}/{help_file}', 'r') as fp:
            print(fp.read())
        input('\nPress Enter to continue... ')

    def display_lore(self):
        with open(f'{resources}/{lore_file}', 'r') as fp:
            print(fp.read())
        input('\nPress Enter to continue... ')

    def display_map_keys(self):
        with open(f'{resources}/{keys_file}', 'r') as fp:
            map_keys = fp.read()
            for key, val in MapTransformFactory.create_file_transform(self.display_type).items(): 
                map_keys = map_keys.replace(key, val)
            print(map_keys)
        input('\nPress Enter to continue... ')
        
        
    @staticmethod
    def display_intro(display_type=SYMBOLIC):
        clear_screen()
        with open(f'{resources}/{intro_file}', 'r') as fp:
            intro = fp.read()
            for key, val in MapTransformFactory.create_file_transform(display_type).items(): 
                intro = intro.replace(key, val)
            print(intro)
        input('\nPress Enter to continue... ')

    def display_spaces_after_numerical_value(self, value):
        if value < 10:
            return " " * 2
        elif value >= 10 and value < 100:
            return " "
        return ""

    def display_spaces_before_enemy_name(self, value):
        return " " * (27 - len(value))