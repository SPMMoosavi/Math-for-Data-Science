import numpy as np

A = np.array([[1,2,3], [3,-5,-6], [1,4,-9]])
eigenvalues, eigenvectors = np.linalg.eig(A)  
print(f'{eigenvalues = }')
print(f'{eigenvectors = }')
