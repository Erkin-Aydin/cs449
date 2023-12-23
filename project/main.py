import sys
sys.path.append('./pyorca/')

import gymnasium as gym
from robotic import ry
from pyorca import Agent, get_avoidance_velocity, orca, normalized, perp
from numpy import array, sqrt, rint, linspace, pi, cos, sin
import time
import random
import pygame
import do_mpc as mpc

N_AGENTS = 8
RADIUS = .3
MAX_SPEED = 0.35

positions1 = [(-0.5, -3.5), (2.0, -2.5), (3.5, -2.5), (4.5, -1.5), (3.5, 0.5), (4.5, 2.0), (3.0, 2.5), (1.0, 2.5)]
positions2 = [(0.5, -2.5), (2.0, -3.5), (4.5, -3.5), (3.5, -1.5), (4.2, -0.2), (3.5, 2.0), (1.0, 3.5), (3.0, 3.5)]
goal_positions = [(0.5, -2.5), (2.0, -3.5), (4.5, -3.5), (3.5, -1.5), (4.2, -0.2), (3.5, 2.0), (1.0, 3.5), (3.0, 3.5)]
isStage1 = [True, True, True, True, True, True, True, True]
#for 4 agents
#initial_positions = [(2.0, 2.0), (2.0, -2.0), (-2.0, -2.0), (-2.0, 2.0)]
#goal_positions = [(-2.0, -2.0), (-2.0, 2.0), (2.0, 2.0), (2.0, -2.0)]

agents = []
for i in range(N_AGENTS):

    vel = 0
    if(i == 0):
        vel = (-0.55, -0.55)
    elif(i == 1):
        vel = (-0.55, 0.55)
    elif(i == 2):
        vel = (0.55, 0.55)
    elif(i == 3):
        vel = (0.55, -0.55)
    elif(i == 4):
        vel = (0.0, -0.75)
    elif(i == 5):
        vel = (0.0, 0.75)
    elif(i == 6):
        vel = (-0.75, 0.0)
    elif(i == 7):
        vel = (0.75, 0.0)
    
    #                   position          initial vel. radius, max speed, preferred vel.
    pref_vel = array(vel)
    agents.append(Agent(positions1[i], vel, .3, MAX_SPEED,  pref_vel))

C = ry.Config()
C.addFile('world.g')
C.view()
qHome = C.getJointState()
C.setJointState(qHome)

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
                

    C.view()

print('Running simulation')

