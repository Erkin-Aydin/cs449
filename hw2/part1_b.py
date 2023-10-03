from robotic import ry
import time
C = ry.Config()
C.addFile(ry.raiPath('../rai-robotModels/objects/kitchen.g'))

C.addFrame(name="item1", parent="sink1") \
    .setShape(ry.ST.ssBox, size=[0.1, 0.1, 0.25, 0.02]) \
    .setRelativePosition([-.1, -.1, .52]) \
    .setColor([1, 0, 0])

C.addFrame(name="item2", parent="sink1") \
    .setShape(ry.ST.ssBox, size=[.1, .1, .25, .02]) \
    .setRelativePosition([.1, .1, .52]) \
    .setColor([1, 1, 0]) \

C.addFrame(name="tray", parent="stove1") \
    .setShape(ry.ST.ssBox, size=[.2, .2, .05, .02]) \
    .setRelativePosition([.0, .0, .42]) \
    .setColor([0, 1, 0]) \
    .setRelativeQuaternion([.45, 0, 0, 1])
    
"C.watchFile(ry.raiPath('../rai-robotModels/objects/kitchen.g'))"
C.view()
time.sleep(500)