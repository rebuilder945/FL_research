def f(x):
    if x <20:
        y=6*x**2+1
    elif 40>x>=20:
        y=(3*x-60)*0.5
    elif x>=40:
        y=100/(x+1)
    return(y)
x=eval(input())
f(x)
print("%.2f"%"y")
