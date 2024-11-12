from abc import ABC, abstractmethod
import random
from result import Result

class Abstract_Agent(ABC):
    @abstractmethod
    def __init__(self):
        pass
        
    @abstractmethod
    def step(self, percept):
        pass

    
class Simple_Ref_Agent(Abstract_Agent):
    def __init__(self, sensors, state):
        super().__init__()
        self.sensors = sensors
        self.state = state
        self.action = Action()
        self.result = Result()
        self.directions = [Action.up, Action.down, Action.left, Action.right]
        
    def step(self, percept):
        if self.state == "on":
            # state sensor
            if "state" in self.sensors:
                if percept.state == "dirty":
                    self.action.clean(percept.room) 
            else:
                self.action.clean(percept.room)
            
            # location sensor
            if "location" in self.sensors:
                if percept.location == [0, 1] or percept.location == (1, 0):
                    new_location = (0, 0)
                elif percept.lcoation == (0, 0):
                    new_location = random.choice([(0, 1), (1, 0)])
            else:
                new_location = percept.location + random.choice(self.directions)
            return percept.state, new_location
                
                
        elif self.state == "sleep": 
            return percept.state, percept.location
    

class Action():
    def clean(self, room):
        room.state = "clean"
        
    def sleep(self):
        self.state = "off"
        
    def up(self, location):
        return location + (0, 1)
    
    def down(self, location):
        return location + (0, -1)
    
    def right(self, location):
        return location + (1, 0)
    
    def left(self, location):
        return location + (-1, 0)
        
