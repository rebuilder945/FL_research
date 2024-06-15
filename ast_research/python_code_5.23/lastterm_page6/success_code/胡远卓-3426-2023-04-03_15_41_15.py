import math
def f(x):
    if x<20:
        return 6*x*x+1
    elif x>=20 and x<40:
        return math.sqrt(3*x-60)
    else:
        return 100/(x+1)

x=eval(input())
print("%.2f"%f(x))
