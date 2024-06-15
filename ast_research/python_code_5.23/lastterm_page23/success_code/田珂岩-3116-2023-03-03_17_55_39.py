x1,y1 = eval(input("(点A的X坐标 , 点A的Y坐标)"))
x2,y2 = eval(input("(点B的X坐标 , 点B的Y坐标)"))
x = abs(x1-x2)
y = abs(y1-y2)
import math
d = math.sqrt(x*x+y*y)
print('%.2f'%d)
#print(round(d,2))

