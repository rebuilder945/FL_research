def f(x):
    if x<20:
        y=6*x**2+1
    elif 20<=x<40:
        y=(3*x-60)**0.5
    elif x>=40:
        y=100/(x+1)
    yi="%.2f"%y
    return yi
n=eval(input())
m=f(n)
print(m)

