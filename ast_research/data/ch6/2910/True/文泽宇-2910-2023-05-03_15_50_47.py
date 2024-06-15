h = float(input())
n = int(input())
zong = h
bounce = h
for i in range(1,n):
    bounce *= 0.5
    zong += bounce * 2
print("{:.2f}".format(zong))

