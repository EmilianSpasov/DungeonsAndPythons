import sys
import tty
import termios
from helpers_and_utilities.verification_mixin import VerificationMixin
from helpers_and_utilities.utils import clear_screen

class _Getch:
    def __call__(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


def check_arrow_key(key, get_key):
    if key == '\x1b':
        new_key = f'{key}{get_key()}{get_key()}'
        return new_key
    return key


def get_key_input(dicts):
    get_key = _Getch()
    key_combination = check_arrow_key(key_combination, get_key())
    
    while not VerificationMixin.is_command_valid(dicts, key_combination):
        key_combination = check_arrow_key(key_combination, get_key())

    value = dicts[key_combination]
    return value
