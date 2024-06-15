def f(x):
    if x <20:
        n = 6*x**2+1
    elif x>=20 and x<40:
        n =(3*x-60)**0.5
    else:
        n = 100/(x+1)
    return n
x=eval(input())
print('%.2f'%f(x))
