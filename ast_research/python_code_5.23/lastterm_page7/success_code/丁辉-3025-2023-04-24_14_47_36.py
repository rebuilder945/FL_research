a=input()
b={}
b[a]=b.get(a,0)+1
c=list(b.items())
c.sort(key=lambda x:x[1],reverse=True)
for i in range(1,len(c)):
    if c[i][1]==c[0][1]:
        print(c[0][0],c[0][1])
        print(c[i][0],c[i][1])
    else:
        print(c[0][0],c[0][1])
