import numpy as np

def angle(u,v):
	a = np.dot(u,v)
	b = np.dot(u,u)
	c = np.dot(v,v)
	theta = np.arccos(a / np.sqrt(b*c))
	return np.degrees(theta)

v1 = np.array([1,2])
v2 = np.array([3,4])
print(angle(v1,v2)) #returns 10.304846468766044 in degree