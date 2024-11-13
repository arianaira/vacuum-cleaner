from environment import State, Result, env
from Agent import Simple_Ref_Agent



state1 = State()
agent1 = Simple_Ref_Agent(sensors=["loc", "is_dirty"])
state1.add_agent(agent1, initial_loc = (0,0))
env1 = env(state1, loc_observability=True, dirt_observability=True, move_determinism=True, suck_determinism=True, static=True)

for i in range(100):
    res = env1.run()
    print('f1',res.f1,'f2', res.f2, 'f3',res.f3,'f4' ,res.f4,'f5 ', res.f5)
print(state1.tiles)


state2 = State()
agent2 = Simple_Ref_Agent(sensors=["loc", "is_dirty"])
state2.add_agent(agent2, initial_loc = (0,0))
env2 = env(state2, loc_observability=True, dirt_observability=True, move_determinism=True, suck_determinism=True, static=False)

for i in range(100):
    res = env2.run()
    print('f1',res.f1,'f2', res.f2, 'f3',res.f3,'f4' ,res.f4,'f5 ', res.f5)
print(state2.tiles)

state3 = State()
agent3 = Simple_Ref_Agent(sensors=["loc", "is_dirty"])
state3.add_agent(agent3, initial_loc = (0,0))
env3 = env(state3, loc_observability=True, dirt_observability=True, move_determinism=True, suck_determinism=False, static=True)

for i in range(100):
    res = env3.run()
    print('f1',res.f1,'f2', res.f2, 'f3',res.f3,'f4' ,res.f4,'f5 ', res.f5)
print(state3.tiles)

state4 = State()
agent4 = Simple_Ref_Agent(sensors=["loc", "is_dirty"])
state4.add_agent(agent4, initial_loc = (0,0))
env4 = env(state4, loc_observability=True, dirt_observability=True, move_determinism=True, suck_determinism=False, static=False)
for i in range(100):
    res = env4.run()
    print('f1',res.f1,'f2', res.f2, 'f3',res.f3,'f4' ,res.f4,'f5 ', res.f5)
print(state4.tiles)


state5 = State()
agent5 = Simple_Ref_Agent(sensors=["loc", "is_dirty"])
state5.add_agent(agent5, initial_loc = (0,0))
env5 = env(state5, loc_observability=True, dirt_observability=True, move_determinism=False, suck_determinism=True, static=True)

for i in range(100):
    res = env5.run()
    print('f1',res.f1,'f2', res.f2, 'f3',res.f3,'f4' ,res.f4,'f5 ', res.f5)
print(state5.tiles)


state6 = State()
agent6 = Simple_Ref_Agent(sensors=["loc", "is_dirty"])
state6.add_agent(agent6, initial_loc = (0,0))
env6 = env(state6, loc_observability=True, dirt_observability=True, move_determinism=False, suck_determinism=True, static=False)

for i in range(100):
    res = env6.run()
    print('f1',res.f1,'f2', res.f2, 'f3',res.f3,'f4' ,res.f4,'f5 ', res.f5)
print(state6.tiles)

state7 = State()
agent7 = Simple_Ref_Agent(sensors=["is_dirty"])
state7.add_agent(agent7, initial_loc = (0,0))
env7 = env(state7, loc_observability=False, dirt_observability=True, move_determinism=True, suck_determinism=True, static=True)

for i in range(100):
    res = env7.run()
    print('f1',res.f1,'f2', res.f2, 'f3',res.f3,'f4' ,res.f4,'f5 ', res.f5)
print(state7.tiles)


state8 = State()
agent8 = Simple_Ref_Agent(sensors=["is_dirty"])
state8.add_agent(agent8, initial_loc = (0,0))
env8 = env(state8, loc_observability=False, dirt_observability=True, move_determinism=True, suck_determinism=True, static=False)

for i in range(100):
    res = env8.run()
    print('f1',res.f1,'f2', res.f2, 'f3',res.f3,'f4' ,res.f4,'f5 ', res.f5)
print(state8.tiles)

state9 = State()
agent9 = Simple_Ref_Agent(sensors=["is_dirty"])
state9.add_agent(agent9, initial_loc = (0,0))
env9 = env(state9, loc_observability=False, dirt_observability=True, move_determinism=False, suck_determinism=True, static=True)
for i in range(100):
    res = env9.run()
    print('f1',res.f1,'f2', res.f2, 'f3',res.f3,'f4' ,res.f4,'f5 ', res.f5)
print(state9.tiles)

state10 = State()
agent10 = Simple_Ref_Agent(sensors=["is_dirty"])
state10.add_agent(agent10, initial_loc = (0,0))
env10 = env(state10, loc_observability=False, dirt_observability=True, move_determinism=False, suck_determinism=True, static=False)
for i in range(100):
    res = env10.run()
    print('f1',res.f1,'f2', res.f2, 'f3',res.f3,'f4' ,res.f4,'f5 ', res.f5)
print(state10.tiles)

state11 = State()
agent11 = Simple_Ref_Agent(sensors=["is_dirty"])
state11.add_agent(agent11, initial_loc = (0,0))
env11 = env(state11, loc_observability=False, dirt_observability=True, move_determinism=True, suck_determinism=False, static=True)
for i in range(100):
    res = env11.run()
    print('f1',res.f1,'f2', res.f2, 'f3',res.f3,'f4' ,res.f4,'f5 ', res.f5)
print(state11.tiles)

state12 = State()
agent12 = Simple_Ref_Agent(sensors=["is_dirty"])
state12.add_agent(agent12, initial_loc = (0,0))
env12 = env(state12, loc_observability=False, dirt_observability=True, move_determinism=True, suck_determinism=False, static=False)
for i in range(100):
    res = env12.run()
    print('f1',res.f1,'f2', res.f2, 'f3',res.f3,'f4' ,res.f4,'f5 ', res.f5)
print(state12.tiles)

state13 = State()
agent13 = Simple_Ref_Agent(sensors=["loc"])
state13.add_agent(agent13, initial_loc = (0,0))
env13 = env(state13, loc_observability=True, dirt_observability=False, move_determinism=True, suck_determinism=True, static=True)
for i in range(100):
    res = env13.run()
    print('f1',res.f1,'f2', res.f2, 'f3',res.f3,'f4' ,res.f4,'f5 ', res.f5)
print(state13.tiles) 

state14 = State()
agent14 = Simple_Ref_Agent(sensors=["loc"])
state14.add_agent(agent14, initial_loc = (0,0))
env14 = env(state14, loc_observability=True, dirt_observability=False, move_determinism=True, suck_determinism=True, static=False)
for i in range(100):
    res = env14.run()
    print('f1',res.f1,'f2', res.f2, 'f3',res.f3,'f4' ,res.f4,'f5 ', res.f5)
print(state14.tiles) 

state15 = State()
agent15 = Simple_Ref_Agent(sensors=["loc"])
state15.add_agent(agent15, initial_loc = (0,0))
env15 = env(state15, loc_observability=True, dirt_observability=False, move_determinism=False, suck_determinism=True, static=True)
for i in range(100):
    res = env15.run()
    print('f1',res.f1,'f2', res.f2, 'f3',res.f3,'f4' ,res.f4,'f5 ', res.f5)
print(state15.tiles) 

state16 = State()
agent16 = Simple_Ref_Agent(sensors=["loc"])
state16.add_agent(agent16, initial_loc = (0,0))
env16 = env(state16, loc_observability=True, dirt_observability=False, move_determinism=False, suck_determinism=True, static=False)
for i in range(100):
    res = env16.run()
    print('f1',res.f1,'f2', res.f2, 'f3',res.f3,'f4' ,res.f4,'f5 ', res.f5)
print(state16.tiles) 

state17 = State()
agent17 = Simple_Ref_Agent(sensors=["loc"])
state17.add_agent(agent17, initial_loc = (0,0))
env17 = env(state17, loc_observability=True, dirt_observability=False, move_determinism=True, suck_determinism=False, static=True)
for i in range(100):
    res = env17.run()
    print('f1',res.f1,'f2', res.f2, 'f3',res.f3,'f4' ,res.f4,'f5 ', res.f5)
print(state17.tiles) 

state18 = State()
agent18 = Simple_Ref_Agent(sensors=["loc"])
state18.add_agent(agent18, initial_loc = (0,0))
env18 = env(state18, loc_observability=True, dirt_observability=False, move_determinism=True, suck_determinism=False, static=False)
for i in range(100):
    res = env18.run()
    print('f1',res.f1,'f2', res.f2, 'f3',res.f3,'f4' ,res.f4,'f5 ', res.f5)
print(state18.tiles) 