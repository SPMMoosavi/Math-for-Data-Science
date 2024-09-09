import numpy as np

np.random.seed(1)
N = 20
rnd = np.random.random
dataset = np.array([ [rnd(), rnd()] for _ in range(N) ])
# covariance
Q = np.cov(dataset,bias=True,rowvar=False)
print(Q)