import numpy as np
#import matplotlib.pyplot as plt
#import matplotlib.patches as mpatches

## input
x1=float(input('enter x coordinate of the first vector: '))
y1=float(input('enter y coordinate of the first vector: '))
x2=float(input('enter x coordinate of the second vector: '))
y2=float(input('enter y coordinate of the second vector: '))

qn=int(input('enter question number to answer: '))

## your code
"""
fig, ax = plt.subplots()

ax.set_xlim(0, 5)
ax.set_ylim(0, 5)

ax.set_title("Vector Addition and Suntraction")
ax.set_xlabel("x (meters)")
ax.set_ylabel("y (meters)")

# first Vector (x1, y1)
arw1 = mpatches.Arrow(0, 0, x1, y1, width=0.1, color="black")
# second Vector (x2, y2)
arw2 = mpatches.Arrow(0, 0, x2, y2, width=0.1, color="black")
# third Vector (x2, y2) - (x1, y1)
arw3 = mpatches.Arrow(x1, y1, x2, y2, width=0.1, color="black")
# fourth Vector (x1, y1) - (x2, y2)
arw4 = mpatches.Arrow(x2, y2, x1, y1, width=0.1, color="black")
# fifth Vector (x1+x2, y1+y2)
arw5 = mpatches.Arrow(0, 0, x1+x2, y1+y2, width=0.1, color="red")

arw6 = mpatches.Arrow(x2, y2, x1-x2, y1-y2, width=0.1, color="green")


# draw the Vectors
ax.add_patch(arw1)
ax.add_patch(arw2)
ax.add_patch(arw3)
ax.add_patch(arw4)
ax.add_patch(arw5)
ax.add_patch(arw6)

plt.show()
"""

vec1 = [x1-x2, y1-y2]
vec2 = [0, 1]
vec3 = [x1+x2, y1+y2]

alpha = np.degrees(np.arccos(np.dot(vec1, vec2) / (np.sqrt(np.dot(vec1, vec1)) * np.sqrt(np.dot(vec2, vec2)))))

middles = np.sqrt(np.dot(vec1, vec1)) * np.sqrt(np.dot(vec3, vec3))
beta = np.arccos(np.dot(vec3, vec1) / (np.sqrt(np.dot(vec1, vec1)) * np.sqrt(np.dot(vec3, vec3))))
S = middles*np.sin(beta)/2

rect = 1 if (np.sqrt(np.dot(vec1, vec1)) == np.sqrt(np.dot(vec3, vec3))) else 0

## output
if qn==1:
    print(f'{alpha:.5g} degrees')
if qn==2:
    print(f'{S:.5g} squared meters')
if qn==3:
    print(rect)