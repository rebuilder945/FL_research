a = input().split()
b = a[0]
c = a[1]
d = a[:]
a[b] = a[c]
a[c] = d[b]
print(a)

