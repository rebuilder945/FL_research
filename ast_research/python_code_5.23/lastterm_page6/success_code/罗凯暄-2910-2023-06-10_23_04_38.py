h = float(input())  # 输入高度
n = int(input())  # 输入次数

s = h  # 第一次落地经过的路程
for i in range(2, n+1):
    s += h  # 落地
    h /= 2  # 反弹
    s += h  # 反弹后再落地经过的路程

print('%.2f' % s)  # 输出结果，保留两位小数

