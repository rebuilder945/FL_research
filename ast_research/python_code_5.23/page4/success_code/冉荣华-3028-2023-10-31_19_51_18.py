n,m,l=map(int,input().split(','))
c=[]
for x in range(m):
    if x==1:
        x=n
        c.append(x)
    else:
        x=n+l(x-1)
        c.append(x)
print(c)




