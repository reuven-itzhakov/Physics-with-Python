import numpy as np

C=float(input())
R=float(input())
w0=float(input())
V0=float(input())

#your code
dt = 20*R*C/1000
t = np.arange(0, 20*R*C, dt)
Q0 = 0
Q = np.zeros_like(t)+Q0

for i in range(0, len(t)-1):
    Q[i+1] = Q[i]*dt/(C*R)+Q[i]+V0*t[i]*np.sin(w0)*dt/R

Imax = Q[-1]

print(f'{Imax:.5g}')

"""
5.816326111374133e-07
225.87772243747472
3044.6532769803043
5.4898605434557455

"""