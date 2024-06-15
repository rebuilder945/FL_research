def f(x):
    ans = 0
    if x < 20:
        ans = 6 * (x ** 2) + 1
    elif x < 40:
        ans = (3 * x - 60) ** 0.5
    else:
        ans = 100 / (x + 1)
    return ans
x = eval(input())
print("%.2f"%f(x))

