from robotic import ry
import numpy as np
import time

C = ry.Config()
C.addFile('cargobot_base.g')
C.addFile('maze.g')

qHome = C.getJointState()

C.setJointState(qHome)
komo = ry.KOMO(C, 1, 1, 2, True)
#komo.addControlObjective([], 0, 1e-1) 
komo.addControlObjective([], 1, 1e0)
komo.addObjective([], ry.FS.accumulatedCollisions, [], ry.OT.eq,[1e-1]);
komo.addObjective([], ry.FS.positionDiff, ['base', 'goal_area'], ry.OT.eq, [1e1])
komo.addObjective([], ry.FS.jointState, [], ry.OT.eq, [1e1], [], order=1)

ret = ry.NLP_Solver(komo.nlp(), verbose=0 ) .solve()
qT = komo.getPath()[-1]
q = komo.getPath()
print('size of path:', q.shape)

#C.setJointState(qT)
C.view(False, "IK solution")

#define a path finding problem
rrt = ry.PathFinder()
rrt.setProblem(C, [qHome], [qT])

for i in range(10):
    ret = rrt.solve()
    path = ret.x
    print("path size:", path.shape[0])
    # display the path
    for t in range(0, path.shape[0] - 1):
        C.setJointState(path[t])
        C.view()
        time.sleep(0.002)

C.setJointState(path[0])
komo2 = ry.KOMO(C, 1, path.shape[0], 2, True)
komo2.addControlObjective([], 0, 1e-1)
komo2.addControlObjective([], 2, 1e0)
komo2.addObjective([], ry.FS.accumulatedCollisions, [], ry.OT.eq, [1e1])
komo2.addObjective([], ry.FS.positionDiff, ['base', 'goal_area'], ry.OT.eq, [1e1])
komo2.addObjective([], ry.FS.jointState, [], ry.OT.eq, [1e1], [], order=1)
komo2.initWithPath_qOrg(path)

ret = ry.NLP_Solver(komo2.nlp(), verbose=0).solve()
print(ret)
q = komo2.getPath()
print('size of path:', q.shape)

qT = komo2.getPath()[-1]

rrt.setProblem(C, [qHome], [qT])

# display the path
for t in range(0, qT.shape[0]):
    C.setJointState(qT[t])
    C.view()
    time.sleep(0.02)

C.view()
