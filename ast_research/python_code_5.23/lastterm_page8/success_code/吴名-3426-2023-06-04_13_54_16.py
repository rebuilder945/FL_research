def calculate_fx(x):
    if x <= -1:
        return round(x**2 + 1.5, 2)
    elif -1 < x <= 1:
        return round(3 * x - 2, 2)
    else:
        return round(x**2 - 1.5, 2)

x = float(input())
result = calculate_fx(x)
print(result)

