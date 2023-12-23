import sys
sys.path.append('./pyorca/')

import gymnasium as gym
from robotic import ry
from pyorca import Agent, get_avoidance_velocity, orca, normalized, perp
from numpy import array, sqrt, rint, linspace, pi, cos, sin
import time
import random
import pygame
import numpy as np
#import do_mpc as mpc

N_AGENTS = 2
RADIUS = .3
MAX_SPEED = 0.55

positions1 = [(0.5, -2.5), (3.5, -2.5)]
positions2 = [(-0.5, -3.5),  (4.5, -3.5)]
goal_positions = [(0.5, -2.5), (4.5, -3.5)]
isStage1 = [True,True]
#for 4 agents
#for 4 agents
#initial_positions = [(2.0, 2.0), (2.0, -2.0), (-2.0, -2.0), (-2.0, 2.0)]
#goal_positions = [(-2.0, -2.0), (-2.0, 2.0), (2.0, 2.0), (2.0, -2.0)]

agents = []
for i in range(N_AGENTS):

    vel = 2

    #                   position          initial vel. radius, max speed, preferred vel.
    pref_vel = array(vel)
    agents.append(Agent(positions1[i], vel, .3, MAX_SPEED,  vel))

C = ry.Config()
C.addFile('world.g')
C.view()
qHome = C.getJointState()
C.setJointState(qHome)
komo = ry.KOMO(C, 1, 1, 2, True)
komo.addControlObjective([], 0, 1e-1)
komo.addControlObjective([], 2, 1e0)
komo.addObjective([], ry.FS.accumulatedCollisions, [], ry.OT.eq, [1e2])
komo.addObjective([1], ry.FS.positionDiff, ['base', 'goal_area'], ry.OT.eq, [1e2])

ret = ry.NLP_Solver(komo.nlp(), verbose=0).solve()
print(ret)
q = komo.getPath()
print('size of path:', q.shape)

qT = komo.getPath()[0]
C.setJointState(qT)
#C.view(False, "IK solution")






time.sleep(5)

FPS = 20
dt = 1/FPS
tau = 5

clock = pygame.time.Clock()
running = True
accum = 0
all_lines = [[]] * len(agents)
while running:
    accum += clock.tick(FPS)
    time.sleep(0.1)
    rrt = ry.PathFinder()
    i = 0
    while True:
        i = i + 1
        print(i)
        rrt.setProblem(C, [qHome], [qT])
        ret = rrt.solve()
        path = ret.x
        print("rettttt: ", ret)
        #print("path size:", path)
        # display the path
        if ret.x.ndim == 2 and ret.x.shape[0] > 0:
            for t in range(0, path.shape[0] - 1):
                print("üffff: ", path[t])
                C.setJointState(path[t])
                C.view()
                time.sleep(0.002)
            break
    C.setJointState(qHome)
    komo2 = ry.KOMO(C, 1, path.shape[0], 2, True)
    komo2.addControlObjective([], 0, 1e-1)
    komo2.addControlObjective([], 2, 1e0)
    komo2.addObjective([], ry.FS.accumulatedCollisions, [], ry.OT.eq, [1e2])
    komo2.addObjective([1], ry.FS.positionDiff, ['base', 'goal_area'], ry.OT.eq, [1e2])
    komo2.initWithPath_qOrg(path)

    ret = ry.NLP_Solver(komo2.nlp(), verbose=0).solve()
    q = komo2.getPath()
    print('last path:', q)

    # display the path for part 1
    for i in range(0, q.shape[0]):
        C.setJointState(q[i])
        C.view(False, f'waypoints{i}')
        time.sleep(0.02)

    while accum >= dt * 1000:
        accum -= dt * 1000

        new_vels = [None] * len(agents)

        #calculation of the new velocities for the goal positions
        
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
            print((agent.velocity * dt)[0])
            print((agent.velocity * dt)[1])
            C.setJointState([agent.position[0] - positions1[i][0] ,agent.position[1] - positions1[i][1], 0], [agent_str])
            if -0.001 < (agent.velocity * dt)[0] < 0.001 and -0.001 < (agent.velocity * dt)[1] < 0.001:
                print("obaa")
                if isStage1[i]:
                    isStage1[i] = False
                    goal_positions[i] = positions1[i]
                else:
                    isStage1[i] = True
                    goal_positions[i] = positions2[i]
                #define a path finding problem
       

    C.view()

print('Running simulation')

