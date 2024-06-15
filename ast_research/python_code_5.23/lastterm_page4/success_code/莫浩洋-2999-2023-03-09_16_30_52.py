a=list(input().split(' '))
x,y=int(input().split(' '))
b=[]
c=a[x]
b.append(c)
a[x]=a[y]
a[y]=b[0]
print(a)

