def f(x):
    if x<20:
        return 6*x**2+1
    elif x>=20 and x<40:
        return (3*x-60)**1/2
    elif x>=40:
        return 100/(x+1)
x=eval(input())
b=f(x)
print("%.2f"%(b))
