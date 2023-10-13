from robotic import ry
import time
C = ry.Config()

C.addFile('HW1-two-link.g')

C.watchFile("HW1-two-link.g")
C.view()

"""time.sleep(5)"""