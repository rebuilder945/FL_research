import math
from math import sqrt 
XA,YA=eval(input('点A的X坐标 , 点A的Y坐标'))
XB,YB=eval(input('点B的X坐标 , 点B的Y坐标'))
a=float((XA-XB)**2)
b=float((YA-YB)**2)
distance=float(sqrt(a+b))
print('%.2f'%(distance))
