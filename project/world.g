base_1: { X: [-0.5, -3.5, 0.0] }
base_2: { X: [2.0, -2.5, 0.0] }
base_3: { X: [3.5, -2.5, 0.0] }
base_4: { X: [4.5, -1.5, 0.0] }
base_5: { X: [3.5, 0.5, 0.0] }
base_6: { X: [4.5, 2.0, 0.0] }
base_7: { X: [3.0, 2.5, 0.0] }
base_8: { X: [1.0, 2.5, 0.0] }
base_9: { X: [-1.5, 2.5, 0.0] }
base_10: { X: [-2.0, -3.5, 0.0]}
base_11: { X: [-2.5, 2.5, 0.0]}

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

a6 (base_7): {
 joint: transXYPhi, limits: [-20,20,-20,20,-4,4],
 shape: ssCylinder, size: [.1, .3, .02], contact: 1,
 color: [1.0 0.0 1.0]  }

a7 (base_8): {
 joint: transXYPhi, limits: [-20,20,-20,20,-4,4],
 shape: ssCylinder, size: [.1, .3, .02], contact: 1,
 color: [1.0 1.0 1.0]  }

a8 (base_9): {
 joint: transXYPhi, limits: [-20,20,-20,20,-4,4],
 shape: ssCylinder, size: [.1, .3, .02], contact: 1,
 color: [0.5 0.5 0.5]  }

a9 (base_10): {
 joint: transXYPhi, limits: [-20,20,-20,20,-4,4],
 shape: ssCylinder, size: [.1, .3, .02], contact: 1,
 color: [0.75 0.75 0.75]  }

a10 (base_11): {
 joint: transXYPhi, limits: [-20,20,-20,20,-4,4],
 shape: ssCylinder, size: [.1, .3, .02], contact: 1,
 color: [0.0 0.0 0.0]  }

frame floorwalls: { }

frame _0(floorwalls): { shape: box, size: [10, 10, 0.01], color: [0.4, 0.4, 0.4], Q: [0, 0, +0.02, 1, 0, 0, 0]  ,contact: 0}
front _1(floorwalls): { shape: box, size: [6, 0.02, 1.2], color: [0.82, 0.7, 0.55], Q: [2, -4, 0.62, 1, 0, 0, 0] ,contact: True}
front _2(floorwalls): { shape: box, size: [2, 0.02, 1.2], color: [0.82, 0.7, 0.55], Q: [2, -2, 0.62, 1, 0, 0, 0] ,contact: True}
front _3(floorwalls): { shape: box, size: [2, 0.02, 1.2], color: [0.82, 0.7, 0.55], Q: [-4, -2, 0.62, 1, 0, 0, 0] ,contact: True}
front _4(floorwalls): { shape: box, size: [4, 0.02, 1.2], color: [0.82, 0.7, 0.55], Q: [-3, -4, 0.62, 1, 0, 0, 0] ,contact: True}
back _1(floorwalls): { shape: box, size: [2, 0.02, 1.2], color: [0.82, 0.7, 0.55], Q: [0, 2, 0.62, 1, 0, 0, 0] ,contact: True}
back _2(floorwalls): { shape: box, size: [8, 0.02, 1.2], color: [0.82, 0.7, 0.55], Q: [1, 4, 0.62, 1, 0, 0, 0] ,contact: True}
side _left1(floorwalls): { shape: box, size: [0.02, 4, 1.2], color: [0.82, 0.7, 0.55], Q: [1, 0, 0.62, 1, 0, 0, 0] ,contact: 1}
side _left2(floorwalls): { shape: box, size: [0.02, 4, 1.2], color: [0.82, 0.7, 0.55], Q: [3, 0, 0.62, 1, 0, 0, 0],contact: True }
side _left3(floorwalls): { shape: box, size: [0.02, 8, 1.2], color: [0.82, 0.7, 0.55], Q: [5, 0, 0.62, 1, 0, 0, 0],contact: True }
side _right1(floorwalls): { shape: box, size: [0.02, 6, 1.2], color: [0.82, 0.7, 0.55], Q: [-1, -1, 0.62, 1, 0, 0, 0] ,contact: True}
side _right2(floorwalls): { shape: box, size: [0.02, 6, 1.2], color: [0.82, 0.7, 0.55], Q: [-3, 1, 0.62, 1, 0, 0, 0],contact: True }
side _right3(floorwalls): { shape: box, size: [0.02, 2, 1.2], color: [0.82, 0.7, 0.55], Q: [-5, -3, 0.62, 1, 0, 0, 0] ,contact: True}
finish_line(floorwalls): { shape: box, size: [0.02, 2, 0.01], color: [0, 1, 0], Q: [-4, -3, 0.03, 1, 0, 0, 0] ,contact: -2}
goal_area(floorwalls): { shape: box, size: [1, 2, 0.01], color: [0, 0, 1], Q: [-4.5, -3, 0.03, 1, 0, 0, 0] ,contact: -2}