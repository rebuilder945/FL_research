n,m,l=eval(input())
c=[]
m=len(m)
for i in range(m):
    if i==1:
        i=n
        c.append(i)
    else:
        i=n+l(i-1)
        c.append(i)
print(c)




