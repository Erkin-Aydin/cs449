from robotic import ry
import time
C = ry.Config()

C.addFile('box.g')

C.view()
C.watchFile("box.g")
"""time.sleep(5)"""