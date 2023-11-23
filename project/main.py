import gymnasium as gym
from robotic import ry
import rvo2
import numpy as np
import time

sim = rvo2.PyRVOSimulator(1/60., 1.5, 5, 1.5, 2, 0.4, 2)
C = ry.Config()
C.addFile('world.g')

qHome = C.getJointState()
C.setJointState(qHome)
C.view()
#time.sleep(500)

# Pass either just the position (the other parameters then use
# the default values passed to the PyRVOSimulator constructor),
# or pass all available parameters.
# Parameters: position, neighborDist, maxNeighbors, timeHorizon, timeHorizonObst, radius, maxSpeed, velocity
a0 = sim.addAgent((2, 2), 1.0, 5, 1.5, 2, 0.4, 0.002, (-0.1, -0.1))
a1 = sim.addAgent((2, -2), 1.0, 5, 1.5, 2, 0.4, 0.002, (-0.1, 0.1))
a2 = sim.addAgent((-2, 2), 1.0, 5, 1.5, 2, 0.4, 0.002, (0.1, -0.1))
a3 = sim.addAgent((-2, -2), 1.0, 5, 1.5, 2, 0.4, 0.002, (0.1, 0.1))

# Obstacles are also supported. Adding coordinates of its corners.
o1 = sim.addObstacle([(0.5, 0.5), (0.5, -0.5), (-0.5, -0.5), (-0.5, 0.5)])
sim.processObstacles()

#sets the preferred velocity for an agent.
sim.setAgentPrefVelocity(a0, (-0.1, -0.1))
sim.setAgentPrefVelocity(a1, (-0.1, 0.1))
sim.setAgentPrefVelocity(a2, (0.1, -0.1))
sim.setAgentPrefVelocity(a3, (0.1, 0.1))

a0.linearProgram3()
print('Simulation has %i agents and %i obstacle vertices in it.' %
      (sim.getNumAgents(), sim.getNumObstacleVertices()))

print('Running simulation')

for step in range(20):
    sim.doStep()

    for agent_no in (a0, a1, a2, a3):
        position = sim.getAgentPosition(agent_no)
        velocity = sim.getAgentVelocity(agent_no)
        position = [position[0], position[1], 0.0]
        agent_str = 'a' + str(agent_no)
        C.setJointState([position[0], position[1], position[2]], [agent_str])
        print('(%5.3f, %5.3f) (%5.3f, %5.3f)' % (position[0], position[1], velocity[0], velocity[1]))
        C.view()
        time.sleep(0.5)
    
    positions = ['(%5.3f, %5.3f)' % sim.getAgentPosition(agent_no)
                 for agent_no in (a0, a1, a2, a3)]
    print('step=%2i  t=%.3f  %s' % (step, sim.getGlobalTime(), '  '.join(positions)))