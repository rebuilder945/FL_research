s=input().split()
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
m=max(d.values())
n=[]
for k,v in d.items():
    if v==m:
        n.append((k,v))
n.sort(key=lambda x:x[0])
for i in n:
    print(i[0],i[1])
