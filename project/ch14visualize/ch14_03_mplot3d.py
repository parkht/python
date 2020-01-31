
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np


def get_test_data(delta=0.05):
    '''
    Return a tuple X, Y, Z with a test data set.
    '''
    x = y = np.arange(-3.0, 3.0, delta)
    X, Y = np.meshgrid(x, y)

    Z1 = np.exp(-(X**2 + Y**2) / 2) / (2 * np.pi)
    Z2 = (np.exp(-(((X - 1) / 1.5)**2 + ((Y - 1) / 0.5)**2) / 2) /
          (2 * np.pi * 0.5 * 1.5))
    Z = Z2 - Z1

    X = X * 10
    Y = Y * 10
    Z = Z * 10
    return X, Y, Z


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Grab some test data.
X, Y, Z = axes3d.get_test_data(0.02)

# Plot a basic wireframe.
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

plt.show()
