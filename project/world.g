base_1: { X: [0.0, 0.0, 0.0] }
base_2: { X: [1.0, 0.0, 0.0] }
base_3: { X: [1.0, 1.0, 0.0] }
base_4: { X: [0.0, 1.0, 0.0] }

base (base_1): {
 joint: transXYPhi, limits: [-20,20,-20,20,-4,4],
 shape: ssCylinder, size: [.1, .3, .02], contact: 1 }

base (base_2): {
 joint: transXYPhi, limits: [-20,20,-20,20,-4,4],
 shape: ssCylinder, size: [.1, .3, .02], contact: 1 }

base (base_3): {
 joint: transXYPhi, limits: [-20,20,-20,20,-4,4],
 shape: ssCylinder, size: [.1, .3, .02], contact: 1 }

base (base_4): {
 joint: transXYPhi, limits: [-20,20,-20,20,-4,4],
 shape: ssCylinder, size: [.1, .3, .02], contact: 1 }