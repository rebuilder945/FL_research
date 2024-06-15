import math
n=float(input())
if n<20:
    s=n*n*6+1
elif n<40 and n>=20:
    m=3*n+6
    s=math.sqrt(m)
elif n>=40:
    s=100/(n+1)
print('%.2f'%s)
