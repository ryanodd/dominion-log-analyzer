import math

def factorial(x):
    if (x == 0):
        return 1
    else:
        return math.gamma(x)

def nCr(n,r):
    return factorial(n) / factorial(r) / factorial(n-r)