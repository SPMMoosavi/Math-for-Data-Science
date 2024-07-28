import matplotlib.pyplot as plt
import numpy as np

def ellipse(a, b, c, levels, color):
    L, delta = 4, .1
    x = np.arange(-L,L,delta)
    y = np.arange(-L,L,delta)
    X,Y = np.meshgrid(x, y)
    plt.contour(X, Y, a*X**2 + 2*b*X*Y + c*Y**2, levels, colors=color)


# Q1
a, b, c = 9, 0, 4

# Inverse Covariance entities
det = a*c - b**2
A, B, C = c/det, -b/det, a/det

plt.grid()
ellipse(a, b, c, [20], 'blue')
ellipse(A, B, C, [1], 'red')
plt.show()

# Q2
a, b, c = 9, 2, 4

# Inverse Covariance entities
det = a*c - b**2
A, B, C = c/det, -b/det, a/det

plt.grid()
ellipse(a, b, c, [1], 'blue')
ellipse(A, B, C, [1], 'red')
plt.show()