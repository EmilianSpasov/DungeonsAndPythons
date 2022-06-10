import argparse
from entities.hero import Hero
from dungeon_module.dungeon import Dungeon
from helpers_and_utilities.key_input import get_key_input
from helpers_and_utilities.utils import clear_screen, end_game, check_choice
from helpers_and_utilities.print_helpers import print_ask_direction
from helpers_and_utilities.display_info import DisplayInfo

dungeon_path='resources/files/level1.txt'
movement_dicts = {
        '\x1b[A': 'up',
        '\x1b[B': 'down',
        '\x1b[C': 'right',
        '\x1b[D': 'left',
        'w': 'up',
        's': 'down',
        'a': 'left',
        'd': 'right',
        'h': 'help',
        'c': 'character_info',
        'l': 'lore',
        'k': 'map_keys',
        'p': 'credits',
        'z': 'exit',
}

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--display_strategy', nargs="?", default="symbolic", const="symbolic", help='Display strategy for the board') # emoji, symbolic
    args = parser.parse_args() 

    hero = Hero.create_hero()
    dungeon = Dungeon(dungeon_path, args.display_strategy)
    dungeon.spawn(hero)
    DisplayInfo.display_intro()
    clear_screen()

    while not end_game(dungeon, dungeon.display_strategy.get_goal()) and dungeon.hero.is_alive():
        dungeon.print_map()
        print_ask_direction(hero)

        try:
            choice = get_key_input(movement_dicts)
            check_choice(choice, dungeon)
        except Exception as e:
            print(e)
            input('\nPress Enter to continue...')

        clear_screen()
    clear_screen()


if __name__ == '__main__':
    main()
