from robotic import ry
import time
C = ry.Config()
C.addFile(ry.raiPath('../rai-robotModels/objects/kitchen.g'))
"##############State 1##############"
"""
C.addFrame(name="tray", parent="stove1") \
    .setShape(ry.ST.ssBox, size=[.4, .4, .05, .02]) \
    .setRelativePosition([.0, .0, .42]) \
    .setColor([0, 1, 0]) \
    .setRelativeQuaternion([.45, 0, 0, 1])
""(0.05 / 2) + (0.25 / 2) = 0.15""
C.addFrame(name="item1", parent="tray") \
    .setShape(ry.ST.ssBox, size=[0.1, 0.1, 0.25, 0.02]) \
    .setRelativePosition([-.1, -.1, .15]) \
    .setColor([1, 0, 0])

C.addFrame(name="item2", parent="tray") \
    .setShape(ry.ST.ssBox, size=[.1, .1, .25, .02]) \
    .setRelativePosition([.1, .1, .15]) \
    .setColor([1, 1, 0])
"""
"##############State 1##############"

"##############State 2##############"
C.addFrame(name="tray", parent="table1") \
    .setShape(ry.ST.ssBox, size=[.4, .4, .05, .02]) \
    .setRelativePosition([.0, .0, .42]) \
    .setColor([0, 1, 0]) \
    .setRelativeQuaternion([.45, 0, 0, 1])
"""(0.05 / 2) + (0.25 / 2) = 0.15"""
C.addFrame(name="item1", parent="tray") \
    .setShape(ry.ST.ssBox, size=[0.1, 0.1, 0.25, 0.02]) \
    .setRelativePosition([-.1, -.1, .15]) \
    .setColor([1, 0, 0])

C.addFrame(name="item2", parent="tray") \
    .setShape(ry.ST.ssBox, size=[.1, .1, .25, .02]) \
    .setRelativePosition([.1, .1, .15]) \
    .setColor([1, 1, 0])
"##############State 2##############"

print("sink1 coordinates: ", C.frame("sink1").getPosition())
print("table1 coordinates: ", C.frame("table1").getPosition())
print("item1 coordinates: ", C.frame("item1").getPosition())
"C.watchFile(ry.raiPath('../rai-robotModels/objects/kitchen.g'))"
C.view()
time.sleep(500)