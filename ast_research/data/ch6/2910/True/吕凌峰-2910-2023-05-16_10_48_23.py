def falldown(x, y):
    s = x
    while y > 1:
        x = x * 0.5
        s += 2 * x
        y = y - 1
    return '%.2f' %s

height = eval(input())
times = eval(input())
print(falldown(height, times))
