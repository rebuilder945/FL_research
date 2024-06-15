def f(x):
    if x < 20:
        return 6*x**2+1
    elif x < 40:
        return (3*x-60)**0.5
    else:
        return 100/(x+1)
a = eval(input())
b = f(a)
print('%.2f'%b)
