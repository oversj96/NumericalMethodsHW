# Author: Justin Overstreet
# Date: August 31, 2019
# Program: Fixed-point iteration test method
# Purpose: Numerical Methods Homework 2, Problem 3a, solution finding.

import math

# Math expression to evaluate.
f = lambda x: math.pi + math.sin(x)/2

# Initial variables.
p0 = 0
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

# Resulting solution after 3 iterations: P = 3.141592653589793