a=eval(input())
a=list(a)
b=[a[0]]
for x in range(a[1]-1):
    a[0]=a[0]+a[2]
    b.append(a[0])
print(b)
