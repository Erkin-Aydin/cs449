import sys
sys.path.append('./pyorca/')

import gymnasium as gym
from robotic import ry
from pyorca import Agent, get_avoidance_velocity, orca, normalized, perp
from numpy import array, sqrt, rint, linspace, pi, cos, sin
import time
import random
import pygame


N_AGENTS = 6
RADIUS = .3
MAX_SPEED = 0.5

#for 8 agents
#initial_positions = [(2.0, 2.0), (2.0, -2.0), (-2.0, -2.0), (-2.0, 2.0), (0.0, 3.5), (0.0, -3.5), (3.5, 0.0), (-3.5, 0.0)]
#goal_positions = [(-2.0, -2.0), (-2.0, 2.0), (2.0, 2.0), (2.0, -2.0), (0.0, -3.5), (0.0, 3.5), (-3.5, 0.0), (3.5, 0.0)]

#for 6 agents
initial_positions = [(2.0, 2.0), (2.0, -2.0), (-2.0, -2.0), (-2.0, 2.0), (0.0, 3.5), (0.0, -3.5)]
goal_positions = [(-2.0, -2.0), (-2.0, 2.0), (2.0, 2.0), (2.0, -2.0), (0.0, -3.5), (0.0, 3.5)]

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
    agents.append(Agent(initial_positions[i], vel, .3, MAX_SPEED,  pref_vel))

C = ry.Config()
C.addFile('world.g')
C.view()
qHome = C.getJointState()
C.setJointState(qHome)
"""
for i, agent in enumerate(agents):
    agent_str = 'a' + str(i)
    C.setJointState([agent.position[0], agent.position[1], 0], [agent_str])
"""
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
            print("i: ", i)
            print("agent pos:", agent.position)
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
            C.setJointState([agent.position[0] - initial_positions[i][0] ,agent.position[1] - initial_positions[i][1], 0], [agent_str])
        
    for line in all_lines[0]:
        alpha = agents[0].position + line.point + perp(line.direction) * 100
        beta = agents[0].position + line.point + perp(line.direction) * -100
        # Update Rai configuration instead of pygame drawing

        gamma = agents[0].position + line.point
        delta = agents[0].position + line.point + line.direction
        # Update Rai configuration instead of pygame drawing
    
    C.view()
    #TODO
    #pygame.display.flip()
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    """
print('Running simulation')

