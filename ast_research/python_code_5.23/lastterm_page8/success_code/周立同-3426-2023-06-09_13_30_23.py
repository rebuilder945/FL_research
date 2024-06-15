def f(x):
    if x<20:
        return 6*(x**2)+1
    elif 20<=x<40:
        return (3*x-60)**(1/2)
    else:
        return 100/(x+1)
a=f(eval(input()))
b="%.2f"%(a)
print(b)
