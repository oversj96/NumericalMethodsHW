# Author: Justin Overstreet
# Date: August 31, 2019
# Program: Fixed-point iteration test method
# Purpose: Numerical Methods Homework 2, Problem 2, solution finding.

# Math expression to evaluate.
f = lambda x: (3*x**2 + 3)**(1/4)

# Initial variables.
p0 = 1
n = 30
tol = 10e-2
itr = 1

# Iterative loop.
while(itr <= n):
    p = f(p0)
    if (abs(p-p0) < tol):
        print(p)
        break
    else:
        itr = itr + 1
        p0 = p

# Resulting solution after 3 iterations: P = 1.8859437430173158