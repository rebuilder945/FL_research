import math
def hanshu(x):
    if x<20:
        a=6*(x**2)+1
    if x>=20 and x<=40:
        a=math.sqrt(3*x-60)
    if x>=40:
        a=100/(x+1)
    return a
x=eval(input())
print('%.2f'%(hanshu(x)))
