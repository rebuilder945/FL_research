a=list(input())
b=[]
for x in a:
    x=(int(x)+5)%10
    b.append(x)
c=b.copy()
for x in range(len(b)):
    c[x]=b[-(x+1)]
print(*c,sep='')


