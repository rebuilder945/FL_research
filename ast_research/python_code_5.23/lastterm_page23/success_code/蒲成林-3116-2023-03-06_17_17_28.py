# import math
# x1, y1 = map(float, input().split(","))
# x2, y2 = map(float, input().split(","))
# d = math.dist([x1, y1], [x2, y2])
# print("%.2f"%d)
x1, y1 = map(int, input().split(","))
x2, y2 = map(int, input().split(","))
d=(((x1-x2)**2+(y1-y2)**2)**0.5)
print("%.2d"%d)
