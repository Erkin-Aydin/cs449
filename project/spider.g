back: {  X: T t(0 -0.05 0.2) d(0 0 0 1)", shape: box, size: [0.1 0.075 0.05], color: [0.5 0.5 0.5], mass: 0.1, contact: true }
middle: {  X: "T t(0 0 0.2) d(0 0 0 1)",  shape: box, size: [0.05 0.075 0.05], color: [0.5 0.5 0.5], mass: 0.1, contact: true }
front: { X: "T t(0 0.05 0.2) d(0 0 0 1)",  shape: box, size: [0.1 0.075 0.05], color: [0.5 0.5 0.5], mass: 0.1, contact: true }
endeffector: { X: "T t(0 0.0875 0.2) d(0 0 0 1)", shape:box, size: [0.025 0.025 0.0125], color: [0 0 1], mass: 0.1, contact: true}

leg10: { shape:capsule mass=0.01 size=[0 0.035 0 .05] color: [0 0 1], contact: true}
leg11: { shape:capsule mass=0.01 size=[0 0.035 0 .05] color: [0 0 1], contact: true}
leg20: { shape:capsule mass=0.01 size=[0 0.035 0 .05] color: [0 0 1], contact: true}
leg21: { shape:capsule mass=0.01 size=[0 0.035 0 .05] color: [0 0 1], contact: true}
leg30: { shape:capsule mass=0.01 size=[0 0.035 0 .05] color: [0 0 1], contact: true}
leg31: { shape:capsule mass=0.01 size=[0 0.035 0 .05] color: [0 0 1], contact: true}
leg40: { shape:capsule mass=0.01 size=[0 0.035 0 .05] color: [0 0 1], contact: true}
leg41: { shape:capsule mass=0.01 size=[0 0.035 0 .05] color: [0 0 1], contact: true}
leg50: { shape:capsule mass=0.01 size=[0 0.035 0 .05] color: [0 0 1], contact: true}
leg51: { shape:capsule mass=0.01 size=[0 0.035 0 .05] color: [0 0 1], contact: true}
leg60: { shape:capsule mass=0.01 size=[0 0.035 0 .05] color: [0 0 1], contact: true}
leg61: { shape:capsule mass=0.01 size=[0 0.035 0 .05] color: [0 0 1], contact: true}

(back middle) { joint:hingeX, pre:"T t(0 0.0375 0)" B:"T t(0 0.0375 0)"}
(middle front) { joint:hingeX, pre:"T t(0 0.0375 0)" B:"T t(0 0.0375 0)"}
(front endeffector) { joint:hingeX, pre:"T t(0 0.0375 0)" B:"T t(0 0 0)"}

(leg10 leg11)
(leg20 leg21)
(leg30 leg31)
(leg40 leg41)
(leg50 leg51)
(leg60 leg61)