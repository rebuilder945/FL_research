import math
x1,y1 = eval(input())
x2,y2 = eval(input())
d = (x1-x2)**2
e = (y1-y2)**2
f = math.sqrt(d+e)
print('%.2f' %f)
