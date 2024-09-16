import numpy as np

A = np.arange(1,13).reshape(3,4)
v = np.array([1,2,3,4])

Av = np.dot(A, v)
print(Av)
