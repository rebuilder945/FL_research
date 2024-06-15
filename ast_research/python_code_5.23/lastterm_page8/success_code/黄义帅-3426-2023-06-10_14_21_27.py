x = float(input())
import math
def hanshu(a):
    if a < 20:
        b = float(6*a*a+1)
        return b
    elif a >= 20 and a < 40:
        c = 3*a - 60
        b = float(math.sqrt(c))
        return b
    elif a >= 40:
        b = float(100/a+1)
        return b
print(f"{hanshu(x):.2f}")

