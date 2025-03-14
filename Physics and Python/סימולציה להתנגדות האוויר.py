import numpy as np

#input
v0=float(input())
V=float(input())

# your code

dt = 1e-2
N = 10**6
L = 5
m = 4e-26

# x coordinates of the air balls
x0 = np.random.uniform(0, L, N)

# velocity of the air balls
v = np.random.normal(0, v0, N)

# location of board
board = np.full_like(x0, L/2)
Xboard = np.full_like(x0, board+V*dt)

# location of the air balls
x = x0 + v*dt

# check for collision
diff = (((x0>board) & (x<Xboard)) | ((x0<board) & (x>Xboard)))

F = np.sum(diff*(m*V-m*v))/dt

#output
print(np.round(F*1e17,1))