import unittest
import sys
sys.path.append('..')


from entities.enemy import Enemy
from entities.hero import Hero
from items.weapon import Weapon
from dungeon_module.dungeon_helpers import read_file, add_coordinates, \
    set_coordinates_for_starting_positions, move_is_legal, reset_hero_attributes, reached_exit
from entities.display.display_factory import DisplayFactory


class TestDungeonHelpers(unittest.TestCase):
    def test_if_read_file_works_correctly(self):
        path_file = './unittests/test_valid_map.txt'
        res = read_file(path_file)
        exp = [['.', '.', '.', '.', '.', '.', '.', '.', 'S'],
               ['#', '#', '#', '#', '.', '.', 'T', '.', 'E'],
               ['.', '.', '.', 'G', '.', '.', 'S', '.', 'T']]

        self.assertEqual(res, exp)

    def test_if_add_coordinates_works_correctly(self):
        lst = []
        add_coordinates(lst)(1, 2)
        exp = [(1, 2)]
        self.assertEqual(lst, exp)

    def test_is_set_coordinates_works_if_there_are_one_or_more_starting_positions(self):
        dungeon_map = [['.', '.', '.', 'S', '.', '.', '.', '.', 'S'],
                       ['#', '#', '#', '#', '.', '.', 'T', '.', 'E'],
                       ['.', '.', '.', 'G', '.', '.', 'S', '.', 'T']]

        starting_positions = []
        exp = [(0, 3), (0, 8), (2, 6)]
        set_coordinates_for_starting_positions(dungeon_map, starting_positions, "S")
        self.assertEqual(starting_positions, exp)

    def test_is_set_coordinates_works_if_there_are_no_starting_positions(self):
        dungeon_map = [['.', '.', '.', '.', '.', '.', '.', '.', '.'],
                       ['#', '#', '#', '#', '.', '.', 'T', '.', 'E'],
                       ['.', '.', '.', 'G', '.', '.', '.', '.', 'T']]

        starting_positions = []
        exp = []
        set_coordinates_for_starting_positions(dungeon_map, starting_positions, "S")
        self.assertEqual(starting_positions, exp)

    def test_if_move_is_legal_raises_exception_when_row_is_negative(self):
        dungeon_map = [['.']]
        
        row = -1
        column = 0
        res = None
        exp = "\nYou cannot go out of the map."
        try:
            move_is_legal(dungeon_map, DisplayFactory.create_display_strategy("symbolic"), row, column)
        except Exception as e:
            res = str(e)

        self.assertEqual(res, exp)

    def test_if_move_is_legal_exception_raises_when_column_is_negative(self):
        dungeon_map = [['.']]

        row = 0
        column = -1
        res = None
        exp = "\nYou cannot go out of the map."
        try:
            move_is_legal(dungeon_map, DisplayFactory.create_display_strategy("symbolic"), row, column)
        except Exception as e:
            res = str(e)

        self.assertEqual(res, exp)

    def test_if_move_is_legal_raises_exception_when_row_is_equal_or_bigger_than_dungeon_map_length(self):
        dungeon_map = [['.']]
        row = len(dungeon_map)
        column = 0
        res = None
        exp = "\nYou cannot go out of the map."
        try:
            move_is_legal(dungeon_map, DisplayFactory.create_display_strategy("symbolic"), row, column)
        except Exception as e:
            res = str(e)

        self.assertEqual(res, exp)

    def test_if_move_is_legal_raises_exception_when_column_is_equal_or_bigger_than_dungeon_map_length(self):
        dungeon_map = [['.']]

        row = 0
        column = len(dungeon_map[row])
        res = None
        exp = "\nYou cannot go out of the map."
        try:
            move_is_legal(dungeon_map, DisplayFactory.create_display_strategy("symbolic"), row, column)
        except Exception as e:
            res = str(e)

        self.assertEqual(res, exp)

    def test_if_move_is_legal_raises_exception_when_position_is_a_wall(self):
        dungeon_map = [['#']]

        row = 0
        column = 0
        res = None
        exp = "\nThere is a wall. You cannot go there."
        try:
            move_is_legal(dungeon_map, DisplayFactory.create_display_strategy("symbolic"), row, column)
        except Exception as e:
            res = str(e)

        self.assertEqual(res, exp)

    def test_if_move_is_legal_raises_exception_when_position_is_a_spawn_zone(self):
        dungeon_map = [['S']]

        row = 0
        column = 0
        res = None
        exp = "\nYou cannot enter the Spawn Zone"
        try:
            move_is_legal(dungeon_map, DisplayFactory.create_display_strategy("symbolic"), row, column)
        except Exception as e:
            res = str(e)

        self.assertEqual(res, exp)

    def test_if_reset_hero_attributes_works_correctly(self):
        hero = Hero()
        hero.MAX_MANA = 100
        hero.MAX_HEALTH = 100

        reset_hero_attributes(hero)
        self.assertEqual(hero.health, 100)
        self.assertEqual(hero.mana, 100)

    def test_if_reached_the_exit_works_when_at_the_exit(self):
        position = 'G'
        res = reached_exit(position, 'G')
        self.assertTrue(res)

    def test_if_reached_the_exit_works_when_not_at_the_exit(self):
        position = '.'
        res = reached_exit(position, 'G')
        self.assertFalse(res)

if __name__ == '__main__':
    unittest.main()
