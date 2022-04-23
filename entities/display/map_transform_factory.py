from entities.display.constants import SYMBOLIC, EMOJI
from entities.display.emoji import EmojiDisplay
from entities.display.symbolic import SymbolicDisplay
from entities.display.display_factory import DisplayFactory

class MapTransformFactory:
    @staticmethod
    def create_map_transform(transform_type=SYMBOLIC):
        display = DisplayFactory.create_display_strategy(transform_type)
        return {
            'H': display.get_hero(),
            'E': display.get_enemy(),
            'T': display.get_treasure(), 
            'G': display.get_goal(),
            'S': display.get_spawn(),
            '.': display.get_path(), 
            '#': display.get_obstacle(),  
        }