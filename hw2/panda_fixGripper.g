## this should be the default panda we use on the real system
# with NO dofs for the gripper

Include: <../rai-robotModels/panda/panda.g>

# make fingers part of the gripper link
Edit panda_finger_joint1: { Q: "t(0 .05 0)", joint: none }
Edit panda_finger_joint2: { Q: "t(0 -.05 0)", joint: none }

Edit panda_finger_joint1: { joint_active: False }

gripper (panda_joint7){
    shape:marker, size:[.03], color:[.9 .9 .5],
    Q: "d(-90 0 1 0) d(135 0 0 1) t(0 0 -.155) t(0 0 -.05)"  
}