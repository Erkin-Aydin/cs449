from robotic import ry
import time
C = ry.Config()
C.addFile(ry.raiPath('../rai-robotModels/objects/kitchen.g'))

C.addFrame(name="item1", parent="sink1") \
    .setShape(ry.ST.ssBox, size=[0.1, 0.1, 0.25, 0.02]) \
    .setRelativePosition([-.1, -.1, .52]) \
    .setColor([1, 0, 0])
    
print("sink1 coordinates: ", C.frame("sink1").getPosition())
print("item1 coordinates: ", C.frame("item1").getPosition())
"C.watchFile(ry.raiPath('../rai-robotModels/objects/kitchen.g'))"
C.view()
time.sleep(500)