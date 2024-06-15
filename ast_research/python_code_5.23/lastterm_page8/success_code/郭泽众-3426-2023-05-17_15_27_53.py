import math
def mathf(x):
    if x < 20:
        return 6 * (x **2) + 1
    elif 20 <= x < 40:
        return math.sqrt(3 * x - 60)
    else:
        return 100 / (x + 1)
x = eval(input())
print('%.2f'%mathf(x))
