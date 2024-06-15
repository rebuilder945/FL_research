def f(x):
    if x <20:
        n=6*x**2+1
        return n
    elif 20<= x <40:
        n=(3*x-60)**0.5
        return n
    elif x>=40:
        n=100/(x+1)
        return n

x=float(input())
n=f(x)
print("%.2f"%n)

