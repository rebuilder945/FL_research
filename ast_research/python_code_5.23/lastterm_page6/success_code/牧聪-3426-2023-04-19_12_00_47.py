def found(x):
    if x <20:
        t=6*(x**2)+1
        print("%.2f"%t)
    elif x>=20 and x<40:
        t=(3*x-60)**0.5
        print("%.2f"%t)
    else:
        t=100/(x+1)
        print("%.2f"%t)
x=float(input())
found(x)


