from robotic import ry
import time
C = ry.Config()

C.addFile('links_modified.g')

C.watchFile("links_modified.g")
C.view()

"""time.sleep(5)"""