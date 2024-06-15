a = input().split(",")
b = eval(input())
a = list(a)
m =  []
for x in range(0,len(a)):
    d = a[x]+b[x]
    d = list(d)
    m.append(d)
print(m)
