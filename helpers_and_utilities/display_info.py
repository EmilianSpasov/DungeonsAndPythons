from helpers_and_utilities.utils import clear_screen

resources = 'resources/files'
credits_file = 'credits.txt'
help_file = 'help.txt'
lore_file = 'lore.txt'
keys_file = 'map_keys.txt'
intro_file = 'intro.txt'

class DisplayInfo:
    def __init__(self, hero):
        self.hero = hero

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
            f'{FORMAT_SPACES} {self.hero.name} the {self.hero.title} {3*FORMAT_SPACES} versus {2*FORMAT_SPACES} Enemy: {enemy.name}\n\n'
            f'{FORMAT_SPACES} Current health: {self.hero.health} {5*FORMAT_SPACES}    Current health: {enemy.health}\n'
            f'{FORMAT_SPACES} Current mana: {self.hero.mana}\n'
            f'{FORMAT_SPACES} Mana regeneration: {self.hero.mana_regeneration_rate} {5*FORMAT_SPACES}   Regular attack damage:  {enemy.damage}\n\n'
            f'{FORMAT_SPACES} Current Weapon: {5*FORMAT_SPACES}        Current Spell:\n'
            f'{2*FORMAT_SPACES} Name: {self.hero.weapon.name}  {6*FORMAT_SPACES}  Name: {enemy.spell.name}\n'
            f'{2*FORMAT_SPACES} Damage: {self.hero.weapon.damage}   {6*FORMAT_SPACES}     Damage: {self.hero.spell.damage}\n\n'
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
            print(fp.read())
        input('\nPress Enter to continue... ')
        
        
    @staticmethod
    def display_intro():
        clear_screen()
        with open(f'{resources}/{intro_file}', 'r') as fp:
            print(fp.read())
        input('\nPress Enter to continue... ')
