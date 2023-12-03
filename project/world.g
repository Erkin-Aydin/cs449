base_1: { X: [2.0, 2.0, 0.0] }
base_2: { X: [2.0, -2.0, 0.0] }
base_3: { X: [-2.0, -2.0, 0.0] }
base_4: { X: [-2.0, 2.0, 0.0] }
base_5: { X: [0.0, 3.5, 0.0] }
base_6: { X: [0.0, -3.5, 0.0] }
#base_7: { X: [3.5, 0.0, 0.0] }
#base_8: { X: [-3.5, 0.0, 0.0] }

a0 (base_1): {
 joint: transXYPhi, limits: [-20,20,-20,20,-4,4],
 shape: ssCylinder, size: [.1, .3, .02], contact: 1,
 color: [ 1.0 0.0 0.0] }

a1 (base_2): {
 joint: transXYPhi, limits: [-20,20,-20,20,-4,4],
 shape: ssCylinder, size: [.1, .3, .02], contact: 1,
 color: [0.0 1.0 0.0] }

a2 (base_3): {
 joint: transXYPhi, limits: [-20,20,-20,20,-4,4],
 shape: ssCylinder, size: [.1, .3, .02], contact: 1,
 color: [0.0 0.0 1.0]  }

a3 (base_4): {
 joint: transXYPhi, limits: [-20,20,-20,20,-4,4],
 shape: ssCylinder, size: [.1, .3, .02], contact: 1,
 color: [0.0 0.0 0.0]  }

a4 (base_5): {
joint: transXYPhi, limits: [-20,20,-20,20,-4,4],
shape: ssCylinder, size: [.1, .3, .02], contact: 1,
color: [ 1.0 1.0 0.0] }

a5 (base_6): {
 joint: transXYPhi, limits: [-20,20,-20,20,-4,4],
 shape: ssCylinder, size: [.1, .3, .02], contact: 1,
 color: [0.0 1.0 1.0] }

#a6 (base_7): {
# joint: transXYPhi, limits: [-20,20,-20,20,-4,4],
# shape: ssCylinder, size: [.1, .3, .02], contact: 1,
# color: [1.0 0.0 1.0]  }

#a7 (base_8): {
# joint: transXYPhi, limits: [-20,20,-20,20,-4,4],
# shape: ssCylinder, size: [.1, .3, .02], contact: 1,
# color: [1.0 1.0 1.0]  }