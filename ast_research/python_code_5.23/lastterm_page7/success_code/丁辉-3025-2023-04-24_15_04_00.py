a=input().split()
b={}
for x in a:
    if x not in b.keys():
        b[x]=1
    else:
        b[x]+=1
c=list(b.items())
c.sort(key=lambda x:x[1],reverse=True)
for i in range(0,len(c)):
    if c[i][1]==c[0][1]:
        print(c[i][0],c[i][1])
