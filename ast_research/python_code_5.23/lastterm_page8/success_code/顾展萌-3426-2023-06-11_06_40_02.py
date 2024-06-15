
def f(x):
    if x < -10:
        return -1/x
    elif -10 <= x and x < 0:
        return -x**2 + 2*x
    elif 0 <= x and x < 10:
        return x + 3
    else:
        return x

x = float(input())
print('%.2f' % f(x))

