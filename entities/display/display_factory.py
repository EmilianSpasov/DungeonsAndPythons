from entities.display.emoji import EmojiDisplay
from entities.display.symbolic import SymbolicDisplay
from entities.display.constants import SYMBOLIC, EMOJI

class DisplayFactory:
    @staticmethod
    def create_display_strategy(display_type="symbolic"):
        if display_type == SYMBOLIC:
            return SymbolicDisplay()
        elif display_type == EMOJI:
            return EmojiDisplay()
        
        return SymbolicDisplay()
