def f(x):
    if x<20:
        return(6*x**2+1)
    elif x>=40:
        return(100/(x+1))
    elif x<40 and x>=20:
        return((3*x-60)**0.5)
a=eval(input())
b=f(a)
print("{x:.2f}".format(x=b))
