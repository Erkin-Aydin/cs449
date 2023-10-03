from robotic import ry
import time
C = ry.Config()

C.addFrame('box') \
.setPosition([0, 0, .25]) \
.setShape(ry.ST.ssBox, size=[.5, .5, .5, .05]) \
.setColor([1, .5, 0]) \
.setMass(.1) \
.setContact(True)

C.view()
time.sleep(5)