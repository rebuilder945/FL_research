import math
from math import sqrt 
XA,YA=eval(input())
XB,YB=eval(input())
a=float((XA-XB)**2)
b=float((YA-YB)**2)
distance=float(sqrt(a+b))
print('%.2f'%(distance))
