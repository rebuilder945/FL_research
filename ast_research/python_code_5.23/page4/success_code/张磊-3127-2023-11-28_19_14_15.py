n=int(input())
b=[]
while n>0:
    b.append((n))
    n=n-1
b.reverse()
c=b[0]
b.insert(-1,c)
b.pop(0)
b[-2],b[-1]=b[-1],b[-2]
print(b)





