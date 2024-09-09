import numpy as np

A = np.array([[1,6,11],[2,7,12],[3,8,13],[4,9,14],[5,10,15]])
print(A)
print(A.shape)
print(len(A))
print(A[1])
print(A[1,2])
print(A[1:3])

# transpose
At = np.transpose(A)
print(At)
print(At.shape)
print(len(At))
print(At[1])
print(At[1,2])
print(At[1:3])
