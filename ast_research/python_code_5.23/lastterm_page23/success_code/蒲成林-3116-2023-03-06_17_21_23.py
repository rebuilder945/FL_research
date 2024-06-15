# import math
# x1, y1 = map(float, input().split(","))
# x2, y2 = map(float, input().split(","))
# d = math.dist([x1, y1], [x2, y2])
# print("%.2f"%d)
x1, y1 = map(eval, input().split(","))
x2, y2 = map(eval, input().split(","))
d=(((x1-x2)**2+(y1-y2)**2)**(1/2))
print("%.2f"%d)
