import numpy as np
# import matplotlib.pyplot as plt

qn=int(input('enter question number: '))
a=float(input('enter acceleration: '))
print()

# if qn==1:
#     t=np.arange(0, 8, 0.1)
#     v=a*t
#     y=0.5*a*t**2

#     fig1, ax1 = plt.subplots()
#     ax1.plot(t, v, label="r(t)")
#     ax1.set_xlabel("time (sec")
#     ax1.set_ylabel("velocity (meters\sec)")
#     ax1.set_title("Velocity over time")
#     ax1.legend()

#     fig2, ax2 = plt.subplots()
#     ax2.plot(t, y, label="v(t)", color="red")
#     ax2.set_xlabel("time (sec)")
#     ax2.set_ylabel("distance (meters)")
#     ax2.set_title("Distance over time")
#     ax2.legend()

#     plt.show()

if qn==2:
    t=float(input('enter t: '))

    ## your answer
    v=a*t
    
    ## output
    print(f'v={v:.5g} m/s')

if qn==3:
    t=float(input('enter t: '))

    ## your answer
    x=0.5*a*t**2
    
    ## output
    print(f'x={x:.5g} m')
    
if qn==4:
    v=float(input('enter v: '))

    ## your answer
    t=v/a
    x=0.5*v*t
    
    ## output
    print(f'x={x:.5g} m')

# if qn==5:
#     t=np.arange(0, 8, 0.1)
#     x=0.5*a*t**2
#     y=np.zeros_like(x)
#     t1=np.random.default_rng().uniform(low=1, high=7)

#     xT=0.5*a*t1**2
#     yT=[0]

#     fig3, ax3 = plt.subplots()
#     ax3.plot(x, y)
#     ax3.set_xlabel("x (meters)")
#     ax3.set_ylabel("y (meters)")
#     ax3.plot(xT, yT, "ro", label=f"Coordinates at time {t1:.2g}sec")
#     ax3.set_label("Route")
#     ax3.legend()

#     plt.show()

# if qn==6:
#     t=np.arange(0, 8, 0.1)
#     v0=2.7
#     x=0.5*a*t**2
#     y=v0*t
#     t1=np.random.default_rng().uniform(low=1, high=7)

#     xT=0.5*a*t1**2
#     yT=v0*t1

#     fig4, ax4 = plt.subplots()
#     ax4.plot(x, y)
#     ax4.set_xlabel("x (meters)")
#     ax4.set_ylabel("y (meters)")
#     ax4.plot(xT, yT, "ro", label=f"Coordinates at time {t1:.2g}sec")
#     ax4.set_label("Route")
#     ax4.legend()

#     plt.show()

if qn==7:
    ANS=False
    print(ANS)