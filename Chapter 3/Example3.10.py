from keras.datasets import mnist
import numpy as np

(train_X, train_y), (test_X, test_y) = mnist.load_data()

dataset = train_X.reshape(60000,784)
labels = train_y

# Covariance and total variance
Q = np.cov(dataset.T)
totvar = Q.trace()

# Eigendata
eigenvalues, eigenvectors = np.linalg.eig(Q)

# Percentage of eigenvalues in total varince
percent = eigenvalues*100/totvar

# cumulative sums
sums = np.cumsum(percent)

data = np.array([percent,sums])
data20 = data.T[:20].real.round(decimals=3)
for index in range(len(data20)):
    print(f'{index} ==> {data20[index][0]} ==> {data20[index][1]}')

# Plots
import matplotlib.pyplot as plt

plt.stairs(percent, range(len(eigenvalues)+1))

plt.stairs(percent, range(len(eigenvalues)+1))
plt.xlim(0,20)

plt.stairs(sums, range(len(eigenvalues)+1))
indices_above_50 = np.where(sums > 50)[0][0]
plt.scatter(indices_above_50, sums[indices_above_50], color='red', label='Above 50', zorder=5)
text = f'({indices_above_50}, {sums[indices_above_50].real:.2f})'
plt.annotate(text, xy=(indices_above_50, sums[indices_above_50]), xytext=(indices_above_50+200, sums[indices_above_50]),
arrowprops=dict(arrowstyle= '->', color='blue', lw=3.5, ls='--'))

# projection matrix onto top 11
# eigenvectors of covariance
# of dataset
order = eigenvalues.argsort()[::-1]
V = eigenvectors[:,order[:11]]
P = np.dot(V,V.T)
