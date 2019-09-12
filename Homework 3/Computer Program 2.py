# Author: Justin Overstreet
# Program: Implementation of Newton's Method.
# Purpose: Use Newton's Method to find A^(1/N).
# Date: 9-12-2019


def root(p, A, N):
    return p - ((p**N - A)/(N*p**(N-1)))


def display(iterations, error, interval, tol, A, N):
    print(f"Process took {interval} iterations and resulted in an error less than {error}.")
    print(f"Desired error was to be less than {tol}")
    print(f"Final result for {A}^(1/{N}) was: {iterations[len(iterations)-1]}")
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
    display(iter_val, e, i, tol, A, N)


iterate(3, 4, root)

''' ---- Output ----
Process took 7 iterations and resulted in an error less than 2.662514442253183e-07.
Desired error was to be less than 1e-06
Final result for 3^(1/4) was: 1.3160740129525732
N = 0 : 3
N = 1 : 2.2777777777777777
N = 2 : 1.7717972993233797
N = 3 : 1.463688102853308
N = 4 : 1.336940995805593
N = 5 : 1.3165574873704087
N = 6 : 1.3160742792040174
N = 7 : 1.3160740129525732
'''