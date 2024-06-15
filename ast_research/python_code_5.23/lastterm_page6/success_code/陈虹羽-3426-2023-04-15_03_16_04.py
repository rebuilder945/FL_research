def f(x):
    if x<20:
        c=6*x**2+1
    elif  20<=x<40:
        c=(3*x-60)**(1/2)
    else:
        c=100/(x+1)
    return c
x=eval(input())
print("%.2f"%(f(x)))

