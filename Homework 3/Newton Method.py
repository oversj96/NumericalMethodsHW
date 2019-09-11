# Author: Justin Overstreet
# Purpose: Test Newton-Raphson Method for finding zeros.


def f(x):
    return x - ((x ** 2 - 2 * x - 1) / (2 * x - 2))

list = [2.5]
i = 0
while (len(list) < 4):
    list.append(f(list[i]))
    i += 1
print(list)
