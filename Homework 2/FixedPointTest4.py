# Author: Justin Overstreet
# Date: August 31, 2019
# Program: Fixed-point iteration test method
# Purpose: Numerical Methods Homework 2, Problem 4, solution finding.

import math

def print_row(n, p):
    print("N =", n, " P =", p)

# Math expression to evaluate.
f = lambda x: (1/2)*(x + 3/x)

# Initial variables.
p0 = 1
n = 10
tol = 10e-4
itr = 1

# Iterative loop.
while(itr <= n):
    p = f(p0)
    print_row(itr, p)
    if (abs(p-p0) < tol):
        print("Solution within tolerance = ", p)
        break
    else:
        itr = itr + 1
        p0 = p

