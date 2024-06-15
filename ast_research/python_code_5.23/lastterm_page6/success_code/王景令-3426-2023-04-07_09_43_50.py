def f(x):
    if x < 20:
        x = 6*x*x + 1
        return x
    elif x < 40:
        x = pow(3*x - 60,1/2)
        return x
    elif x >= 40:
        x = 100/(x+1)
        return x
a = eval(input())
a = f(a)
print('%.2f'%a)
