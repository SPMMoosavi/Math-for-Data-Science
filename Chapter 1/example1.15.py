import matplotlib.pyplot as plt
import numpy as np

np.random.seed(1)
N = 20
rnd = np.random.random
dataset = np.array([ [rnd(), rnd()] for _ in range(N) ])
# Mean
m = np.mean(dataset, axis=0)
#Random point
p = np.array([rnd(), rnd()])

plt.grid()
X, Y = dataset[:,0], dataset[:,1]
plt.scatter(X,Y)
for v in dataset:
    plt.plot([m[0],v[0]],[m[1],v[1]],c='green')
    plt.plot([p[0],v[0]],[p[1],v[1]],c='red')
plt.show()

# Comparison of MSD of the mean and a random point
MSD_m = np.sum(np.abs(dataset-m)**2)/N
MSD_p = np.sum(np.abs(dataset-p)**2)/N
print(MSD_m, MSD_p) # 0.160478187272121 0.5984208474157081
