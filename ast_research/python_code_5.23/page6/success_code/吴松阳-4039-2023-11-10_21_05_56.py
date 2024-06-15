import math
def amour(x):
    if x < 20:
        y = 6*x**2+1
        return y
    elif x in range(20,40):
        y = 3*x-60
        z = math.sqrt(y)
        return z
    else:
        y = 100/(x+1)
        return y
x = float(input())
y = amour(x)
print('{:.2f}'.format(y))
