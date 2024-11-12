from abc import ABC, abstractmethod
import random

class Abstract_Agent(ABC):
    @abstractmethod
    def __init__(self):

        
    @abstractmethod
    def action(self, percept):
        pass
    
    
class Simple_Ref_Agent(Abstract_Agent):
    def __init__(self, sensors, state):
        super().__init__()
        self.sensors = sensors
        self.state = state
        self.action = Action()
        self.directions = [Action.up, Action.down, Action.left, Action.right]
        
    def action(self, percept):
        if self.state == "on":
            # state sensor
            if "state" in self.sensors:
                if percept.state == "dirty":
                    self.action.clean(percept.room) 
            else:
                self.action.clean(percept.room)
            
            # location sensor
            if "location" in self.sensors:
                if percept.location == [0, 1] or percept.location == [1, 0]:
                    new_location = [0, 0]
                elif percept.lcoation == [0, 0]:
                    new_location = random.choice([[0, 1], [1, 0]])
            else:
                new_location = self.find_valid_move(percept.location)
            return percept.state, new_location
                
                
        elif self.state == "sleep": 
            return percept.state, percept.location
    
    
    def find_valid_move(self, location):
        for move in self.directions:
            new_location = move(location)
            if not is_wall(new_location):
                break
        return new_location
        
        
    

class Action():
    def clean(self, room):
        room.state = "clean"
        
    def sleep(self):
        self.state = "off"
        
    def up(self, location):
        return location + [0, 1]
    
    def down(self, location):
        return location + [0, -1]
    
    def right(self, location):
        return location + [1, 0]
    
    def left(self, location):
        return location + [-1, 0]
        