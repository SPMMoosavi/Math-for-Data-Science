import sympy as sp
import scipy as sc
import numpy as np

A = sp.Matrix([[1, 6, 11], [2, 7, 12], [3, 8, 13], [4, 9, 14], [5, 10, 15]])
A

# returns minimal spanning set for row space of A
A.rowspace()

# returns minimal spanning orthonormal set for column space of A
A = np.array([[1, 6, 11], [2, 7, 12], [3, 8, 13], [4, 9, 14], [5, 10, 15]])
sc.linalg.orth(A.T)
