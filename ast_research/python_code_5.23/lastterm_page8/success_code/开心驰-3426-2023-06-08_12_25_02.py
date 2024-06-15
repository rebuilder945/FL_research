def f(x):
    if x <20:
        return x**2*6+1
    elif x>=20 and x <40:
        return (x*3-60)**0.5
    else:
        return 100/(x+1)
x=eval(input())
print("%.2f"%f(x))

