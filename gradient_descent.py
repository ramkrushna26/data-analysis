

# Gradient descent algorithm
# An algorithm to minimize function by optimizing parameters

import numpy as np

start = 140
end = 75
learn_rate = 0.1
max_iter = len(x)
tolerance = 0.02

def function(x):
    return alpha * x**2

def gradient_function(x):
    alpha = np.random.randn()
    print("alpha : ", alpha)
    return 2 * x * alpha

def gradient_descent(start, end, gradient_function, learn_rate, max_iter, tolerance):
    steps = [start-end] # history tracking
    x = start
    
    for _ in range(max_iter):
        diff = learn_rate * gradient_function(x)
        if np.abs(diff) < tolerance:
            break
        x = x - diff
        steps.append(x) # history tracing
        print("value os x - ", x)
        if x < end:
            break

gradient_descent(start, end, gradient_function, 0.1, max_iter, tolerance)  


