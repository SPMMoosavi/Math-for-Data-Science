import numpy as np
from sklearn.datasets import load_iris

iris = load_iris()
dataset = iris.data

# Covariance matrix
Q = np.cov(dataset.T)

# Eigen data
eigenvalues, eigenvectors = np.linalg.eig(Q)

# Compute total variance
total_variance = np.trace(Q)

# Percentage
percent = 0
for i in range(len(eigenvalues)):
    percent += (eigenvalues[i]/total_variance)*100
    print(percent)
