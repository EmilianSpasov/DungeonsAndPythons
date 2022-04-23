from entities.display.base import BaseDisplay

class EmojiDisplay(BaseDisplay):
    def get_hero(self):
        return '\U0001F9DD'
    
    def get_enemy(self):
        return '\U0001F9DF'
        
    def get_obstacle(self):
        return '\U0001F9F1'

    def get_treasure(self):
        return '\U00002753'
    
    def get_goal(self):
        return '\U0001F3C1'

    def get_path(self):
        return '\U0001F532'
    
    def get_spawn(self):
        return '\U0001F300' 