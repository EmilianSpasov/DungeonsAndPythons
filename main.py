from entities.hero import Hero
from dungeon_module.dungeon import Dungeon
from helpers_and_utilities.key_input import get_key_input
from helpers_and_utilities.utils import clear_screen, end_game, check_choice
from helpers_and_utilities.print_helpers import print_ask_direction
from helpers_and_utilities.display_info import DisplayInfo

dungeon_path='resources/files/level1.txt'

def main():
    hero = Hero.create_hero()
    dungeon = Dungeon(dungeon_path, "emoji")
    dungeon.spawn(hero)
    DisplayInfo.display_intro()
    clear_screen()

    while not end_game(dungeon, dungeon.display_strategy.get_goal()) and dungeon.hero.is_alive():
        dungeon.print_map()
        print_ask_direction(hero)

        try:
            choice = get_key_input()
            check_choice(choice, dungeon)
        except Exception as e:
            print(e)
            input('\nPress Enter to continue...')

        clear_screen()
    clear_screen()


if __name__ == '__main__':
    main()
