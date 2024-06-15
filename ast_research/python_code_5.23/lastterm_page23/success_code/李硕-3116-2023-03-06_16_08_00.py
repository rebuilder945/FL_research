import math
x,y=map(float,input("点A1,2"))
a,b=map(float,input("点B,2"))
d=math.sqrt((a-x)**2+(b-y)**2)
print("{:.2f}".format(d))
