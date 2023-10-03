zero: { X:"T t(0 0 0) d(180 0 0 1)" shape:sphere mass=1 size=[0 0 .2 .05] }
link1: { shape:capsule mass=1 size=[0 0 .3 .05] color: [0 0 1]}
one: { Q:"T t(0 0 .3) d(180 0 0 1)" shape:sphere mass=1 size=[0 0 .2 .05] color: [0 1 0]}
link2: { shape: capsule mass=1 size=[0 0 .3 .05] color: [1 0 0]}
endeffector: { shape:sphere mass=1 size=[0. 0. .2 .05] color: [0 1 0]}

(zero link1): { joint:hingeX, pre:"T t(0 0 0)" B:"T t(0 0 .2)" }
(link1 one): { joint:hingeX, pre:"T t(0 0 0)" B:"T t(0 0 .2)"}
(one link2): { joint:hingeX, pre:"T t(0 0 0)" B:"T t(0 0 .2)"}
(link2 endeffector): { joint:hingeX, pre:"T t(0 0 .18)" B:"T t(0 0 0)" }