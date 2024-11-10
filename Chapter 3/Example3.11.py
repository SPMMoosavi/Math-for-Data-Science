from keras.datasets import mnist
import numpy as np

(train_X, train_y), (test_X, test_y) = mnist.load_data()

dataset = train_X.reshape(60000,784)
dataset = dataset[:2000,:]
labels = train_y

# center dataset
m = np.mean(dataset,axis=0)
vectors = dataset - m

# rows of V are right singular vectors
V = np.linalg.svd(vectors)[2]

# no need to sort, already decreasing order
U = V[:11].T # top n rows as columns
P = np.dot(U,U.T)
