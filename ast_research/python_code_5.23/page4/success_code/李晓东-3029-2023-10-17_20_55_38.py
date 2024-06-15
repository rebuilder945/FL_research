a = input().split(",")
a = list(a)
b = eval(input())
m = []
for x in range(len(a)):
    n = []
    n.append(a[x])
    n.appeng(b[x])
    m.append(n)
print(m)
