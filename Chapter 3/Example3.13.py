from keras.datasets import mnist
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

(train_X, train_y), (test_X, test_y) = mnist.load_data()
dataset = train_X.reshape(60000,784)

N = len(dataset)
n = 10
engine = PCA(n_components = n)

reduced = engine.fit_transform(dataset)
reduced.shape

projected = engine.inverse_transform(reduced)
projected.shape

plt.figure(figsize=(10,5))
# eight subplots
rows, cols = 2, 4
v = dataset[1] # second image
plt.subplot(rows, cols, 1)
plt.imshow(np.reshape(v,(28,28)),cmap="gray_r")

for i,n in enumerate([784,600,350,150,50,10,1],start=2):
    engine = PCA(n_components = n)
    reduced = engine.fit_transform(dataset)
    projected = engine.inverse_transform(reduced)
    projv = projected[1]
    A = np.reshape(projv,(28,28))
    plt.subplot(rows, cols, i)
    plt.imshow(A,cmap="gray_r")
