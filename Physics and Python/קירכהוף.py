# Electric Circuits Q1 - solve linear equations representing an electrical circuit
import numpy as np

# input
V1=float(input('Enter value for Vone(Volts):'))

#your code - assign the requested current to a variable named I

A = np.array([[-1, 1, 1, 1],
              [11, 2, 0, 0],
              [11, 0, 2, 0],
              [11, 0, 0, 8]])

b = np.array([0, V1-1, V1, V1-3])
I = np.linalg.solve(A, b)[0]

#output
print(f'Current drawn from main source: {I:1.4} A')