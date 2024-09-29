import sympy as sp
import scipy as sc
import numpy as np

# using sympy
A = sp.Matrix([[1, 6, 11], [2, 7, 12], [3, 8, 13], [4, 9, 14], [5, 10, 15]])
A.nullspace()

# using numpy and scipy
A = np.array([[1, 6, 11], [2, 7, 12], [3, 8, 13], [4, 9, 14], [5, 10, 15]])
sc.linalg.null_space(A)
