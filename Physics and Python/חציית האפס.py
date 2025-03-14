
#imports
import numpy as np

def zero_cross(ar_of_a_sampled_f):
    #your code
    ar_of_sign_change_indxs = np.sign(ar_of_a_sampled_f)
    ar_of_sign_change_indxs = np.diff(ar_of_sign_change_indxs)
    ar_of_sign_change_indxs = np.nonzero(ar_of_sign_change_indxs)
    return ar_of_sign_change_indxs

# input 
v0=float(input())
# const
g=9.8 # m/s^2
t=np.arange(0,5,0.01)
y=-0.3+v0*t-0.5*g*t**2
## your code
idx = zero_cross(y)[0]
time_of_flight = t[idx[1]] - t[idx[0]] 

#output
print(f'time of flight: {time_of_flight:.5g} s')