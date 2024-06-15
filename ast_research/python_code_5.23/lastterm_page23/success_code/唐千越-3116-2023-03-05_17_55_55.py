import math
x1,y1=eval(input("请按照a,b的格式输入第一个点的坐标"))
x2,y2=eval(input("请按照a,b的格式输入第一个点的坐标"))
d=math.sqrt((x1-x2)**2+(y1-y2)**2)
print("%.2f"%(d))
