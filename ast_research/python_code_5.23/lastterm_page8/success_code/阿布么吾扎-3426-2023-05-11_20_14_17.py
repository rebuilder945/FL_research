def f(x):
    if x<20:
        s=6*x**2+1
    elif 20<=x<40:
        s=(3*x-60)**0.5
    else:
        s=100/(x+1)
    return s
a=eval(input())
s=f(a)
print("%.2f"%s)
