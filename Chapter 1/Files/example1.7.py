import numpy as np
from numpy.random import random as rd
import matplotlib.pyplot as plt
N = 20
dataset = np.array([[rd(), rd()] for _ in range(N)])
mean = np.mean(dataset,axis=0)
plt.grid()
X, Y = dataset[:,0], dataset[:,1]
plt.scatter(X,Y)
plt.scatter(*mean)
plt.annotate('$m$', xy=mean+0.01)
plt.show()