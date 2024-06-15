n=eval(input())
a=[x for x in range(1,n+1)]
m=a[0]
for i in range(len(a)-1):
    a[i]=a[i+1]
a[-1]=m
print(a)
