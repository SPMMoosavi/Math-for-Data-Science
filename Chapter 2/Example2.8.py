import numpy as np

A = np.arange(1,13).reshape(3,4)
B = np.arange(13,21).reshape(4,2)

AB = np.dot(A, B)
print(AB)
