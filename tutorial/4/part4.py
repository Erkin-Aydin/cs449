from robotic import ry
import time
C = ry.Config()

C.addFile('links.g')

C.watchFile("links.g")
C.view()

"""time.sleep(5)"""