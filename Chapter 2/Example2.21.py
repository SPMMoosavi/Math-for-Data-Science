import numpy as np
import scipy as sc

dataset = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]])
Q = np.cov(dataset.T)
N = sc.linalg.null_space(Q)
nullity = N.shape[1]
