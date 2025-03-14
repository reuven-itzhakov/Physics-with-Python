import numpy as np
#import matplotlib.pyplot as plt


def zero_cross(ar):
    #returns an array of indices where ar changes sign
    H1t=np.sign(ar)
    H1s=np.abs(H1t[:-1]-H1t[1:])
    return np.nonzero(H1s)[0]

c=float(input("enter c: "))
qn=int(input("enter qn: "))

b=7e-5
m=2.7/1000
g=9.8
v0=10
r0=0
alpha=15*np.pi/180

## your code and answers
# array of time
dt = 1e-4
t = np.arange(0, 1.1, dt)

# calculating velocity
vx = np.zeros_like(t)
vx[0] = v0*np.cos(alpha)
vy = np.zeros_like(t)
vy[0] = v0*np.sin(alpha)
for i in range(1, (int)(1.1/1e-4)):
    vxy = (vx[i-1]**2+vy[i-1]**2)**0.5
    vx[i] = -b*dt/m*vx[i-1]-0*dt/m*vx[i-1]*vxy+vx[i-1]
    vy[i] = -g*dt-b*dt/m*vy[i-1]-0*dt/m*vy[i-1]*vxy+vy[i-1]

# calculating location
rx = np.concatenate(([r0], np.cumsum(vx)*dt+r0))
ry = np.concatenate(([r0], np.cumsum(vy)*dt+r0))

idx = zero_cross(ry)
time = rx[idx[1]] - rx[idx[0]]

ANS1=time

# 2
vx = np.zeros_like(t)
vx[0] = v0*np.cos(alpha)
vy = np.zeros_like(t)
vy[0] = v0*np.sin(alpha)

for i in range(1, (int)(1.1/1e-4)):
    vxy = (vx[i-1]**2+vy[i-1]**2)**0.5
    vx[i] = -b*dt/m*vx[i-1]-c*dt/m*vx[i-1]*vxy+vx[i-1]
    vy[i] = -g*dt-b*dt/m*vy[i-1]-c*dt/m*vy[i-1]*vxy+vy[i-1]

# calculating location
rx = np.concatenate(([r0], np.cumsum(vx)*dt+r0))
ry = np.concatenate(([r0], np.cumsum(vy)*dt+r0))

idx = zero_cross(ry)
time = rx[idx[1]] - rx[idx[0]]

ANS2=time
"""
# velocity graph
fig, ax = plt.subplots()
ax.plot(t, vx, "blue", label="vx")
ax.plot(t, vy, "red", label="vy")
ax.set_xlabel("t (sec)")
ax.set_ylabel("v (m/s)")
ax.legend()
plt.show()
#
"""

"""
# location graph
fig, ax = plt.subplots()
ax.plot(rx, ry, "blue", label="r(t)")
ax.set_xlabel("x (meter)")
ax.set_ylabel("y (meter)")
ax.legend()
plt.show()
#
"""

#ouput
Answers=[0,ANS1,ANS2]
print(f'{Answers[qn]:.5g}')