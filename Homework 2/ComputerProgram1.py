# Author: Justin Overstreet
# Date: August 31, 2019
# Program: Fixed-point iteration test method
# Purpose: Numerical methods Computer Program Assignment #1

import math
import matplotlib.pyplot as pyplot
import numpy as np


class Table:
    def __init__(self, xvals, yvals):
        super().__init__()
        self.x_vals = xvals
        self.y_vals = yvals


tables = []
# Math expression to evaluate.
f1 = lambda x: x - (x**3) - 4*(x**2) + 10
f2 = lambda x: ((10/x) - (4*x))**(1/2)
f3 = lambda x: (1/2)*(10 - x**3)**(1/2)
f4 = lambda x: (10/(4 + x))**(1/2)
f5 = lambda x: x - ((x**3 + 4*x**2 - 10)/(3*x**2 + 8*x))

# To be consistent, entered y=x as a lambda function even though it's so simple.
fp = lambda x: x


def graph(formula, formula2, rows_x, rows_y, x_range):
    """Graph the formula and the lines of convergence with y=x."""
    x = np.linspace(1, x_range, 100)
    y = formula(x)
    y2 = formula2(x)
    pyplot.plot(x, y)
    pyplot.plot(x, y2)   
    pyplot.plot(rows_x, rows_y)
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
    divcheck = []
    rows_x = []
    rows_y = []
    itr = 1
    max_x = p0
    while(itr <= n):
        p = func(p0)
        if (type(p0) is complex or type(p) is complex):
            rows_x.append("Diverging")
            rows_y.append("Diverging")
        else:
            rows_x.append(p0)
            rows_y.append(p)
        # rows_x.append(p)
        # rows_y.append(fp(p))
        divcheck.append(p)
        if (p.real > max_x.real):
            max_x = p 
        if (itr % 5 == 0 and divergence(divcheck)):
            for i in range(itr-1, n):
                rows_x.append("Diverging")
                rows_y.append("Diverging")
            tables.append(Table(rows_x, rows_y))
            break
        if (itr == n):
            print("P = ", p)
            print("n = ", itr)
            # graph(func, fp, rows_x, rows_y, math.ceil(max_x))
            tables.append(Table(rows_x, rows_y))
            break
        else:
            itr = itr + 1
            p0 = p
            # graph(func, fp, rows_x, rows_y, math.ceil(max_x.real))
    

cases_dict = {'A': f1, 'B': f2, 'C': f3, 'D': f4, 'E': f5}


for c,v in cases_dict.items():
    fixed_point(v)
print(f'{"Iteration":<15}|{"A":^25}|{"B":^25}|{"C":^27}|{"D":^27}|{"E":^26}|')
print('{:_<150}'.format(''))
for i in range(1, 31):
    print(f'N = {str(i)[:10]:<10} | {str(tables[0].x_vals[i-1])[:10]:<10} | {str(tables[0].y_vals[i-1])[:10]:<10} | {str(tables[1].x_vals[i-1])[:10]:<10} | {str(tables[1].y_vals[i-1])[:10]:<10} | {tables[2].x_vals[i-1]:<2.9f} | {tables[2].y_vals[i-1]:2.9f} | {tables[3].x_vals[i-1]:<2.9f} | {tables[3].y_vals[i-1]:2.9f} | {tables[4].x_vals[i-1]:<2.9f} | {tables[4].y_vals[i-1]:2.9f}')
print("\nCase 'E': Converged most quickly where N=5 is the first to show repetition.")


# with open('table.txt', 'w') as table:
    
