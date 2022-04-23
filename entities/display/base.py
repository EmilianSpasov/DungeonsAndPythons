from abc import ABC, abstractmethod

class BaseDisplay(ABC):
    @abstractmethod
    def get_hero(self):
        pass
    
    @abstractmethod
    def get_enemy(self):
        pass
    
    @abstractmethod
    def get_obstacle(self):
        pass
    
    @abstractmethod
    def get_treasure(self):
        pass
    
    @abstractmethod
    def get_goal(self):
        pass
    
    @abstractmethod
    def get_path(self):
        pass
    
    @abstractmethod
    def get_spawn(self):
        pass