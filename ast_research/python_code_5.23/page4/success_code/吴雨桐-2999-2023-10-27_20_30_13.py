ls=input().split()
n,m=input().split()
a=[]
for i in ls:
    a.append(i)
b=a[int(n)]
a[int(n)]=a[int(m)]
a[int(m)]=b 
print(a)

