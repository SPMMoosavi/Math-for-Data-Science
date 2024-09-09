import numpy as np

v1 = (1,2)
v2 = (3,4)
print(v1 + v2 == (1+3,2+4)) # returns False

v1 = [1,2]
v2 = [3,4]
print(v1 + v2 == [1+3,2+4]) # returns False

v1 = np.array([1,2])
v2 = np.array([3,4])
print(v1 + v2 == np.array([1+3,2+4])) # returns [ True  True]

print(3*v1 == np.array([3,6])) # returns [ True  True]

print(-v1 == np.array([-1,-2])) # returns [ True  True]

print(v1 - v2 == np.array([1-3,2-4])) # returns [ True  True]
