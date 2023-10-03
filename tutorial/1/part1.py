from robotic import ry

C = ry.Config()
C.addFile('mini.g')
C.view()

C.watchFile('mini.g')