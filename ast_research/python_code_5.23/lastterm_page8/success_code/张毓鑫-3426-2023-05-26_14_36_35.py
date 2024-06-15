def f(x):
    if x<20:
        a=6*(x**2)+1
        print('%.2f',a)
    elif 20<=x<40:
        b=3*x-60
        a=b**0.5
        print('%.2f',a)
    else:
        b=x+1
        a=100/b
        print('%.2f',a)
x=eval(input())
f(x)

