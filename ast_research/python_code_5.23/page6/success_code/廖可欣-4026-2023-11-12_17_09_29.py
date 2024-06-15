n = int(input())
xji = [2]
yji = [1]
zong = [2]
for i in range(2,n+1):
    x = xji[-1]+yji[-1]
    y = xji[-1]
    xji.append(x)
    yji.append(y)
    ebd = x/y
    zong.append(ebd)
print("%.4f"%sum(zong))
