from robotic import ry
import time
C = ry.Config()
C.addFile("cargobot_base.g")
C.addFile("maze.g")

C.view()
time.sleep(500)