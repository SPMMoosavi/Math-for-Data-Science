import numpy as np

A = np.zeros((4,3))
print(A)
B = np.eye(3)
print(B)
C = np.eye(4,3)
print(C)
D = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(D)
E = np.diag([1,2,3,4])
print(E)


print(A+C)
print(C+D)
print(4*D)
print(-D)
print(-2*D)
