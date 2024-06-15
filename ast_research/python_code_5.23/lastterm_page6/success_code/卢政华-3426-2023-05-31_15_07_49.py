def f(x):
    if x<20:
        f=6*x**2+1
    elif 20<=x<40:
        f=(3*x-60)**0.5
    elif x>=40:
        f=100/x+1
x=eval(input())
print(f(x))

