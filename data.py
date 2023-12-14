from math import pow

epslon = pow(10,-10)

#our function F(x)
def function(x):
    f = x**12 - 1.10
    return f
def derivative_function(x):
    return 12*x**11
#absolute value function
def absoluteValue(value):
    if(value < 0 ):
        value *= (-1)
    return value