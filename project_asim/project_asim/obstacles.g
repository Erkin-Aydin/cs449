base_1: { X: [0.5, -2.5, 0.08] }
base_2: { X: [1.5, -2.5, 0.08] }

a0 (base_1): {
 joint: transXYPhi, limits: [-20,20,-20,20,-4,4],
 shape: ssCylinder, size: [.1, .3, .02], contact: 1,
 color: [ 1.0 0.0 0.0] }

a1 (base_2): {
 joint: transXYPhi, limits: [-20,20,-20,20,-4,4],
 shape: ssCylinder, size: [.1, .3, .02], contact: 1,
 color: [0.0 0.0 1.0]  }
