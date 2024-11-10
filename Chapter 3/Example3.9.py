import numpy as np
from sklearn.datasets import load_iris

iris = load_iris()
dataset = iris.data

# center dataset
m = np.mean(dataset, axis=0)
A = dataset - m

# rows of V are right singular vectors of A
V = np.linalg.svd(A)[2]

# any of these will work
Q = np.dot(A.T,A)
Q = np.cov(dataset.T,bias=False)
Q = np.cov(dataset.T,bias=True)

# columns of U are eigenvectors of Q
U = np.linalg.eigh(Q)[1]

# compare columns of U and rows of V
import sympy as sm
U = sm.Matrix(U)
V = sm.Matrix(V)
U
V