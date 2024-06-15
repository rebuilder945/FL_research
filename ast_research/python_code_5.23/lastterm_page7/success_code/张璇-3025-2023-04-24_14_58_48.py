b=input().spilt()
c={}
for x in b:
    c[x]=c.get(x,0)+1
lst=list(c.items())
lst.sort(key=lambda x:x[1],reverse=True)
for x in lst:
    while lst[x][1]==lst[0][1]:
        print(lst[x][0],lst[x][1])


