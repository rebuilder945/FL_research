n=eval(input())
a=[x for x in range(1,n+1)]
for i in range(0,n-1):
    a[i],a[i+1]=a[i+1],a[i]
print(a)


# print(a)
