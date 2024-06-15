def f(x):
    if x<20:
        a=6*x**2+1
    elif x>=20 and x<40:
        a=(3*x-60)**0.5
    else:
        a=100/(x+1)
    return a
n=eval(input())
t=f(n)
print("%.2f"%t)
