# Author: Justin Overstreet
# Date: August 31, 2019
# Program: Fixed-point iteration test method
# Purpose: Numerical methods Computer Program Assignment #1

import math
import matplotlib.pyplot as pyplot
import matplotlib.lines as mlines
import numpy as np

# Store the rows of the fixed point iterations
rows = []

# Math expression to evaluate.
f1 = lambda x: x - (x**3) - 4*(x**2) + 10
f2 = lambda x: ((10/x) - (4*x))**(1/2)
f3 = lambda x: (1/2)*(10 - x**3)**(1/2)
f4 = lambda x: (10/(4 + x))**(1/2)
f5 = lambda x: x - ((x**3 + 4*x**2 - 10)/(3*x**2 + 8*x))

# To be consistent, entered y=x as a lambda function even though it's so simple.
fp = lambda x: x


def graph(formula, formula2, x_values, y_values, x_range):
    """Graph the formula and the lines of convergence with y=x."""
    x = np.linspace(1, x_range, 100)
    y = formula(x)
    y2 = formula2(x)
    pyplot.plot(x, y)
    pyplot.plot(x, y2)   
    pyplot.plot(x_values, y_values)
    pyplot.grid()
    pyplot.show()


def divergence(values):
    """Given a set of values, will determine if the pattern is diverging."""
    growth = 0
    max_value = 0
    for i in values:
        if(abs(i) > max_value):
            max_value = abs(i)
            growth = growth + 1
    if(growth == len(values)):
        return True
    else:
        return False


def fixed_point(func, p0=1, n=30, tol=1e-9):
    """Method for obtaining the fixed-point"""
    x_values = []
    y_values = []
    divcheck = []
    itr = 1
    max_x = p0
    while(itr <= n):
        p = func(p0)
        x_values.append(p0)
        y_values.append(p)
        x_values.append(p)
        y_values.append(fp(p))
        divcheck.append(p)
        if (p.real > max_x.real):
            max_x = p 
        if (itr % 5 == 0 and divergence(divcheck)):
            print("The formula is diverging.")
            break
        if (abs(p-p0) < tol):
            print("P = ", p)
            print("n = ", itr)
            graph(func, fp, x_values, y_values, math.ceil(max_x))
            break
        else:
            itr = itr + 1
            p0 = p
        if (itr == n):
            print("P = ", p)
            print("n = ", itr)
            graph(func, fp, x_values, y_values, math.ceil(max_x.real))
    

fixed_point(f1) # Function 1 is divergent. While n goes to infinity, so too does f1.
fixed_point(f2)
fixed_point(f3)
fixed_point(f4)
fixed_point(f5)

#with open('table.txt', 'w') as table:
    
