import math

x1,y1 = map(float, input().split(","))
x2,y2 = map(float, input().split(","))
distance = math.dist([x1,y1], [x2,y2])
print(distance)
