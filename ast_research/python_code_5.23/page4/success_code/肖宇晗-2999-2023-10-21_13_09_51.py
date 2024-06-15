l = input().split()
n,m = map(int,input().split())
a = l[n]
l[n] = l[m]
l[m] = a
print(l)
