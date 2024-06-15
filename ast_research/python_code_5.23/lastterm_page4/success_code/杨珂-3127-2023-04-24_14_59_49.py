x=eval(input())
a=[x for x in range(1,x+1)]
for i in range(len(a)-1):
    a[i]=a[i+1]
a[x]=a[0]
print(a)

