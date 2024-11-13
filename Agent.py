from abc import ABC, abstractmethod
import random

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
        # state of agent includes the interpretation it has of the precept
        self.state = Agent_State()
        # the action instance is similar to action space definition
        self.action = Action()
        
        
    def interpret_input(self, percept):
        # if the agent is sleep it can't interpret anything!
        if self.state.is_sleep:
            return
        else:
            #if it is not sleep then itt should update its own state
            if "loc" in self.sensors:
                self.state.location = percept["loc"]
            if "is_dirty" in self.sensors:
                self.state.is_dirty = percept["is_dirty"]
        
    # the step method is going to receive the percept and output the action it wants to implemeent on the environment    
    def step(self, percept):
        # first it should interpret the perception and update its state
        self.interpret_input(percept)
        # there is a suck command and the next tile the agent wants to go to as the output action
        suck_command = False
        next_move = None
        
        # if agent is not sleep then it needs to process some information
        if not self.state.is_sleep:
            # sensor related to the suck command
            suck_command = self.action.suck(self.sensors, self.state.is_dirty)
            
            # sensor related to the output movement
            # if it has location sensor then the agent is not going to go to wall
            if "loc" in self.sensors:
                # if the agent is at the top most tile then  there is only one way to go
                if self.state.location == (0, 1):
                    next_move = "down"
                # if the agent is at the right most tile then  there is only one way to go
                elif self.state.location == (1, 0):
                    next_move = "left"
                # if it is at the middle point then it should randomly select to go up or right
                elif self.state.location == (0, 0):
                    next_move = random.choice(self.action.movement[:2])
            # but if it doesnt know its lcoation then it would randomly choose one of 4 movements
            else:
                next_move =  random.choice(self.action.movement)
            
        return suck_command, next_move
    

# this class is equivalent to the action space
class Action():
    def __init__(self):
        self.movement = ["up", "right", "left", "down"]
        
    def suck(self, sensors, is_dirty):
        command = False
        # if the tile is already clean then it doesn't have to clean
        if "is_dirty" in sensors:
                if is_dirty:
                    command = True
        else:
            command = True
        return command
        
    def sleep(self):
        return False
    
# the interpretation the agent has of its percept    
class Agent_State():
    def __init__(self):
        self.location = (0, 0)
        self.is_dirty = True
        self.is_sleep = False
