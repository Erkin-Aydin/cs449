box1: { X: "t(0 0 .25) d(0 0 0 1)", shape: ssBox, size: [.5 .5 .5 .05], color: [1 .5 0], mass: .1, contact: true }
box2(box1): { Q: "t(0 0 1) d(0 0 0 0)", shape: ssBox, size: [.5 .5 .5 .05], color: [0 0 1], mass: .1, contact: true }