n=int(input())
a=[i for i in range(1,n+1)]
b=[]
b.append(a[0])
a.pop(0)
c=a+b
print(c)

