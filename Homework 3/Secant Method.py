# Author: Justin Overstreet
# Purpose: Test Secant Method for homework questions 3 and 4.

from sympy import E, sin, ln


def secant_method(form, x,  x2):
    pass


def secant_method_trig(x, x2):
    return x - ((((sin(x)) - E ** -x) * (x - x2)) / ((sin(x)) - E ** -x - (sin(x2) - E ** -x2)))


def secant_method_q6(x, x2):
    return x - ((((x-2)**2 - ln(x))*(x-x2))/(((x-2)**2 - ln(x)) - ((x2-2)**2 - ln(x2))))


def iterate_method_multi_val(iter_val, func, tol=1e-5, maxiter=None):
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


print(iterate_method_multi_val([0.2, 0.1], secant_method_q6))
print()
