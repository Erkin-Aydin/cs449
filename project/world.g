base_1: { X: [2.0, 2.0, 0.0] }
base_2: { X: [2.0, -2.0, 0.0] }
base_3: { X: [-2.0, 2.0, 0.0] }
base_4: { X: [-2.0, -2.0, 0.0] }

a0 (base_1): {
 joint: transXYPhi, limits: [-20,20,-20,20,-4,4],
 shape: ssCylinder, size: [.1, .3, .02], contact: 1 }

a1 (base_2): {
 joint: transXYPhi, limits: [-20,20,-20,20,-4,4],
 shape: ssCylinder, size: [.1, .3, .02], contact: 1 }

a2 (base_3): {
 joint: transXYPhi, limits: [-20,20,-20,20,-4,4],
 shape: ssCylinder, size: [.1, .3, .02], contact: 1 }

a3 (base_4): {
 joint: transXYPhi, limits: [-20,20,-20,20,-4,4],
 shape: ssCylinder, size: [.1, .3, .02], contact: 1 }