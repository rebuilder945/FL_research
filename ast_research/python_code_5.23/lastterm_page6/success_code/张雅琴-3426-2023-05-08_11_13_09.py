def f(x):
    if x<20:
        a=6*(x**2)+1
        return a
    elif 20<=x<40:
        b=(3*x-60)**0.5
        return b
    else:
        c=100/(x+1)
        return c
x=eval(input())
d=f(x)
print("%.2f"%d)
