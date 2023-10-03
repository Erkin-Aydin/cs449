from robotic import ry
import time
C = ry.Config()

C.addFile('box.g')

C.addFrame(name="box2", parent="box1") \
.setShape(ry.ST.ssBox, size=[.5, .5, .5, .05]) \
.setRelativePosition([0,0,1]) \
.setColor([0,0,1])

f = C.frame("box2")
print("position:", f.getPosition())
print("orientation:", f.getQuaternion())

print(1)
C.watchFile("box.g")
C.view()
time.sleep(1)