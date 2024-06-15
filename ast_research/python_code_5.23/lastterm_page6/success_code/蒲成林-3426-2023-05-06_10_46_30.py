def fton(x):
    if x < 20:
        x = 6*x**2+1
    elif 20 <= x < 40:
        x = (3*x-60)**0.5
    else:
        x = 100/(x+1)
    return x

x = float(input())
print("{:.2f}".format(fton(x)))

