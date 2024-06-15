a=eval(input())
m=""
for x in a:
    m+=x
d={}
for x in m:
    d[x]=d.get(x,0)+1
dlist=[]
for k,v in d.items():
    dlist.append([k,v])
dlist.sort(key=lambda x:x[0],reverse=False)
for x in dlist:
    print("%s,%s"%(x[0],x[1]))
