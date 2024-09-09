import numpy as np

def tensor(u,v):
    return np.array([ [ a*b for b in v] for a in u ])

np.random.seed(1)
N = 20
rnd = np.random.random
dataset = np.array([ [rnd(), rnd()] for _ in range(N) ])
# mean
m = np.mean(dataset,axis=0)
# center dataset
vectors = dataset - m
# covariance
Q = np.mean([ tensor(v,v) for v in vectors ],axis=0)
print(Q)