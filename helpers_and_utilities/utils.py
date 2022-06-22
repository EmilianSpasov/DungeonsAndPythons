from helpers_and_utilities.display.constants import SYMBOLIC

def clear_screen():
    print("\033c", end="")


def is_direction(choice):
    directions = ('up', 'down', 'left', 'right')
    return choice in directions


def check_choice(choice, dungeon, display=SYMBOLIC):
    from helpers_and_utilities.display_info import DisplayInfo
    if is_direction(choice):
        dungeon.move_hero(choice)
        return

    clear_screen()
    display_info = DisplayInfo(dungeon.hero, display)
    display_info.display_info(choice)


def end_game(dungeon, goal):
    row = dungeon.curr_row
    column = dungeon.curr_column
    if dungeon.dungeon_map[row][column] == goal:
        input('Game over, you won!\n\nPress Enter to leave')
        return True
    return False
