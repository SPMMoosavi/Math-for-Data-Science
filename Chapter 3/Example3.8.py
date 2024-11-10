import numpy as np
from sklearn.datasets import load_iris

iris = load_iris()
dataset = iris.data

# SVD
U, sigma, V = np.linalg.svd(dataset)
p = np.min(dataset.shape)
S = np.zeros(dataset.shape)
S[:p,:p] = np.diag(sigma)

np.allclose(dataset, np.dot(U, np.dot(S, V)))
