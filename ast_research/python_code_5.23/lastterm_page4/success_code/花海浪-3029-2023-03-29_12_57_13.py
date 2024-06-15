sName=input().split(',')
sP=eval(input())
c=[]
for x in range(len(sName)):
    if x not in c:
        d=[sName[x],sP[x]]
        c.append(d)
print(c)


