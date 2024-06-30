import numpy as np

v1 = np.array([1,2])
v2 = np.array([3,4])
print(np.linalg.norm(v1)) #returns 2.23606797749979
print(np.linalg.norm(v1-v2)) #returns 2.8284271247461903