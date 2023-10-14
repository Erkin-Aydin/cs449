from robotic import ry
import time
import numpy as np

C = ry.Config()

C.addFile('HW1-two-link.g')
target = C.frame("target")
joint_angles = 2 * np.pi * np.random.rand(3)

def forward_kinematics(q):
    q0 = np.pi / 2 - q[0]
    q1 =  np.pi / 2 - q[0] - q[1];
    y = np.cos(q0) + np.cos(q1);
    z = np.sin(q0) + np.sin(q1);
    return np.array([0, y, z])
pos_target = forward_kinematics(joint_angles)
target.setPosition(pos_target)
C.setJointState(joint_angles)
C.view()
time.sleep(10)
q = np.zeros(C.getJointDimension())
C.setJointState(q)



