a = input().split(",")
b = eval(input())
a = list(a)
m =  []
for x in range(0,len(a)):
    n = []
    n.append(a[x])
    n.append(b[x])
    m.append(n)
print(m)
