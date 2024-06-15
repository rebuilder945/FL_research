a=list(map(int,input().split(",")))
n=a[0]
m=a[1]
l=a[2]
b=[]
for i in range(m):
    e=n+i*l
    b.append(e)
print(b)

