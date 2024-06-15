n=int(input())
a=[i for i in range(1,n+1)]
print(a)
m=len(a)-1
for x in a[1:]:
    a[m-1],a[m]=a[m],a[m-1]
    m-=1
    print(a,m)
print(a)
