import sympy as sp
import scipy as sc
import numpy as np

A = sp.Matrix([[1, 6, 11], [2, 7, 12], [3, 8, 13], [4, 9, 14], [5, 10, 15]])
A
# column vectors
u = sp.Matrix([1,2,3,4,5])
v = sp.Matrix([6,7,8,9,10])
w = sp.Matrix([11,12,13,14,15])
A = sp.Matrix.hstack(u,v,w)
A
# returns minimal spanning set for column space of A
A.columnspace()
# returns minimal spanning orthonormal set for column space of A
A = np.array([[1, 6, 11], [2, 7, 12], [3, 8, 13], [4, 9, 14], [5, 10, 15]])
sc.linalg.orth(A)
