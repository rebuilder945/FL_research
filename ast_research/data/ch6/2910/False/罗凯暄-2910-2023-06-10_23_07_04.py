h = float(input())
n = int(input())

# 第一次落地时球经过的路程为h米
total_distance = h

# 计算第2到第n次落地时球经过的路程
for i in range(2, n+1):
    # 第i次落地时球下落的路程为h + h/2 + h/2^2 + ... + h/2^(i-1)米
    # 使用等比数列求和公式：Sn = a1(1-q^n)/(1-q)，其中a1为首项，q为公比，n为项数
    # 则球下落的路程为h*(1-0.5^i)/(1-0.5)米
    down_distance = h*(1-0.5**i)/(1-0.5)
    # 第i次落地时球弹起的路程为h/2^i米
    up_distance = h/2**i
    # 第i次落地时球经过的路程为球下落的路程加上球弹起的路程
    distance = down_distance + up_distance
    # 第i次落地时球经过的总路程为前i-1次落地时球经过的总路程加上第i次落地时球经过的路程
    total_distance += distance

print(total_distance)

