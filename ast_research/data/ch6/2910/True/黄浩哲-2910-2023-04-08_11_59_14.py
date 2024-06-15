h = float(input())
N = int(input())

total_distance = h  # 初始高度算一次
distance = h  # 第一次落地算一次
for i in range(2, N+1):
    distance *= 0.5  # 反弹高度
    total_distance += distance * 2  # 加上上下两段距离

print("%.2f" % total_distance)  # 保留两位小数输出
