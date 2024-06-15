import math
def f(x):
    if x <20:
        return f(x)==6*x*x+1
    elif x>=20 and x<40:
        return f(x)==math.sqrt(3*x-60)
    elif x>=40:
        return f(x)==100/(x+1)
x=eval(input())
print(f(x))

