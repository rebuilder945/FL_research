n=eval(input())
a=[x for x in range(1,n+1)]
for i in range(n-1):
    a[i]=a[i+1]
a[n-1]=1
print(a)    
