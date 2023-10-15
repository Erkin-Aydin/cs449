import numpy as np
joint_angles= [1.95205226, 3.15753276, 0]

def Jacobian(angles):
    
    return np.array([[(np.cos( angles[0]) + np.cos( angles[0] + angles[1])), np.cos( angles[0] +angles[1])], 
                    [-(np.sin( angles[0]) + np.sin( angles[0] + angles[1])), -np.sin( angles[0] + angles[1])]])

print(Jacobian(joint_angles))
