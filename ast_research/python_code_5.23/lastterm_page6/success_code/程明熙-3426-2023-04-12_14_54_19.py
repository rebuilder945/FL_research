def f(x):
    if x<20:
        s=6*x**2+1
    elif 20<=x<40:
        s=(3*x-60)**1/2
    else:
        s=100/(x+1)
    print('%.2f'%s)
x=eval(input())
f(x)
