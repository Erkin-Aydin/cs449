from robotic import ry
import numpy as np
import time

C = ry.Config()
C.addFile('cargobot_base.g')
C.addFile('cargo.g')
C.addFile('maze.g')

qHome = C.getJointState()
C.setJointState(qHome)

komo = ry.KOMO(C, 1, 1, 2, True)
komo.addControlObjective([], 0, 1e-1)
komo.addControlObjective([], 2, 1e0)
komo.addObjective([], ry.FS.accumulatedCollisions, [], ry.OT.eq, [1e2])
komo.addObjective([1], ry.FS.positionDiff, ['base', 'goal_area'], ry.OT.eq, [1e2])
komo.addObjective([1], ry.FS.jointState, [], ry.OT.eq, [1e2], [], order=1)


ret = ry.NLP_Solver(komo.nlp(), verbose=0).solve()
print(ret)
q = komo.getPath()
print('size of path:', q.shape)

qT = komo.getPath()[0]
C.setJointState(qT)
C.view(False, "IK solution")

#define a path finding problem
rrt = ry.PathFinder()
rrt.setProblem(C, [qHome], [qT])

for i in range(0, 2):
    ret = rrt.solve()
    print("rettttt: ", ret)
    path = ret.x
    print("path size:", path.shape[0])

C.setJointState(qHome)
komo2 = ry.KOMO(C, 1, path.shape[0], 2, True)
komo2.addControlObjective([], 0, 1e-1)
komo2.addControlObjective([], 2, 1e0)
komo2.addObjective([], ry.FS.accumulatedCollisions, [], ry.OT.eq, [1e2])
komo2.addObjective([1], ry.FS.positionDiff, ['base', 'goal_area'], ry.OT.eq, [1e2])
komo2.addObjective([1], ry.FS.jointState, [], ry.OT.eq, [1e1], [], order=1)
print(1)
komo2.initWithPath_qOrg(path)
print(2)
ret = ry.NLP_Solver(komo2.nlp(), verbose=0).solve()
print("ret,", ret)
print(3)
q = komo2.getPath()
print('last path:', q)

# display the path
for i in range(0, q.shape[0] - 1):
    C.setJointState(q[i])
    C.view()
    time.sleep(0.02)

C.view()