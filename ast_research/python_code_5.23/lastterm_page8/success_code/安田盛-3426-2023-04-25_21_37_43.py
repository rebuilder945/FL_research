import math
def f(x):
    if x<20:
        return 6*x**2+1
    elif 20<=x<40:
        y=(3*x-60)
        return math.sqrt(y)
    else:
        return(100/(x+1))
        




x=eval(input())
print("{:.2f}".format(f(x)))
