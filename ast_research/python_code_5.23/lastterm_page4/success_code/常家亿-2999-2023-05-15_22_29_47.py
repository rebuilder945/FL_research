c = input().split()
n,m = map(int,input().split())
a = c[n]
b = c[m]
c[m] = a
c[n] = b
print(c)

