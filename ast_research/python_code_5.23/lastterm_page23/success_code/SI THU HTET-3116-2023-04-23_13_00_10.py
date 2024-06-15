import math

# 输入点A的坐标
x1, y1 = map(float, input().split(','))
# 输入点B的坐标
x2, y2 = map(float, input().split(','))

# 计算两点之间的距离
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# 输出结果，保留两位小数
print("{:.2f}".format(distance))


