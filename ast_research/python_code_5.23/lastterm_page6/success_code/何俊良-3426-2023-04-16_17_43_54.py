def f(x):
    if x < 20:
        return round(6 * x ** 2 + 1, 2)
    elif x < 40:
        return round((3 * x - 60) ** 0.5, 2)
    else:
        return round(100 / (x + 1), 2)

x = float(input().strip())
print(f(x))

