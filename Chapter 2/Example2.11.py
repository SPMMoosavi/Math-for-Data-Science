import numpy as np
from sklearn import datasets
from sklearn.preprocessing import StandardScaler

iris = datasets.load_iris()

# The dataset
dataset = iris["data"]

# standardize dataset
vectors = StandardScaler().fit_transform(dataset)
Qcorr = np.corrcoef(dataset.T)
Qcov = np.cov(vectors.T,bias=True)
np.allclose(Qcov,Qcorr)
