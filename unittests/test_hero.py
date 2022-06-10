import unittest
import sys

sys.path.append('..')

from entities.hero import Hero
from items.spell import Spell
from items.weapon import Weapon


class TestHeroClass(unittest.TestCase):

    def test_if_know_as_works_as_expected(self):
        h = Hero()
        exp = 'Hero the No title'
        self.assertEqual(h.known_as(), exp)


if __name__ == '__main__':
    unittest.main()
