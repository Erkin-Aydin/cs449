seat: {
    X: "T t(0 0 0.5) d(0 0 0 1)",
    shape: box,
    size: [0.8 0.8 0.05],
    color: [0.5 0.5 0.5],
    mass: 0.1,
    contact: true
}

backrest: {
    X: "T t(0 0.4 0.90) d(0 0 0 1)",
    shape: box,
    size: [0.8 0.1 0.8],
    color: [0.5 0.5 0.5],
    mass: 0.1,
    contact: true
}

leg1: {
    X: "T t(-0.35 -0.35 0.25) d(0 0 0 1)",
    shape: box,
    size: [0.05 0.05 0.5],
    color: [0.5 0.5 0.5],
    mass: 0.1,
    contact: true
}

leg2: {
    X: "T t(-0.35 0.35 0.25) d(0 0 0 1)",
    shape: box,
    size: [0.05 0.05 0.5],
    color: [0.5 0.5 0.5],
    mass: 0.1,
    contact: true
}

leg3: {
    X: "T t(0.35 -0.35 0.25) d(0 0 0 1)",
    shape: box,
    size: [0.05 0.05 0.5],
    color: [0.5 0.5 0.5],
    mass: 0.1,
    contact: true
}

leg4: {
    X: "T t(0.35 0.35 0.25) d(0 0 0 1)",
    shape: box,
    size: [0.05 0.05 0.5],
    color: [0.5 0.5 0.5],
    mass: 0.1,
    contact: true
}




zero: { X:"T t(0 0 0.5) d(180 0 0 1)" shape:sphere mass=1 size=[0. 0. .6 .10] }
link1: { shape:capsule mass=1 size=[0 0 1 .05] color: [0 0 1]}
link2: { shape:capsule mass=1 size=[0 0 1 .05] color: [1 0 0]}
link3: { shape:box mass=1 size=[0.1  0.1 1 .05] color: [1 1 1]}
endeffector: { shape:sphere mass=1 size=[0. 0. .6 .05] color: [0 1 1]}


(zero link1): { joint:hingeY, pre:"T t(0 0 .0)" B:"T t(0 0 .5)" }
(link1 link2): { joint:hingeX, pre:"T t(0 0 0.5)" B:"T t(0 0 0.5)"}
(link2 link3): { joint:hingeX, pre:"T t(0 0 0.5)" B:"T t(0 0 0.5)"}
(link3 endeffector): { joint:hingeX, pre:"T t(0 0 .5)" B:"T t(0 0 .05)" }
