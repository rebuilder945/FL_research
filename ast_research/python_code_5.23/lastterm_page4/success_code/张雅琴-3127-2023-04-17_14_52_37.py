n=int(input())
a=[i for i in range(1,n+1)]
b=[]
for x in range(1,n):
    b.append(a[x])
    b.append(1)
print(b)

