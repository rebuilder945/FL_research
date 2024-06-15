import math
x1,y1=eval(input())
x2,y2=eval(input())
length=math.sqrt((x1-x2)**2+(y1-y2)**2)
print("点1(%d,%d)和点2(%d,%d)的距离是%.2f"%(x1,y1,x2,y2,length))
