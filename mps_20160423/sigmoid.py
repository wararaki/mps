import numpy as np
from matplotlib import pyplot as plt

def sigmoid(alpha, x):
    return 1.0 / (1.0 + np.exp(-alpha * x))

if __name__ == '__main__':
    x = np.linspace(-5.0, 5.0, 100)
    s = np.vectorize(sigmoid)

    plt.plot(x, s(1.0, x), label = str(1.0))
    plt.show()

# 後で書く。
