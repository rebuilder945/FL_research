def f(x):
    import math
    if x<20:
        a=6*x**2+1
    elif x>=20 and x<40:
        a=math.sqrt(3*x-60)
    else:
        a=100/(x+1)
    return a
x=eval(input())
f(x)
print(x)
