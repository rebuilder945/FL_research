a = input().split()
b,c = eval(input())
d = a.copy()
a[b] = a[c]
a[c] = d[b]
print(a)

