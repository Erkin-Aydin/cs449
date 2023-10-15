from robotic import ry
import time
import numpy as np
C = ry.Config()
C.addFile(ry.raiPath('../rai-robotModels/objects/kitchen.g'))
K = ry.Config()
K.addFile(ry.raiPath('../rai-robotModels/objects/kitchen.g'))
C.addFile('part5.g')
K.addFile('part5.g')

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

n = K.getJointDimension()
q = K.getJointState()
w = 1e-4
W = w * np.identity(n) # W is equal the ID_n matrix times scalar w
input("initial posture, press Enter to continue...")
y_target = [0.0, 0.7, 0]
for i in range(10):
    # 1st task
    F = K.feature(ry.FS.position, ["endeffector"])
    y, J = F.eval(K)
    # compute joint updates
    q += np.linalg.inv(J.T @ J + W) @ J.T @ (y_target - y)
    # NOTATION: J.T is the transpose of J; @ is matrix multiplication (dot product)
    # sets joint angles AND computes all frames AND updates display
    K.setJointState(q)
    # optional: pause and watch OpenGL
    K.view()
    input("Press Enter to continue...")


  
for t in range(q.shape[0]):
    C.setJointState(q[t])
    C.view(False, f'waypoint {t}')
    time.sleep(0.2)


