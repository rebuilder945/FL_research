w=input().split()
d={}
for t in w:
    d[t]=d.get(t,0)+1
lst=[]
for k,v in d.items():
    lst.append([k,v])
lst.sort(key=lambda x:x[1],reverse=True)
c=1
for i in range(len(lst)-1):
    if lst[i][1]==lst[i+1][1]:
        c+=1
ls=[]
for s in range(c):
    ls.append(lst[s])
ls.sort(key=lambda x:x[0])
for h in range(c):
    print(ls[h][0],ls[h][1])
