import numpy as np
from sklearn import datasets

iris = datasets.load_iris()

# The dataset
dataset = iris["data"]

# Mean
m = np.mean(dataset,axis=0)

# Centered dataset
vectors = dataset - m

# Covariance
N = len(vectors)
#   Biased
Q = np.dot(vectors.T,vectors)/N
Q = np.cov(dataset,rowvar=False,ddof=0)
Q = np.cov(dataset.T,ddof=0)

#   Unbiased
Q = np.dot(vectors.T,vectors)/(N-1)
Q = np.cov(dataset,rowvar=False)
Q = np.cov(dataset.T)

# Total Variance
TV = np.trace(Q)
