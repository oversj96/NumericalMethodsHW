# Author: Justin Overstreet
# Purpose: Testing Newton's Method for finding zeros with a harder polynomial.
import numpy as np


def newton_method(x):
    return x - (np.sin(x) - np.e ** (np.negative(x))) / (np.cos(x) + np.e ** (np.negative(x)))


def newton_method_2(x):
    return x - ((4 * x ** 2 - np.e ** x - np.e ** np.negative(x)) / (8 * x - 2*np.sinh(x)))


def iterate(p0, func, tol=1e-5, maxiter=None):
    iter_val = [p0]
    i: int = 0
    e = 1
    while e > tol:
        p = func(iter_val[i])
        e = abs(iter_val[i] - p)
        iter_val.append(p)
        i += 1
        if maxiter is not None and i >= maxiter:
            break
    return iter_val


print(iterate(-1, newton_method_2))
print()
