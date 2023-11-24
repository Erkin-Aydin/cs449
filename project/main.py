import sys
sys.path.append('./pyorca/')

import gymnasium as gym
from robotic import ry
from pyorca import Agent, get_avoidance_velocity, orca, normalized, perp
from numpy import array, rint, linspace, pi, cos, sin
import time
import random
import pygame


N_AGENTS = 4
RADIUS = .3
SPEED = 1

initial_positions = [(2.0, 2.0), (2.0 -2.0), (-2.0, -2.0), (-2.0, 2.0)]
agents = []
for i in range(N_AGENTS):
    theta = 2 * pi * i / N_AGENTS
    x = RADIUS * array((cos(theta), sin(theta))) #+ random.uniform(-1, 1)
    vel = normalized(-x) * SPEED
    if(i == 0):
        vel = (-0.5, -0.5)
    elif(i == 1):
        vel = (-0.5, 0.5)
    elif(i == 2):
        vel = (0.5, 0.5)
    elif(i == 3):
        vel = (0.5, -0.5)
    #                   position          initial vel. radius, max speed, preferred vel.
    agents.append(Agent(initial_positions[i], vel, 0.3, SPEED, vel))

C = ry.Config()
C.addFile('world.g')

qHome = C.getJointState()
C.setJointState(qHome)



def draw_orca_circles(a, b):
    for x in linspace(0, tau, 21):
        if x == 0:
            continue
        #TODO
        """
        C.delFrame('circle' + str(x))
        C.addFrame('circle' + str(x)) \
            .setPosition([0, 0, .25]) \
            .setShape(ry.ST.ssCylinder, size=[.5, .5, .5, .05]) \
            .setColor([1, .5, 0]) \
            .setMass(.1) \
            .setContact(True)
        print("dsfaf")
        """
        #pygame.draw.circle(screen, pygame.Color(0, 0, 255), rint((-(a.position - b.position) / x + a.position) * scale + O).astype(int), int(round((a.radius + b.radius) * scale / x)), 1)
"""
def draw_velocity(a):
    #TODO
    pygame.draw.line(screen, pygame.Color(0, 255, 255), rint(a.position * scale + O).astype(int), rint((a.position + a.velocity) * scale + O).astype(int), 1)
    # pygame.draw.line(screen, pygame.Color(255, 0, 255), rint(a.position * scale + O).astype(int), rint((a.position + a.pref_velocity) * scale + O).astype(int), 1)
"""
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
        for i, agent in enumerate(agents):
            candidates = agents[:i] + agents[i + 1:]
            # print(candidates)
            new_vels[i], all_lines[i] = orca(agent, candidates, tau, dt)
            # print(i, agent.velocity)

        for i, agent in enumerate(agents):
            agent.velocity = new_vels[i]
            agent_str = 'a' + str(i)
            agent.position = agent.position + agent.velocity * dt
            C.setJointState([agent.position[0], agent.position[1], 0], [agent_str])
    
    for agent in agents[1:]:
        draw_orca_circles(agents[0], agent)
    """
    for agent, color in zip(agents, itertools.cycle(colors)):
        draw_agent(agent, color)
        draw_velocity(agent)
        # print(sqrt(norm_sq(agent.velocity)))
    """
    # Draw ORCA line and normal to ORCA line
    #TODO
    """
    for line in all_lines[0]:
        alpha = agents[0].position + line.point + perp(line.direction) * 100
        beta = agents[0].position + line.point + perp(line.direction) * -100
        # Update Rai configuration instead of pygame drawing
        C.delFrame('line_alpha')
        C.addFrame('line_alpha', alpha)
        C.delFrame('line_beta')
        C.addFrame('line_beta', beta)

        gamma = agents[0].position + line.point
        delta = agents[0].position + line.point + line.direction
        # Update Rai configuration instead of pygame drawing
        C.delFrame('line_gamma')
        C.addFrame('line_gamma', gamma)
        C.delFrame('line_delta')
        C.addFrame('line_delta', delta)
    """
    C.view()
    #TODO
    #pygame.display.flip()
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    """
print('Running simulation')

