x = eval(input())
import math
from math import sqrt
if x < 20:
    y = 6*x**2+1
elif 20<=x<40:
    x2 = 3*x-60
    y = sqrt(x2)
elif x>=40:
    y = 100/(x+1)
print("%.2f"%y)

