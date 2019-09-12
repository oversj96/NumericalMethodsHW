# Author: Justin Overstreet
# Program: Implementation of Newton's Method.
# Purpose: Use Newton's Method to find A^(1/N).
# Date: 9-12-2019


def root(p, A, N):
    return p - ((p**N - A)/((N*p)**(N-1)))


def display(iterations, error, interval, tol):
    print(f"Process took {interval} iterations and resulted in an error less than {error}.")
    print(f"Desired tolerance was: {tol}")
    for x in range(0, len(iterations)):
        print(f"N = {x} : {str(iterations[x]):<9}")


def iterate(A, N, func, tol=1e-6, maxiter=None):
    p0 = A
    if A is 0:
        return 0
    if A < 0 and N % 2 == 0:
        print(f"Error: A = {p0} and N = {N} are respectively negative and even.")
        return None
    iter_val = [p0]
    i: int = 0
    e = 1
    while e > tol:
        p = func(iter_val[i], A, N)
        e = abs(iter_val[i] - p)
        iter_val.append(p)
        i += 1
        if maxiter is not None and i >= maxiter:
            break
    display(iter_val, e, i, tol)


iterate(3, 4, root)

