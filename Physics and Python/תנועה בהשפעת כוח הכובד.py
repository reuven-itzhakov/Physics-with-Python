import numpy as np
#import matplotlib.pyplot as plt

def zero_cross(ar):
    #returns an array of indices where ar changes sign
    H1t=np.sign(ar)
    H1s=np.abs(H1t[:-1]-H1t[1:])
    return np.nonzero(H1s)[0]

#inputs
V0x=float(input('enter V_ox: '))
V0y=float(input('enter V_oy: '))
qn=int(input('enter qn: '))
print()

#your code

R0x = 0
R0y = 0
g = -9.8
dt = (2.5*V0y/-g)/3000
t = np.linspace(0, 2.5*V0y/-g, 3000)
# Given the force is only -9.8y
ax = np.ones_like(t)*0
ay = np.ones_like(t)*g

vx = np.concatenate(([V0x], np.cumsum(ax)*dt+V0x))
vy = np.concatenate(([V0y], np.cumsum(ay)*dt+V0y))

Rx = np.concatenate(([R0x], np.cumsum(vx)*dt+R0x))
Ry = np.concatenate(([R0y], np.cumsum(vy)*dt+R0y))

"""
# Should've done by gradient and cumsum..

# I've done the integration in the notebook
vx = np.zeros_like(t)+V0x
vy = np.zeros_like(t)+(V0y-g*t)

Rx = np.zeros_like(t)+(R0x+vx*t)
Ry = np.zeros_like(t)+(R0y+V0y*t+(ay*t**2)/2)
"""
idx = zero_cross(Ry)
Ans1 = t[idx[1]] - t[idx[0]]
Ans2= Rx[idx[1]] - Rx[idx[0]]

"""
fig, ax = plt.subplots()
ax.plot(Rx, Ry, label="Route")
ax.set_title("Route of a figure")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
plt.show()
"""

# using the fomula and givens:
# ax = 0, ay = -9.8, v0x, v0y
# y = y0 + v0t + 0.5*a*t**2
# finding the t and then assign it to
# the next formula to find the x
# x = x0 + v0t + 0.5*a*t**2
t1 = 2*V0y/9.8
t0 = 0
Ans3 = t1 - t0
Ans4 = V0x*t1

Answers=[0,Ans1,Ans2,Ans3,Ans4]
#output
print(f'{Answers[qn]:.5g}')