n = eval(input())
a=range(1,n+1)
b = []
m=a[0]
for i in range(len(a)-1):
    b.append(a[i+1])
b.append(m)
print(b)
