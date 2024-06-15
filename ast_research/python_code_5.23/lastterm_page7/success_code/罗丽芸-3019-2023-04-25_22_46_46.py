a=input().split(" ")
print(a[0],end=" ")
del a[0]
for x in range(len(a)):
    a[x]=int(a[x])
a.sort(reverse=True)
b=sum(a)/3
for x in a:
    print('%.2f'%(x),end=" ")
print('%.2f'%b)

