# Author: Justin Overstreet
# Date: August 31, 2019
# Program: Fixed-point iteration test method
# Purpose: Numerical methods Computer Program Assignment #1

import math
import matplotlib.pyplot as pyplot
import matplotlib.lines as mlines
import numpy as np

# Math expression to evaluate.
f1 = lambda x: x - (x**3) - 4*(x**2) + 10
f2 = lambda x: ((10/x) - (4*x))**(1/2)
f3 = lambda x: (1/2)*(10 - x**3)**(1/2)
f4 = lambda x: (10/(4 + x))**(1/2)
f5 = lambda x: x - ((x**3 + 4*x**2 - 10)/(3*x**2 + 8*x))

# To be consistent, entered y=x as a lambda function even though it's so simple.
fp = lambda x: x

def newline(p1, p2):
    line = mlines.Line2D(np.linspace(p1[0], p1[1], 100), np.linspace(p2[0], p2[1], 100), None, '--')
    return line

# Graph the formula and the lines of convergence with y=x.
def graph(formula, formula2, x_values, y_values, x_range):
    x = np.linspace(1, x_range, 100)
    y = formula(x)
    y2 = formula2(x)
    pyplot.plot(x, y)
    pyplot.plot(x, y2)   
    pyplot.plot(x_values, y_values)
    pyplot.grid()
    pyplot.show()


# Method for obtaining the fixed-point
def fixed_point(func, p0=1, n=30, tol=1e-9):
    x_values = []
    y_values = []
    itr = 1
    max_x = p0
    while(itr <= n):
        p = func(p0)
        x_values.append(p0)
        y_values.append(p)
        x_values.append(p)
        y_values.append(fp(p))
        if (p > max_x):
            max_x = p       
        if (abs(p-p0) < tol):
            print("P = ", p)
            print("n = ", itr)
            graph(func, fp, x_values, y_values, math.ceil(max_x))
            break
        else:
            itr = itr + 1
            p0 = p
        if (itr == n):
            print("Exceeds", itr, "iterations to obtain a value within tolerance, if possible at all.")
    

#fixed_point(f1) # Function 1 is divergent. While n goes to infinity, so too does f1.
#fixed_point(f2)
#fixed_point(f3)
fixed_point(f4)
fixed_point(f5)

# Divergent
# Exceeded 30 iterations to obtain a value within tolerance.
# Exceeded 30 iterations to obtain a value within tolerance.
# P =  1.3652300134682094
# n =  11
# P =  1.3652300134140969
# n =  5
# Conclusion: The fifth function converges to the fixed-point the quickest.
