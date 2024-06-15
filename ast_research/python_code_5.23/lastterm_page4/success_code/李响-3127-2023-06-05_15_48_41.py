n = int(input())
a = list(range(1,n+1))
for i in range(len(a)-1):
    a[i],a[i+1] = a[i+1],a[i]
print(a)



