import numpy as np
#from MyFunc import zero_cross
#import matplotlib.pyplot as plt


def zero_cross(arr):
    return np.nonzero(np.diff(np.sign(arr)))

v0=float(input("vo: "))
gamma=float(input("gamma: "))
qn=int(input("q#:"))

dt=1e-2
t=np.arange(0,7,dt)
v=v0*np.exp(-gamma*t)*np.cos(10*gamma*t)
x0=0
a=np.gradient(v, dt)
x=np.concatenate(([x0], np.cumsum(v)*dt+x0))
"""
fid, ax = plt.subplots()
ax.plot(t, x[:-1], label="x(t)")
ax.set_title("Location")
ax.set_xlabel("x (meter)")
ax.set_ylabel("y (meter)")
ax.legend()
plt.show()
"""
if qn==1: 
    print(t[:10])
elif qn==2: 
    # your solution
    print(v[:10])
elif qn==3:
    print(a[:10])
elif qn==4:
    print(x[:10])    
elif qn==5:
    # t=(np.pi)/(4*gamma)
    print(zero_cross(v)[0][2]*dt)
