a = input().split()
b,c = eval(input().split())
d = a[:]
a[b] = a[c]
a[c] = d[b]
print(a)

