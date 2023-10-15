from robotic import ry
import time
C = ry.Config()
C.addFile(ry.raiPath('../rai-robotModels/objects/kitchen.g'))
C.addFile('part5.g')

C.addFrame(name="item1", parent="sink1") \
    .setShape(ry.ST.ssBox, size=[0.1, 0.1, 0.25, 0.02]) \
    .setRelativePosition([-.1, -.1, .52]) \
    .setColor([1, 0, 0])

C.addFrame(name="item2", parent="sink1") \
    .setShape(ry.ST.ssBox, size=[.1, .1, .25, .02]) \
    .setRelativePosition([.1, .1, .52]) \
    .setColor([1, 1, 0]) \

C.addFrame(name="tray", parent="stove1") \
    .setShape(ry.ST.ssBox, size=[.2, .2, .05, .02]) \
    .setRelativePosition([.0, .0, .42]) \
    .setColor([0, 1, 0]) \
    .setRelativeQuaternion([.45, 0, 0, 1])
qHome = C.getJointState()
C.setJointState(qHome)
komo = ry.KOMO(C, 5, 10, 1, True)
komo.addControlObjective([], 0, 1e-1)
komo.addControlObjective([], 1, 1e0)
komo.addObjective([], ry.FS.accumulatedCollisions, [], ry.OT.eq,[1e1]);
komo.addObjective([1], ry.FS.positionDiff, ['endeffector', 'item2'], ry.OT.eq, [1e1])
komo.addObjective([2], ry.FS.positionDiff, ['endeffector', 'tray'], ry.OT.eq, [1e1])
komo.addObjective([3], ry.FS.positionDiff, ['endeffector', 'item1'], ry.OT.eq, [1e1])

ret = ry.NLP_Solver(komo.nlp(), verbose=0 ) .solve()
print(ret)
q = komo.getPath()
print(q)

    
for t in range(q.shape[0]):
    C.setJointState(q[t])
    C.view(False, f'waypoint {t}')
    time.sleep(0.2)


