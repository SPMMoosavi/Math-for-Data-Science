import numpy as np

# projection of column vector b onto column space of A
def project_col(A,b):
    Aplus = np.linalg.pinv(A)
    x = np.dot(Aplus,b) # reduced
    return np.dot(A,x) # projected

# projection of column vector b onto row space of A
def project_row(A,b):
    Aplus = np.linalg.pinv(A)
    AplusA = np.dot(Aplus,A)
    return np.dot(AplusA,b) # projected

A = np.array([[1,6,11],[2,7,12],[3,8,13],[4,9,14],[5,10,15]])

b = np.array([-9,-3,3,9,10])
project_col(A, b.T)

b = np.array([-9,-3,3])
project_row(A, b.T)
