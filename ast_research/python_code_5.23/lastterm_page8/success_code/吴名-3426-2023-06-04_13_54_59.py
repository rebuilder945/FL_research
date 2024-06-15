def f(x):
    if x <= -10:
        return 0
    elif x <= 0:
        return x + 10
    elif x <= 10:
        return x**2 + 1
    else:
        return 21.5

x = float(input())
result = f(x)
rounded_result = round(result, 2)

print(rounded_result)

