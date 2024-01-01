import sys
sys.path.append('./pyorca/')

from robotic import ry
from pyorca import Agent, orca
from numpy import array, sqrt
import time
import pygame
import numpy as np

N_AGENTS = 4
RADIUS = .25
MAX_SPEED = 0.30

positions1 = [(0.5, -2.5), (3.5, -3.5), (3.5, 2.5), (4.5, -0.5)]
positions2 = [(-0.5, -3.5),  (2.5, -2.5), (4.5, 2.5), (3.5, -0.5)]
goal_positions = [(0.5, -2.5), (3.5, -3.5), (3.5, 2.5), (4.5, -0.5)]
isStage1 = [True,True,True,True]

"""
positions1 = [(0.5, -2.5)]
positions2 = [(-0.5, -3.5)]
goal_positions = [(0.5, -2.5)]
isStage1 = [True,True]
"""
agents = []
for i in range(N_AGENTS):
    vel = 2
    pref_vel = array(vel)
    agents.append(Agent(positions1[i], vel, .3, MAX_SPEED,  vel))

C = ry.Config()
C.addFile('world.g')
C.addFile('obstacles.g')
C.view()

#C2 = ry.Config()
#C2.addFile('world.g')


time.sleep(2)

FPS = 20
dt = 1/FPS
tau = 5
clock = pygame.time.Clock()
running = True
accum = 0
all_lines = [[]] * len(agents)
area_num = 1;
while running:
    if(area_num > 4):
        break
    qNow = C.getJointState()
    komo = ry.KOMO(C, 1, 1, 4, True)
    komo.addControlObjective([], 0, 1e-1)
    komo.addControlObjective([], 2, 1e0)
    komo.addObjective([], ry.FS.accumulatedCollisions, [], ry.OT.eq, [1e2])
    komo.addObjective([1], ry.FS.positionDiff, ['base', 'goal_area' + str(area_num)], ry.OT.eq, [1e2])
    ret = ry.NLP_Solver(komo.nlp(), verbose=0).solve()

    qT = komo.getPath()[0]
    i = 0
    path = 0
    print("Finding RRT path...")
    while True:
        i = i + 1
        rrt = ry.PathFinder()
        rrt.setProblem(C, [qNow], [qT])
        ret = rrt.solve()
        path = ret.x
        if hasattr(ret, 'x') and isinstance(ret.x, np.ndarray) and ret.x.ndim == 2 and ret.x.shape[0] > 0:
            break
    
    print("RRT path found!\nCalculating the optimal path using a second KOMO...")
    komo2 = ry.KOMO(C, 1, path.shape[0], 4, True)
    komo2.addControlObjective([], 0, 1e-1)
    komo2.addControlObjective([], 2, 1e0)
    komo2.addObjective([], ry.FS.accumulatedCollisions, [], ry.OT.eq, [1e2])
    komo2.addObjective([1], ry.FS.positionDiff, ['base', 'goal_area' + str(area_num)], ry.OT.eq, [1e2])
    komo2.initWithPath_qOrg(path)
    print("Optimal path calculated!")
    ret = ry.NLP_Solver(komo2.nlp(), verbose=0).solve()
    komoPath = komo2.getPath()
    min = 20;
    if min > komoPath.shape[0]:
        min = komoPath.shape[0]
    for i in range(0, min):
        C.setJointState(komoPath[i])
        
        new_vels = [None] * len(agents)
        
        for i, agent in enumerate(agents):
            pos_dif = goal_positions[i] - agents[i].position
            magnitude = sqrt(pos_dif[0]**2 + pos_dif[1]**2)
            direction = pos_dif / magnitude
            if(magnitude > MAX_SPEED):
                pos_dif = direction * MAX_SPEED
            agent.pref_velocity = pos_dif
        
        for i, agent in enumerate(agents):
            candidates = agents[:i] + agents[i + 1:]
            new_vels[i], all_lines[i] = orca(agent, candidates, tau, dt)
        
        for i, agent in enumerate(agents):
            agent.velocity = new_vels[i]
            agent_str = 'a' + str(i)
            agent.position = agent.position + agent.velocity * dt
            C.setJointState([agent.position[0] - positions1[i][0] ,agent.position[1] - positions1[i][1], 0], [agent_str])
            if -0.001 < (agent.velocity * dt)[0] < 0.001 and -0.001 < (agent.velocity * dt)[1] < 0.001:
                if isStage1[i]:
                    isStage1[i] = False
                    goal_positions[i] = positions1[i]
                else:
                    isStage1[i] = True
                    goal_positions[i] = positions2[i]
                #define a path finding problem
        
        C.view(False, f'waypoints{i}')

        time.sleep(0.02)
    if(min < 4):
        area_num = area_num + 1
    accum += clock.tick(FPS)
    while accum >= dt * 1000:
        accum -= dt * 1000

    C.view()

print('Simulation Done!')