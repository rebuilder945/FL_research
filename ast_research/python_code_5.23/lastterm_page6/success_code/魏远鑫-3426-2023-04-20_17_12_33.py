def f(x):
    if x<20:
        m=6*x*x+1
        return m
    if 20<= x <40:
        m=(3*x-60)**0.5
        return m
    else:
        m=100/(x+1)
        return m
n=eval(input())
f(n)
print("%.2f"%n)
