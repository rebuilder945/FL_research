def f(x):
    if x < -10:
        return 0
    elif -10 <= x < -5:
        return 0.5 * x + 5
    elif -5 <= x < 0:
        return 2 - 0.2 * x
    elif 0 <= x < 5:
        return 2 + 0.1 * x
    elif 5 <= x < 10:
        return 3 - 0.1 * x
    else:
        return 0

x = float(input())
result = f(x)
print("%.2f" % result)
