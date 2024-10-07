import sympy as sm

u = sm.Matrix([1,2,3,4,5])
v = sm.Matrix([6,7,8,9,10])
w = sm.Matrix([11,12,13,14,15])
A = sm.Matrix.hstack(u,v,w)

A.pinv()

b = sm.Matrix([-9,-3,3,9,10])
A.pinv()*b
