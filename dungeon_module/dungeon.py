from dungeon_module.dungeon_helpers import *
from entities.hero import Hero
from helpers_and_utilities.display.display_factory import DisplayFactory
from helpers_and_utilities.display.map_transform_factory import MapTransformFactory 
from helpers_and_utilities.utils import clear_screen

class Dungeon:

    def __init__(self, file_path: str = None, display_strategy: str = "symbolic"):
        self.display_strategy = DisplayFactory.create_display_strategy(display_strategy)

        self.starting_positions = []

        self.dungeon_map = read_file(file_path, MapTransformFactory.create_map_transform(display_strategy))
        self.__set_starting_positions()

        self.curr_row = 0
        self.curr_column = 0
        

    def spawn(self, hero_instance: Hero = None):
        self.hero = hero_instance
        self.__set_hero_coordinates()

    def print_map(self):
        print()
        for rows in self.dungeon_map:
            print(" ",*rows, " ")
        print()
        

    def move_hero(self, direction):
        row, col = apply_direction(direction, self.curr_row, self.curr_column)

        move_is_legal(self.dungeon_map, self.display_strategy, row, col)

        position = self.dungeon_map[row][col]

        if reached_exit(position, self.display_strategy.get_goal()):
            self.__update_position(row, col)
            return

        take_action_after_move(self.hero, position, self.display_strategy)
        print("Battle is over")
        if not self.hero.is_alive():
            self.__respawn_hero()
            return

        self.hero.take_mana(self.hero.mana_regeneration_rate)
        self.__move_hero_on_the_map(row, col)
        self.__update_position(row, col)

    def __set_starting_positions(self):
        set_coordinates_for_starting_positions(self.dungeon_map, self.starting_positions, self.display_strategy.get_spawn())
        if not self.starting_positions:
            raise ValueError('Invalid map. No place to spawn.')

    def __respawn_hero(self):
        if not self.starting_positions:
            clear_screen()
            raise Exception('Game over. No place to respawn.')

        reset_hero_attributes(self.hero)

        row = self.starting_positions[0][0]
        col = self.starting_positions[0][1]

        self.__move_hero_on_the_map(row, col)
        self.__set_hero_coordinates()
        self.__update_position(row, col)

        print(f'{self.hero.known_as()} has respawn at {self.curr_row} {self.curr_column}')

    def __update_position(self, row, col):
        self.curr_row = row
        self.curr_column = col

    def __move_hero_on_the_map(self, row, col):
        self.dungeon_map[self.curr_row][self.curr_column] = self.display_strategy.get_path()
        self.dungeon_map[row][col] = self.display_strategy.get_hero()

    def __set_hero_coordinates(self):
        self.curr_row = self.starting_positions[0][0]
        self.curr_column = self.starting_positions[0][1]
        del self.starting_positions[0]
        self.dungeon_map[self.curr_row][self.curr_column] = self.display_strategy.get_hero()