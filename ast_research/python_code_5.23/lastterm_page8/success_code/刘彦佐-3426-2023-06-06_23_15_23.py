def f(x):
    if x<20:
        q=6*x**2+1
    if 20<=x<40:
        q=(3*x-60)**0.5
    if x>=40:
        q=100/(x+1)
    return q
a=eval(input())
print("%.2f"%f(a))
