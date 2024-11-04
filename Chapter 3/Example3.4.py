import numpy as np

Q = np.array([[2, 1], [1, 2]])
eigenvalues, eigenvectors = np.linalg.eig(Q)
V = eigenvectors
D = np.diag(eigenvalues)
VDV_t = np.dot(V, np.dot(D,V.T))
print(f'{V = }')
print(f'{D = }')
print(np.allclose(Q, VDV_t))

import sympy as sm

Q = sm.Matrix([[2, 1], [1, 2]])
V, D = Q.diagonalize()
V
D
