from robotic import ry
import time
import numpy as np

C = ry.Config()
C.addFile(ry.raiPath('../rai-robotModels/objects/kitchen.g'))
C.addFile('spider.g')

C.view();
time.sleep(10)