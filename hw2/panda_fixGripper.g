Include: <../rai-robotModels/panda/panda.g>

#Edit panda_link0{ X: "t(-.3 0 .65)" }

#Edit panda_finger_joint1 { joint_active: False }

gripper (panda_joint_7){
    shape:marker, size:[.03], color:[.9 .9 .5],
    Q: "d(-90 0 1 0) d(135 0 0 1) t(0 0 -.155) t(0 0 -.05)"  
}