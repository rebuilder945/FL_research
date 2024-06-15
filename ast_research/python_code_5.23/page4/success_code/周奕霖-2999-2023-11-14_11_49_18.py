a = input().split()
b,c = int(input().split())
d = a[:]
a[b] = a[c]
a[c] = d[b]
print(a)

