from keras.datasets import mnist
import numpy as np
import matplotlib.pyplot as plt

def pca_evd(dataset,n):
    Q = np.cov(dataset.T)
    eigenvalues, eigenvectors = np.linalg.eig(Q)
    order = eigenvalues.argsort()[::-1]
    V = eigenvectors[:,order[:n]]
    P = np.dot(V,V.T)
    return P

def pca_svd(dataset,n):
    dataset = dataset[:2000,:]
    m = np.mean(dataset,axis=0)
    vectors = dataset - m
    V = np.linalg.svd(vectors)[2]
    U = V[:n].T
    P = np.dot(U,U.T)
    return P

def plot_mnist(dataset, func_name):
    plt.figure(figsize=(10,5))
    # eight subplots
    rows, cols = 2, 4
    v = dataset[1] # second image
    plt.subplot(rows, cols, 1)
    plt.imshow(np.reshape(v,(28,28)),cmap="gray_r")

    for i,n in enumerate([784,600,350,150,50,10,1],start=2):
        P = func_name(dataset,n)
        projv = np.dot(P.real,v)
        A = np.reshape(projv,(28,28))
        plt.subplot(rows, cols, i)
        plt.imshow(A,cmap="gray_r")

(train_X, train_y), (test_X, test_y) = mnist.load_data()
dataset = train_X.reshape(60000,784)
plot_mnist(dataset, pca_evd)
plot_mnist(dataset, pca_svd)

