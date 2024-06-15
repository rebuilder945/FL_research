h=float(input())
N=int(input())

dis = h
for i in range(1,N):
    s=(h*(0.5**i))*2
    dis += s

print("{:.2f}".format(dis))


