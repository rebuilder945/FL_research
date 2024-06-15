def f(x):
    if x<20:
        a=6*x**2+1
        return a
    elif 20<=x<40:
        a=(3*x-60)**1/2
        return a
    elif x>=40:
        a=100/(x+1)
        return a
x=eval(input())
a=f(x)
print(a)
