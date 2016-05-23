# import library
import math

# define an accepted rate
accepted_error = 0.1
delta_x = 0.01
learning_rate = 0.05
number_of_trial = 1000


# test function
# f(x) = x^2
def test_func(x):
    return x ** 2


# differential function
# f'(x) = (f(x_1) - f(x_0)) / (x_1 - x_0)
def diff(f, x):
    return (f(x + delta_x) - f(x)) / ((x + delta_x) - x)


# exploring a minimum result
def test(f, x):
    # number of trial
    i = 1
    
    # exploring
    while math.sqrt(x ** 2) > accepted_error and i <= number_of_trial:
        print("test case {0}: {1}".format(i, x))
        x = x - learning_rate * diff(f, x)
        i = i + 1
    
    return x
        
if __name__ == "__main__":
    result = test(test_func, 5)
    print("final result: {0}".format(result))
    
