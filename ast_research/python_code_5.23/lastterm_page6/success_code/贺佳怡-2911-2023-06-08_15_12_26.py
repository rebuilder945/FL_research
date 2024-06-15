a=int(input())
for x in range(0,len(a)+1):
    a[x]=(a[x]+5)%10
a[0],a[1],a[2]=a[2],a[1],a[0]
print(str(a))


