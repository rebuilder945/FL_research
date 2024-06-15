a=input().split()
a.sort()
b={}
for x in a:
    if x in b:
        b[x]+=1
    else:
        b[x]=1
c=0
for x in b.values():
    if x>c:
        c=x
for x in b.keys():
    if b[x]==c:
        print(x,c)
        
                
