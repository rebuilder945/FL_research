a = input().split(' ')
d = a.copy()
ls = list(map(int,input().split(' ')))
b = ls[0]
c = ls[1]
e = a[b]
f  = a[c]
d[b] = f
d[c] = e
print(d)

