x=eval(input())
import math
from math import sqrt
if x<20:
    c=6*x**2+1
    print("%.2f"%c)
elif 20<=x<40:
    d=math.sqrt(3*x-60)
    print("%.2f"%d)
else :
    f=100/(x+1)
    print("%.2f"%f)


