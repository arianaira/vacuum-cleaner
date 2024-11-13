from abc import ABC, abstractmethod
import random
from result import Result

class Abstract_Agent(ABC):
    @abstractmethod
    def __init__(self, sensors):
        self.sensors = sensors
    
    @abstractmethod
    def interpret_input(self, percept):
        pass
        
    @abstractmethod
    def step(self, percept):
        pass

    
class Simple_Ref_Agent(Abstract_Agent):
    def __init__(self, sensors):
        super().__init__(sensors)
        self.state = Agent_State()
        self.action = Action()
        
        
    def interpret_input(self, percept):
        if self.state.is_sleep:
            return
        else:
            if "loc" in self.sensors:
                self.state.location = percept["loc"]
            if "is_dirty" in self.sensors:
                self.state.is_dirty = percept["is_dirty"]
        
        
    def step(self, percept):
        self.interpret_input(percept)
        suck_command = False
        next_move = None
        
        if not self.is_sleep:
            # state sensor
            suck_command = self.action.suck(percept.is_dirty)
            
            # location sensor
            if "loc" in self.sensors:
                if self.state.location == (0, 1):
                    next_move = "down"
                if self.state.location == (1, 0):
                    next_move = "left"
                elif self.state.location == (0, 0):
                    next_move = random.choice(self.action.movement[:2])
            else:
                next_move =  random.choice(self.action.movement)
            
        return suck_command, next_move
    

class Action():
    def __init__(self):
        self.movement = ["up", "right", "left", "down"]
        
    def suck(self):
        command = False
        if "is_dirty" in self.sensors:
                if self.state.is_dirty:
                    command = True
        return command
        
    def sleep(self):
        self.state = "off"
    
    
class Agent_State():
    def __init__(self):
        self.location = (0, 0)
        self.is_dirty = True
        self.is_sleep = False
