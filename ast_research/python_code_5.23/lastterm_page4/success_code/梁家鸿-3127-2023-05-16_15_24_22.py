n = eval(input())
a = []
for i in range(n):
    a.append(i+1)
a[0]=a[n-1]
a[n-1]=1
print(a)
