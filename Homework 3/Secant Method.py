# Author: Justin Overstreet
# Purpose: Test Secant Method for homework questions 3 and 4.

import numpy as np


def secant_method(x, x2):
    return x - ((x**2 - 2*x - 1)*(x - x2))/((x**2 - 2*x - 1) - (x2**2 - 2*x2 - 1))


def secant_method_trig(x, x2):
    return x - (((np.sin(x)) - np.e**(np.negative(x)))*(x - x2))/(((np.sin(x)) - np.e**(np.negative(x))) - (
                np.sin(x2) - np.e ** (np.negative(x2))))


def iterate_method_multi_val(iter_val, func, tol=1e-4, maxiter=None):
    i: int = 0
    e = 1
    while e > tol:
        p = func(iter_val[i+1], iter_val[i])
        e = abs(iter_val[i+1] - p)
        iter_val.append(p)
        i += 1
        if maxiter is not None and i >= maxiter:
            break
    return iter_val


print(iterate_method_multi_val([0.2, 0.1], secant_method_trig))
print()
