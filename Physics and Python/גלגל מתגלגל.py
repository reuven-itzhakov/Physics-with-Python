import numpy as np
#import matplotlib.pyplot as plt

R=float(input('Enter R: '))
V=float(input('Enter V: '))
t=float(input('Enter t: '))
qn=int(input("Enter question number: "))
print()

### your code

omg= V/R

X= V*t
Y= 0

Xcp= R*np.sin(omg*t)
Ycp= R*np.cos(omg*t)

Xp= R*np.sin(omg*t) + V*t
Yp= R*np.cos(omg*t)

t1= np.pi/(omg)

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Vp = np.sqrt(Xp**2 + Yp**2)
Vt1 = np.sqrt((R*np.sin(omg*t1) + V*t1)**2 + (R*np.cos(omg*t1))**2)

t2 = np.random.default_rng().uniform(6*np.pi/omg, 8*np.pi/omg)

time = np.arange(0, t2, 0.01)

XpTime = R*np.sin(omg*time) + V*time
YpTime = R*np.cos(omg*time)

XcpTime= R*np.sin(omg*time)
YcpTime= R*np.cos(omg*time)

XpT2 = R*np.sin(omg*t2) + V*t2
YpT2 = R*np.cos(omg*t2)


fig, ax1 = plt.subplots()
ax1.plot(XpTime, YpTime)
ax1.set_title("Route of point 'P'")
ax1.set_xlabel("x (meter)")
ax1.set_ylabel("y (meter)")

fig, ax2 = plt.subplots()
ax1.plot(XpT2, YpT2, "ro")
ax1.plot(XcpTime + t2, YcpTime, "green")
ax2.set_title("Coordinates of point 'P' at time 't2'")
ax2.set_xlabel("x (meter)")
ax2.set_ylabel("y (meter)")

plt.show()
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

### output
X=round(X,5)
Xcp=round(Xcp,5)
Ycp=round(Ycp,5)
Xp=round(Xp,5)
Yp=round(Yp,5)
t1=round(t1,5)

ANS=[0,omg,(X,Y),(Xcp,Ycp),(Xp,Yp),t1]
print(ANS[qn])
