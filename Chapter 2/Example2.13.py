import numpy as np

A = np.array([[1,2,3],[-3,6,0], [10,-5,23]])
b = np.array([1,2,3])
# Determinant of A
np.linalg.det(A)
# Inverse of A
np.linalg.inv(A)
# Solution of Ax=b
x = np.dot(np.linalg.inv(A),b)
