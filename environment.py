import random

class State:
   #  the state of the cleaning environment

    def __init__(self, tiles={(0,0):True, (0,1):True, (1,0):True}):
        """
        tiles (dict) has tile cordinations as key and their dirtiness as  a boolean value for example {(0,0):True, (0,1): True}
        agents (dict) has agent number as key and their location as value for example {1:(0,0), 2:(1,0)}
        agent_obj is a list containing all agent objects
        """
        self.tiles = tiles
        self.agents = {}
        self.agent_count =0
        self.agent_obj = []


    def add_agent(self, agent, initial_loc = (0,0)):
      agent_count = self.agent_count
      self.agent_count += agent_count+1

      if(initial_loc in self.tiles):
        self.agents[self.agent_count] = initial_loc

      else:
        self.agents[self.agent_count] = (0,0)

      self.agent_obj.append(agent)

    def clean_update(self, agent_number):
        # this function activates when agent does "clean" action
        agent_loc = self.agents[agent_number]
        print("clean_update_", agent_loc)
        self.tiles[agent_loc] = False

    def make_room_dirty(self):
        clean_rooms = [room for room, state in self.tiles.items() if not state]

        if clean_rooms:  # Check if there are any 'False' rooms
            # Randomly select one of the 'False' rooms
            room_to_change = random.choice(clean_rooms)

            # Generate a random number between 0 and 1
            if random.random() < 0.2:  # 20% probability
                self.tiles[room_to_change] = True  # Change to True / dirty
                print('randomly making room dirty')
                


    def movement_update(self, agent_number, direction):
        # this function activates when agent does any of movement actions
        # returns false when agent hits the wall
        # returns true when it makes a correct move
        agent_loc = self.agents[agent_number]
        print("mvmnt_update_ agent is at", agent_loc,' is moving ', direction)
        i = agent_loc[0]
        j = agent_loc[1]

        if (direction == "up"):
          if ((i,j+1) in self.tiles):
            self.agents[agent_number] = (i, j+1)
            return True
          else:
            return False

        elif (direction == "down"):
          if ((i,j-1) in self.tiles):
            self.agents[agent_number] = (i, j-1)
            return True
          else:
            return False

        elif (direction == "left"):
          if ((i-1,j) in self.tiles):
            self.agents[agent_number] = (i-1, j)
            return True
          else:
            return False

        elif (direction == "right"):
          if ((i+1,j) in self.tiles):
            self.agents[agent_number] = (i+1, j)
            return True
          else:
            return False

        return False


    def get_percept_for_agent(self, agent_number):
      #percept is a dictionary. for example {"loc":(1,1), "is_dirty":True}
      agent_loc = self.agents[agent_number]
      print("send_percept to agent at ", agent_loc)
      isdirty = self.tiles[agent_loc]
      percept = {"loc": agent_loc, "is_dirty": isdirty}
      return percept



# class Action:
#     """Defines actions that a specific cleaning agent can perform."""

#     def __init__(self, agent_number, env):
#         self.agent_number = agent_number
#         self.env = env

#     def move(self, direction):
#         self.env.move_agent(self.agent_number, direction)

#     def clean(self):
#         """Cleans the current position of the agent."""
#         self.env.clean_room(self.agent_number)

class Result:
    def __init__(self):
        self.f1 = 0 #all steps
        self.f2 = 0 #wall
        self.f3 = 0 #sucks
        self.f4 = 0 #all sucks
        self.f5 = 0 #all dirty rooms
        self.total = 0

    def fail(self):
        return

class env:
    def __init__(self, state, loc_observability, dirt_observability, move_determinism, suck_determinism, static):
        self.state = state
        self.loc_observability = loc_observability
        self.dirt_observability = dirt_observability
        self.move_determinism = move_determinism
        self.suck_determinism = suck_determinism,
        self.static = static

        self.res = Result()


    def clean_room(self, agent_number):
      self.res.f3 += 1
      if(self.suck_determinism==False):
          if random.random() < 0.2:  # 20% probability to not suck despite order of suck
            print(f"Agent {agent_number} intended to suck, but didn't.")
            return
      self.state.clean_update(agent_number)
      self.res.f4 +=1



    def move_agent(self, agent_number, direction):
      if(self.move_determinism==False):
          if random.random() < 0.2:  # 20% probability to change the direction of move
            # Choose a new direction randomly from the available options
            new_direction = random.choice(['up', 'down', 'left', 'right'])
            print(f"Agent {agent_number} intended to move {direction}, but moved {new_direction} instead.")
            direction = new_direction
      correct_move = self.state.movement_update(agent_number, direction)
      if not (correct_move):
        self.res.f2 += 1
      self.res.f1 += 1



    def send_percept_to_agent(self, agent_number):
      p = self.state.get_percept_for_agent(agent_number)
      if(self.loc_observability==False):
        return {"is_dirty":p["is_dirty"]}
      if(self.dirt_observability==False):
        return {"loc":p["loc"]}
      if(self.static == False):
        self.state.make_room_dirty()
      return p


    def run(self, step = 1):

      for i in range(step):
        for index, agent in enumerate(self.state.agent_obj, start=1):
          p = self.send_percept_to_agent(agent_number=index)
          suck_command, next_move = agent.step(percept = p)
          if (suck_command):
            self.clean_room(agent_number=index)
            print(self.state.tiles)
          if not (next_move is None):
            self.move_agent(agent_number= index, direction=next_move)
            print(self.state.tiles)

        dirty_rooms = 0
        for value in self.state.tiles.values():
          if value:  # If the value is True the room is dirty
              dirty_rooms += 1
        self.res.f5 += dirty_rooms

      return self.res

