import numpy as np

# projection of column vector b onto column space of U
# with orthonormal columns
def project_col_ortho(U,b):
    x = np.dot(U.T,b) # reduced
    return np.dot(U,x) # projected

# Matrices with orthnormal columns
U1 = np.array([[1,0,0],[0,1,0],[0,0,1]])
U2 = np.array([[1,1,1]/np.sqrt(3),[1,-1,0]/np.sqrt(2),[1,1,-2]/np.sqrt(6)])
U3 = np.array([[1,0,0],[0,1,0],[0,0,1],[0,0,0],[0,0,0]])

b = np.array([1,2,3]).reshape(3,1)

project_col_ortho(U1, b)
project_col_ortho(U2, b)

b = np.array([1,2,3,4,5]).reshape(5,1)

project_col_ortho(U3, b)
