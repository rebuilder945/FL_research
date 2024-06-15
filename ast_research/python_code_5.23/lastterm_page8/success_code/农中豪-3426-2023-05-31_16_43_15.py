from math import sqrt
def f(n):
    if n<20:
        return 6*n**2+1
    elif n>=20 and n<40:
        return sqrt(3*n-60)
    else:
        return 100/(n+1)
x=eval(input())
print('%.2f'%f(x))
