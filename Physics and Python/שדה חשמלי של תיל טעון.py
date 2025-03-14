import numpy as np

N=100000
k=9e9

#input 
lam=float(input("lambda:"))
L=float(input("Length:"))
qn=int(input("qn:"))

## your code
realdx = np.linspace(-L/2, L/2, N)
realdx = realdx[1] - realdx[0]
x = np.linspace(-100*L, 100*L, N)
dx = x[1] - x[0]
y = np.linspace(-100*L, 100*L, N)
dy = y[1] - y[0]

q = lam*L
dq = lam*realdx

def routine(x0, y0):
    #Ex = np.concatenate(([x0], np.cumsum(X*k*dq/((X-x0)**2+(Y-y0)**2)**1.5)*dx+x0))
    #Ex = np.sum(X*k*dq/((X-x0)**2+(Y-y0)**2)**1.5)
    # Ex = X*k*dq/((X-x0)**2+(Y-y0)**2)**1.5
    # Ey = Y*k*dq/((X-x0)**2+(Y-y0)**2)**1.5
    Ex = x*k*q/(x0**2+y0**2)**1.5
    Ey = y*k*q/(x0**2+y0**2)**1.5
    x0 = int(np.round((x0+100*L)/dx, 0))
    y0 = int(np.round((y0+100*L)/dy, 0))
    #print(x0, y0)
    return Ex[x0], Ey[y0]

Ex1 ,Ey1 = routine(2*L, 3*L)
Ex2 ,Ey2 = routine(0, L)
Ex4 ,Ey4 = routine(0, 100*L)
Ex5 ,Ey5 = routine(0, 100*L)
Ex6 ,Ey6 = routine(0, 0.01*L)
Ex7 ,Ey7 = routine(0, 0.01*L)


## output.  change 3,8,9 according to your answers 
if qn==1:
    print(f'{Ex1:.5g},{Ey1:.5g}')
elif qn==2:
    print(f'{Ex2:.5g},{Ey2:.5g}')
elif qn==3:
    print("yes")
elif qn==4:
    print(Ey4)
elif qn==5:
    print(Ey5)
elif qn==6:
    print(Ey6)
elif qn==7:
    print(Ey7)
elif qn==8:
    print("1")
elif qn==9:
    print("2")

"""
11
11
1

""" 