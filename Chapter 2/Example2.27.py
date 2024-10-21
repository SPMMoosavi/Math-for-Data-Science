from keras.datasets import mnist
import numpy as np

(train_X, train_y), (test_X, test_y) = mnist.load_data()

vectors = train_X.reshape(60000,784) # each image in one row

vectors = np.array(vectors)
rank = np.linalg.matrix_rank(vectors) # returns 712
