a=input().split()
c={}
for x in a:
    c[x]=c.get(x,0)+1
cl=list(c.items())
cl.sort(key=lambda x:x[1],reverse=True)
if cl[0][1]==cl[1][1]:
    print(*cl[0])
    print(*cl[1])
else:
    print(*cl[0])
