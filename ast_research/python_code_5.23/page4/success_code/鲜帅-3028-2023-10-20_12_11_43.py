n,m,l = map(int,input().split(","))
ls1 = [n]
while m-1 > 0:
    ls1.append(n+l)
    n = n+l
    m -= 1
print(ls1)

