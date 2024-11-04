import sympy as sm

a, b, c = sm.symbols("a b c")

Q = sm.Matrix([[a, b], [b, c]])
V, D = Q.diagonalize()
Q
V
D
