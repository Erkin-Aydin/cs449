from robotic import ry
import time
C = ry.Config()

C.addFile('HW1-two-link.g')

#.watchFile("HW1-two-link.g")
C.setJointState([0.6, 0, 0])
C.view()

time.sleep(15)