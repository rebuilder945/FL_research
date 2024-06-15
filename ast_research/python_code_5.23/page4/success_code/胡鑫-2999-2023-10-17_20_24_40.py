lst = input().split()
n,m = map(int,input(),split())
r = lst[::]
r[m] = lst[n]
r[n] = lst[m]
print(r)
