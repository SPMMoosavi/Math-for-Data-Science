import numpy as np

u = np.array([1,2,3])
v = np.array([4, 5, 6])

u_dot_v = np.dot(u,v)
print(u_dot_v)

u_dot_v_ = u[0]*v[0] + u[1]*v[1] + u[2]*v[2]
print(u_dot_v_)

print(u_dot_v == u_dot_v_)
