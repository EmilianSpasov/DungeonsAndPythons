from helpers_and_utilities.display.emoji import EmojiDisplay
from helpers_and_utilities.display.symbolic import SymbolicDisplay
from helpers_and_utilities.display.constants import SYMBOLIC, EMOJI

class DisplayFactory:
    @staticmethod
    def create_display_strategy(display_type="symbolic"):
        if display_type == SYMBOLIC:
            return SymbolicDisplay()
        elif display_type == EMOJI:
            return EmojiDisplay()
        
        return SymbolicDisplay()
