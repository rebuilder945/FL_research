import math

def f(x):
    if x < 20:
        return round(6 * x ** 2 + 1, 2)
    elif 20 <= x < 40:
        return round(math.sqrt(3 * x- 60) , 2)
    else:
        return round(100/(x+1), 2)

x = float(input())
result = f(x)
print('%.2f' % result)
