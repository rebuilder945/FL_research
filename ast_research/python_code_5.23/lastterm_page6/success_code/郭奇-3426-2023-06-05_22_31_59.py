import math
n=eval(input())
if n<20:
    r=6*n*n+1
elif n>=20 and n<40:
    r=math.sqrt(3*n-60)
elif n>=40:
    r=100/(n+1)
print("%.2f"%r)
