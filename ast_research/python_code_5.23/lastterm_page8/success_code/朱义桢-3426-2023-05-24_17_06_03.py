def f(x):
    if x <20:
        return(6*x**2+1)
    elif x>=40:
        return(100/(x+1))
    else:
        return((3*x-60)**(1/2))
a=eval(input())
b=f(a)
print("%.2f"%b)
