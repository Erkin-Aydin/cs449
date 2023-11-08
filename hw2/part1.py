from robotic import ry
import numpy as np
import time

C = ry.Config()
C.addFile('Gfiles/cargobot_base.g')
C.addFile('Gfiles/maze.g')

qHome = C.getJointState()
C.setJointState(qHome)
komo = ry.KOMO(C, 1, 10, 2, True)

komo.addControlObjective([], 1, 1e-1)
komo.addControlObjective([], 2, 1e0)

komo.addObjective([], ry.FS.accumulatedCollisions, [], ry.OT.eq,[1e2])
komo.addObjective([1], ry.FS.positionDiff, ['base', 'goal_area'], ry.OT.eq, [1e1])
komo.addObjective([1], ry.FS.jointState, [], ry.OT.eq, [1e1], [], order=1)

ret = ry.NLP_Solver(komo.nlp(), verbose=0 ) .solve()
print(ret)
q = komo.getPath()

print('size of path:', q.shape)

for t in range(q.shape[0]):
    C.setJointState(q[t])
    C.view(False, f'waypoint {t}')
    time.sleep(.1)

# that's the goal configuration
qT = komo.getPath()[-1]
C.setJointState(qT)
C.view(False, "IK solution")

#define a path finding problem
rrt = ry.PathFinder()
rrt.setProblem(C, [qHome], [qT])

ret = rrt.solve()
print(ret)
path = ret.x

komo2 = ry.KOMO(C, 1, 10, 2, True)
komo2.addControlObjective([], 1, 1e-1)
komo2.addControlObjective([], 2, 1e0)

komo2.addObjective([], ry.FS.accumulatedCollisions, [], ry.OT.eq,[1e2])
komo2.addObjective([1], ry.FS.positionDiff, ['base', 'goal_area'], ry.OT.eq, [1e1])
komo2.addObjective([1], ry.FS.jointState, [], ry.OT.eq, [1e1], [], order=1)

ret = ry.NLP_Solver(komo2.nlp(), verbose=0 ) .solve()
print(ret)
q = komo2.getPath()

print('size of path:', q.shape)

for t in range(q.shape[0]):
    C.setJointState(q[t])
    C.view(False, f'waypoint {t}')
    time.sleep(.1)

# that's the goal configuration
qT = komo2.getPath()[-1]
C.setJointState(qT)

#define a path finding problem
rrt = ry.PathFinder()
rrt.setProblem(C, [qHome], [qT])

ret = rrt.solve()
print(ret)
path = ret.x

komo2.initWithPath_qOrg(path)

# display the path
for t in range(0, path.shape[0]-1):
    C.setJointState(path[t])
    C.view()
    time.sleep(.1)

C.view()

