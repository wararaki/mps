# import python library (numpy)
import numpy as np

# To Do: read a numpy official document
#      : axis parameter

# define neuron class
class Neuron:
    # initialization Neuron instance
    def __init__(self, w, b, f):
        # concat weights parameter and bias parameter
        self.w = np.concatenate((w, b), axis=1)
        self.f = f

    # define output neuron calulation
    def output(self, x):
        x = np.concatenate((x, [[1,],]))
        # calculate this neuron
        return self.f(self.w.dot(x))


# define evaluation function
def f(u):
    u[u > 0] = 1
    u[u <= 0] = -1
    return u


if __name__ == '__main__':
    # sample parameters
    # 4 input, 1 output
    # w_ary = [[0, 1, -0.5, 0.3],]
    # bias = [[1,],]
    # x_ary = [[0.6,], [0.1,], [-0.2,], [0.3,],]

    # 2 input, 2 output
    w_ary = [[0.5, 0.7,], [-0.1, -0.3,]]
    bias = [[0.1,], [0.1]]
    x_ary = [[-1,], [0.2,]]

    # create a neuron instance
    neuron = Neuron(w_ary, bias, f)

    # output the results of the neuron calculation
    print(neuron.output(x_ary))
