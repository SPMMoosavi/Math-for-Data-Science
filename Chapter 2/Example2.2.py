import numpy as np

v1 = [1,6,11]
v2 = [2,7,12]
v3 = [3,8,13]
v4 = [4,9,14]
v5 = [5,10,15]
A = np.row_stack((v1,v2,v3,v4,v5))
print(A)
A_t = np.column_stack((v1,v2,v3,v4,v5))
print(A_t)
