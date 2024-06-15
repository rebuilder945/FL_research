a=list(input())
b=[]
for x in a:
    x=(int(x)+5)%10
    b.append(x)
c=b.copy()
c[0],c[1],c[2]=b[-1],b[-2],b[-3]
print(*c,sep='')


