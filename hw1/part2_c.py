import numpy as np
joint_angles= [1.95205226, 3.15753276, 0]

def Jacobian(angles):
    return np.array([[(np.sin(np.pi/2-angles[0]) + np.sin(np.pi/2-angles[0]-angles[1])), np.sin(np.pi/2-angles[0]-angles[1])], 
                     [(-np.cos(np.pi/2-angles[0]) - np.cos(np.pi/2-angles[0]-angles[1])), - np.cos(np.pi/2-angles[0]-angles[1])]])

print(Jacobian(joint_angles))