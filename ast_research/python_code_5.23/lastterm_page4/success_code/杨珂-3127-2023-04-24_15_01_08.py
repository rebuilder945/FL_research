x=int(input())
a=[x for x in range(1,x+1)]
b=a[0]
for i in range(len(a)-1):
    a[i]=a[i+1]
a[-1]=b
print(a)

