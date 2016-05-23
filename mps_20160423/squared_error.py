from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
#from draw_sigmoid import sigmoid

def squared_error(y, y0):
    return np.power(y - y0, 2.0)

if __name__ = '__main__':
    w = np.linspace(-20, 20, 100)
    b = np.linspace(-20, 20, 100)
    W, B = np.meshgrid(w, b)
    Z = squared_error(0, sigmoid(W, 1, B))
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot_wireframe(W, B, Z)
    plt.show()

