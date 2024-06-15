ls=input().split()
ls.sort()
dit={}
for x in ls:
    dit[x]=dit.get(x,0)+1
ls1=[]
for k,v in dit.items():
    ls1.append(k+' '+str(v))
for x in ls1:
    if x[-1]==str(max(dit.values())):
        print(x)


