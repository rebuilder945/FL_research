h = float(input())  # 输入高度
N = int(input())  # 输入次数

s = h  # 第一次落地经过的路程
for i in range(2, N+1):
    s += h * 0.5**(i-1) * 2  # 第 i 次落地经过的路程
s -= h * 0.5**N  # 最后一次反弹不算路程

print("%.2f" % s)  # 输出结果，保留两位小数
