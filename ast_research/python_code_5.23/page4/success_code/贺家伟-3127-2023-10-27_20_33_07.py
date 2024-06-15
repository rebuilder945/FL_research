n=eval(input())
a=[]
for i in range(1,n+1):
    a.append(i)
for i in range(0,n-1):
    a[i]=a[i+1]
a[n-1]=a[1]
print(a)
