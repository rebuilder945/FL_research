a = input().split()
b,c = map(int,input().split())
d = a[:]
a[b] = a[c]
a[c] = d[b]
print(a)

