# Author: Justin Overstreet
# Purpose: Testing Newton's Method for finding zeros with a harder polynomial.
import numpy as np

def f(x):
        return x - (np.sin(x) - np.e**(np.negative(x))) / (np.cos(x) + np.e**(np.negative(x)))


def newton_method(p0, func, tol=1e-4, maxiter=None):
    iter_val = [p0]
    i: int = 0
    e = 1
    while (e > tol):
        p = func(iter_val[i])
        e = abs(iter_val[i] - p)
        iter_val.append(p)
        i += 1
        if (maxiter is not None and i >= maxiter):
            break
    return iter_val


print(newton_method(0, f))
print("test")