# Author: Justin Overstreet
# Program: Implementation of Newton's Method.
# Purpose: Use Newton's Method to find A^(1/N).
# Date: 9-12-2019

def root(A, N):
    return A**(1/N)

def iterate(p0, N, func, tol=1e-6, maxiter=None):
    if p0 is 0:
        return 0
    if p0 < 0 and N % 2 == 0:
        print(f"Error: A = {p0} and N = {N} are respectively negative and even.")
        return None
    iter_val = [p0]
    i: int = 0
    e = 1
    while e > tol:
        p = func(iter_val[i], N)
        e = abs(iter_val[i] - p) / iter_val[i]
        iter_val.append(p)
        i += 1
        if maxiter is not None and i >= maxiter:
            break
    return iter_val


print(iterate(1, 4, root))
print()

