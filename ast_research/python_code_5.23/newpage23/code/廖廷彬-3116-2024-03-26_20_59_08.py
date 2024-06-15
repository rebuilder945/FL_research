x1, y1 = map(int, input("请输入点A的坐标 (x1, y1): ").split(','))
x2, y2 = map(int, input("请输入点B的坐标 (x2, y2): ").split(',')
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"{distance:.2f}")
