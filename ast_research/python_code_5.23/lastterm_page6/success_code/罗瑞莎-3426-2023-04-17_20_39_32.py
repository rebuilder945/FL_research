def f(x):
    s = 0
    if x<20:
        s = 6*x**2+1
        print("%.2f"%s)
    elif x>=20 and x<40:
        s = (3*x-60)**0.5
        print("%.2f"%s)
    elif x>=40:
        s = 100/(x+1)
        print("%.2f"%s)
x = eval(input())
f(x)
