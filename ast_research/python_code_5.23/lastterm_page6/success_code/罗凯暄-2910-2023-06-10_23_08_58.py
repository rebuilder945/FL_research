h = float(input())
n = int(input())

s = h  # 第一次落地时球经过的路程为h米
for i in range(2, n+1):
    s += h/2**(i-1) * 2  # 第i次落地时球经过的路程为h/2^(i-1)*2米

print("%.2f"% s)


