import math
def f(x):
    if x<20:
        y=6*x**2+1
    elif 20<=x<40:
        y=math.sqrt(3*x-60)
    else:
        y=100/(x+1)
    return y

x=eval(input())
y=f(x)
print ("%.2f"%y)

