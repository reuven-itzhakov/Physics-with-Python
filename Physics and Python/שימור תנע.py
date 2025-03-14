import numpy as np

#inputs
m1=float(input())
m2=float(input())
F0=float(input())
v0=float(input())
sn=int(input())


###############

dt = 10/1000
t = np.linspace(0, 10, 1000)

a = F0/m1
v1 = v0 - a*t
p1 = m1*v1

p2 = m1*v0 - p1
P = p1 + p2
#######


#output
if sn==1:
    print(p1[0:10])
elif sn==2:
    print(p2[0:10])
elif sn==3:
    print(P[0:10])