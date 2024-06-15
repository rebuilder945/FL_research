# a和b输入点的坐标
a=eval(input()) # x1,y1
b=eval(input()) # x2,y2
import math
n=math.sqrt(a*a-b*b)
stext='%.2f'%(n)
print(stext)