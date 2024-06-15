def f(x):
    if x<20:
        x=6*x**2+1
        print("%.2f"%x)
    elif (x>=20 and x<40):
        x=(3*x-60)**0.5
        print("%.2f"%x)
    elif x>=40:
        x=100/(x+1)
        print("%.2f"%x)

n=eval(input())
f(n)
