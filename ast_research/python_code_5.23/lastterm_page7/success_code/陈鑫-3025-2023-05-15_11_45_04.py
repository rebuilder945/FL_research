a=input().split()
b={}
d=[]
for i in range(len(a)):            
    b[a[i]]=b.get(a[i],0)+1    
c=list(map(int,b.values()))
for i in range(len(c)):
    if c[i]==max(c):
        if list(b.keys())[i] not in d:
            d.append(list(b.keys())[i])
d.sort()
for x in range(len(d)):
    print(d[x],max(c)) 

