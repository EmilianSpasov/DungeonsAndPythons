from entities.display.base import BaseDisplay

class SymbolicDisplay(BaseDisplay):
    def get_hero(self):
        return 'H'
    
    def get_enemy(self):
        return 'E'
    
    def get_obstacle(self):
        return '#'
    
    def get_treasure(self):
        return 'T'
    
    def get_goal(self):
        return 'G'
    
    def get_path(self):
        return '.'
    
    def get_spawn(self):
        return 'S'