def f(x):
    if x < -10:
        return 0
    elif x >= -10 and x < 0:
        return x + 10
    elif x >= 0 and x < 10:
        return x
    elif x >= 10 and x <20:
        return 0.5 * x - 5
    else:
        return 0.8 * x - 8
x = float(input())
result = f(x)
print("%.2f" % result)

