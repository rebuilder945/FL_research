def f(x):
    if x<20:
        a=6*x**2+1
    elif 20<=x<40:
        a=(3*x-60)**0.5
    else: a=100/(x+1)
    return a
x=eval(input())
print('%.2f'%(f(x)))
