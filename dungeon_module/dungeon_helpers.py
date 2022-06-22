import random
from resources.constants.names import WEAPON_NAMES, SPELL_NAMES
from resources.constants.treasures import TYPES_OF_TREASURES
from entities.enemy import Enemy
from entities.hero import Hero
from helpers_and_utilities.display_info import DisplayInfo
from helpers_and_utilities.verification_mixin import VerificationMixin
from helpers_and_utilities.print_helpers import print_hero_takes_damage, print_collect_treasure, print_has_been_slain
from helpers_and_utilities.key_input import get_key_input
from helpers_and_utilities.utils import clear_screen


__all__ = ['read_file',
           'set_coordinates_for_starting_positions',
           'move_is_legal',
           'apply_direction',
           'take_action_after_move',
           'fight_enemy',
           'reset_hero_attributes',
           'collect_treasure',
           'reached_exit'
           ]


def read_file(file_path: str, map_transform=None):
    with open(file_path, 'r') as f:
        content = f.readlines()
    dungeon_map = [[map_transform[char] if map_transform is not None else char for char in line.strip()] for line in content]
    return dungeon_map


def add_coordinates(lst: list):
    def add_row_and_col(row: int, col: int):
        lst.append((row, col))

    return add_row_and_col


def set_coordinates_for_starting_positions(dungeon_map: list, starting_positions: list, spawn_symbol: str):
    for row in range(len(dungeon_map)):
        for col in range(len(dungeon_map[row])):
            if dungeon_map[row][col] == spawn_symbol:
                add_coordinates(starting_positions)(row, col)


def move_is_legal(dungeon_map: list, display_strategy, row: int, col: int):
    if row < 0 or col < 0 or row >= len(dungeon_map) or col >= len(dungeon_map[row]):
        raise ValueError('\nYou cannot go out of the map.')

    if dungeon_map[row][col] == display_strategy.get_obstacle():
        raise ValueError('\nThere is a wall. You cannot go there.')

    if dungeon_map[row][col] == display_strategy.get_spawn():
        raise ValueError('\nYou cannot enter the Spawn Zone')


def apply_direction(direction: str, curr_row: int, curr_column: int):
    dicts = {
        'up': (curr_row - 1, curr_column),
        'down': (curr_row + 1, curr_column),
        'left': (curr_row, curr_column - 1),
        'right': (curr_row, curr_column + 1)
    }

    if not VerificationMixin.is_command_valid(dicts, direction):
        raise ValueError('No such command')

    row = dicts[direction][0]
    col = dicts[direction][1]

    return row, col


def take_action_after_move(hero: Hero, position: str, display_strategy):
    if position == display_strategy.get_path():
        return

    dict_of_actions = {
        display_strategy.get_enemy(): fight_enemy,
        display_strategy.get_treasure(): collect_treasure,
    }

    dict_of_actions[position](hero)


def fight_enemy(hero: Hero):
    from entities.enemy import Enemy
    enemy = Enemy.spawn_enemy()
    dicts = {
        "x":  hero.attack_by_spell,
        "z":  hero.attack,
        "q":  exit,
    }

    while True:
        clear_screen()
        DisplayInfo(hero).display_fight_information(enemy)
        action = get_key_input(dicts)
        enemy.take_damage(action())
        
        clear_screen()
        DisplayInfo(hero).display_fight_information(enemy)
        if not enemy.is_alive():
            print_has_been_slain('Enemy')
            return

        hero.take_damage(enemy.attack())
        
        clear_screen()
        DisplayInfo(hero).display_fight_information(enemy)
        if not hero.is_alive():
            print_has_been_slain(hero.known_as())
            return

def collect_treasure(hero: Hero):
    dict_add_treasure = {
        'health': hero.take_healing,
        'mana': hero.take_mana,
        'weapon': hero.equip,
        'spell': hero.learn
    }

    treasure = random.choice(TYPES_OF_TREASURES)
    treasure_value = generate_random_value_of_treasure(treasure)

    result = dict_add_treasure[treasure](treasure_value)
    if result:
        print_collect_treasure(treasure)
    input('\nPress Enter to continue... ')



def generate_random_value_of_treasure(treasure: str):
    from items.weapon import Weapon
    from items.spell import Spell

    dict_treasure_values = {
        'health': random.randint(1, 20),
        'mana': random.randint(1, 20),
        'weapon': Weapon.create_weapon(random.choice(WEAPON_NAMES)),
        'spell': Spell.create_spell(random.choice(SPELL_NAMES))
    }

    treasure_value = dict_treasure_values[treasure]
    return treasure_value


def reset_hero_attributes(hero: Hero):
    from items.weapon import Weapon
    from items.spell import Spell
    hero.health = hero.MAX_HEALTH
    hero.mana = hero.MAX_MANA
    hero.weapon = Weapon.create_weapon(random.choice(WEAPON_NAMES))
    hero.spell = Spell.create_spell(random.choice(SPELL_NAMES))


def reached_exit(position: str, goal: str):
    if position == goal:
        print("You've successfully reached the exit!")
        return True
    return False
